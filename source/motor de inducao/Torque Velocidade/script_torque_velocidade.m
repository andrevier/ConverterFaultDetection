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

% O per�odo transit�rio termina em 1.0s. Para melhorar o gr�fico, podemos
% preencher esse per�odo com a melhor curva parab�lica que se encaixa nesse
% intervalo.
tempo_transitorio = 1.0;
remover_indice = tempo < tempo_transitorio;
constante = lsqcurvefit(@f,[0;0],tempo(remover_indice),Te(remover_indice));
Te(remover_indice) = f(constante,tempo(remover_indice));

% Torque m�ximo (pull-out)
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
% Fator de pot�ncia na velocidade nominal
pf_nom = power_factor(indice_rnom);

fprintf('-------------------\n')
fprintf('Fator de pot�ncia nominal: %.2f \n', pf_nom)
fprintf('M�ximo torque (pull-out): %.2f N.m\n', Te_max)
fprintf('M�ximo slip (pull-out): %.2f \n', slip_max)


linhasnovas = {'Torque m�ximo', round(Te_max,2), 'N.m';...
               'Slip m�ximo', round(slip_max,4), '--'};
tabelanova = [tabela;linhasnovas];

% Pegar a localiza��o da pasta source que est� 2 n�veis acima:
cd ..\
cd ..\
source = pwd;
nomeArquivo = '\variaveisNominais.txt';
writetable(tabelanova, strcat(source,nomeArquivo));

% Voltar para o arquivo Torque Velocidade
cd 'motor de inducao'\'Torque Velocidade'

% Gr�fico Torque el�trico x tempo
figure(1);
subplot(1,2,1);
plot(tempo, Te)
xlabel('Tempo (s)');
ylabel('Torque El�trico (N.m)');
title('Torque x tempo');
hold on
plot(tempo(indice_Te_max),Te_max,'ro')
grid on

% Gr�fico Velocidade do rotor x tempo
subplot(1,2,2);
plot(tempo, rotor_speed)
xlabel('Tempo (s)');
ylabel('Velocidade do rotor (rpm)');
title('Velocidade do rotor x tempo');
grid on


% Gr�fico torque x velocidade
figure(2);
plot(rotor_speed,Te)
xlabel('velocidade do rotor (rpm)');
ylabel('Torque el�trico (N.m)');
title('Curva torque x velocidade do motor de indu��o 3 HP- 220 Vrms - 60 Hz.')
hold on
plot(rotor_speed(indice_Te_max),Te_max,'ro')

% Gr�fico com a magnitude da corrente
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

% Gr�fico do fator de pot�ncia
figure(4)
subplot(1,2,1);
plot(tempo,power_factor)
xlabel('Tempo (s)');
ylabel('Fator de pot�ncia');
title('Curva do fator de pot�ncia');

subplot(1,2,2);
plot(rotor_speed,power_factor)
xlabel('velocidade do rotor (rpm)');
ylabel('Fator de pot�ncia');
title('Curva do fator de pot�ncia');





