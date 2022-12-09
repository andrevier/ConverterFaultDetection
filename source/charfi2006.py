"""Implement the paper: Fault Diagnostic in Power System Using Wavelet
Transforms and Neural Networks.
Authors: F.Charfi, F.Sellami, and K.Al-Haddad
Year: 2006
1. Training stage.
    1.1 Get the data from the path.
    1.2 Separate the data in windows.
    1.3 Over the windows, extract DWT from each window.
    1.4 Create pairs of input, output data: the input is the DWTs and
        the output, 1 if it is in normal stage, 0 if it is in fault. 
    1.5 Use the pairs to train the NN.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import pywt
import tools

# Main line current parameters.
f = 50
Ibase = 8.15

# Total simulation time.
maxTime = 10.0

# Length of the time interval.
timeInterval = 5*1/f
numberOfIntervals = int(maxTime//timeInterval)
Ibound = 0.10
I21Bound = .10
I31Bound = .10

# Trainning data
path = "D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T1FullSpeed"

# Choose one path to analyze the data.
os.chdir(path)

# Convert all the csv data into dataframe series.
Isa = pd.read_csv("isa.csv")
Isb = pd.read_csv("isb.csv")
Isc = pd.read_csv("isc.csv")
Te = pd.read_csv("Te.csv")
time = pd.read_csv("time.csv")
Vab = pd.read_csv("Vab.csv")
wm = pd.read_csv("wm.csv")

# Make a dataframe with time and currents
Isadf = pd.concat([time, Isa], ignore_index=True, axis=1)
Isbdf = pd.concat([time, Isb], ignore_index=True, axis=1)
Iscdf = pd.concat([time, Isc], ignore_index=True, axis=1)

timeList = []
TIME = 0
PHASE = 1

# Experience with part of the signal.
ia = Isadf[(Isadf[TIME] >= 5.5) & (Isadf[TIME] <= 5.7)]

ia0 = ia[PHASE].to_list()
ia0 = [i/Ibase for i in ia0]
time0 = ia[TIME].to_list()

# Calculate the DWT of daubechies with 2 vanishing moments and signal 
# extension mode "antisymmetric". Using pywt.dwt:
(a, d) = pywt.dwt(ia0, "db2", "antisymmetric")

# pywt.dwt decomposes the signal in the first level: a1 and d1.
ia0reverse = pywt.idwt(a, d, "db2", mode="antisymmetric")
print("The coefficients:")
print("length of a = ", len(a))
print("d = ", len(d))

# Sometimes the inverse DWT gives different length of signal.
if len(time0) != len(ia0reverse):
    ia0reverse = ia0reverse[:len(time0)]

# _, axs = plt.subplots(2)
# axs[0].plot(time0, ia0)
# axs[1].plot(time0, ia0reverse)
# plt.show()

# Use pywt.wavedec to decompose into more levels and pywt.waverec with
# modes "periodization" or "antisymmetric".
a6, d6, d5, d4, d3, d2, d1  = pywt.wavedec(ia0, "db4", mode="antisymmetric", level=6)
print("a3 lenght = " + str(len(a6)))
print(a6)
print("d3 lenght = " + str(len(d6)))
print(d6)
print("d2 lenght = " + str(len(d5)))
print(d5)
print("d1 lenght = " + str(len(d4)))
print(d4)

_, axs = plt.subplots(5)
axs[0].plot(time0, ia0)
axs[0].legend("Ia")

axs[1].plot(a6)
axs[1].legend("a6")

axs[2].plot(d6)
axs[2].legend("d6")

axs[3].plot(d5)
axs[3].legend("d5")

axs[4].plot(d4)
axs[4].legend("d4")
plt.show()

# # Divide the simulation into segments to calculate and analize the
# # parameters.
# for i in range(0, numberOfIntervals):
#     timeList.append((i+1)*timeInterval)
#     ia = Isadf[(Isadf[TIME] >= i*timeInterval)
#                & (Isadf[TIME] <= (i+1)*timeInterval)]

#     ib = Isbdf[(Isbdf[TIME] >= i*timeInterval)
#                & (Isbdf[TIME] <= (i+1)*timeInterval)]

#     ic = Iscdf[(Iscdf[TIME] >= i*timeInterval)
#                & (Iscdf[TIME] <= (i+1)*timeInterval)]

#     ia0 = ia[PHASE].values
#     ib0 = ib[PHASE].values
#     ic0 = ic[PHASE].values
