# Functions, classes related to fault identification of the data of a
# induction motor drive system.
import tools
import numpy

def hasFaultState(iA, iB, iC, h1:float, Ts:float, baseCurrentRMS:float):
    # Receive a numpy array iA, iB, and iC with the sampling data of
    # each single-phase stator current and process it with the 
    # Jung-Hyun Choi algorithm to detect if the signal has any 
    # open-circuit fault in the switches.
    # Input:
    # Isa, Isb, Isc -> numpy array with stator current signal.
    # h1 -> frequency of the first harmonics;
    # Ts -> sampling period, time interval between two samples in 
    # seconds.
    # baseCurrentRMS -> the RMS value of the single-phase current in 
    # Amper.
    # The function returns a tupple (faultState, switch) in which:
    # faultState is true if any fault is detected;
    # If a fault is detected, switch tells the number of the switch.

    # Get the first 3 harmonics of the signal: h1, h2 and h3.
    maxHarmonicNumber = 3

    # Limit of the interval of search the first harmonic.
    freqSearchInterval = 5

    # Standard for fault identification of the first harmonic.
    infCurrentLimit = 0.1
    
    # Record tupples for each interval in study.
    signalParameters = []

    # phase A
    freqArrayA, fftArrayA = tools.calcFFT(iA, Ts)
    freqOfHarmA, fftOfHarmA = tools.harmonics(freqArrayA, fftArrayA, h1, 
                                              maxHarmonicNumber,
                                              freqSearchInterval)
    firstHarmonic = 1
    secondHarmonic = 2
    thirdHarmonic = 3                                                
    fftOfH1A = fftOfHarmA[firstHarmonic]
    fftOfH2A = fftOfHarmA[secondHarmonic]
    fftOfH3A = fftOfHarmA[thirdHarmonic]
    
    # Signal characteristics: Average, RMS and normalized RMS.
    iAAve = sum(iA)/len(iA)
    iARMS = tools.RMS(iA, h1, Ts)
    iARMSNorm = [i/baseCurrentRMS for i in iARMS]

    # phase B
    freqArrayB, fftArrayB = tools.calcFFT(iB, Ts)
    freqOfHarmB, fftOfHarmB = tools.harmonics(freqArrayB, fftArrayB, h1, 
                                              maxHarmonicNumber,
                                              freqSearchInterval)                                          
    fftOfH1B = fftOfHarmB[firstHarmonic]
    fftOfH2B = fftOfHarmB[secondHarmonic]
    fftOfH3B = fftOfHarmB[thirdHarmonic]
    
    # Signal characteristics: Average, RMS and normalized RMS.
    iBAve = sum(iB)/len(iB)
    iBRMS = tools.RMS(iB, h1, Ts)
    iBRMSNorm = [i/baseCurrentRMS for i in iBRMS]

    # Phase C
    freqArrayC, fftArrayC = tools.calcFFT(iC, Ts)
    freqOfHarmB, fftOfHarmC = tools.harmonics(freqArrayC, fftArrayC, h1, 
                                              maxHarmonicNumber,
                                              freqSearchInterval)
    fftOfH1C = fftOfHarmC[firstHarmonic]
    fftOfH2C = fftOfHarmB[secondHarmonic]
    fftOfH3C = fftOfHarmB[thirdHarmonic]
    
    # Signal characteristics: Average, RMS and normalized RMS. 
    iCAve = sum(iC)/len(iC)
    iCRMS = tools.RMS(iC, h1, Ts)
    iCRMSNorm = [i/baseCurrentRMS for i in iCRMS]

    # Check for fault state and fault modes.
    # Fault state can be True if fault occurs or False, otherwise.
    # Fault mode 0 -> normal state. 
    #            1 -> 2 open-switches in one leg.
    #            2 -> 1 open-switch.
    #            3 -> 2 open-switches in upper leg positions or in the 
    #                 lower leg positions.
    #            4 -> 2 open-switches: 1 in the upper part and 1 in the
    #                 lower part. 
    faultMode = 0
    faultState = False
    switch = ""
    
    # Relative harmonic values of fft: 
    # fft21x = (fft of harmonic 2)/(fft of harmonic 1) 
    # x correspond to the phases A,B,C. 
    try:
        fft21A = fftOfH2A/fftOfH1A
        fft21B = fftOfH2B/fftOfH1B
        fft21C = fftOfH2C/fftOfH1C

        fft31A = fftOfH3A/fftOfH1A
        fft31B = fftOfH3B/fftOfH1B
        fft31C = fftOfH3C/fftOfH1C
    except ZeroDivisionError as err:
        print("Zero division error. Check the first harmonics. ", err)
        raise SystemExit

    fft21Threshold = .10
    fft31Threshold = .10
    
    # Check for fault states.
    if ((max(iARMSNorm) <= infCurrentLimit)
        or (max(iBRMSNorm) <= infCurrentLimit)
        or (max(iCRMSNorm) <= infCurrentLimit)):
        faultState = True
    elif ((fft21A >= fft21Threshold)
          or (fft21B >= fft21Threshold)
          or (fft21C >= fft21Threshold)):
        faultState = True
    
    # Check for fault modes
    if faultState:
        if ((max(iARMSNorm) <= infCurrentLimit)
            or (max(iBRMSNorm) <= infCurrentLimit)
            or (max(iCRMSNorm) <= infCurrentLimit)):
            faultMode = 1
        elif not ((fft31A >= fft31Threshold)
                  or (fft31B >= fft31Threshold)
                  or (fft31C >= fft21Threshold)):
            faultMode = 2
    
    # Check for switches
    if faultMode == 1:
        if max(iARMSNorm) <= infCurrentLimit: 
            switch = "T1 and T4"
        elif max(iBRMSNorm) <= infCurrentLimit:
            switch = "T3 and T6"
        elif max(iCRMSNorm) <= infCurrentLimit:
            switch = "T5 and T2"
        else:
            switch = "undefined"
    elif faultMode == 2:
        if max(iARMSNorm) <= infCurrentLimit:
            if iAAve < 0:
                switch = "T1"
            else:
                switch = "T4"
        elif max(iBRMSNorm) <= infCurrentLimit:
            if iBAve < 0:
                switch = "T3"
            else:
                switch = "T6"
        elif max(iCRMSNorm) <= infCurrentLimit:
            if iCAve < 0:
                switch = "T5"
            else:
                switch = "T2"
        else:
            switch = "undefined"
    return (faultState,switch)


   
