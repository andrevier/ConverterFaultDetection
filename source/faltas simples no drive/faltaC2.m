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
% Não abre.
C11 = ones(length(t),1); 
C11 = [t, C11];

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
% Abertura da chave C21 em 2s.
C21 = ones(length(t),1);
i_t = t > 2.;
C21(i_t) = 0.; 
C21 = [t, C21];

% chave C22 abre em 4s.
C22 = ones(length(t),1);
i_t = t > 4.;
C22(i_t) = 0.; 
C22 = [t, C22];

% chave C23 abre em 6s.
C23 = ones(length(t),1);
i_t = t > 6.;
C23(i_t) = 0.; 
C23 = [t, C23];

% chave C24 abre em 8s.
C24 = ones(length(t),1);
i_t = t > 8.;
C24(i_t) = 0.; 
C24 = [t, C24];

% chave C25 abre em 10s.
C25 = ones(length(t),1);
i_t = t > 10.;
C25(i_t) = 0.; 
C25 = [t, C25];

% chave C26 abre em 12s.
C26 = ones(length(t),1);
i_t = t > 12.;
C26(i_t) = 0.; 
C26 = [t, C26];

% chave C27 abre em 14s.
C27 = ones(length(t),1);
i_t = t > 14.;
C27(i_t) = 0.; 
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
% Não abre.
C51 = C11; 

C52 = C11;

C53 = C11;

C54 = C11;

C55 = C11;

C56 = C11;

C57 = C11;

% C6 ----------------------------
% Não abre.
C61 = C11; 

C62 = C11;

C63 = C11;

C64 = C11;

C65 = C11;

C66 = C11;

C67 = C11;

% Executar a simulação.
sim('drive_falta', tempo_max)

cd ../
CM = calculaCM(2.5, (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas simples no drive'

