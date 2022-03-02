% Análise dos dados do modelo drive_AC1.slx

clearvars
close all

% Dados indiciais 
Ts = 2e-5;
tempo_max = 5.0;

% Obter os valores nominais na tabela source\valoresNominais.txt
cd ..\
tabela = readtable('variaveisNominais.txt');

% Voltar para o arquivo Acionamento do Drive MI
cd 'Acionamento do Drive do MI'

var = tabela.Variavel;
Ipn = var(4);
Ten = var(5);

% Execução do modelo.
sim('drive_AC1',tempo_max)

% Análise dos dados
% variáveis importantes: 
% tempo de transitório; 
% tamanho da amostra; 
% corrente nominal.
cd ../
CM = calculaCM(1.5, (1/60)/Ts, Ipn, tempo, Is_alpha, Is_beta);
cd 'Acionamento do Drive do MI'

% Gráficos
figure(1)
plot(tempo, N)
xlabel('Tempo (s)');
ylabel('Velocidade (rpm)');
title('Velocidade do rotor');
grid on
legend('Velocidade do rotor','referência');

figure(2)
plot(tempo,Isa)
hold on
plot(tempo,Isb)
hold on 
plot(tempo,Isc)
xlabel('Tempo (s)');
ylabel('Correntes (A)');
title('Correntes do estator');
legend('Isa','Isb','Isc');
grid on

figure(3)
plot(tempo,Is_alpha)
hold on
plot(tempo,Is_beta)
xlabel('Tempo (s)');
ylabel('Correntes do estator (A)');
title('Correntes alpha e beta');
legend('Is alpha', 'Is beta');
grid on

figure(4)
plot(tempo,Te)
hold on
plot(tempo,Tmref)
xlabel('Tempo (s)');
ylabel('Torque (N.m)');
title('Torque eletromagnético');
grid on

figure(5)
plot(tempo,Vdc)
xlabel('Tempo (s)');
ylabel('Tensão (V)');
title('Tensão no elo CC');
grid on


figure(6)
plot(tempo, Is_alpha/Ipn)
hold on 
plot(tempo, Is_beta/Ipn)
xlabel('Tempo (s)');
ylabel('Correntes do estator (pu)');
title('Correntes alpha e beta normalizadas');
grid on

figure(7)
plot(real(CM),imag(CM),'mo')
xlabel('I alpha');
ylabel('I beta');
xlim([-2 2])
ylim([-2 2])
grid on


