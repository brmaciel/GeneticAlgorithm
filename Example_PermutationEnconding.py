# Problema:
# Caixeiro Viajante

# Objetivo:
# Encontrar a menor distancia necessaria para percorrer todas as cidades

from GeneticAlgorithm import GeneticAlgorithm


def funcaoAdaptacao(propSolution):
    #print(f'Proposta de solucao: {propSolution}')
    # [2, 3, 4, 1, 0] indica que:
    # cidadeA eh a terceira,
    # cidadeB eh a quarta,
    # cidadeC eh a ultima,
    # cidadeD eh a segunda,
    # cidadeE eh a primeira

    # cria dicionario para associar indices a ordem estabelecida
    dicion_aux = {}
    for n in range(len(propSolution)):
        dicion_aux[n] = propSolution[n]
    # ordena as cidades de acordo com a proposta de solucao
    ordem = sorted(dicion_aux.items(), key=lambda x: x[1])

    distancia = 0
    # Codigo para comecar em uma cidade e terminar em outra
    #cidadeInicial = ordem[0][0]                 # Descomente para considerar que deve retornar a cidade inicial
    for i in range(len(propSolution) - 1):
        cidade1 = ordem[i][0]
        cidade2 = ordem[i + 1][0]
        distancia += mapa[cidade1][cidade2]
    #distancia = distancia + mapa[cidade2][cidadeInicial]   # Descomente p/ considerar que deve retornar a 1 cidade
    #print(f'Distance: {distancia}')

    return -distancia


cidades = ['Linden', 'Parika', 'Lethem', 'Rosignol', 'New Amsterdam']
mapa = [[0, 8, 25, 10, 9],
        [8, 0, 13, 10, 10],
        [25, 13, 0, 12, 14],
        [10, 10, 12, 0, 21],
        [9, 10, 14, 21, 0]]

ga_permut = GeneticAlgorithm(populationSize=12, numIterations=25, fitnessFunction=funcaoAdaptacao, elitism=0.4)
ga_permut.permutation_encoding(lower=[0, 0, 0, 0, 0], upper=[4, 4, 4, 4, 4], names=cidades, crossover='position-based')
