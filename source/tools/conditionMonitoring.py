import tools
import numpy
import scipy

class ConditionMonitoring:
    def __init__(self, Ia, Ib, Ic, lineFrequency, baseCurrentRMS, Ts,
                 infCurrentBound=0.1, h21Bound=0.1, h31Bound=0.1):
        '''Class to check the state of the three phase motor drive
        system based on the stator currents (Ia, Ib and Ic), line 
        frequency (lineFrequency) and base current (baseCurrentRMS), 
        sample period (Ts) and bounderies:
        infCurrentBound -> detect leg open-circuit.
        h21Bound and h31Bound -> detect open-circuit in switches.
        '''
        # Assign input data to attributes: 
        # Stator Currents
        self._Ia = Ia
        self._Ib = Ib
        self._Ic = Ic

        # Line Frequency of first harmonic frequency.
        self._lineFrequency = lineFrequency

        # Base RMS current of the motor.
        self._baseCurrent = baseCurrentRMS

        # Sampling period.
        self._Ts = Ts

        # Parameters to detect irregularities.
        self._infCurrentBound = infCurrentBound
        self._h21Bound = h21Bound
        self._h31Bound = h31Bound

        # Average current of the interval.
        self._IaAve = 0.
        self._IbAve = 0.
        self._IcAve = 0.

        # RMS current of the interval.
        self._IaRMS = 0.
        self._IbRMS = 0.
        self._IcRMS = 0.

        # FFT and the corresponding frequency list for each phase.
        self._IaFFT = list()
        self._IaFreq = list()

        self._IbFFT = list()
        self._IbFreq = list()

        self._IcFFT = list()
        self._IcFreq = list()

        # List with the first 3 harmonics and corresponding frequencies.
        self._IaFreqList = list()
        self._IaFFTList = list()
        
        self._IbFreqList = list()
        self._IbFFTList = list()
        
        self._IcFreqList = list()
        self._IcFFTList = list()

        # Fault state: 0 -> normal; 1 -> fault.
        self._faultState = 0
        
        # Fault mode: {0,1,2,3,4} depending on the number of fault 
        # switches.
        self._faultMode = 0
        
        # Relative FFTs
        #  I21x = (FFT from 2nd harmonic) / (FFT from 1st harmonic)
        # x = current phases a,b or c.
        self._I21a = 0.
        self._I21b = 0.
        self._I21c = 0.
        self._I31a = 0.
        self._I31b = 0.
        self._I31c = 0.

        # State of the switches. Normal state is 0 and the integer 
        # corresponding the index is a fault state.
        self._T1 = 0
        self._T2 = 0
        self._T3 = 0
        self._T4 = 0
        self._T5 = 0
        self._T6 = 0

    def setAverageCurrent(self):
        '''Calculate and return a tupple with average input currents 
        with all the input interval. 
        Return tupple: average(Ia, Ib, Ic)'''
        try:
            self._IaAve = sum(self._Ia)/len(self._Ia)
            self._IbAve = sum(self._Ib)/len(self._Ib)
            self._IcAve = sum(self._Ic)/len(self._Ic)
        except ZeroDivisionError as err:
            print("Current array length must be non-zero.")
            raise ZeroDivisionError 

    def getAverageCurrent(self):
        return (self._IaAve,self._IbAve,self._IcAve)
    
    def setRMSValues(self):
        '''Calculate the RMS values of the currents calculated with
        all the input interval.
        '''
        self._IaRMS = ConditionMonitoring.RMS(self._Ia)
        self._IbRMS = ConditionMonitoring.RMS(self._Ib)
        self._IcRMS = ConditionMonitoring.RMS(self._Ic)
        
    def getRMSValues(self):
        return (self._IaRMS,self._IbRMS,self._IcRMS)

    def getNormalRMSValues(self):
        '''Calculate and return a tupple with the normalized RMS 
        values of the currents calculated with all the input interval.
        Return tupple: RMS(Ia, Ib, Ic)'''
        try:
            IaRMSN = self._IaRMS/self._baseCurrent
            IbRMSN = self._IbRMS/self._baseCurrent
            IcRMSN = self._IcRMS/self._baseCurrent
        except ZeroDivisionError as err:
            print("Base current must be non zero.")
            raise ZeroDivisionError 
        return (IaRMSN,IbRMSN,IcRMSN)

    @staticmethod
    def FFT(signal, Ts):
        '''Calculates the real part of the Fast Fourier Transform (fft)
        with the scipy package for an array of samples 'signal'.
        Return f array with the frequencies and Y1 with array with an
        intensity for each frequency.
        The output can be used to plot results as: 
        matplotlib.pyplot.plot(f, Y1)
        'signal' is a numpy array with (1xN) dimension.
        'Ts' is the sample period of the signal.
        The input signal is corrected to have an even number of 
        samples. '''

        N = len(signal)
        
        # Correct the length of the signal is it is odd.
        if (N%2 != 0):
            signal = numpy.append(signal, [0])
            N = len(signal)
        
        # Calculate the Fourier transform of the signal.
        Y2 = scipy.fft.fft(signal)*Ts
        Y1 = numpy.abs(Y2)[0:N//2]
        Y1[1:] = 2*Y1[1:]      
    
        # Calculate the range of the frequencies based on the sample rate.
        #f = (1/Ts)*np.arange(0, N//2, 1)/N
        f = scipy.fft.fftfreq(N, Ts)[0:N//2]
        
        return (f, Y1)
    
    @staticmethod
    def harmonics(x, Y, f1, n, interval=10):
        '''Calculate and return an array 'h' with (n+1) dimensions with
        of the first 'n' harmonics from the Y spectrum.
        The function add all intensities of the near frequencies within
        the interval to the intensities of the harmonic frequency.
        Y : spectrum with intensities in the frequencies.
        x : frequencies which index correspond to the intensities
        in Y.
        n : number of harmonic frequencies in the vector.'''
        fftList = [0.]*(n + 1)

        freqList = [i*float(f1) for i in range(n+1)]

        for k in range(0, len(freqList)):
            # Find the indexes of the frequencies in the frequency vector
            # near the interval established.
            indexArray = numpy.where((x >= freqList[k] - interval) 
                                     & (x <= freqList[k] + interval))[0]
            
            # Those neighbour frequencies are incremented in the harmonic
            # frequency position.
            for j in indexArray:
                fftList[k] = fftList[k] + Y[j]
        return freqList, fftList

    def checkFaultState(self):
        '''Method to check the fault state according to the Jung-Hyun
        Choi algorithm. Fault state can be 0 if the system is normal 
        or 1 if there is a fault.
        The detection is based on the normalized RMS current and the 
        boundarie for the relative harmonic FFTs:
        2nd harmonic FFT / 1st harmonic FFT.
        boundaries are set in the constructor.'''
        self._faultState = 0
        
        (IaRMSN, IbRMSN, IcRMSN) = self.getNormalRMSValues()
        
        # Condition for open-circuit in a leg.
        if ((IaRMSN <= self._infCurrentBound) or
            (IbRMSN <= self._infCurrentBound) or
            (IcRMSN <= self._infCurrentBound)):
            self._faultState = 1
        elif ((self._I21a >= self._h21Bound) or 
             (self._I21b >= self._h21Bound) or
             (self._I21c >= self._h21Bound)):
            self._faultState = 1

        return self._faultState

    def getFaultState(self):
        '''Return the current fault state of the system.'''
        return self._faultState
    
    def checkFaultMode(self):
        '''Check for fault modes. Return integer from 0 to 4 
        corresponding to the number of open-circuit switches in the
        inverter.
        Fault mode 0 -> normal state. 
                   1 -> 2 open-switches in one leg.
                   2 -> 1 open-switch.
                   3 -> 2 open-switches in upper leg positions or
                        in the lower leg positions.
                   4 -> 2 open-switches: 1 in the upper part and 1
                        in the lower part. '''
        self._faultMode = 0
        
        (IaRMSN, IbRMSN, IcRMSN) = self.getNormalRMSValues()
        
        if self._faultState == 1:
            # Open-Circuit of two switches in the same leg.
            if ((IaRMSN <= self._infCurrentBound) or
                (IbRMSN <= self._infCurrentBound) or
                (IcRMSN <= self._infCurrentBound)):
                self._faultMode = 1
            # One switch only.
            elif not ((self._I31a >= self._h31Bound) 
                    or (self._I31b >= self._h31Bound) 
                    or (self._I31c >= self._h31Bound)):
                self._faultMode = 2

        return self._faultMode
    
    def getFaultMode(self) -> int:
        '''Return the current fault mode of the system.'''
        return self._faultMode

    def checkSwitchesState(self):
        '''Detect fault switch according to the RMS currents and 
        average value.'''
        self._T1 = 0
        self._T2 = 0
        self._T3 = 0
        self._T4 = 0
        self._T5 = 0
        self._T6 = 0
        
        minElement = self._getMin(self._IaFFTList[1], 
                                  self._IbFFTList[1], self._IcFFTList[1])
        
        # Inverter leg faults.
        if self._faultMode == 1:
            if minElement == 1:
                self._T1 = 1
                self._T4 = 4
            elif minElement == 2:
                self._T3 = 3
                self._T6 = 6
            elif minElement == 3:
                self._T2 = 2
                self._T5 = 5

        # Problem.
        if self._faultMode == 2:
            if minElement == 1:
                if self._IaAve < 0:
                    self._T1 = 1
                else:
                    self._T4 = 4
            elif minElement == 2:
                if self._IbAve < 0:
                    self._T3 = 3
                else:
                    self._T6 = 6
            elif minElement == 3:
                if self._IcAve < 0:
                    self._T5 = 2
                else:
                    self._T2 = 5 

        return self._T1, self._T2, self._T3, self._T4, self._T5, self._T6

    def getSwitchesState(self):
        '''Return a tupple with the current state of the switches.
        0 if normal; 1 if it has a fault.
        Return tupple: (T1,T2,T3,T4,T5,T6)'''
        return self._T1, self._T2, self._T3, self._T4, self._T5, self._T6

    def getRelativeFFTs(self):
        '''Return a tupple with the current values of the relative 
        FFTs.
        I21x = (FFT from 2nd harmonic) / (FFT from 1st harmonic)
        I31x = (FFT from 3rd harmonic) / (FFT from 1st harmonic)
        x = current phases a,b or c.
        Return tupple: (I21a,I21b,I21c,I31a,I31b,I31c)
        '''
        return (self._I21a,self._I21b,self._I21c,
                self._I31a,self._I31b,self._I31c)
    
    def checkIaFreqAndFFT(self, n):
        '''Method to calculate and return a list with the first n
        harmonic frequencies and FFT values from the phase-A current,
        with the DC value at the index 0.
        Return tupple: (Ia frequencies, Ia FFTs)'''
        return ConditionMonitoring.harmonics(self._IaFreq, self._IaFFT,
                                    self._lineFrequency, n)
    
    def getIaFreqAndFFT(self):
        return self._IaFreqList, self._IaFFTList
    
    def getIbFreqAndFFT(self):
        return self._IbFreqList, self._IbFFTList
    
    def getIcFreqAndFFT(self):
        return self._IcFreqList, self._IcFFTList
        
    def checkIbFreqAndFFT(self, n):
        '''Method to calculate and return a list with the first n
        harmonic frequencies and FFT values from the phase-B current,
        with the DC value at the index 0.
        Return tupple: (Ib frequencies, Ib FFTs)'''
        return ConditionMonitoring.harmonics(self._IbFreq, self._IbFFT,
                                    self._lineFrequency, n)

    def checkIcFreqAndFFT(self, n):
        '''Method to calculate and return a list with the first n
        harmonic frequencies and FFT values from the phase-C current,
        with the DC value at the index 0.
        Return tupple: (Ic frequencies, Ic FFTs)'''
        return ConditionMonitoring.harmonics(self._IcFreq, self._IcFFT,
                                    self._lineFrequency, n)
    
    def getFFTs(self):
        '''Return a tupple with FFTs of the current input
        currents in the interval.
        Return tuple: FFT(Ia,Ib,Ic)'''
        return (self._IaFFT,self._IbFFT,self._IcFFT)

    def getFreqOfFFT(self):
        '''Return a tupple with frequencies matching the FFTs of the
        current input currents in the interval.
        Return tuple: FFT(Ia,Ib,Ic)'''
        return (self._IaFreq,self._IbFreq,self._IcFreq)

    def _getMin(self, a, b, c) -> int:
        ''' Method to get the minimum value of 3 numbers.
        If a is minimum, return 1;
        If b is minimum, return 2;
        If c is minimum, return 3;
        If a == b == c, return 0.'''
        if ((a < b) and (a < c)):
            return 1
        if ((b < a) and (b < c)):
            return 2
        if ((c < a) and (c < b)):
            return 3
        return 0
    
    @staticmethod
    def RMS(signal) -> float:
        '''Calculate a windowed RMS value of a signal with sum of mean
        squares and divide by the number of elements of the signal.
        The difference between this function and RMS is that the later
        divide the signal in steps with size of the period. 
        signal - numpy array with the samples.
        freq - fundamental frequency.
        samplingPeriod - the time between two samples.'''
        signalSquares = 0.0
        if len(signal) == 0:
            print("Input signal must be a non-zero array.")
            raise ZeroDivisionError

        for data in signal:
            signalSquares = signalSquares + data**2

        return numpy.sqrt(signalSquares/len(signal))

    def checkSystemStateWithJHC(self):
        '''Method to run the Jung-Hyun Choi algorithm to check the
        condition of the system: fault or not; and if a fault is
        detected, give the mode of the fault related to the number
        of the switches and which switch is faulty.'''
        
        # Calculate FFTs and corresponding frequencies.
        self._IaFreq, self._IaFFT = ConditionMonitoring.FFT(
                                        self._Ia, self._Ts)
        self._IbFreq, self._IbFFT = ConditionMonitoring.FFT(
                                        self._Ib, self._Ts)
        self._IcFreq, self._IcFFT = ConditionMonitoring.FFT(
                                        self._Ic, self._Ts)

        # Get the first 3 harmonics.
        self._IaFreqList, self._IaFFTList = self.checkIaFreqAndFFT(3)
        self._IbFreqList, self._IbFFTList = self.checkIbFreqAndFFT(3)
        self._IcFreqList, self._IcFFTList = self.checkIcFreqAndFFT(3)

        # Relative frequencies
        try: 
            self._I21a = self._IaFFTList[2]/self._IaFFTList[1]
            self._I21b = self._IbFFTList[2]/self._IbFFTList[1]
            self._I21c = self._IcFFTList[2]/self._IcFFTList[1]

            self._I31a = self._IaFFTList[3]/self._IaFFTList[1]
            self._I31b = self._IbFFTList[3]/self._IbFFTList[1]
            self._I31c = self._IcFFTList[3]/self._IcFFTList[1]
        except ZeroDivisionError as err:
            print("Zero division error. Check the first harmonics. ", err)
            raise SystemExit
        
        self.setRMSValues()
        self.checkFaultState()

        self.checkFaultMode()
        
        self.setAverageCurrent()
        self.checkSwitchesState()
        