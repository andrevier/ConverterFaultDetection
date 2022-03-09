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
% A simulação nesse script trata do disparo da primeira e da segunda chave
% no IGBT C1 (CH1 e CH2) e dos disparos das demais no IGBT C2 (CH1-CH7).

% R21 até R27 de 2 até 8s....................
% C1 ----------------------------
% Abertura da chave C11 em 2s.
C11 = ones(length(t),1);
i_t = t > 2.;
C11(i_t) = 0.; 
C11 = [t, C11];

C12 = ones(length(t),1);
i_t = t > 2.;
C12(i_t) = 0;
C12 = [t, C12];
% ------------------------------

C13 = ones(length(t),1);
C13 = [t, C13];

C14 = ones(length(t),1);
C14 = [t, C14];

C15 = ones(length(t),1);
C15 = [t, C15];

C16 = ones(length(t),1);
C16 = [t, C16];

C17 = ones(length(t),1);
C17 = [t, C17];

% C2 ----------------------------
% Abertura da chave C21 em 2s.
C21 = ones(length(t),1);
i_t = t > 2.;
C21(i_t) = 0.; 
C21 = [t, C21];

% chave C22 abre em 3s.
C22 = ones(length(t),1);
i_t = t > 3.;
C22(i_t) = 0.; 
C22 = [t, C22];

% chave C23 abre em 4s.
C23 = ones(length(t),1);
i_t = t > 4.;
C23(i_t) = 0.; 
C23 = [t, C23];

% chave C24 abre em 5s.
C24 = ones(length(t),1);
i_t = t > 5.;
C24(i_t) = 0.; 
C24 = [t, C24];

% chave C25 abre em 6s.
C25 = ones(length(t),1);
i_t = t > 6.;
C25(i_t) = 0.; 
C25 = [t, C25];

% chave C26 abre em 7s.
C26 = ones(length(t),1);
i_t = t > 7.;
C26(i_t) = 0.; 
C26 = [t, C26];

% chave C27 abre em 8s.
C27 = ones(length(t),1);
i_t = t > 8.;
C27(i_t) = 0.; 
C27 = [t, C27];

% C3 ----------------------------
% Não abre.
C31 = ones(length(t),1); 
C31 = [t, C31];

C32 = C31;

C33 = C31;

C34 = C31;

C35 = C31;

C36 = C31;

C37 = C31;

% C4 ----------------------------
% Não abre.
C41 = C31; 

C42 = C31;

C43 = C31;

C44 = C31;

C45 = C31;

C46 = C31;

C47 = C31;

% C5 ----------------------------
% Não abre.
C51 = C31; 

C52 = C31;

C53 = C31;

C54 = C31;

C55 = C31;

C56 = C31;

C57 = C31;

% C6 ----------------------------
% Não abre.
C61 = C31; 

C62 = C31;

C63 = C31;

C64 = C31;

C65 = C31;

C66 = C31;

C67 = C31;

%%
% Executar a simulação.
sim('drive_faltadupla', tempo_max)

cd ../
CM = calculaCM(2., (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas duplas no drive'/faltaC12

save('C12CH2','CM')

