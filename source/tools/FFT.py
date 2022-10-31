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
