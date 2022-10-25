import numpy as np

def RMS(signal, freq, samplingPeriod):
    # Calculate a windowed RMS value of a signal with sum of squares and
    # dividing by the number of elements in the interval of the fundamental
    # frequency.
    # signal - numpy array with the samples.
    # freq - fundamental frequency.
    # samplingPeriod - the time between two samples.
    # Numpy array to collect all the square points in the fundamental
    # period.
    # Number of points inside the fundamental period.
    T = 1/float(freq)
    n = T//samplingPeriod
    signalSquares = np.zeros(int(n))
    RMS = np.zeros(len(signal))

    j = 0
    for i in range(len(signal)):
        if (i > 0):
            RMS[i] = RMS[i-1]
        
        signalSquares[j] = signal[i]**2

        if (j == n-1):
            RMS[i] = np.sqrt(np.sum(signalSquares)/n)
            j = 0
        else:
            j += 1

    return RMS

def trueRMS(signal, freq, samplingPeriod):
    # Calculate a windowed RMS value of a signal with trapezoidal integration
    # from numpy library and divide by in the interval of the fundamental
    # frequency.
    # signal - numpy array with the samples.
    # freq - fundamental frequency.
    # samplingPeriod - the time between two samples.
    # Numpy array to collect all the square points in the fundamental
    # period.
    # Number of points inside the fundamental period.
    T = 1/float(freq)
    n = T//samplingPeriod
  
    signalSquare = np.zeros(int(n))
    RMS = np.zeros(len(signal))
        
    j = 0
    for i in range(len(signal)):
        if (i > 0):
            RMS[i] = RMS[i-1]

        signalSquare[j] = signal[i]**2

        if (j == (n - 1)):
            RMS[i] = np.sqrt(np.trapz(signalSquare, x=None,
                             dx=samplingPeriod)/T)
            j = 0
        else:
            j += 1
    return RMS
