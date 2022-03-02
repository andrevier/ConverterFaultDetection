% Script para processar os dados dos sinais do drive em
% drive_AC1_modificado.slx em que h� simula��o de condi��es de falta
% atrav�s da aplica��o de uma resist�ncia em s�rie com uma das chaves
% semicondutoras do conversor.

close all
clearvars

% Condi��es da simula��o
Ts = 2.e-05;
tempo_max = 10.;
t = 0.:Ts:tempo_max;
t = transpose(t);

% Refer�ncia de torque: torque nominal a partir de 1s.
Tm = zeros(length(t),1);
i_t = t > 1.;
Tm(i_t) = 7.7;
Tmref = [t, Tm];

% Refer�ncia de velocidade: valor nominal desde a partida. 
n = 1800.*ones(length(t),1);
nref = [t, n];

%% Sinais para ativar as resist�ncias em s�rie com o IGBT. 
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

% chave C14 abre em 6s.
C14 = ones(length(t),1);
i_t = t > 8.;
C14(i_t) = 0.; 
C14 = [t, C14];

% C2 ----------------------------
% N�o abre.
C21 = ones(length(t),1); 
C21 = [t, C21];

C22 = ones(length(t),1);
C22 = [t, C22];

C23 = ones(length(t),1);
C23 = [t, C23];

C24 = ones(length(t),1);
C24 = [t, C24];

% C3 ----------------------------
% N�o abre.
C31 = C21; 

C32 = C22;

C33 = C23;

C34 = C24;

% C4 ----------------------------
% N�o abre.
C41 = C21; 

C42 = C22;

C43 = C23;

C44 = C24;

% C5 ----------------------------
% N�o abre.
C51 = C21; 

C52 = C22;

C53 = C23;

C54 = C24;

% C6 ----------------------------
% N�o abre.
C61 = C21; 

C62 = C22;

C63 = C23;

C64 = C24;
%%
% Executar a simula��o.
sim('drive_falta', tempo_max)

Ipn = 9.23;

cd ../
CM = calculaCM(2.5, (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta); 
cd 'faltas simples no drive'

% Gr�ficos
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
title('Torque el�trico e da carga')

figure(3)
plot(tempo,N)
xlabel('Tempo (s)');
ylabel('Velocidade do rotor (rpm)');
legend('Refer�ncia','rotor')
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
title('Correntes M�dias');
grid on
xlim([-1 1])
ylim([-1 1])

