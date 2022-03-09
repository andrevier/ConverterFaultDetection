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
% A simulação nesse script trata do disparo da 1ª à 4ª chave no IGBT C2 
% (CH1 à CH4) e dos disparos das demais no IGBT C5 (CH1-CH7).

% R41 até R47 de 2 até 8s....................
% C1 ----------------------------
% Não abre.
C11 = ones(length(t),1); 
C11 = [t, C11];

C12 = C11;

C13 = C11;

C14 = C11;

C15 = C11;

C16 = C11;

C17 = C11;

% C2 ----------------------------
% Abertura da chave C21 em 2s.
C21 = ones(length(t),1);
i_t = t > 2.;
C21(i_t) = 0.; 
C21 = [t, C21];

C22 = ones(length(t),1);
C22(i_t) = 0;
C22 = [t, C22];

C23 = ones(length(t),1);
C23(i_t) = 0;
C23 = [t, C23];

C24 = ones(length(t),1);
C24(i_t) = 0;
C24 = [t, C24];
%----------------------------
C25 = ones(length(t),1);
C25 = [t, C25];

C26 = ones(length(t),1);
C26 = [t, C26];

C27 = ones(length(t),1);
C27 = [t, C27];

% C3 ----------------------------
% Não abre.
C31 = C11; 

C32 = C11;

C33 = C11;

C34 = C11;

C35 = C11;

C36 = C11;

C37 = C11;

% C4 ----------------------------
% Não abre.
C41 = C11; 

C42 = C11;

C43 = C11;

C44 = C11;

C45 = C11;

C46 = C11;

C47 = C11;

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
C61 = C11; 

C62 = C11;

C63 = C11;

C64 = C11;

C65 = C11;

C66 = C11;

C67 = C11;

%%
% Executar a simulação.
sim('drive_faltadupla', tempo_max)

cd ../
CM = calculaCM(2., (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas duplas no drive'/faltaC25

save('C25CH4','CM')

