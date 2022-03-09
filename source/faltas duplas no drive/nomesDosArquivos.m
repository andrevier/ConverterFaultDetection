% Gerar os nomes dos arquivos com o tipo de falta a ser acionado por eles.
% As faltas são designadas por Cij, em que i e j são os números das chaves
% que provocarão as faltas.

% São 6 chaves. Logo são C{6,2} = 15 elementos. Para identificar as
% combinações sem repetições, faremos uma matriz com 1's. A versão
% triangular inferior provê todos os índices necessários para as
% combinações sem a repetição.
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


