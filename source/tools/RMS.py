import numpy as np

def RMS(signal, freq, samplingPeriod) -> float:
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

def RMS2(signal) -> float:
    # Calculate a windowed RMS value of a signal with sum of mean 
    # squares and divide by the number of elements of the signal.
    # The difference between this function and RMS is that the later
    # divide the signal in steps with size of the period. 
    # signal - numpy array with the samples.
    # freq - fundamental frequency.
    # samplingPeriod - the time between two samples.
    signalSquares = 0.0
    if len(signal) == 0:
        print("Input signal must be a non-zero array.")
        raise ZeroDivisionError

    for data in signal:
        signalSquares = signalSquares + data**2

    return np.sqrt(signalSquares/len(signal))
