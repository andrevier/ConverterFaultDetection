''' 
Plots data from the open and short-circuit simulations for the model 15
induction motor from the MATLAB preset. The model has scalar control, 
a fan load, and nominal speed.

Summary 
1) Normal Operation
1.1) Frequency domain plots.

2) Open-circuit simulation.
2.1) Frequency domain plots. 

3) Short-circuit simulation.
3.1) Frequency domain plots.

Date: 25/10/2022
'''
 
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

import tools 

# Select to plot or not
togglePlot = False

# Nominal frequency
fn = 50.0

# Sample period
Ts = 1.0e-6

# 1) Normal operation. 
# Import data from the simulation of open circuit with the model 15 at full
# speed.
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
    plt.title("Three-phase currents.")
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
beforeFaultA = 4.0
beforeFaultB = 5.0
afterFaultA = 5.5
afterFaultB = 6.5

# Transform dataframe.series into numpy array.
IsAArray = IsOpenCircuit[PHASEA][
    (IsOpenCircuit[TIME] > beforeFaultA) 
    & (IsOpenCircuit[TIME] < beforeFaultB)].values

xf, yf, N = tools.FFT.calcFFT(IsAArray, beforeFaultA - beforeFaultB)
intensity = 2.0/N*np.abs(yf[N//2+1:])

if (togglePlot):
    plt.plot(xf, intensity)
    plt.title("Phase A current Fourier analysis.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

if (togglePlot):
    xfbar = [0.0, fn*2, fn*3, fn*4, fn*5, fn*6]
    yfbar = [] 
    j = 0
    for i in range(len(xf)):
        if (i == 0 or i%fn == 0):
            yfbar.append(intensity[i])
            j += 1
        if (j == len(xfbar)):
            break
    
    plt.bar(xfbar, yfbar)
    plt.title("Phase A current harmonic frequencies.")
    plt.xlabel("Harmonic frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# RMS of the signal
signalRMS = tools.RMS(IsAArray, fn, Ts)

if (togglePlot):
    plt.plot([i*1.0e-6 for i in range(len(signalRMS))], signalRMS)
    plt.title("True RMS of the phase A normal")
    plt.xlabel("Time(s)")
    plt.ylabel("Stator Current (A)")
    plt.show()

# Normalized version of the plot.
ratio = 1
normalIsA = IsAArray/np.max(IsAArray)*ratio

xf, yf, N = tools.calcFFT(normalIsA, beforeFaultA - beforeFaultB)

if (togglePlot):
    plt.plot(xf, 2.0/N*np.abs(yf[N//2+1:]))
    plt.title("Phase A current (normalized).")
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
    (IsOpenCircuit[TIME] > afterFaultA) 
    & (IsOpenCircuit[TIME] < afterFaultB)].values

xfOC, yfOC, NOC = tools.calcFFT(IsAOpenCircuitFault, afterFaultA - afterFaultB)

if (togglePlot):
    plt.plot(xfOC, 2.0/NOC*np.abs(yfOC[NOC//2+1:]))
    plt.title("Open-circuit phase A current.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# Normalized version of the plot
normalIsAOpenCircuitFault = IsAOpenCircuitFault/np.max(IsAArray)*ratio

xfOC, yfOCN, NOC = tools.calcFFT(normalIsAOpenCircuitFault, 
                               afterFaultA - afterFaultB) 

if (togglePlot):
    plt.plot(xfOC, 2.0/NOC*np.abs(yfOCN[NOC//2+1:]))
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
    (IsShortCircuit[TIME] > afterFaultA) 
    & (IsShortCircuit[TIME] < afterFaultB)].values

xfSC, yfSC, NSC = tools.calcFFT(IsAShortCircuitFault, afterFaultA - afterFaultB)

if (togglePlot):
    plt.plot(xfSC, 2.0/NSC*np.abs(yfSC[NSC//2+1:]))
    plt.title("Short-circuit phase A current.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()

# Normalized version of the plot
normalIsAShortCircuit = IsAShortCircuitFault/np.max(IsAArray)*ratio

xfSC, yfSC, NSC = tools.calcFFT(normalIsAShortCircuit, afterFaultA - afterFaultB)

if (togglePlot):
    plt.plot(xfSC, 2.0/NSC*np.abs(yfSC[NSC//2+1:]))
    plt.title("Short-circuit phase A current normalized.")
    plt.xlabel("Frequencies (Hz)")
    plt.ylabel("Intensity")
    plt.show()