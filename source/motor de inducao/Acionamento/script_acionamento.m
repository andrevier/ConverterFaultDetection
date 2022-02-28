% Script para obter os dados nominais do motor: velocidade nominal, velocidade síncrona
% e torque elétrico na velocidade síncrona.
% acionamento.slx

clearvars
close all

% Tempo da amostra
Ts = 2e-05;
tempo_max = 6.0;

% Execução da simulação.
sim('acionamento',tempo_max)

% Valores nominais rms.
S = 3*745.7;
Vn = 220;
In = S/(sqrt(3)*Vn);
Ipn = In*sqrt(2);

% Fim do período transitório
indice_transitorio = tempo < 1.;
[fim_do_transitortio, indice_fim_do_transitorio] = max(tempo(indice_transitorio));

% Torque máximo por conta do período transitório
[Te_max, indice_Te_max] = max(Te);

% Torque mínimo (na velocidade síncrona)
[Te_min, ~] = min(Te(indice_fim_do_transitorio:end));

% Velocidade máxima do rotor (síncrona)
[rs_max, indice_rs_max] = max(rotor_speed);

% Indice da corrente nominal
is_a_ = is_a(1:indice_fim_do_transitorio);
I_maior_que_nominal = is_a_ >= Ipn;
[Ipn_a, indice_Ipn_a] = min(is_a_(I_maior_que_nominal));
%indice_Ipn = indice_Ipn_a;
indice_Ipn = 36870;
tempo_Ipn = tempo(indice_Ipn);
rs_n = rotor_speed(indice_Ipn);
slip = (1800 - rs_n)/1800;
slip_max = (1800 - rs_max)/1800;

% pico da corrente do estator e pico rms
[isa_max,indice_isa_max] = max(is_a);
[is_rms_max, indice_is_rms_max] = max(is_rms);
is_sinc = is_rms(indice_rs_max);

fprintf('-------------------\n')

fprintf('Torque max: %.2f N.m; indice: %d\n', Te_max, indice_Te_max)
fprintf('Velocidade do torque max: %.2f rpm; indice: %d\n',rotor_speed(indice_Te_max),indice_Te_max)
fprintf('Velocidade máxima sem carga: %.2f rpm\n', rs_max)
fprintf('Torque na velocidade máxima: %.2f N.m\n',Te_min)
fprintf('Corrente na velocidade máxima: %.2f A rms\n',is_sinc)

fprintf('Velocidade nominal: %.2f rpm \n', rs_n)
fprintf('Escorregamento nominal: %.4f \n', slip)
fprintf('Escorregamento na velocidade máxima: %.4f \n', slip_max)
fprintf('Torque elétrico nominal: %.2f N.m\n', Te(indice_Ipn))
fprintf('Corrente nominal (pico): %.2f A \n', is_a(indice_Ipn))
fprintf('Pico da corrente do estator: %.2f A; indice %d\n', isa_max, indice_isa_max)
fprintf('Pico da corrente rms do estator: %.2f A rms; indice %d\n',is_rms_max, indice_is_rms_max)
fprintf('Corrente rms de maior carga: %.2f A rms; indice %d\n',is_rms(indice_Te_max), indice_Te_max);

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

% Gráfico com a magnitude da corrente
figure(2)
plot(tempo,is_a,'b')
xlabel('Tempo (s)');
ylabel('Isa (A)');
title('Curva da magnitude da corrente com o tempo.');
hold on
plot(tempo, is_rms,'r');
hold on
plot(tempo_Ipn,is_a(indice_Ipn),'ro');
xlabel('Tempo (s)');
ylabel('Is rms (A)');
title('Curva da corrente rms com o tempo.');
grid on

% Gráfico corrente e torque
figure(3)
plot(is_rms,Te)
xlabel('Is rms (A)')
ylabel('Torque elétrico N.m')
title('Curva corrente por torque')




