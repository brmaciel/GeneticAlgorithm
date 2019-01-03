from random import randint
from math import ceil, floor


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

        self.__generateNewPopulation(chromosomeRank)  # gera uma nova geracao de cromossomos (Elitismo-ou-Cruzamento+Mutacao)
        self.__chromosomePopulation = self.__newGeneration

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

    # Gera uma nova populacao
    def __generateNewPopulation(self, chromosomeRank):
        self.__newGeneration = []
        numUnvaribleOrganism = int(self.__elitism * self.__popSize)

        # Processo de Elitismo para os melhores adaptados
        for i in range(numUnvaribleOrganism):
            self.__newGeneration.append(self.__chromosomePopulation[chromosomeRank[i][0]])
        #print("New Generation Elitism: ")
        self.__printNewGeneration()

    # Funcoes de CRUZAMENTO entre cromossomos
    def __crossover(self, chromosome1, chromosome2):
        # Inicializa o processo de Crossover(cruzamento)
        if self.__crossoverMethod == 'two-points':
            newChromosome1, newChromosome2 = self.__two_points_crossover(chromosome1, chromosome2)
        else:
            newChromosome1, newChromosome2 = self.__single_point_crossover(chromosome1, chromosome2)

        return newChromosome1, newChromosome2

    @staticmethod
    def __single_point_crossover(chromossomeA, chromossomeB):
        # Utiliza o metodo SinglePoint, dividindo os cromossomos na metade
        # ex: [a,b,c,d, | e,f,g,h] para tamanho de cromossomos pares
        # ex: [a,b,c,d, | e,f,g] para tamanho de cromossomos impares
        # print("Single-Point Crossover Method")
        newChromossomeA = []
        newChromosomeB = []
        tamanho = len(chromossomeA)
        middle = ceil(tamanho / 2)

        # primeira metade do cromossomo permanece igual
        for i in range(middle):
            newChromossomeA.append(chromossomeA[i])
            newChromosomeB.append(chromossomeB[i])

        # segunda metade do cromossomo eh alterada
        # se tamanho do cromosso for impar, segunda metade tem tem um bit a menos que a primeira metade
        if len(chromossomeA) % 2 == 0:
            for i in range(middle, tamanho):
                newChromossomeA.append(chromossomeB[i])
                newChromosomeB.append(chromossomeA[i])
        else:
            for i in range(middle, tamanho):
                newChromossomeA.append(chromossomeB[i])
                newChromosomeB.append(chromossomeA[i])

        return newChromossomeA, newChromosomeB

    @staticmethod
    def __two_points_crossover(chromosomeA, chromosomeB):
        # Utiliza o metodo TwoPoint, dividindo os cromossomos em 3 partes, e trocando a informacao do meio
        # ex: [a b c | d e | f g h] para tamanho de cromossomos pares
        # ex: [a b | c d e | f g]   para tamanho de cromossomos impares
        # ex: [a | b | c]           para tamanho de cromossomos == 3 (caso especial)
        print("Two-Points Crossover Method")
        newChromosomeA = []
        newChromosomeB = []
        tamanho = len(chromosomeA)
        initialPoint = floor(tamanho / 2) - 1

        # primeira parte do cromossomo permanece igual
        for i in range(initialPoint):
            newChromosomeA.append(chromosomeA[i])
            newChromosomeB.append(chromosomeB[i])

        # segunda parte do cromossomo eh alterada
        if tamanho % 2 == 0:
            endPoint = initialPoint + 1
            for i in range(initialPoint, endPoint + 1):
                newChromosomeA.append(chromosomeB[i])
                newChromosomeB.append(chromosomeA[i])
        elif tamanho == 3:
            endPoint = initialPoint + 1
            newChromosomeA.append(chromosomeA[0])
            newChromosomeB.append(chromosomeB[0])
            newChromosomeA.append(chromosomeB[1])
            newChromosomeB.append(chromosomeA[1])
        else:
            endPoint = initialPoint + 2
            for i in range(initialPoint, endPoint + 1):
                newChromosomeA.append(chromosomeB[i])
                newChromosomeB.append(chromosomeA[i])

        # terceira parte do cromossomo permanece igual
        for i in range(endPoint + 1, tamanho):
            newChromosomeA.append(chromosomeA[i])
            newChromosomeB.append(chromosomeB[i])

        return newChromosomeA, newChromosomeB
    # end crossover

    # Funcoes de MUTACAO entre cromossomos
    def __check_mutation(self, chromosome, probability):
        # Verifica se a mutacao occorrera, se sim, inicializa o processo de Mutacao
        # 0 < probability < 1
        # ex: se 0.01   entao contador = 2 probability = 1, multiply 10^2 = 100
        # ex: se 0.0006 entao contador = 4 probability = 6, multiply 10^4 = 10,000

        # processo para tornar a probabilidade um numero inteiro para utilizar a funcao randint()
        contador = 0
        while probability % 1 != 0:
            probability = probability * 10
            contador += 1
        total = pow(10, contador)

        # realiza o sorteio para definir se ocorrera a mutacao
        if randint(1, total) <= probability:
            newChromosome = self.__mutation(chromosome)
        else:
            newChromosome = chromosome

        return newChromosome

    @staticmethod
    def __mutation(chromosome):
        # Altera um bit(gene) aleatorio de um cromossomo
        # print("Mutation Occured")
        bitMutated = randint(0, len(chromosome) - 1)
        chromosome[bitMutated] = 0 if chromosome[bitMutated] == 1 else 1

        return chromosome
    # end mutation

    ###     Metodos Auxiliares     ###
    def __printPopulation(self):
        for chromosome in self.__chromosomePopulation:
            print(chromosome)

    def __printNewGeneration(self):
        for chromosome in self.__newGeneration:
            print(chromosome)