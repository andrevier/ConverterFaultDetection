% Script para obter os dados nominais do motor: velocidade nominal, velocidade s�ncrona
% e torque el�trico na velocidade s�ncrona.
% acionamento.slx

clearvars
close all

% Tempo da amostra
Ts = 2e-05;
tempo_max = 6.0;

% Execu��o da simula��o.
sim('acionamento',tempo_max)

% Valores nominais rms.
S = 3*745.7;
Vn = 220;
In = S/(sqrt(3)*Vn);
Ipn = In*sqrt(2);

% Fim do per�odo transit�rio
indice_transitorio = tempo < 1.;
[fim_do_transitortio, indice_fim_do_transitorio] = max(tempo(indice_transitorio));

% Torque m�ximo por conta do per�odo transit�rio
[Te_max, indice_Te_max] = max(Te);

% Torque m�nimo (na velocidade s�ncrona)
[Te_min, ~] = min(Te(indice_fim_do_transitorio:end));

% Velocidade m�xima do rotor (s�ncrona)
[rs_max, indice_rs_max] = max(rotor_speed);

% O c�lculo da velocidade, escorregamento e torque nominais dependem da
% �nica informa��o sobre o motor dispon�vel: a corrente nominal.
% Indice da corrente nominal calculado a partir do ensaio no tempo 3s, que
% � o tempo em que a velocidade nominal � obtida.
tempo3s = tempo > 3.;
indice3s = find(tempo3s);
indice_Ipn = indice3s(1);
tempo_Ipn = tempo(indice_Ipn);
rs_n = rotor_speed(indice_Ipn);
slip = (1800 - rs_n)/1800;
slip_max = (1800 - rs_max)/1800;

% pico da corrente do estator e pico rms
[isa_max,indice_isa_max] = max(is_a);
[is_rms_max, indice_is_rms_max] = max(is_rms);
is_sinc = is_rms(indice_rs_max);

% Valores nominais salvos em uma tabela
Ipn_ = is_a(indice_Ipn);
Tenom = Te(indice_Ipn);
Variavel = [round(S,2);  round(Vn,2);     round(In,2); round(Ipn_,2); round(Tenom,2); round(slip,2);  round(rs_n,2); round(rs_max,2)];
unidade = {'VA'; 'Vrms'; 'Arms';  'A'; 'N.m';  '--'; 'rpm';  'rpm'};

nomesVar = {'Vari�veis', 'Unidades'};
nomesLinhas = {'Pot�ncia'; 'Tens�o nominal'; 'Corrente nominal'; 'Corrente nominal (pico)'; 'Torque nominal'; 'Slip'; 'Velocidade nominal'; 'Velocidade max'};
T = table(nomesLinhas, Variavel, unidade);

% Pegar o caminho da pasta source que est� 2 n�veis acima:
cd ..\
cd ..\
source = pwd;
nomeArquivo = '\valoresNominais.txt';
writetable(T, strcat(source,nomeArquivo));

% voltar para o diretorio inicial.
cd 'motor de inducao'\Acionamento

fprintf('-------------------\n')
fprintf('Valores nominais:\n')
fprintf('S = %.2f VA \n', S)
fprintf('Vn = %.2f V rms \n',Vn)
fprintf('In = %.2f A rms \n', In)
fprintf('In medida (pico) = %.2f A \n', is_a(indice_Ipn))
fprintf('Torque el�trico nominal medido = %.2f N.m \n', Te(indice_Ipn))
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
fprintf('Escorregamento a vazio: %.4f \n\n', slip_max)

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

% Gr�fico com a magnitude da corrente
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




