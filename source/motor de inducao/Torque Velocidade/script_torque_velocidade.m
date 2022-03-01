% Script para obter a curva Torque x Velocidade do rotor do motor.
clearvars
close all

% Tempo da amostra
Ts = 2e-05;
tempo_max = 5.0;
sim('ensaio_torque_velocidade',tempo_max)

% Obter valores nominais na tabela source\valoresNominais.txt
cd ..\
cd ..\
tabela = readtable('valoresNominais.txt');

% Voltar para o arquivo Torque Velocidade
cd 'motor de inducao'\'Torque Velocidade'

var = tabela.Variavel;
Ipn = var(4);
rnom = var(7);

% O período transitório termina em 1.0s. Para melhorar o gráfico, podemos
% preencher esse período com a melhor curva parabólica que se encaixa nesse
% intervalo.
tempo_transitorio = 1.0;
remover_indice = tempo < tempo_transitorio;
constante = lsqcurvefit(@f,[0;0],tempo(remover_indice),Te(remover_indice));
Te(remover_indice) = f(constante,tempo(remover_indice));

% Torque máximo (pull-out)
[Te_max, indice_Te_max] = max(Te);

% Torque na velocidade nominal
rotorSpeed_round = round(rotor_speed,2);
r_MaiorQueNominal = rotorSpeed_round >= rnom;
indice_MaiorQueNominal = find(r_MaiorQueNominal);
indice_rnom = indice_MaiorQueNominal(1);
Te_nom = Te(indice_rnom);
tempo_nom = tempo(indice_rnom); 
n_nom = rotor_speed(indice_rnom);
slip_max = (1800. - rotor_speed(indice_Te_max))/1800.; 
% Fator de potência na velocidade nominal
pf_nom = power_factor(indice_rnom);

fprintf('-------------------\n')
fprintf('Fator de potência nominal: %.2f \n', pf_nom)
fprintf('Máximo torque (pull-out): %.2f N.m\n', Te_max)
fprintf('Máximo slip (pull-out): %.2f \n', slip_max)


linhasnovas = {'Torque máximo', round(Te_max,2), 'N.m';...
               'Slip máximo', round(slip_max,4), '--'};
tabelanova = [tabela;linhasnovas];

% Pegar a localização da pasta source que está 2 níveis acima:
cd ..\
cd ..\
source = pwd;
nomeArquivo = '\variaveisNominais.txt';
writetable(tabelanova, strcat(source,nomeArquivo));

% Voltar para o arquivo Torque Velocidade
cd 'motor de inducao'\'Torque Velocidade'

% Gráfico Torque elétrico x tempo
figure(1);
subplot(1,2,1);
plot(tempo, Te)
xlabel('Tempo (s)');
ylabel('Torque Elétrico (N.m)');
title('Torque x tempo');
hold on
plot(tempo(indice_Te_max),Te_max,'ro')
grid on

% Gráfico Velocidade do rotor x tempo
subplot(1,2,2);
plot(tempo, rotor_speed)
xlabel('Tempo (s)');
ylabel('Velocidade do rotor (rpm)');
title('Velocidade do rotor x tempo');
grid on


% Gráfico torque x velocidade
figure(2);
plot(rotor_speed,Te)
xlabel('velocidade do rotor (rpm)');
ylabel('Torque elétrico (N.m)');
title('Curva torque x velocidade do motor de indução 3 HP- 220 Vrms - 60 Hz.')
hold on
plot(rotor_speed(indice_Te_max),Te_max,'ro')

% Gráfico com a magnitude da corrente
figure(3)
subplot(1,2,1);
plot(tempo,is_a)
xlabel('Tempo (s)');
ylabel('Isa (A)');
title('Curva da magnitude da corrente com o tempo.');

subplot(1,2,2);
plot(tempo, is_rms);
xlabel('Tempo (s)');
ylabel('Is rms (A)');
title('Curva da corrente rms com o tempo.');

% Gráfico do fator de potência
figure(4)
subplot(1,2,1);
plot(tempo,power_factor)
xlabel('Tempo (s)');
ylabel('Fator de potência');
title('Curva do fator de potência');

subplot(1,2,2);
plot(rotor_speed,power_factor)
xlabel('velocidade do rotor (rpm)');
ylabel('Fator de potência');
title('Curva do fator de potência');





