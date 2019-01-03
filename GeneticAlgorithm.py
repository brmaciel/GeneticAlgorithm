from random import randint


class GeneticAlgorithm(object):

    def __init__(self, populationSize, numIterations, fitnessFunction, mutationProbs=0.01, elitism=0.5):
        self.__popSize = populationSize         # numero total de cromossomos
        self.__numIter = numIterations          # numero maximo de iteracoes(geracoes)
        self.__fitness = fitnessFunction        # funcao de adaptacao (definida pelo usuario)
        self.__mutationProbability = mutationProbs  # probabilidade de ocorrer mutacoes em cada um dos cromossomos
        self.__elitism = elitism                # porcentagem dos individuos que sao mais adaptados e devem sobreviver
        self.__chromosomePopulation = []

    # Algoritmo Genetico para Codificacao Binaria
    def binary_enconding(self, chromosomeSize, names, crossover='single-point'):
        self.__chromosomeSize = chromosomeSize  # numero de genes dos cromossomos
        self.__crossoverMethod = crossover      # metodo de crossover ('single-point' ou 'two-points')
        self.__encoding_type = 'binary'

        self.__initializeGA()       # inicializa o processo do algoritmo genetico

    # Funcao que inicializa o processo do algoritmo genetico
    def __initializeGA(self):
        self.__setPopulation()

        self.__measureFitness(self.__fitness)  # chama a funcao para medir a adaptacao de cada cromossomo
        chromosomeRank = self.__evaluateFitness()  # avalia a pontuacao obtida por cada cromossomo

    # Cria a populacao (conjunto de cromossomos)
    def __setPopulation(self):
        for n in range(self.__popSize):
            self.__chromosomePopulation.append(self.__setChromosome())
        self.__printPopulation()

    # Cria cada um dos cromossomos
    def __setChromosome(self):
        c = []
        # Problemas Binarios tem cromossomos tipo [1, 0, 1, 0, 1, 0]
        for _ in range(self.__chromosomeSize):
            c.append(randint(0, 1))
        return c

    # Mede o nivel de adaptacao de cada cromossomo
    def __measureFitness(self, userFunction):
        self.__adaptabilityLevel = {}       # dicionario keys:'indice do cromossomo'; values:'nivel de adaptacao'
        for index, chromosome in enumerate(self.__chromosomePopulation):
            self.__adaptabilityLevel[index] = userFunction(chromosome)

    # Avalia o nivel de adaptacao de cada cromossomo
    # rankeando os cromossomos do melhor para o pior
    def __evaluateFitness(self):
        chromosomeRank = sorted(self.__adaptabilityLevel.items(), key=lambda x: -x[1])
        #print("Pontuacao:", self.__adaptabilityLevel)
        print("Rank:", chromosomeRank)
        return chromosomeRank

    ###     Metodos Auxiliares     ###
    def __printPopulation(self):
        for chromosome in self.__chromosomePopulation:
            print(chromosome)