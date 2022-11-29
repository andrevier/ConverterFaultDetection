# Test plot mechanism.
import tools
import numpy as np
import matplotlib.pyplot as plt
import random

def helpPlot(numberOfPlots, yAxisList, input1, input2, input3):
    yAxisDict = {"1":input1, "2":input2,"3":input3}
    flag = False
    if numberOfPlots == 1:
        _, axs = plt.subplots()
        flag = True
    else:
        _, axs = plt.subplots(numberOfPlots)

    # For each plot.
    if flag:
        print("flag " + str(flag))
        keyList = list()
        for j in range(len(yAxisList[0])):
            keyList.append(yAxisList[0][j])
            print(keyList[j])
            axs.plot(t,yAxisDict[keyList[j]])
        axs.legend(keyList)
        axs.set(xlabel="t",ylabel="y")
    else:
        print("flag " + str(flag))
        for i in range(len(yAxisList)):
            # For each key in the plot list.
            keyList = list()

            for j in range(len(yAxisList[i])):
                # Save the key in a list.
                keyList.append(yAxisList[i][j])
                print(keyList[j])
                # Get the attribute of the key in a plot.
                axs[i].plot(t, yAxisDict[keyList[j]])

            axs[i].legend(keyList)
            if i == len(yAxisList) - 1:
                axs[i].set(xlabel="t")
    plt.show()
# Peak voltage
VmaxPk = 2

# Sinusoidal frequency
Fi = 2000

# Sample rate of 44.1kHz
Fs = 44.1e3

# Duration of the sinusoid
Tstop = 50e-3

# Time input vector
N = int(Tstop/(1/Fs))
t = np.linspace(0, Tstop, N)

inputVmax = VmaxPk*np.sin(2*np.pi*Fi*t)
input2 = VmaxPk/2*np.sin(2*np.pi*2*Fi*t)
input4 = VmaxPk/3*np.sin(2*np.pi*4*Fi*t)
input6 = VmaxPk/6*np.sin(2*np.pi*6*Fi*t)

ran = np.ones(len(t))
for i in range(len(t)):
    ran[i] = random.random()*VmaxPk/6

# Three y-axis to plot.
input1 = input2 + input4 + input6 + ran + inputVmax

input2 = VmaxPk*np.cos(2*np.pi*Fi*t)

input3 = VmaxPk/2*np.cos(2*np.pi*Fi*t)

helpPlot(2,[["1","2"],["1","3"]], input1, input2, input3)

