% Script para processar os dados dos sinais do drive em
% drive_faltadupla.slx em que há a simulação de condições de falta
% através da aplicação de uma resistência em série em duas das chaves
% semicondutoras do conversor.

close all
clearvars

% Obter valores nominais
cd ..\..
tabela = readtable('variaveisNominais.txt');
cd 'faltas duplas no drive'

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

%% Sinais para ativar as resistências em série com o IGBT. 
% Cada IGBT tem 7 resistores em série que são acionados pelo disparo de uma
% chave em paralelo. A chave abre e o resistor passa a conduzir a corrente.
% A simulação nesse script trata do disparo da 1ª à 4ª chave no IGBT C1 
% (CH1 à CH4) e dos disparos das demais no IGBT C5 (CH1-CH7).

% R41 até R47 de 2 até 8s....................
% C1 ----------------------------
% Abertura da chave C11 em 2s.
C11 = ones(length(t),1);
i_t = t > 2.;
C11(i_t) = 0.; 
C11 = [t, C11];

C12 = ones(length(t),1);
C12(i_t) = 0;
C12 = [t, C12];

C13 = ones(length(t),1);
C13(i_t) = 0;
C13 = [t, C13];

C14 = ones(length(t),1);
C14(i_t) = 0;
C14 = [t, C14];
%----------------------------
C15 = ones(length(t),1);
C15 = [t, C15];

C16 = ones(length(t),1);
C16 = [t, C16];

C17 = ones(length(t),1);
C17 = [t, C17];

% C2 ----------------------------
% Não abre.
C21 = ones(length(t),1); 
C21 = [t, C21];

C22 = C21;

C23 = C21;

C24 = C21;

C25 = C21;

C26 = C21;

C27 = C21;

% C3 ----------------------------
% Não abre.
C31 = C21; 

C32 = C21;

C33 = C21;

C34 = C21;

C35 = C21;

C36 = C21;

C37 = C21;

% C4 ----------------------------
% Não abre.
C41 = C21; 

C42 = C21;

C43 = C21;

C44 = C21;

C45 = C21;

C46 = C21;

C47 = C21;

% C5 ----------------------------
% Abertura da chave C51 em 2s.
C51 = ones(length(t),1);
i_t = t > 2.;
C51(i_t) = 0.; 
C51 = [t, C51];

% chave C52 abre em 3s.
C52 = ones(length(t),1);
i_t = t > 3.;
C52(i_t) = 0.; 
C52 = [t, C52];

% chave C53 abre em 4s.
C53 = ones(length(t),1);
i_t = t > 4.;
C53(i_t) = 0.; 
C53 = [t, C53];

% chave C54 abre em 5s.
C54 = ones(length(t),1);
i_t = t > 5.;
C54(i_t) = 0.; 
C54 = [t, C54];

% chave C55 abre em 6s.
C55 = ones(length(t),1);
i_t = t > 6.;
C55(i_t) = 0.; 
C55 = [t, C55];

% chave C56 abre em 7s.
C56 = ones(length(t),1);
i_t = t > 7.;
C56(i_t) = 0.; 
C56 = [t, C56];

% chave C57 abre em 8s.
C57 = ones(length(t),1);
i_t = t > 8.;
C57(i_t) = 0.; 
C57 = [t, C57];

% C6 ----------------------------
% Não abre.
C61 = C21; 

C62 = C21;

C63 = C21;

C64 = C21;

C65 = C21;

C66 = C21;

C67 = C21;

%%
% Executar a simulação.
sim('drive_faltadupla', tempo_max)

cd ../
CM = calculaCM(2., (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas duplas no drive'/faltaC15

save('C15CH4','CM')

