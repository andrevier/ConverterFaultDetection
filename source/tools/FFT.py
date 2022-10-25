import numpy as np
import scipy

def calcFFT(signal, duration):
    # Calculates the real part of the fft with the scipy package for an
    # array of samples 'signal'. The duration of the time collected is
    # seconds.
    # Return x-axis with the frequencies, y-axis with an intensity for each
    # frequency, and the number of samples corrected N.
    # The output can be used to plot results as: 
    # matplotlib.pyplot.plot(x, 2/N*numpy.abs(y[N//2+1:]))
    # The signal is correct to have an even number of samples N.   
    N = len(signal)

    # Correction of the number of samples if it's not even.
    if (N%2 != 0):
        signal = signal[:N-1]
        N = len(signal)
    
    period = duration/N
    
    yf = scipy.fft.fft(signal)
    xf = scipy.fft.fftfreq(N, period)[N//2+1:]
    
    return (xf, yf, N)
