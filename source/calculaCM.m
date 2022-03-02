function CM = calculaCM(tempoTransitorio, tamanhoAmostra, Ipn, ...
                        tempo, Ialpha, Ibeta)
% C�lculo do vetor com as correntes m�dias (CM) das amostra.
% tempoTransitorio = O CM � calculado ap�s o valor de transit�rio para n�o 
% interferir nos dados. Geralmente, 1s. 
% tamanhoAmostra = O tamanho da amostra em que ser� feita a m�dia. 
% Ipn = valor m�ximo da corrente nominal.
% Ialpha e Ibeta = valor medido das corrente do estator nas transformadas 
% alpha e beta no tempo.
% tempo = vetor coletado do tempo da simula��o.

apos_transitorio = tempo > tempoTransitorio;

% Determinar um intervalo de coleta de amostras (ponto sens�vel de mem�ria):
% A frequ�ncia m�xima do motor � 60 Hz, o per�odo � 1/60 s.
% A amostra do tamanho do per�odoComo o passo de integra��o � Ts = 2e-05 s,
% nesse intervalo s�o coletados (1/60)/Ts pontos.
tamanhoAmostra = round(tamanhoAmostra);

% A quantidade de amostras
total_pontos = length(tempo(apos_transitorio));
qtd_amostra = round(total_pontos/tamanhoAmostra);

% Os pontos s�o particionados e armazenados nas matrizes Ialpha e Ibeta.
amostra_Ialpha = zeros(1,tamanhoAmostra);
amostra_Ibeta = zeros(1,tamanhoAmostra);
matriz_Ialpha = zeros(qtd_amostra,tamanhoAmostra);
matriz_Ibeta = zeros(qtd_amostra,tamanhoAmostra);

% Normalizar as correntes e armazenar os valores do per�do p�s transit�rio
% com o valor nominal da corrente de pico.
Ialpha_n = Ialpha(apos_transitorio)/Ipn;
Ibeta_n = Ibeta(apos_transitorio)/Ipn;

j = 1;
n = 1;
for i = 1:total_pontos
    amostra_Ialpha(j) = Ialpha_n(i);
    amostra_Ibeta(j) = Ibeta_n(i);
    
    if j >= tamanhoAmostra
        j = 1;
        matriz_Ialpha(n,:) = amostra_Ialpha;
        matriz_Ibeta(n,:) = amostra_Ibeta;
        n = n + 1;
        
        amostra_Ialpha = zeros(1,tamanhoAmostra);
        amostra_Ibeta = zeros(1,tamanhoAmostra);        
    else
        j = j + 1;
    end
    
    if n >= qtd_amostra
        break
    end    
end

% C�lculo da corrente m�dia para cada amostra
CM = zeros(1,qtd_amostra);

for i = 1:qtd_amostra
    CM(i) = (sum(matriz_Ialpha(i,:)) + 1j*sum(matriz_Ibeta(i,:)))/tamanhoAmostra;
end


end