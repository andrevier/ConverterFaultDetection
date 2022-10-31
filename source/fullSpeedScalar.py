''' 
Plots data from the open and short-circuit simulations for the model 15
induction motor from the MATLAB preset. The model has scalar control, 
a fan load, and nominal speed.

Summary 
1) Normal operation and general plots.
1.1) Frequency domain plots.

2) Open-circuit simulation.
2.1) Frequency domain plots. 

3) Short-circuit simulation.
3.1) Frequency domain plots.

Date: 31/10/2022
'''
 
from re import I
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import tools 

# Select to plot or not
togglePlot = True

# Nominal frequency
fn = 50.0

# Sample period
Ts = 1.e-06

# 1) Normal operation and general plots. 
# Import data from the simulation of open circuit with the model 15 at
# full speed.
from Simulations.model15ScalarControl.openCircuit.T1FullSpeed import (
    Isa as IsAOpenCircuit,
    Isb as IsBOpenCircuit,
    Isc as IsCOpenCircuit,
    Te,
    wm,
    time as timeSeries,
    Vab as VABOpenCircuit
    )

# Make a dataframe with time and the currents.
IsOpenCircuit = pd.concat([timeSeries, IsAOpenCircuit,
                IsBOpenCircuit, IsCOpenCircuit],
                ignore_index=True, axis=1)

# Substitute the name by the columns' number.
TIME = 0
PHASEA = 1
PHASEB = 2
PHASEC = 3

# Steady-state plot of the currents.
if (togglePlot):
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEA], label="A")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEB], label="B")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Normal three-phase currents.")
    plt.xlim([4.02,4.08])
    plt.ylim([-15,15])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator Current (A)")
    plt.legend(["phase A", "phase B", "phase C"],
                bbox_to_anchor=(0.75,0.80))
    plt.show()

if (togglePlot):
    plt.plot(timeSeries, Te)
    plt.grid(color="gray", linewidth=0.5)
    plt.title("Electromagnetic torque.")
    plt.xlim([0, 10])
    plt.xlabel("Time(s)")
    plt.ylabel("Te")
    plt.show()

if (togglePlot):
    plt.plot(timeSeries, wm)
    plt.grid(color="gray", linewidth=0.5)
    plt.title("Rotor speed.")
    plt.xlabel("Time(s)")
    plt.ylabel("Speed")
    plt.show()

# 1.1) Frequency domain plots. 
# Time window before and after fault for the plots.
TIME_BEFORE_A = 4.0
TIME_BEFORE_B = 5.0
TIME_AFTER_A = 5.5
TIME_AFTER_B = 6.5

# Transform dataframe.series into numpy array.
IsAArray = IsOpenCircuit[PHASEA][
    (IsOpenCircuit[TIME] >= TIME_BEFORE_A) 
    & (IsOpenCircuit[TIME] <= TIME_BEFORE_B)].values

samplePeriod = (TIME_BEFORE_B - TIME_BEFORE_A)/len(IsAArray)
xf, yf = tools.calcFFT(IsAArray, samplePeriod)

if (togglePlot):
    plt.plot(xf, yf)
    plt.title("Normal phase A current Fourier analysis.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# RMS of the signal
signalRMS = tools.RMS(IsAArray, fn, samplePeriod)

if (togglePlot):
    plt.plot([i*1.0e-6 for i in range(len(signalRMS))], signalRMS)
    plt.title("True RMS of the normal phase A")
    plt.xlabel("Time(s)")
    plt.ylabel("Stator Current (A)")
    plt.show()

# Normalized version.
RATIO = 1
normalIsA = IsAArray/np.max(IsAArray)*RATIO
samplePeriod = (TIME_BEFORE_B - TIME_BEFORE_A)/len(normalIsA)
xf, yf = tools.calcFFT(normalIsA, samplePeriod)

if (togglePlot):
    plt.plot(xf, yf)
    plt.title("Normal phase A current (normalized).")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# 2) Open-Circuit simulation.
# Steady-state after the fault.
if (togglePlot):
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEA], label="A")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEB], label="B")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Steady-state after open-circuit fault.")
    plt.xlim([6.02,6.08])
    plt.ylim([-23,23])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator Current (A)")
    plt.legend(["phase A", "phase B", "phase C"],
               bbox_to_anchor=(0.80,0.90))
    plt.show()

if (togglePlot):
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEA], label="A")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEB], label="B")
    plt.plot(IsOpenCircuit[TIME],IsOpenCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Open-circuit fault.")
    plt.xlim([4.55, 5.05])
    plt.ylim([-23,23])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator Current (A)")
    plt.legend(["phase A", "phase B", "phase C"],
               bbox_to_anchor=(0.80,0.90))
    plt.show()

# 2.1)  Frequency domain plots. 
# Transform dataframe.series into numpy array.
IsAOpenCircuitFault = IsOpenCircuit[PHASEA][
    (IsOpenCircuit[TIME] > TIME_AFTER_A) 
    & (IsOpenCircuit[TIME] < TIME_AFTER_B)].values

samplePeriod = (TIME_AFTER_B - TIME_AFTER_A)/len(IsAOpenCircuitFault)
xfOC, yfOC = tools.calcFFT(IsAOpenCircuitFault, samplePeriod)

if (togglePlot):
    plt.plot(xfOC, yfOC)
    plt.title("Open-circuit phase A current.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# Normalized version of the plot
normalIsAOpenCircuitFault = IsAOpenCircuitFault/np.max(IsAArray)*RATIO

samplePeriod = (TIME_AFTER_B - TIME_AFTER_A)/len(normalIsAOpenCircuitFault)
xfOC, yfOCN = tools.calcFFT(normalIsAOpenCircuitFault, samplePeriod)

if (togglePlot):
    plt.plot(xfOC, yfOCN)
    plt.title("Open-circuit phase A current (normalized).")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# 3) Short-circuit simulation. 
from Simulations.model15ScalarControl.shortCircuit.T1FullSpeed import (
    Isa as IsAShortCircuit,
    Isb as IsBShortCircuit,
    Isc as IsCShortCircuit,
    Te as TeShortCircuit,
    wm as wmShortCircuit,
    time as timeSeries,
    Vab as VABShortCircuit
    )

# Make a dataframe with time and the currents.
IsShortCircuit = pd.concat([timeSeries, IsAShortCircuit,
                IsBShortCircuit, IsCShortCircuit],
                ignore_index=True, axis=1)

# Plot the steady-state after the fault.
if (togglePlot):
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEA], label="A")
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEB], label="B")
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Short-circuit three-phase currents.")
    plt.xlim([6.02,6.08])
    plt.ylim([-60,60])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator currents (A)")
    plt.legend(["phase A", "phase B", "phase C"],
                bbox_to_anchor=(0.75,0.80))
    plt.show()

if (togglePlot):
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEA], label="A")
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEB], label="B")
    plt.plot(IsShortCircuit[TIME],IsShortCircuit[PHASEC], label="C")
    plt.grid(color='gray', linewidth=0.5)
    plt.title("Short-circuit event.")
    plt.xlim([4.55,5.10])
    plt.ylim([-60,60])
    plt.xlabel("Time(s)")
    plt.ylabel("Stator currents (A)")
    plt.legend(["phase A", "phase B", "phase C"],
                bbox_to_anchor=(0.75,0.80))
    plt.show()

# 3.1) Frequency domain plots.
IsAShortCircuitFault = IsShortCircuit[PHASEA][
    (IsShortCircuit[TIME] > TIME_AFTER_A) 
    & (IsShortCircuit[TIME] < TIME_AFTER_B)].values

samplePeriod = (TIME_AFTER_B - TIME_AFTER_A)/len(IsAShortCircuitFault)
xfSC, yfSC = tools.calcFFT(IsAShortCircuitFault, samplePeriod)

if (togglePlot):
    plt.plot(xfSC, yfSC)
    plt.title("Short-circuit phase A current.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# Normalized version of the plot
normalIsAShortCircuit = IsAShortCircuitFault/np.max(IsAArray)*RATIO

samplePeriod = (TIME_AFTER_B - TIME_AFTER_A)/len(normalIsAShortCircuit)
xfSC, yfSC = tools.calcFFT(normalIsAShortCircuit, samplePeriod)

if (togglePlot):
    plt.plot(xfSC, yfSC)
    plt.title("Short-circuit phase A current normalized.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()