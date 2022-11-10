"""
Implement the diagnostic method of the paper:
A Diagnostic Method of Simultaneous OpenSwitch Faults in Inverter-Fed 
Linear Induction Motor Drive for Reliability Enhancement.
Authors: 
Jung-Hyun Choi, Sanghoon Kim, Dong Sang Yoo, and Kyeong-Hwa Kim
Link: https://ieeexplore.ieee.org/document/6994788
date: 04/11/2022
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import tools 

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

# List to record 1s intervals of simulation.
ocCurrentsIntervals = []

for i in range(10):
    IsOCArray = IsOpenCircuit[(IsOpenCircuit[TIME] >= i) 
                               & (IsOpenCircuit[TIME] <= i+1)]
    ocCurrentsIntervals.append(IsOCArray)

# Normal simulation.
# Get the first 3 harmonics: h1 = 50 Hz, h2 = 100 Hz and h3 = 150 Hz.
h1 = 50
maxHarmonicNumber = 3
freqSearchInterval = 5
infCurrentLimit = 0.1
timeInterval = 1.0

isa = ocCurrentsIntervals[3][PHASEA]
isb = ocCurrentsIntervals[3][PHASEB]
isc = ocCurrentsIntervals[3][PHASEC]

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


# plt.plot([i*tsa for i in range(len(isaRMS))], isaRMS)
# plt.title("True RMS of the normal phase A")
# plt.xlabel("Time(s)")
# plt.ylabel("Stator Current (A)")
# plt.show()

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

# Relative frequency (harmonic 2)/(harmonic 1)
try:
    h21a = h2a/h1a
    h21b = h2b/h1b
    h21c = h2c/h1c
except ZeroDivisionError as err:
    print("Zero division error. Check the first harmonics. ", err)

# Fault condition.
# if ((isaRMS <= infCurrentLimit) or
#     (isbRMS <= infCurrentLimit) or
#     (iscRMS <= infCurrentLimit)):
#     print("Fault type 1")
# else if (h21a >=)








