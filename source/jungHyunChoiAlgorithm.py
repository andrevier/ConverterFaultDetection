"""
Script to implement the diagnostic method of the paper:
A Diagnostic Method of Simultaneous OpenSwitch Faults in Inverter-Fed 
Linear Induction Motor Drive for Reliability Enhancement.
Authors: 
Jung-Hyun Choi, Sanghoon Kim, Dong Sang Yoo, and Kyeong-Hwa Kim
Link: https://ieeexplore.ieee.org/document/6994788
date: 04/11/2022

Summary
1. Import data and basic plot.
2. Jung-Hyun Choi algorithm
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tools 

# 1. Import data and basic plot.
# Show the plots if togglePlot is true.
togglePlot = False

# Import the simulation data.
from Simulations.model15ScalarControl.openCircuit.T1FullSpeed import (
    Isa as IsAOpenCircuit,
    Isb as IsBOpenCircuit,
    Isc as IsCOpenCircuit,
    time as timeSeries
    )

from Simulations.model15ScalarControl.shortCircuit.T1FullSpeed import (
    Isa as IsAShortCircuit,
    Isb as IsBShortCircuit,
    Isc as IsCShortCircuit,
    time as timeSeries
    )

# Make a dataframe with time and currents
IsOpenCircuit = pd.concat([timeSeries, IsAOpenCircuit,
                IsBOpenCircuit, IsCOpenCircuit],
                ignore_index=True, axis=1)

IsShortCircuit = pd.concat([timeSeries, IsAShortCircuit,
                IsBShortCircuit, IsCShortCircuit],
                ignore_index=True, axis=1)

# Substitute the name by the columns' number.
TIME = 0
PHASEA = 1
PHASEB = 2
PHASEC = 3   

# Plot the currents
if (togglePlot):
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEA], label="A")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEB], label="B")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Normal three-phase currents.")
    plt.xlim([1.,5.])
    plt.ylim([-15,15])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator Current (A)")
    plt.legend(["phase A", "phase B", "phase C"],
                bbox_to_anchor=(0.70,0.80))
    plt.show()

    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEA], label="A")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEB], label="B")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Steady-state after open-circuit fault.")
    plt.xlim([4.55,10.])
    plt.ylim([-23,23])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator Current (A)")
    plt.legend(["phase A", "phase B", "phase C"],
                bbox_to_anchor=(0.70,0.80))
    plt.show()         

    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEA], label="A")
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEB], label="B")
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Short-circuit three-phase currents.")
    plt.xlim([4.55,10.])
    plt.ylim([-60,60])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator currents (A)")
    plt.legend(["phase A", "phase B", "phase C"],
                bbox_to_anchor=(0.70,0.80))
    plt.show()

# 2. Jung-Hyun Choi algorithm.
# (1) Part the simulation in intervals and (2) record the main 
# variables of each interval to (3) check for fault status and fault modes.

# (1) Part the simulation in intervals
# List to record 1s intervals of simulation.
ocCurrentsIntervals = []
maxTime = 10
for i in range(maxTime):
    IsOCArray = IsOpenCircuit[(IsOpenCircuit[TIME] >= i) 
                               & (IsOpenCircuit[TIME] <= i+1)]
    ocCurrentsIntervals.append(IsOCArray)

# Get the first 3 harmonics: h1 = 50 Hz, h2 = 100 Hz and h3 = 150 Hz.
h1 = 50
maxHarmonicNumber = 3
freqSearchInterval = 5
infCurrentLimit = 0.1
timeInterval = 1.0
baseCurrentRMS = 8.15

# Record tupples for each interval in study.
isaTupples = []
isbTupples = []
iscTupples = []

# index 0 -> h1, 1-> h2, 2-> h3, 3-> Is average, 4-> Is RMS
indexH1 = 0
indexH2 = 1
indexH3 = 2
indexAve = 3
indexRMS = 4

# (2) record the main variables of each interval
for index in range(maxTime):
    # Select the interval and convert to series into numpy arrays.
    isa = ocCurrentsIntervals[index][PHASEA].values
    isb = ocCurrentsIntervals[index][PHASEB].values
    isc = ocCurrentsIntervals[index][PHASEC].values

    # Sampling of period.
    tsa = timeInterval/len(isa)
    tsb = timeInterval/len(isb)
    tsc = timeInterval/len(isc)

    # Data for the A current.
    freqArrayA, fftArrayA = tools.calcFFT(isa, tsa)
    freqOfHarmA, fftOfHarmA = tools.harmonics(freqArrayA, fftArrayA, h1, 
                                            maxHarmonicNumber,
                                            freqSearchInterval)
    h1a = fftOfHarmA[1]
    h2a = fftOfHarmA[2]
    h3a = fftOfHarmA[3]

    isaAve = sum(isa)/len(isa)
    isaRMS = tools.RMS(isa, h1, tsa)
    isaRMSNorm = [i/baseCurrentRMS for i in isaRMS]
    isaTupples.append([h1a, h2a, h3a, isaAve, isaRMSNorm])

    # Data for the B current
    freqArrayB, fftArrayB = tools.calcFFT(isb, tsb)
    freqOfHarmB, fftOfHarmB = tools.harmonics(freqArrayB, fftArrayB, h1,
                                        maxHarmonicNumber, 
                                        freqSearchInterval)
    h1b = fftOfHarmB[1]
    h2b = fftOfHarmB[2]
    h3b = fftOfHarmB[3]

    isbAve = sum(isb)/len(isb)
    isbRMS = tools.RMS(isb, h1, tsb)
    isbRMSNorm = [i/baseCurrentRMS for i in isbRMS]
    isbTupples.append([h1b, h2b, h3b, isbAve, isbRMSNorm])
    
    # Data for the C current
    freqArrayC, fftArrayC = tools.calcFFT(isc, tsc)
    freqOfHarmC, fftOfHarmC = tools.harmonics(freqArrayC, fftArrayC, h1,
                                            maxHarmonicNumber, 
                                            freqSearchInterval) 
    h1c = fftOfHarmC[1]
    h2c = fftOfHarmC[2]
    h3c = fftOfHarmC[3]
  
    iscAve = sum(isc)/len(isc)
    iscRMS = tools.RMS(isc, h1, tsc)
    iscRMSNorm = [i/baseCurrentRMS for i in iscRMS]
    iscTupples.append([h1c, h2c, h3c, iscAve, iscRMSNorm])

# (3) Check for fault status and fault modes.
# Fault status can be True if fault occurs or False, otherwise.
# Fault mode 1 -> 2 open-switches in one leg.
#            2 -> 1 open-switch.
#            3 -> 2 open-switches in upper leg positions or in the 
#                 lower leg positions.
#            4 -> 2 open-switches: 1 in the upper part and 1 in the
#                 lower part. 

faultList = []
h21Threshold = .10
h31Threshold = .10
for index in range(maxTime):
    # Relative frequency h21x = (harmonic 2)/(harmonic 1) 
    # from x = a,b,c.
    try:
        h21a = isaTupples[index][indexH2]/isaTupples[index][indexH1]
        h21b = isbTupples[index][indexH2]/isbTupples[index][indexH1]
        h21c = iscTupples[index][indexH2]/iscTupples[index][indexH1]

        h31a = isaTupples[index][indexH3]/isaTupples[index][indexH1]
        h31b = isbTupples[index][indexH3]/isbTupples[index][indexH1]
        h31c = iscTupples[index][indexH3]/iscTupples[index][indexH1]
    except ZeroDivisionError as err:
        print("Zero division error. Check the first harmonics. ", err)
        raise SystemExit

    faultStatus = False
    faultMode = 0
    # Check for faults 
    if ((max(isaTupples[index][indexRMS]) <= infCurrentLimit) or
        (max(isbTupples[index][indexRMS]) <= infCurrentLimit) or
        (max(iscTupples[index][indexRMS]) <= infCurrentLimit)):
        faultStatus = True
    elif ((h21a >= h21Threshold) or 
          (h21b >= h21Threshold) or
          (h21c >= h21Threshold)):
          faultStatus = True
    
    # Check for fault modes.
    if faultStatus:
        if ((max(isaTupples[index][indexRMS]) <= infCurrentLimit) or
            (max(isbTupples[index][indexRMS]) <= infCurrentLimit) or
            (max(iscTupples[index][indexRMS]) <= infCurrentLimit)):
            faultMode = 1
        elif not ((h31a >= h31Threshold) or
            (h31b >= h31Threshold) or
            (h31c >= h31Threshold)):
            faultMode = 2

    faultList.append([faultStatus, faultMode])
    
print("Fault list")
print(faultList)













