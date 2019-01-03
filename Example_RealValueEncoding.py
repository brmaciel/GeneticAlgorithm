# Problema:
# Encontrar melhor valor que resolve a equacao matematica

from GeneticAlgorithm import GeneticAlgorithm


def funcAdaptacao(x):
    # equacao = 2*x + 5 = 20
    resultado = 2 * x[0] + 5

    if resultado > 20:
        return 20 - resultado
    else:
        return resultado - 20


ga_value = GeneticAlgorithm(populationSize=10, numIterations=25, fitnessFunction=funcAdaptacao, elitism=0.4)
ga_value.value_encoding(lower=[-10], upper=[20], names=['valor'])
