import numpy as np

def RMS(signal, freq, samplingPeriod):
    # Calculate a windowed RMS value of a signal with sum of mean 
    # squares and divide by the number of elements in the interval
    # of the fundamental frequency.
    # signal - numpy array with the samples.
    # freq - fundamental frequency.
    # samplingPeriod - the time between two samples.
    # The function return RMS array with the same length of the 
    # input signal.

    # n is the number of points inside the fundamental period.
    try: 
        T = 1/float(freq)
        n = T//samplingPeriod
    except ZeroDivisionError as err:
        print("Zero division error " + str(err) + ". In function RMS:" +
        " freq or " + "samplingPeriod are 0.")
        raise SystemExit

    signalSquares = 0
    RMS = [0]
    RMSValue = 0

    # RMS and signal have the same number of elements while the 
    # signalSquares has n at most.  
    j = 0
    for data in signal:
        signalSquares = signalSquares + data**2

        if (j >= n-1):
            try:
                RMSValue = np.sqrt(signalSquares/n)
            except ZeroDivisionError as err:
                print("Zero division error " + str(err) +
                      " in line 35 of RMS")
                raise SystemExit

            RMS.append(RMSValue)
            signalSquares = 0
            j = 0
        else:
            RMS.append(RMSValue)
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
