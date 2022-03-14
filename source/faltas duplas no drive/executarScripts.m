% Script para executar todos os scripts dos casos de faltas duplas.
% Como há muitos casos e eles estão divididos em pastas para melhor
% organização, prefere-se um código recursivo para que as alterações em 1
% caso possam ser feitas nos demais. 

close all
clearvars

casosFalta = {'faltaC12','faltaC13','faltaC14', 'faltaC15', 'faltaC16',...
              'faltaC23', 'faltaC24', 'faltaC25', 'faltaC26', ...
              'faltaC34', 'faltaC35', 'faltaC36', ...
              'faltaC45', 'faltaC46', ...
              'faltaC56'};

% Salvar os nomes dos arquivos pois eles serão apagados cada vez que os
% scripts rodarem.
save('casosFalta.mat','casosFalta')

% Iteração para percorrer as pastas e rodar todos os scripts nelas.
numPastas = length(casosFalta);
for j = 1:numPastas
    % Recarregar os nomes dos arquivos.
    load('casosFalta.mat','casosFalta')
    nomePasta = char(casosFalta(j));
    fprintf('\nExecutando a pasta %s\n', nomePasta)
    
    % Entrar na pasta.
    cd(nomePasta)
    arquivos = dir;
    save('arquivos','arquivos')
    
    % Quantos arquivos tem na pasta.
    numArquivos = length(arquivos);
    
    % Para cada script:
    for i = 1:numArquivos
        nomeScript = arquivos(i).name;
        
        % se não tiver final 'm', não roda.
        if isempty(regexp(nomeScript(end),'m')) ~= 1
            fprintf(' -> %s \n',nomeScript)
            run(nomeScript)
            % Espaço para testar se há problemas no valor da CM.
            if isempty(CM) == 1
                fprintf('   *VCM do ensaio é vazio\n')
            end
            
            % Recarregar os nomes dos scripts pois eles são apagados pelo 
            % script que foi rodado.
            load('arquivos','arquivos')
        end
    end
    
    % Após executar todos os arquivos, deletar a lista de nomes dos scripts
    % que foi salva.
    delete('arquivos.mat')
    fprintf('...............................\n')
    
    % Retornar para a pasta raíz.
    cd ..
end

% Apagar a lista com os nomes das pastas
delete('casosFalta.mat')
f = msgbox('FIM!');