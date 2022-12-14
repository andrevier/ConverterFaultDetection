Paper: "Fault diagnostic in power system using wavelet transforms and neural networks."
Authors: Charfi, F.; Sellami, F.; Al-Haddad, K.
data: 2006

Discusses fault identification of IGBT switches in a inverter. The fault identification is done in two steps: first detect a fault condition; second, detect which fault occurs. For the last step, three kinds of faults are considered: the open-circuit of the IGBT T1,the open-circuit of the IGBT T2 and the LEG2 open-circuit (IGBT T3 and IGBT T4 simultaneously).

For the fault detection in the first part, the authors considered one neural network (NN) with topology [3, 6, 1] to act as a binary classifier. The input data selected is the discrete wavelet transform of the three input currents decomposed to the level 6 and only the approximation coefficients used. The coefficients were normalized beforehand and the mother wavelet is Daubechies with 4 vanishing moments.

For the kind of fault, a NN as a binary classifier with topology [9, 10, 1] is trained for each fault. The input data is: 
[min(Ia), max(Ia), (A6)a, min(Ib), max(Ib), (A6)b, min(Ic), max(Ic), (A6)c]

This is an early work on the issue. 

Each approximation coefficients are an array. Therefore, the samples are array points of the coefficients. 

Level 6 decomposition shows the sinusoidal represented in the approximation part while a noise in the d6 and d5 coefficients.

There are pendencies:
* The paper doesn't show figures of the normal signal and the fault one.
* The method for normalization of the coefficients is not detailed.
* How to implement the dwt coefficients in the way of figure 4?


