% Script para obter os dados nominais do motor: velocidade nominal, velocidade síncrona
% e torque elétrico na velocidade síncrona.
% acionamento.slx

clearvars
close all

% Tempo da amostra
Ts = 2e-05;
tempo_max = 6.0;

% Valores nominais rms.
S = 3*745.7;
Vn = 220;
In = S/(sqrt(3)*Vn);
Ipn = In*sqrt(2);

% Execução da simulação.
sim('acionamento',tempo_max)

% Fim do período transitório
indice_transitorio = tempo < 1.;
[fim_do_transitortio, indice_fim_do_transitorio] = max(tempo(indice_transitorio));

% Torque máximo por conta do período transitório
[Te_max, indice_Te_max] = max(Te);

% Torque mínimo (na velocidade síncrona)
[Te_min, ~] = min(Te(indice_fim_do_transitorio:end));

% Velocidade máxima do rotor (síncrona)
[rs_max, indice_rs_max] = max(rotor_speed);

% Supondo o escorregamento 5%, podemos calcular a velocidade e torque
% nominal e a corrente. 
slip = 0.05;
slipmin = (1800 - rs_max)/1800;

% Velocidade nominal do motor (rpm).
rs_n_ = rs_max*(1 - slip);

% Encontrar seu índice.
rs_round = round(rotor_speed,2);
indice_menorquers_n = rs_round <= round(rs_n_,2);
[rs_n, indice_rs_n] = max(rs_round(indice_menorquers_n));

% pico da corrente do estator e pico rms
[isa_max,indice_isa_max] = max(is_a);
[is_rms_max, indice_is_rms_max] = max(is_rms);
is_sinc = is_rms(indice_rs_max);

% Valores nominais salvos em uma tabela
Ipn_ = is_a(indice_rs_n);
In_rms = is_rms(indice_rs_n);
Tenom = Te(indice_rs_n);
Valor = [round(S,2);  round(Vn,2); round(In_rms,2); round(Ipn_,2); round(Tenom,2); round(slip,2);  round(rs_n,2); round(rs_max,2)];
Unidade = {'VA'; 'Vrms'; 'Arms';  'A'; 'N.m';  '--'; 'rpm';  'rpm'};

nomesVar = {'Variáveis', 'Unidades'};
Nome = {'Potência'; 'Tensão nominal'; 'Corrente nominal'; 'Corrente nominal (pico)'; 'Torque nominal'; 'Slip'; 'Velocidade nominal'; 'Velocidade max'};
T = table(Nome, Valor, Unidade);

% Pegar o caminho da pasta source que está 2 níveis acima:
cd ..\..
source = pwd;
nomeArquivo = '\variaveisNominais.txt';
writetable(T, strcat(source,nomeArquivo));

% voltar para o diretorio inicial.
cd 'motor de inducao'\Acionamento

fprintf('-------------------\n')
fprintf('Valores nominais:\n')
fprintf('S = %.2f VA \n', S)
fprintf('Vn = %.2f V rms \n',Vn)
fprintf('In = %.2f A rms \n', In_rms)
fprintf('In (pico) = %.2f A \n', Ipn_)
fprintf('Torque elétrico nominal medido = %.2f N.m \n', Tenom)
fprintf('Velocidade nominal = %.2f rpm \n', rs_n)
fprintf('Escorregamento nominal = %.4f \n\n', slip)

fprintf('Valores na partida:\n')
fprintf('Torque de partida: %.2f N.m\n', Te_max)
fprintf('Velocidade do torque de partida: %.2f rpm\n',rotor_speed(indice_Te_max))
fprintf('Pico da corrente do estator: %.2f A; indice %d\n', isa_max, indice_isa_max)
fprintf('Pico da corrente rms do estator: %.2f A rms; indice %d\n\n',is_rms_max, indice_is_rms_max)

fprintf('Valores a vazio:\n')
fprintf('Velocidade a vazio: %.2f rpm\n', rs_max)
fprintf('Torque a vazio: %.2f N.m\n',Te_min)
fprintf('Corrente a vazio: %.2f A rms\n',is_sinc)
fprintf('Escorregamento a vazio: %.4f \n\n', slipmin)

% Gráfico Torque elétrico x tempo
figure(1);
subplot(1,2,1);
plot(tempo, Te)
xlabel('Tempo (s)');
ylabel('Torque Elétrico (N.m)');
title('Torque x tempo');
% hold on
% plot(tempo(indice_Te_max),Te_max,'ro')
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
hold on
plot(tempo, is_rms,'r');
xlabel('Tempo (s)');
ylabel('Corrente do estator(A)');
title('Curva da magnitude da corrente com o tempo.');
legend('|Isa|', 'Isa rms')
grid on



