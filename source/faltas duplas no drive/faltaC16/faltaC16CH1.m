% Script para processar os dados dos sinais do drive em
% drive_faltadupla.slx em que h? a simula??o de condi??es de falta
% atrav?s da aplica??o de uma resist?ncia em s?rie em duas das chaves
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

% Condi??es da simula??o
Ts = 2.e-05;
tempo_max = 9.;
t = 0.:Ts:tempo_max;
t = transpose(t);

% Refer?ncia de torque: torque nominal a partir de 1s.
Tm = zeros(length(t),1);
i_t = t > 1.;
Tm(i_t) = Ten;
Tmref = [t, Tm];

% Refer?ncia de velocidade: valor nominal desde a partida. 
n = 1800.*ones(length(t),1);
nref = [t, n];

%% Sinais para ativar as resist?ncias em s?rie com o IGBT. 
% Cada IGBT tem 7 resistores em s?rie que s?o acionados pelo disparo de uma
% chave em paralelo. A chave abre e o resistor passa a conduzir a corrente.
% A simula??o nesse script trata do disparo da primeira chave no IGBT C1 
% (CH1) e dos disparos das demais no IGBT C6 (CH1-CH7).

% R11 at? R17 de 2 at? 8s....................
% C1 ----------------------------
% Abertura da chave C11 em 2s.
C11 = ones(length(t),1);
i_t = t > 2.;
C11(i_t) = 0.; 
C11 = [t, C11];
%----------------------------
C12 = ones(length(t),1);
C12 = [t, C12];

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
% N?o abre.
C21 = ones(length(t),1); 
C21 = [t, C21];

C22 = C21;

C23 = C21;

C24 = C21;

C25 = C21;

C26 = C21;

C27 = C21;

% C3 ----------------------------
% N?o abre.
C31 = C21; 

C32 = C21;

C33 = C21;

C34 = C21;

C35 = C21;

C36 = C21;

C37 = C21;

% C4 ----------------------------
% N?o abre.
C41 = C21; 

C42 = C21;

C43 = C21;

C44 = C21;

C45 = C21;

C46 = C21;

C47 = C21;

% C5 ----------------------------
% N?o abre.
C51 = C21; 

C52 = C21;

C53 = C21;

C54 = C21;

C55 = C21;

C56 = C21;

C57 = C21;

% C6 ----------------------------
% Abertura da chave C61 em 2s.
C61 = ones(length(t),1);
i_t = t > 2.;
C61(i_t) = 0.; 
C61 = [t, C61];

% chave C62 abre em 3s.
C62 = ones(length(t),1);
i_t = t > 3.;
C62(i_t) = 0.; 
C62 = [t, C62];

% chave C63 abre em 4s.
C63 = ones(length(t),1);
i_t = t > 4.;
C63(i_t) = 0.; 
C63 = [t, C63];

% chave C64 abre em 5s.
C64 = ones(length(t),1);
i_t = t > 5.;
C64(i_t) = 0.; 
C64 = [t, C64];

% chave C65 abre em 6s.
C65 = ones(length(t),1);
i_t = t > 6.;
C65(i_t) = 0.; 
C65 = [t, C65];

% chave C66 abre em 7s.
C66 = ones(length(t),1);
i_t = t > 7.;
C66(i_t) = 0.; 
C66 = [t, C66];

% chave C67 abre em 8s.
C67 = ones(length(t),1);
i_t = t > 8.;
C67(i_t) = 0.; 
C67 = [t, C67];

%%
% Executar a simula??o.
sim('drive_faltadupla', tempo_max)

cd ../
CM = calculaCM(2., (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas duplas no drive'/faltaC16

save('C16CH1','CM')

