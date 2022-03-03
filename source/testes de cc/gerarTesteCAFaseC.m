% An�lise dos dados para o testeCAFaseC.slx

clearvars
close all

% Dados indiciais 
Ts = 2e-5;
tempo_max = 10.0;

% Obter os valores nominais na tabela source\valoresNominais.txt
cd ..\
tabela = readtable('variaveisNominais.txt');

% Voltar para o arquivo testes de cc
cd 'testes de cc'

var = tabela.Variavel;
Ipn = var(4);
Ten = var(5);

% Execu��o do modelo.
sim('testeCAFaseC',tempo_max)

% An�lise dos dados
% vari�veis importantes: 
% tempo de transit�rio; 
% tamanho da amostra; 
% corrente nominal.
cd ../
CM = calculaCM(1.5, (1/60)/Ts, Ipn, tempo, Ialphad, Ibetad);
cd 'testes de cc'

