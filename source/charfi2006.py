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
import tensorflow as tf
from tensorflow import keras
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
# BEFORE = 4.3
# AFTER = 4.6
# ia = Isadf[(Isadf[TIME] >= BEFORE) & (Isadf[TIME] <= AFTER)]
# ib = Isbdf[(Isbdf[TIME] >= BEFORE) & (Isbdf[TIME] <= AFTER)]
# ic = Iscdf[(Iscdf[TIME] >= BEFORE) & (Iscdf[TIME] <= AFTER)]

# ia0 = ia[PHASE].to_list()
# ia0 = [i/Ibase for i in ia0]

# ib0 = ia[PHASE].to_list()
# ib0 = [i/Ibase for i in ib0]

# ib0 = ia[PHASE].to_list()
# ib0 = [i/Ibase for i in ib0]

# time0 = ia[TIME].to_list()

# Calculate the DWT of daubechies with 4 vanishing moments with
# pywt.wavedec to decompose into more levels with modes 
# "periodization" or "antisymmetric".
# IACoef  = pywt.wavedec(ia0, "db4", mode="antisymmetric", level=6)

# print("length of IACoef is ", len(IACoef))
# print("shape of each coef array: ", IACoef[0].shape)
# _, axs = plt.subplots(4,2)
# axs[0,0].plot(IACoef[0])
# axs[0,0].legend("a10")

# axs[0,1].plot(IACoef[1])
# axs[0,1].legend("d9")

# axs[1,0].plot(IACoef[2])
# axs[1,0].legend("d8")

# axs[1,1].plot(IACoef[3])
# axs[1,1].legend("d7")

# axs[2,0].plot(IACoef[4])
# axs[2,0].legend("d6")

# axs[2,1].plot(IACoef[5])
# axs[2,1].legend("d5")

# axs[3,0].plot(IACoef[6])
# axs[3,0].legend("d4")

# plt.show()

# Built a NN with 3 layers: input, hidden and output.
model = keras.models.Sequential([
    keras.layers.Input(shape=(3,)),
    keras.layers.Dense(6, activation=keras.activations.sigmoid,
        name="hidden"),
    keras.layers.Dense(1, activation=keras.activations.softmax,
        name="output")
    ])

model.summary()

# Creating a trainning and test set. Each line is a instance.

# Divide the simulation into segments to calculate and analize the
# parameters.
IACoefList = []
IBCoefList = []
ICCoefList = []
for i in range(20, 50):
    timeList.append((i+1)*timeInterval)
    ia = Isadf[(Isadf[TIME] >= i*timeInterval)
               & (Isadf[TIME] <= (i+1)*timeInterval)]

    ib = Isbdf[(Isbdf[TIME] >= i*timeInterval)
               & (Isbdf[TIME] <= (i+1)*timeInterval)]

    ic = Iscdf[(Iscdf[TIME] >= i*timeInterval)
               & (Iscdf[TIME] <= (i+1)*timeInterval)]

    ia0 = ia[PHASE].values
    ib0 = ib[PHASE].values
    ic0 = ic[PHASE].values

    IACoef  = pywt.wavedec(ia0, "db4", mode="antisymmetric", level=6)
    IACoefList.append(IACoef[0])
    IBCoef  = pywt.wavedec(ib0, "db4", mode="antisymmetric", level=6)
    IBCoefList.append(IBCoef[0])
    ICCoef  = pywt.wavedec(ic0, "db4", mode="antisymmetric", level=6)
    ICCoefList.append(ICCoef[0])

print("Coefficients...")
print(len(IACoefList))
print(IACoefList[0].shape)

""" Lack of details for implementing the neural network. How does each
coefficient array are supplied?
"""