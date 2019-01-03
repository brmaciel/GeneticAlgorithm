# Problema:
# Em uma viagem a um acampamento dispoem-se de uma lista de objetos,
# cada objeto tem seu valor em utilidade (pontos) e seu peso.

# Objetivo:
# Escolher a melhor combinacao de objetos (maior utilidade), nao ultrapassando o peso limite

from GeneticAlgorithm import GeneticAlgorithm


def funcaoAdaptacao(x):
    pesoLimite = 15
    pontos = [10, 20, 15, 2, 30, 10, 30]
    peso = [1, 5, 10, 1, 7, 5, 1]
    pesoTotal = pontosTotal = 0

    for i, j, k in zip(pontos, peso, x):
        pesoTotal += k * j
        pontosTotal += k * i

    if pesoTotal > pesoLimite:
        return 0
    else:
        return pontosTotal


objetos = ['canivete', 'feijao', 'batata', 'lanterna', 'saco de dormir', 'corda', 'bussola']
ga_binary = GeneticAlgorithm(populationSize=12, numIterations=12, fitnessFunction=funcaoAdaptacao, elitism=0.4)
ga_binary.binary_enconding(chromosomeSize=7, names=objetos, crossover='single-point')
