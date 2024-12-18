import random
import numpy as np
import matplotlib.pyplot as plt

NUM_CITIES = 15
DISTANCE_MATRIX = [
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
]

population_size = 50
num_generations = 2000
mutation_rate = 0.1
crossover_rate = 0.9
elitism_size = 2


def calculate_distance(path):
    return sum(DISTANCE_MATRIX[path[i]][path[i + 1]] for i in range(-1, NUM_CITIES - 1))


def generate_initial_population():
    return [
        random.sample(range(NUM_CITIES), NUM_CITIES) for _ in range(population_size)
    ]


def tournament_selection(population, k=5):
    selected = random.sample(population, k)
    return min(selected, key=calculate_distance)


def pmx_crossover(parent1, parent2):
    size = len(parent1)
    cx1, cx2 = sorted(random.sample(range(size), 2))
    child = [-1] * size
    child[cx1:cx2] = parent1[cx1:cx2]

    for i in range(cx1, cx2):
        if parent2[i] not in child:
            pos = i
            while child[pos] != -1:
                pos = parent2.index(parent1[pos])
            child[pos] = parent2[i]

    for i in range(size):
        if child[i] == -1:
            child[i] = parent2[i]

    return child


def mutate(path):
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(path)), 2)
        path[i], path[j] = path[j], path[i]
    return path


def genetic_algorithm():
    population = generate_initial_population()
    best_distances = []

    for generation in range(num_generations):
        new_population = sorted(population, key=calculate_distance)[:elitism_size]

        while len(new_population) < population_size:
            parent1 = tournament_selection(population)
            parent2 = tournament_selection(population)
            if random.random() < crossover_rate:
                child = pmx_crossover(parent1, parent2)
            else:
                child = parent1[:]
            child = mutate(child)
            new_population.append(child)

        population = new_population
        best_distances.append(calculate_distance(population[0]))

    return population[0], best_distances


best_path, best_distances = genetic_algorithm()
print(f"Best Route: {best_path}")
print(f"Total Cost: {best_distances[-1]}")

# Plota a evolução das distâncias
plt.plot(best_distances)
plt.title("Evolution of Cost - Genetic")
plt.xlabel("Generation")
plt.ylabel("Cost")
plt.show()
