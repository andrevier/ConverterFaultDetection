% Executar os testes e resumir os dados dos valores das correntes médias em
% 1 só gráfico.

faltaC1
save('CMC1','CM')

faltaC2
save('CMC2','CM')

faltaC3
save('CMC3','CM')

faltaC4
save('CMC4','CM')

faltaC5
save('CMC5','CM')

faltaC6
save('CMC6','CM')

clearvars

% Load
load('CMC1', 'CM')
CMC1 = CM;

load('CMC2', 'CM')
CMC2 = CM;

load('CMC3', 'CM')
CMC3 = CM;

load('CMC4', 'CM')
CMC4 = CM;

load('CMC5', 'CM')
CMC5 = CM;

load('CMC6', 'CM')
CMC6 = CM;

% Gráfico
close all
figure(1)
scatter(real(CMC1),imag(CMC1),'b')
hold on
scatter(real(CMC2),imag(CMC2),'y')
hold on 
scatter(real(CMC3),imag(CMC3),'m')
hold on 
scatter(real(CMC4),imag(CMC4),'k')
hold on 
scatter(real(CMC5),imag(CMC5),'r')
hold on 
scatter(real(CMC6),imag(CMC6),'g')
hold on 
xlabel('I alpha');
ylabel('I beta');
xlim([-1 1]);
ylim([-1 1]);
title('VCM ao adicionar resistências em série a 1 IGBT por vez.')
legend('C1', 'C2', 'C3', 'C4', 'C5', 'C6')
grid on

