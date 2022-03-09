% Gerar os nomes dos arquivos com o tipo de falta a ser acionado por eles.
% As faltas s�o designadas por Cij, em que i e j s�o os n�meros das chaves
% que provocar�o as faltas.

% S�o 6 chaves. Logo s�o C{6,2} = 15 elementos. Para identificar as
% combina��es sem repeti��es, faremos uma matriz com 1's. A vers�o
% triangular inferior prov� todos os �ndices necess�rios para as
% combina��es sem a repeti��o.
A = ones(6,6);
Tri = triu(A,1);
prodcart = '';
for i = 1:6
    for j = 1:6
        if Tri(i,j) > 0
            l = num2str(i);
            c = num2str(j);
            lc = [l c];
            prodcart = [prodcart ' ' lc];
            nome = ['faltaC' lc];
            mkdir(nome)
        end
    end
end

fprintf('\n')
fprintf(prodcart)
fprintf('\n')


