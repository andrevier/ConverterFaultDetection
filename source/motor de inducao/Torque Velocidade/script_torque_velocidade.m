% Script para obter a curva Torque x Velocidade do rotor do motor.
clearvars
close all

% Tempo da amostra
Ts = 2e-05;
tempo_max = 5.0;
sim('ensaio_torque_velocidade',tempo_max)

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
rotor_speed_nom = 1704.20;
maior_que_nominal = rotor_speed > rotor_speed_nom;
tam_maior_que_nominal = length(rotor_speed(maior_que_nominal));
indice_n_nom = length(Te) - tam_maior_que_nominal;
Te_nom = Te(indice_n_nom);
n_nom = rotor_speed(indice_n_nom);

% Fator de pot�ncia na velocidade nominal
pf_nom = power_factor(indice_n_nom);

% Velocidade m�xima do rotor
[rs_max,indice_rs_max] = max(rotor_speed);

% pico da corrente do estator
[isa_max,indice_isa_max] = max(is_a);
[is_rms_max, indice_is_rms_max] = max(is_rms);

% C�lculo do torque nominal a partir da corrente nominal:
I_nom = 5.87;
menor_que_nominal = is_rms < I_nom;
tam_menor_que_nominal = length(is_rms(menor_que_nominal));
indice_I_nom = length(is_rms) - tam_menor_que_nominal;
verificar_I_nom = is_rms(indice_I_nom);

% fator de pot�ncia
[pf,indice_pf] = max(power_factor);

fprintf('-------------------\n')
fprintf('Velocidade s�ncrona rotor: %.2f rpm; indice %d \n',rs_max,indice_rs_max)

fprintf('Torque max: %.2f N.m; indice: %d\n', Te_max, indice_Te_max)
fprintf('Velocidade do torque max: %.2f rpm ; indice: %d\n',rotor_speed(indice_Te_max),indice_Te_max)
fprintf('Escorregamento do torque max: %.2f \n\n',(rs_max - rotor_speed(indice_Te_max))/rs_max)

fprintf('Pico da corrente do estator: %.2f A ; indice %d\n', isa_max, indice_isa_max)
fprintf('Pico da corrente rms do estator: %.2f A rms; indice %d\n', is_rms_max, indice_is_rms_max)
fprintf('Corrente rms de maior carga: %.2f A rms; indice %d\n', is_rms(indice_Te_max), indice_Te_max);
fprintf('Fator de pot�ncia m�ximo atingido: %.2f\n', pf)
fprintf('corrigir:\n')
fprintf('Fator de pot�ncia nominal: %.2f\n', pf_nom)
fprintf('Torque nominal: %.2f\n', Te_nom)
fprintf('Velocidade nominal: %.2f\n\n', n_nom)

fprintf('Corrente nominal: %.2f\n', verificar_I_nom)
fprintf('Torque nominal: %.2f\n', Te(indice_I_nom))
fprintf('Fator de pot�ncia: %.2f\n', power_factor(indice_I_nom))
fprintf('Velocidade nominal: %.2f\n',rotor_speed(indice_I_nom))
fprintf('Escorregamento nominal: %.2f\n',(rs_max - rotor_speed(indice_I_nom))/rs_max)

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





