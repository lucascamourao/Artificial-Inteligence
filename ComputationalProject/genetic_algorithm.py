import random
import numpy as np
import matplotlib.pyplot as plt

# Parâmetros do problema
num_cidades = 15  # número de cidades
cost_matrix = [
    [0, 10, 15, 45, 5, 45, 50, 44, 30, 100, 67, 33, 90, 17, 50],
    [15, 0, 100, 30, 20, 25, 80, 45, 41, 5, 45, 10, 90, 10, 35],
    [40, 80, 0, 90, 70, 33, 100, 70, 30, 23, 80, 60, 47, 33, 25],
    [100, 8, 5, 0, 5, 50, 20, 20, 35, 55, 25, 5, 15, 3, 10],
    [17, 10, 33, 45, 0, 14, 50, 27, 33, 60, 17, 10, 20, 13, 71],
    [15, 70, 90, 20, 11, 0, 35, 30, 15, 18, 15, 35, 90, 23, 25],
    [25, 19, 18, 15, 20, 15, 0, 20, 10, 14, 10, 20, 15, 10, 18],
    [8, 20, 15, 60, 40, 33, 25, 0, 27, 60, 80, 35, 30, 41, 35],
    [21, 34, 17, 10, 11, 40, 8, 32, 0, 47, 76, 40, 21, 9, 31],
    [45, 5, 10, 60, 8, 20, 8, 20, 25, 0, 55, 30, 45, 25, 40],
    [38, 20, 23, 30, 5, 55, 50, 33, 70, 14, 0, 60, 35, 30, 21],
    [12, 15, 45, 21, 10, 100, 8, 20, 35, 43, 8, 0, 15, 100, 23],
    [80, 10, 90, 33, 70, 35, 45, 30, 40, 80, 45, 30, 0, 50, 20],
    [33, 90, 40, 18, 15, 50, 25, 90, 44, 43, 70, 5, 50, 0, 25],
    [25, 70, 45, 50, 5, 45, 20, 100, 25, 50, 35, 10, 90, 5, 0],
]  # tabela de distâncias entre as cidades

# Parâmetros do algoritmo genético
tamanho_populacao = 10
num_geracoes = 100
taxa_mutacao = 0.2
taxa_crossover = 0.8


# Função para calcular o comprimento de um caminho
def calcular_distancia(caminho):
    distancia_total = 0
    for i in range(len(caminho) - 1):
        distancia_total += cost_matrix[caminho[i]][caminho[i + 1]]
    distancia_total += cost_matrix[caminho[-1]][caminho[0]]  # Retorna à cidade inicial
    return distancia_total


# Função para gerar uma população inicial
def gerar_populacao_inicial():
    populacao = []
    for _ in range(tamanho_populacao):
        caminho = list(range(num_cidades))
        random.shuffle(caminho)
        populacao.append(caminho)
    return populacao


# Função para selecionar os melhores indivíduos (caminhos)
def selecionar(populacao):
    aptidoes = [1 / calcular_distancia(caminho) for caminho in populacao]
    soma_aptidoes = sum(aptidoes)
    probabilidades = [aptidao / soma_aptidoes for aptidao in aptidoes]

    # Seleção por roleta
    selecionados = random.choices(populacao, probabilidades, k=tamanho_populacao)
    return selecionados


# Função de cruzamento (crossover)
def crossover(pai, mae):
    if random.random() > taxa_crossover:
        return pai[:]

    ponto_inicial = random.randint(0, num_cidades - 1)
    ponto_final = random.randint(ponto_inicial + 1, num_cidades)

    filho = [None] * num_cidades
    filho[ponto_inicial:ponto_final] = pai[ponto_inicial:ponto_final]

    indice_mae = 0
    for i in range(num_cidades):
        if filho[i] is None:
            while mae[indice_mae] in filho:
                indice_mae += 1
            filho[i] = mae[indice_mae]

    return filho


# Função de mutação
def mutacao(caminho):
    if random.random() > taxa_mutacao:
        return caminho

    i, j = random.sample(range(num_cidades), 2)
    caminho[i], caminho[j] = caminho[j], caminho[i]
    return caminho


# Função principal do algoritmo genético
def algoritmo_genetico():
    populacao = gerar_populacao_inicial()
    melhores_caminhos = []
    melhores_distancias = []

    for geracao in range(num_geracoes):
        # Seleção
        selecionados = selecionar(populacao)

        # Cruzamento (crossover)
        nova_populacao = []
        for i in range(0, len(selecionados), 2):
            pai = selecionados[i]
            mae = selecionados[i + 1] if i + 1 < len(selecionados) else selecionados[0]
            filho = crossover(pai, mae)
            nova_populacao.append(filho)

        # Mutação
        nova_populacao = [mutacao(caminho) for caminho in nova_populacao]

        # Avaliar e atualizar a população
        populacao = nova_populacao
        distancias_caminhos = [calcular_distancia(caminho) for caminho in populacao]
        melhor_distancia_geracao = min(distancias_caminhos)
        melhor_caminho_geracao = populacao[np.argmin(distancias_caminhos)]

        melhores_caminhos.append(melhor_caminho_geracao)
        melhores_distancias.append(melhor_distancia_geracao)

    return melhores_caminhos, melhores_distancias


# Executando o algoritmo genético
melhores_caminhos, melhores_distancias = algoritmo_genetico()

# Exibindo o melhor caminho encontrado e a distância
melhor_caminho = melhores_caminhos[-1]
melhor_distancia = melhores_distancias[-1]

print(f"Melhor caminho encontrado: {melhor_caminho}")
print(f"Distância total: {melhor_distancia}")

# Plotando a evolução das distâncias ao longo das gerações
plt.plot(melhores_distancias)
plt.title("Evolução da distância ao longo das gerações")
plt.xlabel("Geração")
plt.ylabel("Distância total do caminho")
plt.show()
