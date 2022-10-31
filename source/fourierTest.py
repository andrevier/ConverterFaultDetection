# Test the fourier analysis.
import tools
import numpy as np
import matplotlib.pyplot as plt
import random

# Peak voltage
VmaxPk = 2

# Sinusoidal frequency
Fi = 2000

# Sample rate of 44.1kHz
Fs = 44.1e3

# Duration of the sinusoid
Tstop = 50e-3

# Time input vector
N = int(Tstop/(1/Fs))
t = np.linspace(0, Tstop, N)

inputVmax = VmaxPk*np.sin(2*np.pi*Fi*t)
input2 = VmaxPk/2*np.sin(2*np.pi*2*Fi*t)
input4 = VmaxPk/3*np.sin(2*np.pi*4*Fi*t)
input6 = VmaxPk/6*np.sin(2*np.pi*6*Fi*t)

ran = np.ones(len(t))
for i in range(len(t)):
    ran[i] = random.random()*VmaxPk/6
inputVmax = input2 + input4 + input6 + ran + inputVmax

plt.plot(t, inputVmax)
plt.show()

x, y = tools.calcFFT(inputVmax, 1/Fs)

plt.plot(x, y)
plt.title("Spectrum analysis")
plt.xlabel("Frequency(Hz)")
plt.ylabel("Intensity")
plt.show()