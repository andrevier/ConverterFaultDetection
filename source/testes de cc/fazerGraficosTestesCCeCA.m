% Fazer os gr�ficos com os dados do workspace para as simula��es de teste
% de cc e ca.

figure(1)
plot(tempo, N)
xlabel('Tempo (s)');
ylabel('Velocidade (rpm)');
title('Velocidade do rotor');
grid on
legend('Velocidade do rotor','refer�ncia');

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
plot(tempo,Ialphad)
hold on
plot(tempo,Ibetad)
xlabel('Tempo (s)');
ylabel('Correntes do estator (A)');
title('Correntes alpha e beta medidas na sa�da do drive.');
legend('I alpha', 'I beta');
grid on

figure(4)
plot(tempo,Te)
hold on
plot(tempo,Tmref)
xlabel('Tempo (s)');
ylabel('Torque (N.m)');
title('Torque eletromagn�tico');
grid on

figure(5)
plot(tempo,Vdc)
xlabel('Tempo (s)');
ylabel('Tens�o (V)');
title('Tens�o no elo CC');
grid on

figure(6)
plot(tempo, Ialphad/Ipn)
hold on 
plot(tempo, Ibetad/Ipn)
xlabel('Tempo (s)');
ylabel('Correntes do estator (pu)');
title('Correntes alpha e beta normalizadas');
legend('I alpha', 'I beta');
grid on

% A corrente deve ser medida na sa�da do inversor.
figure(7)
plot(real(CM),imag(CM),'mo')
xlabel('I alpha');
ylabel('I beta');
% xlim([-2 2])
% ylim([-2 2])
title('Valor da Corrente M�dia por amostra.')
grid on

% Correntes medidas na sa�da do inversor.
figure(8)
plot(tempo, Iarmsd,'g')
hold on 
plot(tempo, Ibrmsd, 'm')
hold on 
plot(tempo, Icrmsd, 'b')
xlabel('Tempo (s)');
ylabel('Correntes  (A rms)');
legend('Isa','Isb','Isc')
title('Correntes na sa�da do inversor (A RMS)')
grid on

