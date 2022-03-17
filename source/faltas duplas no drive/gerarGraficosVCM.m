% Script para gerar gráficos dos casos de faltas duplas.

close all
clearvars


%1
fprintf('\n Executando...%d de 15 \n',1)

cd('faltaC12')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%2
fprintf('\n Executando...%d de 15 \n',2)
cd('faltaC13')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%3
fprintf('\n Executando...%d de 15 \n',3)
cd('faltaC14')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%4
fprintf('\n Executando...%d de 15 \n',4)
cd('faltaC15')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%5
fprintf('\n Executando...%d de 15 \n',5)
cd('faltaC16')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%6
fprintf('\n Executando...%d de 15 \n',6)
cd('faltaC23')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%7
fprintf('\n Executando...%d de 15 \n',7)
cd('faltaC24')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%8
fprintf('\n Executando...%d de 15 \n',8)
cd('faltaC25')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%9

fprintf('\n Executando...%d de 15 \n',9)
cd('faltaC26')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%10
fprintf('\n Executando...%d de 15 \n',10)
cd('faltaC34')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%11
fprintf('\n Executando...%d de 15 \n',11)
cd('faltaC35')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%12
fprintf('\n Executando...%d de 15 \n',12)
cd('faltaC36')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%13
fprintf('\n Executando...%d de 15 \n',13)
cd('faltaC45')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%14
fprintf('\n Executando...%d de 15 \n',14)
cd('faltaC46')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..

%15
fprintf('\n Executando...%d de 15 \n',15)
cd('faltaC56')
arquivos = dir;
save('arquivos','arquivos')
tamArquivos = length(arquivos);
nome = '';
for i = 1:length(arquivos)
    nome = arquivos(i).name;
    if isempty(regexp(nome(end),'m')) ~= 1
        fprintf('executando %s ...\n',nome)
        run(nome)
        % Espaço para testar se há problemas no valor da CM.
        if isempty(CM) == 1
            fprintf('   -> VCM do ensaio é vazio\n')
        end
        % Os dados são apagados pelo script rodado.
        load('arquivos','arquivos')
    end
end
delete('arquivos.mat')
fprintf('...............................\n')
cd ..
f = msgbox('FIM!');