# Script to test the function tools.checkHarmonic
import numpy as np
import random
import matplotlib.pyplot as plt
import tools

# Peak voltage
VmaxPk = 2

# Actual sinusoidal frequency.
Fi = 2010

# Nominal sinusoidal frequency.
Fn = 2000

# Sample frequency.
Fs = 50e3

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
    ran[i] = random.random()*VmaxPk/8
inputVmax = input2 + input4 + input6 + ran + inputVmax

# Calculate FFT
x, y = tools.calcFFT(inputVmax, 1/Fs)
f1Freq, f1FFT = tools.getHighest(x, y)
print("Results:")
print("calcFFT and getHighest")
print("highest fft {fft:.2f} with freq {freq:.2f}".format(fft=f1FFT, freq=f1Freq))

plt.plot(x, y)
plt.title("Fourier Analisis of the signal")
plt.show()

f1, f1Index = tools.checkHarmonic(x, y, f1Freq, interval=10)
print("checkHarmonic")
print("first harmonic: ", f1)
print("index: ", f1Index)
print("Check: ", x[f1Index])

freqList, fftList = tools.harmonics(x, y, f1Freq, 6)
print("harmonics")
print("Frequency list: ", freqList)
print("FFT list: ", fftList)