# Gerar script para os ensaios 

import re
import os

def C_init(nomeChave, chavesAbertas):
    """
        Inicia as chaves no tempo 2s de simulação.
    """
    if chavesAbertas == 1:
        texto =f"""
        % {nomeChave} ----------------------------
        % Abertura da chave {nomeChave}1 em 2s.
        {nomeChave}1 = ones(length(t),1);
        i_t = t > 2.;
        {nomeChave}1(i_t) = 0.; 
        {nomeChave}1 = [t, {nomeChave}1];

        {nomeChave}2 = ones(length(t),1);
        {nomeChave}2 = [t, {nomeChave}2];

        {nomeChave}3 = ones(length(t),1);
        {nomeChave}3 = [t, {nomeChave}3];

        {nomeChave}4 = ones(length(t),1);
        {nomeChave}4 = [t, {nomeChave}4];

        {nomeChave}5 = ones(length(t),1);
        {nomeChave}5 = [t, {nomeChave}5];

        {nomeChave}6 = ones(length(t),1);
        {nomeChave}6 = [t, {nomeChave}6];

        {nomeChave}7 = ones(length(t),1);
        {nomeChave}7 = [t, {nomeChave}7];
        """
    elif chavesAbertas == 2:
        texto =f"""
        % {nomeChave} ----------------------------
        % Abertura da chave {nomeChave}1 em 2s.
        {nomeChave}1 = ones(length(t),1);
        i_t = t > 2.;
        {nomeChave}1(i_t) = 0.; 
        {nomeChave}1 = [t, {nomeChave}1];

        {nomeChave}2 = ones(length(t),1);
        {nomeChave}2(i_t) = 0.;
        {nomeChave}2 = [t, {nomeChave}2];

        {nomeChave}3 = ones(length(t),1);
        {nomeChave}3 = [t, {nomeChave}3];

        {nomeChave}4 = ones(length(t),1);
        {nomeChave}4 = [t, {nomeChave}4];

        {nomeChave}5 = ones(length(t),1);
        {nomeChave}5 = [t, {nomeChave}5];

        {nomeChave}6 = ones(length(t),1);
        {nomeChave}6 = [t, {nomeChave}6];

        {nomeChave}7 = ones(length(t),1);
        {nomeChave}7 = [t, {nomeChave}7];
        """
    elif chavesAbertas == 3:
        texto = f"""
        % {nomeChave} ----------------------------
        % Abertura da chave {nomeChave}1 em 2s.
        {nomeChave}1 = ones(length(t),1);
        i_t = t > 2.;
        {nomeChave}1(i_t) = 0.; 
        {nomeChave}1 = [t, {nomeChave}1];

        {nomeChave}2 = ones(length(t),1);
        {nomeChave}2(i_t) = 0.;
        {nomeChave}2 = [t, {nomeChave}2];

        {nomeChave}3 = ones(length(t),1);
        {nomeChave}3(i_t) = 0.;
        {nomeChave}3 = [t, {nomeChave}3];

        {nomeChave}4 = ones(length(t),1);
        {nomeChave}4 = [t, {nomeChave}4];

        {nomeChave}5 = ones(length(t),1);
        {nomeChave}5 = [t, {nomeChave}5];

        {nomeChave}6 = ones(length(t),1);
        {nomeChave}6 = [t, {nomeChave}6];

        {nomeChave}7 = ones(length(t),1);
        {nomeChave}7 = [t, {nomeChave}7];
        """
    elif chavesAbertas == 4:
        texto = f"""
        % {nomeChave} ----------------------------
        % Abertura da chave {nomeChave}1 em 2s.
        {nomeChave}1 = ones(length(t),1);
        i_t = t > 2.;
        {nomeChave}1(i_t) = 0.; 
        {nomeChave}1 = [t, {nomeChave}1];

        {nomeChave}2 = ones(length(t),1);
        {nomeChave}2(i_t) = 0.;
        {nomeChave}2 = [t, {nomeChave}2];

        {nomeChave}3 = ones(length(t),1);
        {nomeChave}3(i_t) = 0.;
        {nomeChave}3 = [t, {nomeChave}3];

        {nomeChave}4 = ones(length(t),1);
        {nomeChave}4(i_t) = 0.;
        {nomeChave}4 = [t, {nomeChave}4];

        {nomeChave}5 = ones(length(t),1);
        {nomeChave}5 = [t, {nomeChave}5];

        {nomeChave}6 = ones(length(t),1);
        {nomeChave}6 = [t, {nomeChave}6];

        {nomeChave}7 = ones(length(t),1);
        {nomeChave}7 = [t, {nomeChave}7];
        """
    elif chavesAbertas == 5:
        texto = f"""
        % {nomeChave} ----------------------------
        % Abertura da chave {nomeChave}1 em 2s.
        {nomeChave}1 = ones(length(t),1);
        i_t = t > 2.;
        {nomeChave}1(i_t) = 0.; 
        {nomeChave}1 = [t, {nomeChave}1];

        {nomeChave}2 = ones(length(t),1);
        {nomeChave}2(i_t) = 0.;
        {nomeChave}2 = [t, {nomeChave}2];

        {nomeChave}3 = ones(length(t),1);
        {nomeChave}3(i_t) = 0.;
        {nomeChave}3 = [t, {nomeChave}3];

        {nomeChave}4 = ones(length(t),1);
        {nomeChave}4(i_t) = 0.;
        {nomeChave}4 = [t, {nomeChave}4];

        {nomeChave}5 = ones(length(t),1);
        {nomeChave}5(i_t) = 0.;
        {nomeChave}5 = [t, {nomeChave}5];

        {nomeChave}6 = ones(length(t),1);
        {nomeChave}6 = [t, {nomeChave}6];

        {nomeChave}7 = ones(length(t),1);
        {nomeChave}7 = [t, {nomeChave}7];
        """
    else:
        texto =f"""
        % {nomeChave} ----------------------------
        % Não abre.
        {nomeChave}1 = ones(length(t),1);
        {nomeChave}1 = [t, {nomeChave}1];

        {nomeChave}2 = ones(length(t),1);
        {nomeChave}2 = [t, {nomeChave}2];

        {nomeChave}3 = ones(length(t),1);
        {nomeChave}3 = [t, {nomeChave}3];

        {nomeChave}4 = ones(length(t),1);
        {nomeChave}4 = [t, {nomeChave}4];

        {nomeChave}5 = ones(length(t),1);
        {nomeChave}5 = [t, {nomeChave}5];

        {nomeChave}6 = ones(length(t),1);
        {nomeChave}6 = [t, {nomeChave}6];

        {nomeChave}7 = ones(length(t),1);
        {nomeChave}7 = [t, {nomeChave}7];
        """
    return texto

def C_seq(nomeChave):
    """
    Função para determinar o grupo de resistências que abrem em sequência.
    """
    texto =f"""
        % {nomeChave} ----------------------------
        % Abre em 2s.
        {nomeChave}1 = ones(length(t),1);
        i_t = t > 2.;
        {nomeChave}1(i_t) = 0.; 
        {nomeChave}1 = [t, {nomeChave}1];

        % Abre em 3s.
        {nomeChave}2 = ones(length(t),1);
        i_t = t > 3.;
        {nomeChave}2(i_t) = 0;
        {nomeChave}2 = [t, {nomeChave}2];
        
        % Abre em 4s.  
        {nomeChave}3 = ones(length(t),1);
        i_t = t > 4.;
        {nomeChave}3(i_t) = 0.;
        {nomeChave}3 = [t, {nomeChave}3];

        % Abre em 5s.
        {nomeChave}4 = ones(length(t),1);
        i_t = t > 5.;
        {nomeChave}4(i_t) = 0.;
        {nomeChave}4 = [t, {nomeChave}4];

        % Abre em 6s.
        {nomeChave}5 = ones(length(t),1);
        i_t = t > 6.;
        {nomeChave}5(i_t) = 0.;
        {nomeChave}5 = [t, {nomeChave}5];
        
        % Não abrem.
        {nomeChave}6 = ones(length(t),1);
        {nomeChave}6 = [t, {nomeChave}6];

        {nomeChave}7 = ones(length(t),1);
        {nomeChave}7 = [t, {nomeChave}7];
        """
    return texto

def fim(nomeCaso,nomePasta,numSim,numR1):
    texto = f"""
    % Executar a simulação.
    sim('drive_faltatripla', tempo_max)

    cd ../
    CM = calculaCM(2., (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
    cd 'faltas triplas no drive'/{nomePasta}

    save('CM_{nomeCaso}_{numR1}_{numSim}','CM')"""
    return texto

cabecalho = """% Script para iniciar os dados da simulação 
% drive_faltatripla.slx. O objetivo é fazer a simulação das condições de falta   
% através da aplicação de uma resistência em série em três das chaves
% semicondutoras do conversor por vez."""

inicio = \
"""
close all
clearvars

% Obter valores nominais
cd ..\..
tabela = readtable('variaveisNominais.txt');
cd 'faltas triplas no drive'

var = tabela.Valor;
Ipn = var(4);
Ten = var(5);

% Condições da simulação
Ts = 2.e-05;
tempo_max = 9.;
t = 0.:Ts:tempo_max;
t = transpose(t);

% Referência de torque: torque nominal a partir de 1s.
Tm = zeros(length(t),1);
i_t = t > 1.;
Tm(i_t) = Ten;
Tmref = [t, Tm];

% Referência de velocidade: valor nominal desde a partida. 
n = 1800.*ones(length(t),1);
nref = [t, n];

"""
introAcionamentoChaves = \
"""
% Sinais para ativar as resistências em série com o IGBT. 
% Cada IGBT tem 7 resistores em série que são acionados pelo disparo de uma
% chave em paralelo. 
"""
nomeDasPastas = []
mypath = os.getcwd()
for (dirpath, dirnames, filenames) in os.walk(mypath):
    nomeDasPastas.extend(dirnames)
    break

# Valores da resistência em série da primeira chave do nome.
r1 = ['1','2','3','4','5']

# Número de simulações para cada caso da resistência da primeira chave do nome.
numSim = [1,2,3,4,5]

# Dicionário para a orientação de cada grupo de resistores.
# O nome do caso (nomeCaso) é solicitado e o comportamento de cada 
# grupo de resistor é definido.
seq = {'C123':['C1','C2','C3','C4','C5','C6'],
       'C124':['C1','C2','C4','C3','C5','C6'],
       'C125':['C1','C2','C5','C4','C3','C6'],
       'C126':['C1','C2','C6','C4','C5','C3'],
       'C134':['C1','C3','C4','C2','C5','C6'],
       'C135':['C1','C3','C5','C2','C4','C6'],
       'C136':['C1','C3','C6','C2','C4','C5'],
       'C145':['C1','C4','C5','C2','C3','C6'],
       'C146':['C1','C4','C6','C2','C5','C3'],
       'C156':['C1','C5','C6','C4','C2','C3'],
       'C234':['C2','C3','C4','C1','C5','C6'],
       'C235':['C2','C3','C5','C1','C4','C6'],
       'C236':['C2','C3','C6','C1','C4','C5'],
       'C245':['C2','C4','C5','C1','C3','C6'],
       'C246':['C2','C4','C6','C1','C3','C5'],
       'C256':['C2','C5','C6','C1','C3','C4'],
       'C345':['C3','C4','C5','C1','C2','C6'],
       'C346':['C3','C4','C6','C1','C2','C5'],
       'C356':['C3','C5','C6','C1','C2','C4'],
       'C456':['C4','C5','C6','C1','C2','C3']}
# Para cada uma das pastas encontradas
for k in range(len(nomeDasPastas)):
    # Adicionar um verificador de nome de pasta. Só pastas que possuem nome 'falta'
    if re.match(r"falta",nomeDasPastas[k]):
        nomeCaso = re.sub('falta','',nomeDasPastas[k])
        # Os casos envolvem as variações das resistências em série com os IGBTs, por isso:
        # Para cada valor da resistência em série na primeira chave
        for j in range(len(r1)):
            # Para cada valor da resistência em série na segunda chave
            for i in range(len(numSim)):
                chaveC1 = C_init(seq[nomeCaso][0],j+1)
                chaveC2 = C_init(seq[nomeCaso][1],i+1)
                chaveC3 = C_seq(seq[nomeCaso][2])
                chaveC4 = C_init(seq[nomeCaso][3],-1)
                chaveC5 = C_init(seq[nomeCaso][4],-1)
                chaveC6 = C_init(seq[nomeCaso][5],-1)
                conclusao = fim(nomeCaso,nomeDasPastas[k], str(i+1), str(j+1))
                nomeArquivo = mypath + '\\' + nomeDasPastas[k] + '\\' + nomeCaso + '_' + r1[j] + '_' + str(numSim[i]) + '.m'
                
                # Escrever o código no script
                with open(nomeArquivo,'w') as f:
                    f.write(cabecalho)
                    f.write(inicio)
                    f.write(introAcionamentoChaves)
                    f.write(chaveC1)
                    f.write(chaveC2)
                    f.write(chaveC3)
                    f.write(chaveC4)
                    f.write(chaveC5)
                    f.write(chaveC6)
                    f.write(conclusao)
    else:
        pass





