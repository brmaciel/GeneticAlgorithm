# Problema:
# Quebra Cabeca 8 Rainhas

# Objetivo:
# Colocar 8 rainhas num tabuleiro de xadrez de forma que nenhum ataque seja possivel
# No xadrez, a rainha de locomove em qualquer direcao (horizontal/vertical/diagonal) e sem limites de casas

from GeneticAlgorithm import GeneticAlgorithm


def printBoard(tab):
    for r in tab:
        for c in r:
            print(f'{c}', end='  ')
        print(end='\n')


def criaTabuleiro(propSolution):
    numRows = len(propSolution)
    numCols = numRows
    # Cria tabuleiro de (n x n)
    board = []
    for n in range(numRows):
        board.append([0] * numCols)

    # Insere solucao proposta no tabuleiro
    for n in range(numRows):
        board[n][propSolution[n] - 1] = 1

    return board


def funcaoAdaptacao(propSolution):
    # print(f'Proposta de solucao: {propSolution}')
    # [1, 5, 8, 4, 2, 6, 7, 3]
    # cada numero representa qual a linha que a rainha ocupa em cada coluna
    # ex: rainha nas casas (linha,coluna): (1,1) (2,5) (3,8) (4,4) (5,2) (6,6) (7,7) (8,3)

    numRows = len(propSolution)
    numCols = numRows
    # Cria tabuleiro de 8x8
    tabuleiro = criaTabuleiro(propSolution)

    totalATK = 0  # conta o numero de ataques encontrados
    # Verifica quantos ATAQUES estao ocorrendo em LINHAS e COLUNAS
    for index, row in enumerate(tabuleiro):
        # se encontrar n rainhas, significa que ha n-1 ataque
        totalATK += sum(row) - 1  # soma ataques na linha
        count_queen_found = 0
        for c in range(len(propSolution)):
            count_queen_found += tabuleiro[c][index]
        totalATK += count_queen_found - 1 if count_queen_found > 0 else 0  # soma ataques na coluna

    # Verifica quantos ATAQUES estao ocorrendo nas DIAGONAIS
    # coleta as diagonais principais
    numDiagonais = (numCols - 1) * 2 + 1 - 2
    diag_principal = []
    n = 0
    while n < numDiagonais:
        if n <= int(numDiagonais / 2):
            # coleta as diagonais da parte superior do tabuleiro
            i = 0
            j = n
            diag_principal.append([])
            while j < numCols:
                diag_principal[n].append(tabuleiro[i][j])
                i += 1
                j += 1
            n += 1
        else:
            # coleta as diagonais da parte inferior do tabuleiro
            i = numRows - (numDiagonais - n) - 1
            j = 0
            diag_principal.append([])
            while i < numRows:
                diag_principal[n].append(tabuleiro[i][j])
                i += 1
                j += 1
            n += 1

    # coleta as diagonais secundarias
    diag_secondary = []
    n = 0
    while n < numDiagonais:
        if n <= int(numDiagonais / 2):
            # coleta as diagonais da parte inferior do tabuleiro
            i = numRows - 1
            j = n
            diag_secondary.append([])
            while j < numCols:
                diag_secondary[n].append(tabuleiro[i][j])
                i -= 1
                j += 1
            n += 1
        else:
            # coleta as diagonais da parte superior do tabuleiro
            i = (numDiagonais - n)
            j = 0
            diag_secondary.append([])
            while i > 0:
                diag_secondary[n].append(tabuleiro[i][j])
                i -= 1
                j += 1
            n += 1

    for p, s in zip(diag_principal, diag_secondary):
        totalATK += sum(p) - 1 if sum(p) > 0 else 0  # soma ataques nas diagonais principal
        totalATK += sum(s) - 1 if sum(s) > 0 else 0  # soma ataques nas diagonais secundarias

    return -totalATK


lower = [1, 1, 1, 1, 1, 1, 1, 1]
upper = [8, 8, 8, 8, 8, 8, 8, 8]
names = ['coluna da linha 1', 'coluna da linha 2', 'coluna da linha 3', 'coluna da linha 4',
         'coluna da linha 5', 'coluna da linha 6', 'coluna da linha 7', 'coluna da linha 8']

ga_permut = GeneticAlgorithm(populationSize=12, numIterations=25, fitnessFunction=funcaoAdaptacao, elitism=0.4)
resp, rank = ga_permut.permutation_encoding(lower=lower, upper=upper, names=names, crossover='position-based')

# Visualiza o tabuleiro objetido com a resposta final do algoritmo
tabuleiroResposta = criaTabuleiro(resp)
print(f'Proposta de resposta com {-rank} ataque(s): ')
printBoard(tabuleiroResposta)
