% Script para processar os dados dos sinais do drive em
% drive_AC1_modificado.slx em que há a simulação de condições de falta
% através da aplicação de uma resistência em série com uma das chaves
% semicondutoras do conversor.

close all
clearvars

% Obter valores nominais
cd ..\
tabela = readtable('variaveisNominais.txt');
cd 'faltas simples no drive'

var = tabela.Valor;
Ipn = var(4);
Ten = var(5);


% Condições da simulação
Ts = 2.e-05;
tempo_max = 16.;
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
% C1 ----------------------------
% Abertura da chave C11 em 2s.
C11 = ones(length(t),1);
i_t = t > 2.;
C11(i_t) = 0.; 
C11 = [t, C11];

% chave C12 abre em 4s.
C12 = ones(length(t),1);
i_t = t > 4.;
C12(i_t) = 0.; 
C12 = [t, C12];

% chave C13 abre em 6s.
C13 = ones(length(t),1);
i_t = t > 6.;
C13(i_t) = 0.; 
C13 = [t, C13];

% chave C14 abre em 8s.
C14 = ones(length(t),1);
i_t = t > 8.;
C14(i_t) = 0.; 
C14 = [t, C14];

% chave C15 abre em 10s.
C15 = ones(length(t),1);
i_t = t > 10.;
C15(i_t) = 0.; 
C15 = [t, C15];

% chave C16 abre em 12s.
C16 = ones(length(t),1);
i_t = t > 12.;
C16(i_t) = 0.; 
C16 = [t, C16];

% chave C17 abre em 14s.
C17 = ones(length(t),1);
i_t = t > 14.;
C17(i_t) = 0.; 
C17 = [t, C17];

% C2 ----------------------------
% Não abre.
C21 = ones(length(t),1); 
C21 = [t, C21];

C22 = ones(length(t),1);
C22 = [t, C22];

C23 = ones(length(t),1);
C23 = [t, C23];

C24 = ones(length(t),1);
C24 = [t, C24];

C25 = ones(length(t),1);
C25 = [t, C25];

C26 = ones(length(t),1);
C26 = [t, C26];

C27 = ones(length(t),1);
C27 = [t, C27];

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
% Não abre.
C51 = C21; 

C52 = C21;

C53 = C21;

C54 = C21;

C55 = C21;

C56 = C21;

C57 = C21;

% C6 ----------------------------
% Não abre.
C61 = C21; 

C62 = C21;

C63 = C21;

C64 = C21;

C65 = C21;

C66 = C21;

C67 = C21;

% Executar a simulação.
sim('drive_falta', tempo_max)

cd ../
CM = calculaCM(2.5, (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas simples no drive'

