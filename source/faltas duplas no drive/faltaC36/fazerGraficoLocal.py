import os 
import re
import scipy.io
import matplotlib.pyplot as plt

fig1 = plt.figure('Variação da corrente média com resistências em C3 e C6',figsize = (6.3,6.3))
ax = fig1.add_subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

nomesArquivos = []
mypath = os.getcwd()
for (dirpaths, dirnames, filenames) in os.walk(mypath):
    nomesArquivos.extend(filenames)
    break
for arq in nomesArquivos:
    if re.search('\.mat',arq):
        dictCM = scipy.io.loadmat(mypath+'\\'+arq)
        CM = dictCM['CM']
        CM = CM[0]
        CMreal = [CM[m].real for m in range(len(CM))]
        CMimag = [CM[m].imag for m in range(len(CM))]
        plt.scatter(CMreal,CMimag,marker='+')

ax.set_xlabel(r'I$\alpha$ (A)',loc='right')
ax.set_ylabel(r'I$\beta$ (A)', loc='top', rotation = 0)
plt.xlim([-1, 1])
plt.ylim([-1, 1])
plt.show()
plt.savefig('C36.jpg',dpi=300)