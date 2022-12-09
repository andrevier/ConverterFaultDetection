'''Run analysis of the simulation data.
1. Open-circuit simulation of T1 switch.
2. Open-circuit simulation of T4 switch.
3. Open-circuit simulation of T3 switch.
4. Open-circuit simulation of T6 switch.
5. Open-circuit simulation of T5 switch.
6. Open-circuit simulation of T2 switch.
7. Open-circuit simulation of T1-T4 switches (same leg).
8. Open-circuit simulation of T3-T6 switches (same leg).
9. Open-circuit simulation of T2-T5 switches (same leg). '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import tools

# Main line current parameters.
f = 50
Ibase = 8.15

# Total simulation time.
maxTime = 10.0

# Length of the time interval.
timeInterval = 5*1/f
Ibound = 0.10
I21Bound = .10
I31Bound = .10

# Open-circuit simulation with data from the following paths.
pathT1 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T1FullSpeed'''
pathT2 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T2FullSpeed'''
pathT3 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T3FullSpeed'''
pathT4 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T4FullSpeed'''
pathT5 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T5FullSpeed'''
pathT6 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T6FullSpeed'''
pathT1T4 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T1T4FullSpeed'''
pathT3T6 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T3T6FullSpeed'''
pathT2T5 = '''D:\\mestrado\\projeto\\Simulations\\model15ScalarControl\\openCircuit\\T2T5FullSpeed'''

# Choose one path to analyze the data.
os.chdir(pathT1)

# Convert all the csv data into dataframe series.
Isa = pd.read_csv("isa.csv")
Isb = pd.read_csv("isb.csv")
Isc = pd.read_csv("isc.csv")
Te = pd.read_csv("Te.csv")
time = pd.read_csv("time.csv")
Vab = pd.read_csv("Vab.csv")
wm = pd.read_csv("wm.csv")

# Make a dataframe with time and currents
Isadf = pd.concat([time, Isa], ignore_index=True, axis=1)
Isbdf = pd.concat([time, Isb], ignore_index=True, axis=1)
Iscdf = pd.concat([time, Isc], ignore_index=True, axis=1)


analysisT1 = tools.AnalysisManager(Ia=Isadf, Ib=Isbdf, Ic=Iscdf,
                                   lineFreq=f,
                                   baseCurrentRMS=Ibase,
                                   timeInterval=timeInterval,
                                   maxTime=maxTime,
                                   infCurrentBound=Ibound, 
                                   I21Bound=I21Bound, 
                                   I31Bound=I31Bound)

analysisT1.runAnalysis()
# analysisT1.plot([["I1a","I1b","I1c"],["faultstate"],
#                  ["faultmode"],["t1","t2","t3","t4","t5","t6"]],
#                   windowTitle="Open-circuit of T1")
analysisT1.plot([["Ia","Ib","Ic"]], windowTitle="Open-circuit of T1")