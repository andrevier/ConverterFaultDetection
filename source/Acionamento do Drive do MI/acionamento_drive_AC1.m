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
apos_transitorio = tempo > 1.5;

% Determinar um intervalo de coleta de amostras (ponto sensível de memória):
% A frequência máxima do motor é 60 Hz, o período é 1/60 s.
% A amostra do tamanho do períodoComo o passo de integração é Ts = 2e-05 s,
% nesse intervalo são coletados (1/60)/Ts pontos.
tam_amostra = round((1/60)/Ts);

% A quantidade de amostras
total_pontos = length(tempo(apos_transitorio));
qtd_amostra = round(total_pontos/tam_amostra);

% Os pontos são particionados e armazenados nas matrizes Ialpha e Ibeta.
amostra_Ialpha = zeros(1,tam_amostra);
amostra_Ibeta = zeros(1,tam_amostra);
matriz_Ialpha = zeros(qtd_amostra,tam_amostra);
matriz_Ibeta = zeros(qtd_amostra,tam_amostra);

% Normalizar as correntes e armazenar os valores do perído pós transitório
% com o valor nominal da corrente de pico.
max_I = Ipn;
Ialpha_n = Is_alpha(apos_transitorio)/max_I;
Ibeta_n = Is_beta(apos_transitorio)/max_I;

j = 1;
n = 1;
for i = 1:total_pontos
    amostra_Ialpha(j) = Ialpha_n(i);
    amostra_Ibeta(j) = Ibeta_n(i);
    
    if j >= tam_amostra
        j = 1;
        matriz_Ialpha(n,:) = amostra_Ialpha;
        matriz_Ibeta(n,:) = amostra_Ibeta;
        n = n + 1;
        
        amostra_Ialpha = zeros(1,tam_amostra);
        amostra_Ibeta = zeros(1,tam_amostra);        
    else
        j = j + 1;
    end
    
    if n >= qtd_amostra
        break
    end    
end

% Cálculo da corrente média para cada amostra
CM = zeros(1,qtd_amostra);

for i = 1:qtd_amostra
    CM(i) = (sum(matriz_Ialpha(i,:)) + 1j*sum(matriz_Ibeta(i,:)))/tam_amostra;
end

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
plot(tempo, Is_alpha/max_I)
hold on 
plot(tempo, Is_beta/max_I)
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


