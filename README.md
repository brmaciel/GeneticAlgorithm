# GeneticAlgorithm


Ajuda para compreender a interface do algoritmo:
1. Criacao de Objeto:
  <p>GeneticAlgorithm(populationSize, numIterations, fitnessFunction, mutationProbs[opcional], elitism[opcional])</p>

2. Metodos Públicos:
2.1 Problemas Binarios:
  <p>binary_enconding(chromosomeSize, names, crossover[opcional])</p>
2.2 Problemas de Valor Real:
  <p>value_encoding(lower, upper, names, crossover[opcional])</p>
2.3 Problemas de Permutacao:
  <p>permutation_encoding(lower, upper, names, crossover[opcional])</p>

3. Valores de Retorno:
  <p>Os 3 metodos de resolucao de problemas (binary, value, permutation) retornam sempre o cromossomo melhor adaptado e seu respectivo nivel de adaptacao medido</p>
