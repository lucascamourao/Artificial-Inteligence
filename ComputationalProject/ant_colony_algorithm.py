import random
import numpy as np
import matplotlib.pyplot as plt

"""
DEFINING THE PROBLEM ======================================================================


pij = amount of pheromone between i-city and j-city
cost matrix 'pheromone_matrix'
ex: pheromone_matrix[i][j]

cij = distance between i-city and j-city
cost matrix 'DISTANCE_MATRIX'
ex: DISTANCE_MATRIX[i][j]

The DESIRE of moving from city i to city j is (pij**ALPHA) * (cij**BETA)

Let 

S = SUM[ (pim**ALPHA) * (cim**BETA) ], for all m-city allowed

be the sum of desires of moving from city i to all *allowed* cities

Thus, the probability P of moving from city i to city j is 

P = DESIRE/ S
"""

ALPHA = 1  # definied empirically
BETA = 2  # definied empirically
NUM_CITIES = 15
MAX_ITERATIONS = 1000
Q = 100  # constant for pheromone formula
p = 0.5  # coeficient of evaporation

ANT_PATHS = []  # choose how many ants (iterations)
# ([path], cost) tuple

# Cost of going from i-city and j-city. Lines (i)/ Rows (j)
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

# amount of pheromone between i-city and j-city
# Initialized with 0s
pheromone_matrix = np.full((NUM_CITIES, NUM_CITIES), 1.0, dtype=float)


# List of probability of a city 'start' to go to all other cities
# The nodes are integers and we use cost matrices
def probability_to_go(start, allowed, pheromone_matrix, DISTANCE_MATRIX):
    total_desires = 0.0
    list_probability = []  # list of probabilities by city

    for city in allowed:
        pij = (pheromone_matrix[start][city]) ** ALPHA
        cij = (1 / DISTANCE_MATRIX[start][city]) ** BETA
        desire = pij * cij
        list_probability.append(desire)
        total_desires += desire

    if total_desires > 0:
        # Dividing all the element (the desires) by the total to find the probability
        list_probability = [p / total_desires for p in list_probability]

    return list_probability


"""
    Update Pheromone ==========================================

    Let Q be a constant
    Let Lk(t) the length of the root traveled by the ant k

    The pheromone adition A the ant_k makes in route i-j at iteration iter is

    A = Q/ Lk(t), provide the root i-j is in line with route of the ant (there is no going back to visited places)
    if it's not, the A = 0
    """


# Update the pheromone matrix
def update_pheromone(path, pheromone_matrix, length_route):
    for i in range(len(path) - 1):
        i_city = path[i]
        j_city = path[i + 1]
        pheromone_matrix[i_city][j_city] += Q / length_route
        pheromone_matrix[j_city][i_city] += Q / length_route  # simetric


def update_evaporation_pheromone(pheromone_matrix):
    # total_p is the total of pheromones that all the ants left in this area
    pheromone_matrix *= 1 - p


# Colony of Ants Optimization Algorithm ========================================================================


def ant_colony_optimization(MAX_ITERATIONS):
    best_path = []
    best_cost = float("inf")
    best_cost_history = []

    for _ in range(MAX_ITERATIONS):
        current_path = []  # Track the ant's path
        total_length = 0
        current_city = random.randint(
            0, NUM_CITIES - 1
        )  # Começar de uma cidade aleatória
        visited = {current_city}
        current_path.append(current_city)

        while len(visited) < NUM_CITIES:
            # Get probabilities for the current city
            allowed_cities = set(range(NUM_CITIES)) - visited  # not visited cities
            probabilities = probability_to_go(
                current_city,
                allowed_cities,
                pheromone_matrix,
                DISTANCE_MATRIX,
            )

            # Select the next city based on the probabilities
            next_city = np.random.choice(list(allowed_cities), p=probabilities)

            visited.add(next_city)
            total_length += DISTANCE_MATRIX[current_city][next_city]
            current_path.append(next_city)
            current_city = next_city

        # Adding the cost of going back to the starting city
        total_length += DISTANCE_MATRIX[current_city][current_path[0]]
        current_path.append(current_path[0])

        # Verify if it's the best route
        if total_length < best_cost:
            best_cost = total_length
            best_path = current_path

        update_pheromone(current_path, pheromone_matrix, total_length)
        update_evaporation_pheromone(pheromone_matrix)

        best_cost_history.append(
            best_cost
        )  # Save the history of best cost, for plotting

    return best_path, best_cost, best_cost_history


best_path, best_cost, best_cost_history = ant_colony_optimization(MAX_ITERATIONS)

# Results
best_path_as_ints = [int(city) for city in best_path]  # Converte para int
print(f"Best Route: {best_path_as_ints}")
print(f"Total Cost: {best_cost}")

# Visualize evolution of cost
plt.plot(best_cost_history)
plt.title("Evolution of Cost - Ant Colony")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.show()
