"""
Script to implement the diagnostic method of the paper:
A Diagnostic Method of Simultaneous OpenSwitch Faults in Inverter-Fed 
Linear Induction Motor Drive for Reliability Enhancement.
Authors: 
Jung-Hyun Choi, Sanghoon Kim, Dong Sang Yoo, and Kyeong-Hwa Kim
Link: https://ieeexplore.ieee.org/document/6994788
date: 23/11/2022

Summary
1. Import data.
2. Jung-Hyun Choi algorithm.
2.1 Part the simulation in intervals.
2.2 Record the main parameters from each interval.
2.3 Check for fault states and fault modes.
3. Plot the relevant data.
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tools 

# 1. Import data.
from Simulations.model15ScalarControl.openCircuit.T1FullSpeed import (
    Isa as IsAOpenCircuit,
    Isb as IsBOpenCircuit,
    Isc as IsCOpenCircuit,
    time as timeSeries
    )

# Make a dataframe with time and currents
IsOpenCircuit = pd.concat([timeSeries, IsAOpenCircuit,
                IsBOpenCircuit, IsCOpenCircuit],
                ignore_index=True, axis=1)

# Substitute the name by the columns' number.
TIME = 0
PHASEA = 1
PHASEB = 2
PHASEC = 3

# 2. Jung-Hyun Choi algorithm.
# 2.1 Part the simulation in intervals
ocCurrentsIntervals = []
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
baseCurrentRMS = 8.15

# Record tupples for each interval in study.
# First harmonics of phases A, B and C.
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

h21Threshold = .10
h31Threshold = .10

for i in range(0,numberOfIntevals):
    ocCurrentsIntervals.append(
        IsOpenCircuit[(IsOpenCircuit[TIME] >= i*timeInterval) 
                       & (IsOpenCircuit[TIME] <= (i+1)*timeInterval)]
        )
    timeList.append((i+1)*timeInterval)

    # 2.2) Record the main parameters from each interval
    # 2.2.1) Select the interval and convert the series into numpy arrays.
    isa = ocCurrentsIntervals[i][PHASEA].values
    isb = ocCurrentsIntervals[i][PHASEB].values
    isc = ocCurrentsIntervals[i][PHASEC].values

    # 2.2.2) Collect data.
    # Sampling of period.
    tsa = timeInterval/len(isa)
    tsb = timeInterval/len(isb)
    tsc = timeInterval/len(isc)
    
    # Data for the phase-A current: first 3 harmonics, average, RMS and
    # normalized RMS.
    freqArrayA, fftArrayA = tools.calcFFT(isa, tsa)
    freqOfHarmA, fftOfHarmA = tools.harmonics(freqArrayA, fftArrayA, h1, 
                                              maxHarmonicNumber,
                                              freqSearchInterval)
    h1A = np.append(h1A,fftOfHarmA[1])
    h2A = np.append(h2A,fftOfHarmA[2])
    h3A = np.append(h3A,fftOfHarmA[3])
    
    averageA = np.append(averageA, sum(isa)/len(isa))
    
    isaRMS = tools.RMS2(isa)
    RMSA = np.append(RMSA, isaRMS)
    RMSANorm = np.append(RMSANorm, RMSA/baseCurrentRMS)
    
    # Data for the phase-B current
    freqArrayB, fftArrayB = tools.calcFFT(isb, tsb)
    freqOfHarmB, fftOfHarmB = tools.harmonics(freqArrayB, fftArrayB, h1,
                                        maxHarmonicNumber, 
                                        freqSearchInterval)
    
    h1B = np.append(h1B,fftOfHarmB[1])
    h2B = np.append(h2B,fftOfHarmB[2])
    h3B = np.append(h3B,fftOfHarmB[3])
    
    averageB = np.append(averageB, sum(isb)/len(isb))
    
    isbRMS = tools.RMS2(isb)
    RMSB = np.append(RMSB, isbRMS)
    RMSBNorm = np.append(RMSBNorm, RMSB/baseCurrentRMS)
    
    # Data for the phase-C current
    freqArrayC, fftArrayC = tools.calcFFT(isc, tsc)
    freqOfHarmC, fftOfHarmC = tools.harmonics(freqArrayC, fftArrayC, h1,
                                            maxHarmonicNumber, 
                                            freqSearchInterval) 
    h1C = np.append(h1C,fftOfHarmC[1])
    h2C = np.append(h2C,fftOfHarmC[2])
    h3C = np.append(h3C,fftOfHarmC[3])
    
    averageC = np.append(averageC, sum(isc)/len(isc))
    
    iscRMS = tools.RMS2(isc)
    RMSC = np.append(RMSC, iscRMS)
    RMSCNorm = np.append(RMSCNorm, RMSC/baseCurrentRMS)

    # 2.3) Check for fault states and fault modes.
    # Fault state can be 1 if fault occurs or 0, otherwise.
    # Fault mode 0 -> normal state. 
    #            1 -> 2 open-switches in one leg.
    #            2 -> 1 open-switch.
    #            3 -> 2 open-switches in upper leg positions or in the 
    #                 lower leg positions.
    #            4 -> 2 open-switches: 1 in the upper part and 1 in the
    #                 lower part. 

    # Relative frequency h21x = (harmonic 2)/(harmonic 1) 
    # from x = a,b,c.
    
    try:
        h21a = np.append(h21a, h2A[i]/h1A[i])
        h21b = np.append(h21b, h2B[i]/h1B[i])
        h21c = np.append(h21c, h2C[i]/h1C[i])
        h31a = np.append(h31a, h3A[i]/h1A[i])
        h31b = np.append(h31b, h3B[i]/h1A[i])
        h31c = np.append(h31c, h3C[i]/h1A[i])
    except ZeroDivisionError as err:
        print("Zero division error. Check the first harmonics. ", err)
        raise SystemExit    

    # Reset the variables before the fault detection.
    faultState = 0
    faultMode = 0
    
    # Check for faults 
    if ((np.max(RMSANorm[i]) <= infCurrentLimit) or
        (np.max(RMSBNorm[i]) <= infCurrentLimit) or
        (np.max(RMSCNorm[i]) <= infCurrentLimit)):
        faultState = 1
    elif ((h21a[i] >= h21Threshold) or 
          (h21b[i] >= h21Threshold) or
          (h21c[i] >= h21Threshold)):
          faultState = 1
    
    # Check for fault modes.
    if (faultState == 1):
        if ((np.max(RMSANorm[i]) <= infCurrentLimit) or
            (np.max(RMSBNorm[i]) <= infCurrentLimit) or
            (np.max(RMSCNorm[i]) <= infCurrentLimit)):
            faultMode = 1
        elif not ((h31a[i] >= h31Threshold) 
                  or (h31b[i] >= h31Threshold) 
                  or (h31c[i] >= h31Threshold)):
            faultMode = 2
        else:
            faultMode = 3

    faultStateList.append(faultState)
    faultModeList.append(faultMode)

# 3. Plot the relevant data.
# Show the plots if togglePlot is true.
togglePlot = False

if (togglePlot):
    # Currents
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEA], label="A")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEB], label="B")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.ylabel ('Stator Current (A)')
    plt.legend(["IA", "IB", "IC"])
    plt.show()

# Plot of the first three harmonics over time.
if (True):
    fig, axs = plt.subplots(8)
    fig.set_figwidth(10)
    fig.set_figheight(20)
    axs[0].plot(timeList, RMSA)
    axs[0].plot(timeList, RMSB)
    axs[0].plot(timeList, RMSC)
    axs[0].legend(["IA RMS", "IB RMS", "IC RMS"])

    axs[1].plot(timeList, h1A)
    axs[1].plot(timeList, h2A)
    axs[1].plot(timeList, h3A)
    axs[1].legend(["IA1", "IA2", "IA3"])

    axs[2].plot(timeList, h1B)
    axs[2].plot(timeList, h2B)
    axs[2].plot(timeList, h3B)
    axs[2].legend(["IB1", "IB2", "IB3"])
    axs[2].set(ylabel='FFT of the first 3 harmonics')

    axs[3].plot(timeList, h1C)
    axs[3].plot(timeList, h2C)
    axs[3].plot(timeList, h3C)
    axs[3].legend(["IC1", "IC2", "IC3"])
    
    axs[4].plot(timeList, h21a)
    axs[4].plot(timeList, h21b)
    axs[4].plot(timeList, h21c)
    axs[4].legend(["h21a", "h21b", "h21c"])

    axs[5].plot(timeList, h31a)
    axs[5].plot(timeList, h31b)
    axs[5].plot(timeList, h31c)
    axs[5].legend(["h31a", "h31b", "h31c"])

    if (len(timeList) != len(faultStateList)):
        print("Time and fault list doesnt match.")
        print("timeList: " + str(len(timeList)) + " faultList[0]: "
              + str(len(faultStateList)))
        raise ValueError

    axs[6].plot(timeList, faultStateList)
    axs[6].legend("Fault State")
        
    if (len(timeList) != len(faultModeList)):
        print("Time and fault list doesnt match.")
        print("timeList: " + str(len(timeList)) + " faultList[0]: " + str(len(faultModeList)))
        raise ValueError

    axs[7].plot(timeList, faultModeList)
    axs[7].legend("Fault Mode")
    plt.show()