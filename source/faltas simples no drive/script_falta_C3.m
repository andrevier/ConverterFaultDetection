% Script para processar os dados dos sinais do drive em
% drive_AC1_modificado.slx em que há simulação de condições de falta
% através da aplicação de uma resistência em série com uma das chaves
% semicondutoras do conversor.

close all
clearvars

% Condições da simulação
Ts = 2.e-05;
tempo_max = 10.;
t = 0.:Ts:tempo_max;
t = transpose(t);

% Referência de torque: torque nominal a partir de 1s.
Tm = zeros(length(t),1);
i_t = t > 1.;
Tm(i_t) = 7.7;
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

% C2 ----------------------------
% Não abre.
C21 = C11; 

C22 = C12;

C23 = C13;

C24 = C14;

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

% chave C34 abre em 6s.
C34 = ones(length(t),1);
i_t = t > 8.;
C34(i_t) = 0.; 
C34 = [t, C34];

% C4 ----------------------------
% Não abre.
C41 = C11; 

C42 = C12;

C43 = C13;

C44 = C14;

% C5 ----------------------------
% Não abre.
C51 = C11; 

C52 = C12;

C53 = C13;

C54 = C14;

% C6 ----------------------------
% Não abre.
C61 = C11; 

C62 = C12;

C63 = C13;

C64 = C14;
%%
% Executar a simulação.
sim('drive_falta', tempo_max)

Ipn = 9.23;

cd ../
CM = calculaCM(2.5, (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas simples no drive'

% Gráficos
figure(1)
plot(tempo,Isa,'b')
hold on 
plot(tempo, Isb, 'r')
hold on
plot(tempo, Isc, 'g')
xlabel('Tempo (s)');
ylabel('Is (A)');
legend('Isa','Isb','Isc');
title('Correntes no estator')

figure(2)
plot(tempo, Te,'m')
hold on
plot(tempo, Tm, 'b')
xlabel('Tempo (s)');
ylabel('Torque (N.m)');
legend('Te','Tm');
title('Torque elétrico e da carga')

figure(3)
plot(tempo,N)
xlabel('Tempo (s)');
ylabel('Velocidade do rotor (rpm)');
legend('Referência','rotor')
title('Velocidade do rotor')

figure(4)
plot(tempo,Is_alpha,'b')
hold on 
plot(tempo,Is_beta,'r')
hold on
plot(tempo,Is_0)
legend('I alpha','I beta')
xlabel('Tempo (s)');
ylabel('Corrente (A)');
title('Correntes alpha e beta');

figure(5)
plot(real(CM), imag(CM), 'mo')
xlabel('Ialpha');
ylabel('Ibeta');
title('Correntes Médias');
grid on
xlim([-1 1])
ylim([-1 1])

