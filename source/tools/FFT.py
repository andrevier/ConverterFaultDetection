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
    return freqList, fftList

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

def checkHarmonics(x, Y, h1, numberOfElements):
    # Check the existence of approximate multiples of frequency h1.
    # Receive two lists: x with the frequencies and Y with the 
    # corresponding FFT values. 
    zipped = zip(x,Y)
    
    # Create a list to record the tupple (freq, FFT) 
    harmonicList = []

    # L is the length of interval to check approximate multiples.
    L = 3
    i = 0

    for item in zipped:
        if ((item[0] >= i*h1 - L) and (item[0] <= i*h1 + L)):
            harmonicList.append(item)
        if i == numberOfElements:
            break
        i += 1
    
    # Unzipping the tupples.
    selectedFreq, selectedY = zip(*harmonicList)
    return selectedFreq, selectedY