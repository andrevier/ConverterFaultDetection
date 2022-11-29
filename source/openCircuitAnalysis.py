'''Analize open-circuits'''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tools 


# 1. Import data.
from Simulations.model15ScalarControl.openCircuit.T1FullSpeed import (
    Isa,Isb,Isc,time as timeSeries)

print("Isa")
print(type(Isa))
print(Isa.head())
print(Isa.values[:5])
# Make a dataframe with time and currents
Is = pd.concat([timeSeries, Isa, Isb, Isc], ignore_index=True, axis=1)
print("Is")
print(Is.head())
# Substitute the name by the columns' number.
TIME = 0
PHASEA = 1
PHASEB = 2
PHASEC = 3

# 2. Jung-Hyun Choi algorithm.
# 2.1 Part the simulation in intervals
lineCurrentIntervals = []
timeList = [0.0]
maxTime = 10.0

# Important parameters: 
# First harmonic frequency (Hz). 
h1 = 50.0
timeInterval = 5*1/h1
numberOfIntevals = int(maxTime//timeInterval)

# Sampling period, the distance of two samples in time.
Ts = 1.e-06

# Max number harmonic frequencies for the FFT. 
maxHarmonicNumber = 3

# Search interval means the neighbourhood of the harmonics. 
freqSearchInterval = 5

# Standard for normalized harmonics and the base RMS current. 
infCurrentLimit = 0.1
baseCurrent = 8.15

# Record tupples for each interval in study.
# FFT of the first harmonic of phases A, B and C.
h1A = np.array([0.])
h1B = np.array([0.])
h1C = np.array([0.])

# Second harmonics of phases A, B and C.
h2A = np.array([0.])
h2B = np.array([0.])
h2C = np.array([0.])

# Third harmonics of phases A, B and C.
h3A = np.array([0.])
h3B = np.array([0.])
h3C = np.array([0.])

# Relative harmonics
h21a = np.array([0.])
h21b = np.array([0.])
h21c = np.array([0.])
h31a = np.array([0.])
h31b = np.array([0.])
h31c = np.array([0.])

# Average of each phase.
averageA = np.array([0.])
averageB = np.array([0.])
averageC = np.array([0.])

# RMS of each phase.
RMSANorm = np.array([0.])
RMSA = np.array([0.])

RMSBNorm = np.array([0.])
RMSB = np.array([0.])

RMSCNorm = np.array([0.])
RMSC = np.array([0.])

# List of fault states and fault mode: item (2.3)
faultStateList = [0]
faultModeList = [0]
T1 = [0]
T2 = [0]
T3 = [0]
T4 = [0]
T5 = [0]
T6 = [0]

h21Threshold = .10
h31Threshold = .10

for i in range(0,numberOfIntevals):
    lineCurrentIntervals.append(Is[(Is[TIME] >= i*timeInterval)
                               & (Is[TIME] <= (i+1)*timeInterval)])
    timeList.append((i+1)*timeInterval)

    # 2.2) Record the main parameters from each interval
    # 2.2.1) Select the interval and convert the series into numpy arrays.
    isa = lineCurrentIntervals[i][PHASEA].values
    isb = lineCurrentIntervals[i][PHASEB].values
    isc = lineCurrentIntervals[i][PHASEC].values

    # Sample period.
    tsa = timeInterval/len(isa)
    cm = tools.ConditionMonitoring( Ia=isa, Ib=isb, Ic=isc, lineFrequency=h1,
                                    baseCurrentRMS=baseCurrent, Ts=tsa,
                                    infCurrentBound=0.1, 
                                    h21Bound=0.1, h31Bound=0.1)
    
    # Run the algorithm.  
    cm.checkSystemStateWithJHC()

    # Get the data from the algorithm: 
    # first 3 harmonics; 
    IaFreq, IaFFT = cm.getIaFreqAndFFT()
    h1A = np.append(h1A, IaFFT[1])
    h2A = np.append(h2A, IaFFT[2])
    h3A = np.append(h3A, IaFFT[3])
    
    IbFreq, IbFFT = cm.getIbFreqAndFFT()
    h1B = np.append(h1B, IbFFT[1])
    h2B = np.append(h2B, IbFFT[2])
    h3B = np.append(h3B, IbFFT[3])

    IcFreq, IcFFT = cm.getIcFreqAndFFT()
    h1C = np.append(h1C, IcFFT[1])
    h2C = np.append(h2C, IcFFT[2])
    h3C = np.append(h3C, IcFFT[3])

    # Relative FFTs
    i21a, i21b, i21c, i31a, i31b, i31c = cm.getRelativeFFTs()
    h21a = np.append(h21a, i21a)
    h31a = np.append(h31a, i31a)

    h21b = np.append(h21b, i21b)
    h31b = np.append(h31b, i31b)

    h21c = np.append(h21c, i21c)
    h31c = np.append(h31c, i31c)

    # RMS;
    IaRMS, IbRMS, IcRMS = cm.getRMSValues()
    RMSA = np.append(RMSA, IaRMS)
    RMSB = np.append(RMSB, IbRMS)
    RMSC = np.append(RMSC, IcRMS)

    # Average currents;
    IaAve, IbAve, IcAve = cm.getAverageCurrent()
    averageA = np.append(averageA, IaAve)
    averageB = np.append(averageB, IbAve)
    averageC = np.append(averageC, IcAve)

    # Fault states, fault modes and switches' states.
    faultStateList.append(cm.getFaultState())
    faultModeList.append(cm.getFaultMode()) 

    switchStateTupple = cm.getSwitchesState()
    T1.append(switchStateTupple[0])
    T2.append(switchStateTupple[1])
    T3.append(switchStateTupple[2])
    T4.append(switchStateTupple[3])
    T5.append(switchStateTupple[4])
    T6.append(switchStateTupple[5])

# 3. Plot the relevant data.
# Show the plots if togglePlot is true.
togglePlot = False

# Currents along the simulation.
if (togglePlot):
    # Currents
    plt.plot(Is[TIME],Is[PHASEA], label="A")
    plt.plot(Is[TIME],Is[PHASEB], label="B")
    plt.plot(Is[TIME],Is[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.ylabel ('Stator Current (A)')
    plt.legend(["IA", "IB", "IC"])
    plt.show()

# RMS currents and average value along the simulation.
if (togglePlot):
    fig, axs = plt.subplots(2)
    axs[0].plot(timeList, RMSA)
    axs[0].plot(timeList, RMSB)
    axs[0].plot(timeList, RMSC)
    axs[0].legend(["IA", "IB", "IC"])

    axs[1].plot(timeList, averageA)
    axs[1].plot(timeList, averageB)
    axs[1].plot(timeList, averageC)
    axs[1].legend(["IA ave", "IB ave", "IC ave"])
    plt.show()

# Plot of the first three harmonics over time.
if (togglePlot):
    fig, axs = plt.subplots(10)
    fig.set_figwidth(10)
    fig.set_figheight(20)
    axs[0].plot(timeList, RMSA)
    axs[0].plot(timeList, RMSB)
    axs[0].plot(timeList, RMSC)
    axs[0].legend(["IA", "IB", "IC"])

    axs[1].plot(timeList, averageA)
    axs[1].plot(timeList, averageB)
    axs[1].plot(timeList, averageC)
    axs[1].legend(["IAave", "IBave", "ICave"])

    axs[2].plot(timeList, h1A)
    axs[2].plot(timeList, h2A)
    axs[2].plot(timeList, h3A)
    axs[2].legend(["IA1", "IA2", "IA3"])

    axs[3].plot(timeList, h1B)
    axs[3].plot(timeList, h2B)
    axs[3].plot(timeList, h3B)
    axs[3].legend(["IB1", "IB2", "IB3"])
    axs[3].set(ylabel='FFT of the first 3 harmonics')

    axs[4].plot(timeList, h1C)
    axs[4].plot(timeList, h2C)
    axs[4].plot(timeList, h3C)
    axs[4].legend(["IC1", "IC2", "IC3"])
    
    axs[5].plot(timeList, h21a)
    axs[5].plot(timeList, h21b)
    axs[5].plot(timeList, h21c)
    axs[5].legend(["h21a", "h21b", "h21c"])

    axs[6].plot(timeList, h31a)
    axs[6].plot(timeList, h31b)
    axs[6].plot(timeList, h31c)
    axs[6].legend(["h31a", "h31b", "h31c"])

    if (len(timeList) != len(faultStateList)):
        print("Time and fault list doesnt match.")
        print("timeList: " + str(len(timeList)) + " faultList[0]: "
              + str(len(faultStateList)))
        raise ValueError

    axs[7].plot(timeList, faultStateList)
    axs[7].legend("State")
        
    if (len(timeList) != len(faultModeList)):
        print("Time and fault list doesnt match.")
        print("timeList: " + str(len(timeList)) + " faultList[0]: " + str(len(faultModeList)))
        raise ValueError

    axs[8].plot(timeList, faultModeList)
    axs[8].legend("Mode")

    axs[9].plot(timeList, T1)
    axs[9].plot(timeList, [i*2 for i in T2])
    axs[9].plot(timeList, [i*3 for i in T3])
    axs[9].plot(timeList, [i*4 for i in T4])
    axs[9].plot(timeList, [i*5 for i in T5])
    axs[9].plot(timeList, [i*6 for i in T6])
    axs[9].legend(["T1","T2","T3","T4","T5","T6"])
    plt.show()

# Relationship between RMS current values, first harmonics and for switch 
if (True):
    fig, axs = plt.subplots(5)
    fig.set_figwidth(10)
    fig.set_figheight(20)
    axs[0].plot(timeList, RMSA)
    axs[0].plot(timeList, RMSB)
    axs[0].plot(timeList, RMSC)
    axs[0].legend(["IA", "IB", "IC"])

    axs[1].plot(timeList, h1A)
    axs[1].plot(timeList, h1B)
    axs[1].plot(timeList, h1C)
    axs[1].legend(["h1A","h1B","h1C"])

    axs[2].plot(timeList, faultStateList)
    axs[2].legend("State")

    axs[3].plot(timeList, faultModeList)
    axs[3].legend("Mode")

    axs[4].plot(timeList, T1)
    axs[4].plot(timeList, [i*2 for i in T2])
    axs[4].plot(timeList, [i*3 for i in T3])
    axs[4].plot(timeList, [i*4 for i in T4])
    axs[4].plot(timeList, [i*5 for i in T5])
    axs[4].plot(timeList, [i*6 for i in T6])
    axs[4].legend(["1","2","3","4","5","6"])
    plt.show()