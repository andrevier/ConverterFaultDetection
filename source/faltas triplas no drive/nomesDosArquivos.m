% Gerar os nomes das pastas com o tipo de caso tratado por elas.
% As faltas s�o designadas por Cijk, em que i, j e k s�o os n�meros das 
% chaves em s�rie com as resist�ncias que provocar�o as faltas.

% S�o 6 chaves. Logo s�o C{6,3} = 20 elementos. 
nomesFaltas = {'C123', 'C124', 'C125', 'C126', ...
               'C134', 'C135', 'C136', ...
               'C145', 'C146', ...
               'C156', ...
               'C234', 'C235', 'C236', ...
               'C245', 'C246', ...
               'C256', ...
               'C345', 'C346', ...
               'C356', ...
               'C456'};

for i = 1:length(nomesFaltas)
    tipo = char(nomesFaltas(i));
    nome = ['falta' tipo];
    mkdir(nome)
end
           

