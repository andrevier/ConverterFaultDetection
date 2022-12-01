'''Run analysis of the simulation data.
1. Open-circuit simulation of T1 switch.
2. Open-circuit simulation of T4 switch.
3. Open-circuit simulation of T3 switch.
4. Open-circuit simulation of T6 switch.
5. Open-circuit simulation of T5 switch.
6. Open-circuit simulation of T2 switch. '''
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
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

# 1. Open-circuit simulation of T1 switch.
# from Simulations.model15ScalarControl.openCircuit.T1FullSpeed import (
#     Isa,Isb,Isc,time as timeSeries)

# Convert all the csv data into dataframe series.
path = "Simulations\\model15ScalarControl\\openCircuit\\T1FullSpeed\\"

Isa = pd.read_csv(path + "isa.csv")
Isb = pd.read_csv(path + "isb.csv")
Isc = pd.read_csv(path + "isc.csv")
Te = pd.read_csv(path + "Te.csv")
time = pd.read_csv(path + "time.csv")
Vab = pd.read_csv(path + "Vab.csv")
wm = pd.read_csv(path + "wm.csv")

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
analysisT1.plot([["I1a","I1b","I1c"],["faultstate"],
                 ["faultmode"],["t1","t2","t3","t4","t5","t6"]],
                  windowTitle="Open-circuit of T1")

# # 2. Open-circuit simulation of T4 switch.
# from Simulations.model15ScalarControl.openCircuit.T4FullSpeed import (
#     Isa,Isb,Isc,time as timeSeries)

# # Make a dataframe with time and currents
# Isadf = pd.concat([timeSeries, Isa], ignore_index=True, axis=1)
# Isbdf = pd.concat([timeSeries, Isb], ignore_index=True, axis=1)
# Iscdf = pd.concat([timeSeries, Isc], ignore_index=True, axis=1)

# analysisT4 = tools.AnalysisManager(Ia=Isadf, Ib=Isbdf, Ic=Iscdf,
#                                    lineFreq=f,
#                                    baseCurrentRMS=Ibase,
#                                    timeInterval=timeInterval,
#                                    maxTime=maxTime,
#                                    infCurrentBound=Ibound, 
#                                    I21Bound=I21Bound, 
#                                    I31Bound=I31Bound)

# analysisT4.runAnalysis()
# analysisT4.plot([["I1a","I1b","I1c"],["faultstate"],
#                  ["faultmode"],["t1","t2","t3","t4","t5","t6"]],
#                  windowTitle="Open-circuit of T4")

# # 3. Open-circuit simulation of T3 switch.
# from Simulations.model15ScalarControl.openCircuit.T3FullSpeed import (
#     Isa,Isb,Isc,time as timeSeries)

# # Make a dataframe with time and currents
# Isadf = pd.concat([timeSeries, Isa], ignore_index=True, axis=1)
# Isbdf = pd.concat([timeSeries, Isb], ignore_index=True, axis=1)
# Iscdf = pd.concat([timeSeries, Isc], ignore_index=True, axis=1)

# analysisT3 = tools.AnalysisManager(Ia=Isadf, Ib=Isbdf, Ic=Iscdf,
#                                    lineFreq=f,
#                                    baseCurrentRMS=Ibase,
#                                    timeInterval=timeInterval,
#                                    maxTime=maxTime,
#                                    infCurrentBound=Ibound, 
#                                    I21Bound=I21Bound, 
#                                    I31Bound=I31Bound)

# analysisT3.runAnalysis()
# analysisT3.plot([["I1a","I1b","I1c"],["faultstate"],
#                  ["faultmode"],["t1","t2","t3","t4","t5","t6"]],
#                  windowTitle="Open-circuit of T3")

# # 4. Open-circuit simulation of T6 switch.
# from Simulations.model15ScalarControl.openCircuit.T6FullSpeed import (
#     Isa,Isb,Isc,time as timeSeries)

# # Make a dataframe with time and currents
# Isadf = pd.concat([timeSeries, Isa], ignore_index=True, axis=1)
# Isbdf = pd.concat([timeSeries, Isb], ignore_index=True, axis=1)
# Iscdf = pd.concat([timeSeries, Isc], ignore_index=True, axis=1)

# analysisT6 = tools.AnalysisManager(Ia=Isadf, Ib=Isbdf, Ic=Iscdf,
#                                    lineFreq=f,
#                                    baseCurrentRMS=Ibase,
#                                    timeInterval=timeInterval,
#                                    maxTime=maxTime,
#                                    infCurrentBound=Ibound, 
#                                    I21Bound=I21Bound, 
#                                    I31Bound=I31Bound)

# analysisT6.runAnalysis()
# analysisT6.plot([["I1a","I1b","I1c"],["faultstate"],
#                  ["faultmode"],["t1","t2","t3","t4","t5","t6"]],
#                  windowTitle="Open-circuit of T6")

# # 5. Open-circuit simulation of T5 switch.
# from Simulations.model15ScalarControl.openCircuit.T5FullSpeed import (
#     Isa,Isb,Isc,time as timeSeries)

# # Make a dataframe with time and currents
# Isadf = pd.concat([timeSeries, Isa], ignore_index=True, axis=1)
# Isbdf = pd.concat([timeSeries, Isb], ignore_index=True, axis=1)
# Iscdf = pd.concat([timeSeries, Isc], ignore_index=True, axis=1)

# analysisT5 = tools.AnalysisManager(Ia=Isadf, Ib=Isbdf, Ic=Iscdf,
#                                    lineFreq=f,
#                                    baseCurrentRMS=Ibase,
#                                    timeInterval=timeInterval,
#                                    maxTime=maxTime,
#                                    infCurrentBound=Ibound, 
#                                    I21Bound=I21Bound, 
#                                    I31Bound=I31Bound)

# analysisT5.runAnalysis()
# analysisT5.plot([["I1a","I1b","I1c"],["faultstate"],
#                  ["faultmode"],["t1","t2","t3","t4","t5","t6"]],
#                  windowTitle="Open-circuit of T5")
# acionou T2 ao invés de T5.
# # 6. Open-circuit simulation of T2 switch.
# from Simulations.model15ScalarControl.openCircuit.T2FullSpeed import (
#     Isa,Isb,Isc,time as timeSeries)

# # Make a dataframe with time and currents
# Isadf = pd.concat([timeSeries, Isa], ignore_index=True, axis=1)
# Isbdf = pd.concat([timeSeries, Isb], ignore_index=True, axis=1)
# Iscdf = pd.concat([timeSeries, Isc], ignore_index=True, axis=1)

# analysisT2 = tools.AnalysisManager(Ia=Isadf, Ib=Isbdf, Ic=Iscdf,
#                                    lineFreq=f,
#                                    baseCurrentRMS=Ibase,
#                                    timeInterval=timeInterval,
#                                    maxTime=maxTime,
#                                    infCurrentBound=Ibound, 
#                                    I21Bound=I21Bound, 
#                                    I31Bound=I31Bound)

# analysisT2.runAnalysis()
# analysisT2.plot([["I1a","I1b","I1c"],["faultstate"],
#                  ["faultmode"],["t1","t2","t3","t4","t5","t6"]],
#                  windowTitle="Open-circuit of T2")
