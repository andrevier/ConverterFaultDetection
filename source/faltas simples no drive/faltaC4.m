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
% Não abre.
C31 = C11; 

C32 = C11;

C33 = C11;

C34 = C11;

C35 = C11;

C36 = C11;

C37 = C11;

% C4 ----------------------------
% Abertura da chave C41 em 2s.
C41 = ones(length(t),1);
i_t = t > 2.;
C41(i_t) = 0.; 
C41 = [t, C41];

% chave C42 abre em 4s.
C42 = ones(length(t),1);
i_t = t > 4.;
C42(i_t) = 0.; 
C42 = [t, C42];

% chave C43 abre em 6s.
C43 = ones(length(t),1);
i_t = t > 6.;
C43(i_t) = 0.; 
C43 = [t, C43];

% chave C44 abre em 8s.
C44 = ones(length(t),1);
i_t = t > 8.;
C44(i_t) = 0.; 
C44 = [t, C44];

% chave C45 abre em 10s.
C45 = ones(length(t),1);
i_t = t > 10.;
C45(i_t) = 0.; 
C45 = [t, C45];

% chave C46 abre em 12s.
C46 = ones(length(t),1);
i_t = t > 12.;
C46(i_t) = 0.; 
C46 = [t, C46];

% chave C47 abre em 14s.
C47 = ones(length(t),1);
i_t = t > 14.;
C47(i_t) = 0.; 
C47 = [t, C47];

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

