from .conditionMonitoring import ConditionMonitoring
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class AnalysisManager:
    _TIME = 0
    _PHASE = 1

    def __init__(self, Ia, Ib, Ic, lineFreq, baseCurrentRMS,
        timeInterval, maxTime, infCurrentBound, I21Bound, I31Bound):
        '''Helper class to run analysis and manage data from each
        simulation. Get the total simulation data, separate it into
        parts (timeInterval) and process it to generate parameters to
        understand the state of the system at that time interval. 
        Receive the main data from the simulation as input:
        Ia, Ib, Ic -> pandas dataframe with the time and the current
        value. Each column: {number, time, Ix}; x = a,b or c.
        lineFreq -> fundamental frequency of the line currents.
        timeInterval -> length of the time interval in which the 
        simulation is divided to process the data. 
        maxTime -> total time of the simulation.
        baseCurrentRMS -> RMS value of the base line currents.'''
        # Simulation data
        self._Ia = Ia
        self._Ib = Ib
        self._Ic = Ic
        self._lineFreq = lineFreq
        self._baseCurrent = baseCurrentRMS

        # size of time intervals
        self._timeInterval = timeInterval
        self._maxTime = maxTime
        self._numberOfIntervals = int(self._maxTime//self._timeInterval)

        # List to get match the parameters with their time step.
        self._timeList = []
        
        # Necessary bounds
        self._infCurrentBound = infCurrentBound
        self._I21Bound = I21Bound
        self._I31Bound = I31Bound

        # Initialize arrays to record data from each signal segment.
        self._phaseAHarmonics = np.zeros((self._numberOfIntervals,4))
        self._phaseBHarmonics = np.zeros((self._numberOfIntervals,4))
        self._phaseCHarmonics = np.zeros((self._numberOfIntervals,4))

        # Attributes to store harmonics
        self._harmonicRatio21 = np.zeros((self._numberOfIntervals,3))

        self._harmonicRatio31 = np.zeros((self._numberOfIntervals,3))

        # Average of each phase.
        self._average = np.zeros((self._numberOfIntervals,3))
        
        # RMS of each phase.
        self._RMS = np.zeros((self._numberOfIntervals,3))

        # List of fault states and fault mode: item (2.3)
        self._faultStateList = []
        self._faultModeList = []
        self._switchState = np.zeros((self._numberOfIntervals,6))

    def getTime(self):
        '''Return the time matching the parameters.'''
        return self._timeList
    
    def getIaHarmonics(self):
        '''Return the numpy array with the FFTs for the first 
        selected harmonics of phase A. The array has size: 
        (number of intervals x number of harmonics + 1)
        in the columns: DC value, 1st harmonic, 2nd harmonic, ...
        '''
        return self._phaseAHarmonics

    def getIbHarmonics(self):
        '''Return the numpy array with the FFTs for the first 
        selected harmonics of phase B. The array has size: 
        (number of intervals x number of harmonics + 1)
        in the columns: DC value, 1st harmonic, 2nd harmonic, ...
        '''
        return self._phaseBHarmonics
    
    def getIcHarmonics(self):
        '''Return the numpy array with the FFTs for the first 
        selected harmonics of phase C. The array has size: 
        (number of intervals x number of harmonics + 1)
        in the columns: DC value, 1st harmonic, 2nd harmonic, ...
        '''
        return self._phaseCHarmonics
    
    def getHarmonicRatio21(self):
        '''Return the numpy array with the FFT ratio of the 2nd
        harmonic to the 1st harmonic of the three phases.
        array size:
        (number of intervals x number of phases)
        in the columns: phase A, phase B, phase C.'''
        return self._harmonicRatio21
    
    def getHarmonicRatio31(self):
        '''Return the numpy array with the FFT ratio of the 2rd
        harmonic to the 1st harmonic of the three phases.
        array size:
        (number of intervals x number of phases)
        in the columns: phase A, phase B, phase C.'''
        return self._harmonicRatio31
    
    def getRMS(self):
        '''Return the numpy array with the RMS values of the currents
        in each time interval. Array size:
        (number of intervals x number of phases)
        in the columns: phase A, phase B, phase C.
        '''
        return self._RMS

    def getAverageCurrents(self):
        '''Return the numpy array with the average values of the three
        phase currents taken from each time interval. Array size:
        (number of intervals x number of phases)
        in the columns: phase A, phase B, phase C.'''
        return self._average
    
    def getFaultState(self):
        '''Return a list with the fault state detected from each time
        interval. 0 if normal state; 1 if there is a fault.'''
        return self._faultStateList
    
    def getFaultMode(self):
        '''Return a list with the fault mode detected in each time
        interval. List has size of the number of intervals. The values
        can be:
        Fault mode 0 -> normal state. 
                   1 -> 2 open-switches in one leg.
                   2 -> 1 open-switch.
                   3 -> 2 open-switches in upper leg positions or
                        in the lower leg positions.
                   4 -> 2 open-switches: 1 in the upper part and 1
                        in the lower part. '''
        return self._faultModeList
    
    def getSwitchStates(self):
        '''Return a numpy array with the state of the switches detected
        in each time interval. The array has size:
        (number of intervals x number of switches)
        The order of the columns are:
        T1, T2, T3, T4, T5, T6.'''
        return self._switchState
    
    def runAnalysis(self):
        '''Run analysis of the simulation data.'''
        for i in range(0,self._numberOfIntervals):
            # Divide the simulation into segments to calculate and analize the
            # parameters.
            self._timeList.append((i+1)*self._timeInterval)
            ia = self._Ia[(self._Ia[self._TIME] >= i*self._timeInterval)
                     & (self._Ia[self._TIME] <= (i+1)*self._timeInterval)]

            ib = self._Ib[(self._Ib[self._TIME] >= i*self._timeInterval)
                     & (self._Ib[self._TIME] <= (i+1)*self._timeInterval)]

            ic = self._Ic[(self._Ic[self._TIME] >= i*self._timeInterval)
                     & (self._Ic[self._TIME] <= (i+1)*self._timeInterval)]
            
            # 2.2) Record the main parameters from each interval
            # 2.2.1) Select the interval and convert the series into numpy arrays.
            ia0 = ia[self._PHASE].values
            ib0 = ib[self._PHASE].values
            ic0 = ic[self._PHASE].values

            # Sample period.
            tsa = self._timeInterval/len(ia)
            cm = ConditionMonitoring( 
                Ia=ia0, Ib=ib0, Ic=ic0, 
                lineFrequency=self._lineFreq,
                baseCurrentRMS=self._baseCurrent,
                Ts=tsa, infCurrentBound=self._infCurrentBound,
                h21Bound=self._I21Bound, h31Bound=self._I31Bound)
            
            # Run the algorithm.  
            cm.checkSystemStateWithJHC()

            # Get the data from the algorithm: 
            # first 3 harmonics; 
            IaFreq, IaFFT = cm.getIaFreqAndFFT()
            self._phaseAHarmonics[i,:] = IaFFT

            IbFreq, IbFFT = cm.getIbFreqAndFFT()
            self._phaseBHarmonics[i,:] = IbFFT

            IcFreq, IcFFT = cm.getIcFreqAndFFT()
            self._phaseCHarmonics[i,:] = IcFFT

            # Relative FFTs
            i21a, i21b, i21c, i31a, i31b, i31c = cm.getRelativeFFTs()
            
            self._harmonicRatio21[i,:] = [i21a, i21b, i21c]
            self._harmonicRatio31[i,:] = [i31a, i31b, i31c]
            
            # RMS;
            IaRMS, IbRMS, IcRMS = cm.getRMSValues()
            self._RMS[i,:] = [IaRMS, IbRMS, IcRMS]

            # Average currents;
            IaAve, IbAve, IcAve = cm.getAverageCurrent()
            self._average[i,:] = [IaAve, IbAve, IcAve]

            # Fault states, fault modes and switches' states.
            self._faultStateList.append(cm.getFaultState())
            self._faultModeList.append(cm.getFaultMode()) 

            switchStateTupple = cm.getSwitchesState()
            self._switchState[i,0] = switchStateTupple[0]
            self._switchState[i,1] = switchStateTupple[1]
            self._switchState[i,2] = switchStateTupple[2]
            self._switchState[i,3] = switchStateTupple[3]
            self._switchState[i,4] = switchStateTupple[4]
            self._switchState[i,5] = switchStateTupple[5]

    def plot(self, yAxisList, windowTitle=''):
        '''Helper method to plots.
        Recieve a list yAxisList with each element as a list of 
        elements to the plots. 
        Ex: [[Ia,Ib,Ic],[Iarms,Ibrms,Icrms], [faultState]]
        There are three plots. The y-axis of the first has all the 
        currents; The second has all the RMS values; and the third 
        has the fault states.
        keys:
        Ia, Ib, Ic : line currents.
        Iarms, Ibrms, Icrms
        '''
        yAxisDict = {"ia":[self._Ia[self._TIME].values,self._Ia[self._PHASE].values],
                    "ib": [self._Ib[self._TIME].values,self._Ib[self._PHASE].values],
                    "ic": [self._Ic[self._TIME].values,self._Ic[self._PHASE].values],
                    "iarms":[self._timeList, self._RMS[:,0]], 
                    "ibrms":[self._timeList,self._RMS[:,1]],
                    "icrms":[self._timeList,self._RMS[:,2]], 
                    "iaave":[self._timeList,self._average[:,0]],
                    "ibave":[self._timeList,self._average[:,1]],
                    "icave":[self._timeList,self._average[:,2]],
                    "i1a":[self._timeList,self._phaseAHarmonics[:,1]],
                    "i2a":[self._timeList,self._phaseAHarmonics[:,2]],
                    "i3a":[self._timeList,self._phaseAHarmonics[:,3]],
                    "i1b":[self._timeList,self._phaseBHarmonics[:,1]],
                    "i2b":[self._timeList,self._phaseBHarmonics[:,2]],
                    "i3b":[self._timeList,self._phaseBHarmonics[:,3]],
                    "i1c":[self._timeList,self._phaseCHarmonics[:,1]],
                    "i2c":[self._timeList,self._phaseCHarmonics[:,2]],
                    "i3c":[self._timeList,self._phaseCHarmonics[:,3]],
                    "i21a":[self._timeList,self._harmonicRatio21[:,0]],
                    "i31a":[self._timeList,self._harmonicRatio31[:,0]],
                    "i21b":[self._timeList,self._harmonicRatio21[:,1]],
                    "i31b":[self._timeList,self._harmonicRatio31[:,1]],
                    "i21c":[self._timeList,self._harmonicRatio21[:,2]],
                    "i31c":[self._timeList,self._harmonicRatio31[:,2]],
                    "faultstate":[self._timeList,self._faultStateList],
                    "faultmode":[self._timeList,self._faultModeList],
                    "t1":[self._timeList,self._switchState[:,0]],
                    "t2":[self._timeList,self._switchState[:,1]],
                    "t3":[self._timeList,self._switchState[:,2]],
                    "t4":[self._timeList,self._switchState[:,3]],
                    "t5":[self._timeList,self._switchState[:,4]],
                    "t6":[self._timeList,self._switchState[:,5]]}

        # Plot object with the number of subplots.
        numberOfPlots = len(yAxisList)
        flag = False
        if numberOfPlots == 1:
            fig,axs = plt.subplots(num=windowTitle)
            flag = True
        else:
            fig, axs = plt.subplots(numberOfPlots,num=windowTitle)
        
        if flag:
            keyList = list()
            legendList = list()
            for j in range(len(yAxisList[0])):
                legendList.append(yAxisList[0][j])
                keyList.append(yAxisList[0][j].lower())
                print(keyList[j])
                #axs.plot(self._timeList ,yAxisDict[keyList[j]])
                axs.plot(yAxisDict[keyList[j]][0],yAxisDict[keyList[j]][1])
            axs.legend(legendList)
            axs.set(xlabel="time")
        else:  
            # For each plot.
            for i in range(len(yAxisList)):
                # For each key in the plot list.
                keyList = list()
                legendList = list()
                for j in range(len(yAxisList[i])):
                    # Save the key in a list.
                    legendList.append(yAxisList[i][j])
                    keyList.append(yAxisList[i][j].lower())
                    # Get the attribute of the key in a plot.
                    #axs[i].plot(self._timeList, yAxisDict[keyList[j]])
                    axs[i].plot(yAxisDict[keyList[j]][0],yAxisDict[keyList[j]][1])
                
                if i == len(yAxisList) - 1:
                    axs[i].set(xlabel="time")
                axs[i].legend(legendList)
        #plt.show()
        fig.show()