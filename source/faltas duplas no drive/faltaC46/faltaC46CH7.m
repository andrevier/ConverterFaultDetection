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
% A simulação nesse script trata do disparo da 1ª à 7ª chave no IGBT C4 
% (CH1 à CH7) e dos disparos das demais no IGBT C6 (CH1-CH7).

% R71 até R77 de 2 até 8s....................
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

C42 = ones(length(t),1);
C42(i_t) = 0;
C42 = [t, C42];

C43 = ones(length(t),1);
C43(i_t) = 0;
C43 = [t, C43];

C44 = ones(length(t),1);
C44(i_t) = 0;
C44 = [t, C44];

C45 = ones(length(t),1);
C45(i_t) = 0;
C45 = [t, C45];

C46 = ones(length(t),1);
C46(i_t) = 0;
C46 = [t, C46];

C47 = ones(length(t),1);
C47(i_t) = 0;
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
% Executar a simulação.
sim('drive_faltadupla', tempo_max)

cd ../
CM = calculaCM(2., (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas duplas no drive'/faltaC46

save('C46CH7','CM')
