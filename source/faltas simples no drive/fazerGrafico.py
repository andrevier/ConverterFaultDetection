import scipy.io
import matplotlib.pyplot as plt

# Captar os arquivos .mat para um dicionário e do dicionario para uma lista.
fig1 = plt.figure('Valor da corrente média em faltas simples',figsize = (6.3,6.3))
ax = fig1.add_subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

CMC1 = scipy.io.loadmat('CMC1')
CMC1 = CMC1['CM']
CMC1 = CMC1[0]
CMC1real = [CMC1[i].real for i in range(len(CMC1))]
CMC1imag = [CMC1[j].imag for j in range(len(CMC1))]
plt.scatter(CMC1real,CMC1imag,label='C1')

CMC2 = scipy.io.loadmat('CMC2')
CMC2 = CMC2['CM']
CMC2 = CMC2[0]
CMC2real = [CMC2[i].real for i in range(len(CMC2))]
CMC2imag = [CMC2[j].imag for j in range(len(CMC2))]
plt.scatter(CMC2real,CMC2imag,label='C2')

CMC3 = scipy.io.loadmat('CMC3')
CMC3 = CMC3['CM']
CMC3 = CMC3[0]
CMC3real = [CMC3[i].real for i in range(len(CMC3))]
CMC3imag = [CMC3[j].imag for j in range(len(CMC3))]
plt.scatter(CMC3real,CMC3imag,label='C3')

CMC4 = scipy.io.loadmat('CMC4')
CMC4 = CMC4['CM']
CMC4 = CMC4[0]
CMC4real = [CMC4[i].real for i in range(len(CMC4))]
CMC4imag = [CMC4[j].imag for j in range(len(CMC4))]
plt.scatter(CMC4real,CMC4imag,label='C4')

CMC5 = scipy.io.loadmat('CMC5')
CMC5 = CMC5['CM']
CMC5 = CMC5[0]
CMC5real = [CMC5[i].real for i in range(len(CMC5))]
CMC5imag = [CMC5[j].imag for j in range(len(CMC5))]
plt.scatter(CMC5real,CMC5imag,label='C5')

CMC6 = scipy.io.loadmat('CMC6')
CMC6 = CMC6['CM']
CMC6 = CMC6[0]
CMC6real = [CMC6[i].real for i in range(len(CMC6))]
CMC6imag = [CMC6[j].imag for j in range(len(CMC6))]
plt.scatter(CMC6real,CMC6imag,label='C6')

#ax.set_title('Valor da corrente média em faltas simples')
ax.set_xlabel(r'I$\alpha$ (A)',loc='right')
ax.set_ylabel(r'I$\beta$ (A)', loc='top', rotation = 0)
plt.legend()
plt.show()
plt.savefig('CorrentesMediasFaltasSimples.jpeg',dpi=300)


