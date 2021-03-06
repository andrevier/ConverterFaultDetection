# Lista de Pendências do Projeto

- [x] 1. Ensaios com o motor de indução escolhido para coletar os dados nominais. Ensaio de torque-velocidade; Ensaio de rotor a vazio. Supor 5% de escorregamento.
- [x] 2. Drive básico montado para o acionamento e coletar as condições nominais. 
- [ ] 3. Controle para o drive do motor de indução. 
- [x] 4. Script em MATLAB analisando os sinais do motor: 
    - Corrente x Tempo;
    - Torque x Tempo;
    - Corrente Ialpha e Ibeta com o tempo;
    - Correntes Ialpha e Ibeta normalizadas;
    - Definição do tamanho da amostra coletada (N) para o cálculo do valor da corrente média (VCM);
- [x] 5. Analisar os sinais com as condições de falta do inversor: acrescentar resistências com vários valores em série com as chaves semicondutoras (IGBTs) e medir o VCM.
- [ ] 6. Definição da proteção do motor.
- [ ] 7. Iniciar o texto da dissertação.
- [ ] 8. Fazer experiências com diferentes tamanhos de amostras para o cálculo da corrente média (VCM).
- [x] 9. Variação das resistências inseridas em série nos conversores para entender o caminho das faltas.
- [x] 10. Testes de CC para a definição da proteção do motor.
- [ ] 11. Gráfico resumindo todas os dados coletados dos ensaios da corrente média (VCM) nas condições de falta (item 5).
- [x] 12. Condições de falta em 2 chaves por vez. Gerar gráfico resumindo os VCM obtidos.
- [ ] 13. Limite para as resistências em série nos ensaios de falta.
- [ ] 14. Fazer testes com motor com controle vetorial e de torque.
- [x] 15. Encontrar caminhos para gerar scripts automáticos para a execução dos testes, sem a necessidade de manualmente digitá-los.
- [ ] 16. Encontrar um critério para o limiar de qualidade do sinal do motor.
- [x] 17. Faltas em 3 semicondutores por vez com a graduação de resistências.
- [ ] 18. Usar filtro indutivo para o drive e estudar a influência no defeito vindo do filtro.
- [ ] 19. Influência do motor no VCM.
- [ ] 20. Influência dos harmônicos nos dados coletados.
- [ ] 21. Análise dos dados coletados: Padrões visuais de como os gráficos de VCM variam com a resistência e compará-los com os trabalhos passados.
- [ ] 22. Experimentos com faltas de C.A. combinadas com resistências em séries.   