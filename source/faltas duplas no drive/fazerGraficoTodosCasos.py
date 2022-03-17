import scipy.io
import matplotlib.pyplot as plt
import os
import re

# Configurações da figura
fig1 = plt.figure('Valor da corrente média em faltas duplas',figsize = (6.3,6.3))
ax = fig1.add_subplot(111)
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Pegar o nome das pastas no arquivo raiz
nomeDasPastas = []
mypath = os.getcwd()
for (dirpath, dirnames, filenames) in os.walk(mypath):
    nomeDasPastas.extend(dirnames)
    break

print(f"{nomeDasPastas}\n")

# para cada uma das pastas
for k in range(len(nomeDasPastas)):
    # verificar se há a string 'falta'
    if re.match(r"falta",nomeDasPastas[k]):
        # se houver, abrir todos os arquivos .mat dentro da pasta
        diretorioAtual= mypath + '\\' + nomeDasPastas[k]
        # os.chdir(diretorioAtual)
        nomeArqs = []
        for (dirpath,dirnames,filenames) in os.walk(diretorioAtual):
            nomeArqs.extend(filenames)
            break
        
        # Para cada arquivo encontrado
        for arq in nomeArqs:
            # Se existir a string '.mat'
            if re.search("\.mat",arq):
                # transformar o arquivo .mat em dicionário.
                nomeCompleto = diretorioAtual + '\\' + arq
                try:
                    dictMat = scipy.io.loadmat(nomeCompleto)
                    # Pegar a lista CM
                    CM = dictMat['CM']
                    CM = CM[0]
                    CMreal = [CM[m].real for m in range(len(CM))]
                    CMimag = [CM[m].imag for m in range(len(CM))]
                    plt.scatter(CMreal,CMimag)
                except KeyError:
                    pass
    else:
        pass

ax.set_xlabel(r'I$\alpha$ (A)',loc='right')
ax.set_ylabel(r'I$\beta$ (A)', loc='top', rotation = 0)
plt.xlim([-1.5,1.5])
plt.ylim([-1.5,1.5])
plt.show()
plt.savefig('CorrentesMediasFaltasDuplas.jpeg',dpi=300)


