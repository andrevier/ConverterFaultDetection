import numpy as np
import scipy

def calcFFT(signal, Ts):
    # Calculates the real part of the Fast Fourier Transform (fft) with
    # the scipy package for an array of samples 'signal'.
    # Return f array with the frequencies and Y1 with array with an 
    # intensity for each frequency.
    # The output can be used to plot results as: 
    # matplotlib.pyplot.plot(f, Y1)
    # 'signal' is a numpy array with (1xN) dimension.
    # 'Ts' is the sample period of the signal.
    # The input signal is corrected to have an even number of samples.   
    N = len(signal)
    
    # Correct the length of the signal is it is odd.
    if (N%2 != 0):
        signal = np.append(signal, [0])
        N = len(signal)
    
    # Calculate the Fourier transform of the signal.
    Y2 = scipy.fft.fft(signal)*Ts
    Y1 = np.abs(Y2)[0:N//2]
    Y1[1:] = 2*Y1[1:]      
  
    # Calculate the range of the frequencies based on the sample rate.
    #f = (1/Ts)*np.arange(0, N//2, 1)/N
    f = scipy.fft.fftfreq(N, Ts)[0:N//2]
       
    return (f, Y1)

def harmonics(x, Y, f1, n, interval=10):
    # Return an array 'h' with (n+1) dimensions with of the first 'n'
    # harmonics from the Y spectrum.
    # The function add all intensities of the near frequencies within
    # the interval to the intensities of the harmonic frequency.
    # Y : spectrum with intensities in the frequencies.
    # x : frequencies which index correspond to the intensities
    # in Y.
    # n : number of harmonic frequencies in the vector.
    fftList = [0.]*(n + 1)

    freqList = [i*float(f1) for i in range(n+1)]

    for k in range(0, len(freqList)):
        # Find the indexes of the frequencies in the frequency vector
        # near the interval established.
        indexArray = np.where((x >= freqList[k] - interval) 
                               & (x <= freqList[k] + interval))[0]
        
        # Those neighbour frequencies are incremented in the harmonic
        # frequency position.
        for j in indexArray:
            fftList[k] = fftList[k] + Y[j]
    return freqList, fftList,

def checkHarmonic(x, Y, f1, interval=10):
    # Check the frequency first harmonic of a signal based on the f1 
    # position and nearby frequencies.
    indexesOfFreq = np.where((x >= f1 - interval) & (x <= f1 + interval))[0]
    
    fftValues = Y[indexesOfFreq]
    maxFFT= np.max(fftValues)
    maxFFTIndex = np.where(Y == maxFFT)[0]
    return maxFFT, maxFFTIndex

def getHighestFFT(x, Y):
    # Return the tupple (frequency,fft) with the highest fft.
    highestFFT = 0.
    highestFreq = 0. 

    # For each element of x.
    for i in range(len(x)):
        if Y[i] >= highestFFT:
            highestFFT = Y[i]
            highestFreq = x[i]
    return highestFreq, highestFFT