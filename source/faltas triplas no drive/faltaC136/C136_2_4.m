% Script para iniciar os dados da simulação 
% drive_faltatripla.slx. O objetivo é fazer a simulação das condições de falta   
% através da aplicação de uma resistência em série em três das chaves
% semicondutoras do conversor por vez.
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


% Sinais para ativar as resistências em série com o IGBT. 
% Cada IGBT tem 7 resistores em série que são acionados pelo disparo de uma
% chave em paralelo. 

        % C1 ----------------------------
        % Abertura da chave C11 em 2s.
        C11 = ones(length(t),1);
        i_t = t > 2.;
        C11(i_t) = 0.; 
        C11 = [t, C11];

        C12 = ones(length(t),1);
        C12(i_t) = 0.;
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
        
        % C3 ----------------------------
        % Abertura da chave C31 em 2s.
        C31 = ones(length(t),1);
        i_t = t > 2.;
        C31(i_t) = 0.; 
        C31 = [t, C31];

        C32 = ones(length(t),1);
        C32(i_t) = 0.;
        C32 = [t, C32];

        C33 = ones(length(t),1);
        C33(i_t) = 0.;
        C33 = [t, C33];

        C34 = ones(length(t),1);
        C34(i_t) = 0.;
        C34 = [t, C34];

        C35 = ones(length(t),1);
        C35 = [t, C35];

        C36 = ones(length(t),1);
        C36 = [t, C36];

        C37 = ones(length(t),1);
        C37 = [t, C37];
        
        % C6 ----------------------------
        % Abre em 2s.
        C61 = ones(length(t),1);
        i_t = t > 2.;
        C61(i_t) = 0.; 
        C61 = [t, C61];

        % Abre em 3s.
        C62 = ones(length(t),1);
        i_t = t > 3.;
        C62(i_t) = 0;
        C62 = [t, C62];
        
        % Abre em 4s.  
        C63 = ones(length(t),1);
        i_t = t > 4.;
        C63(i_t) = 0.;
        C63 = [t, C63];

        % Abre em 5s.
        C64 = ones(length(t),1);
        i_t = t > 5.;
        C64(i_t) = 0.;
        C64 = [t, C64];

        % Abre em 6s.
        C65 = ones(length(t),1);
        i_t = t > 6.;
        C65(i_t) = 0.;
        C65 = [t, C65];
        
        % Não abrem.
        C66 = ones(length(t),1);
        C66 = [t, C66];

        C67 = ones(length(t),1);
        C67 = [t, C67];
        
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
        
        % C4 ----------------------------
        % Não abre.
        C41 = ones(length(t),1);
        C41 = [t, C41];

        C42 = ones(length(t),1);
        C42 = [t, C42];

        C43 = ones(length(t),1);
        C43 = [t, C43];

        C44 = ones(length(t),1);
        C44 = [t, C44];

        C45 = ones(length(t),1);
        C45 = [t, C45];

        C46 = ones(length(t),1);
        C46 = [t, C46];

        C47 = ones(length(t),1);
        C47 = [t, C47];
        
        % C5 ----------------------------
        % Não abre.
        C51 = ones(length(t),1);
        C51 = [t, C51];

        C52 = ones(length(t),1);
        C52 = [t, C52];

        C53 = ones(length(t),1);
        C53 = [t, C53];

        C54 = ones(length(t),1);
        C54 = [t, C54];

        C55 = ones(length(t),1);
        C55 = [t, C55];

        C56 = ones(length(t),1);
        C56 = [t, C56];

        C57 = ones(length(t),1);
        C57 = [t, C57];
        
    % Executar a simulação.
    sim('drive_faltatripla', tempo_max)

    cd ../
    CM = calculaCM(2., (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
    cd 'faltas triplas no drive'/faltaC136

    save('CM_C136_2_4','CM')