# GeneticAlgorithm


Ajuda para compreender a interface do algoritmo:
1. Criacao de Objeto:
  GeneticAlgorithm(populationSize, numIterations, fitnessFunction, mutationProbs[opcional], elitism[opcional])

2. Metodos Públicos:
2.1 Problemas Binarios:
  binary_enconding(chromosomeSize, names, crossover[opcional])
2.2 Problemas de Valor Real:
  value_encoding(lower, upper, names, crossover[opcional])
2.3 Problemas de Permutacao:
  permutation_encoding(lower, upper, names, crossover[opcional])

3. Valores de Retorno:
  Os 3 metodos de resolucao de problemas (binary, value, permutation) retornam sempre o cromossomo melhor adaptado e seu respectivo nivel de adaptacao medido
