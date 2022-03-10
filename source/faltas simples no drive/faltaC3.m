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
% Não abre.
C21 = C11; 

C22 = C11;

C23 = C11;

C24 = C11;

C25 = C11;

C26 = C11;

C27 = C11;

% C3 ----------------------------
% Abertura da chave C31 em 2s.
C31 = ones(length(t),1);
i_t = t > 2.;
C31(i_t) = 0.; 
C31 = [t, C31];

% chave C32 abre em 4s.
C32 = ones(length(t),1);
i_t = t > 4.;
C32(i_t) = 0.; 
C32 = [t, C32];

% chave C33 abre em 6s.
C33 = ones(length(t),1);
i_t = t > 6.;
C33(i_t) = 0.; 
C33 = [t, C33];

% chave C34 abre em 8s.
C34 = ones(length(t),1);
i_t = t > 8.;
C34(i_t) = 0.; 
C34 = [t, C34];

% chave C35 abre em 10s.
C35 = ones(length(t),1);
i_t = t > 10.;
C35(i_t) = 0.; 
C35 = [t, C35];

% chave C36 abre em 12s.
C36 = ones(length(t),1);
i_t = t > 12.;
C36(i_t) = 0.; 
C36 = [t, C36];

% chave C37 abre em 14s.
C37 = ones(length(t),1);
i_t = t > 14.;
C37(i_t) = 0.; 
C37 = [t, C37];

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

