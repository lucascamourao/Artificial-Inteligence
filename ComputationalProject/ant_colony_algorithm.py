import numpy as np
import matplotlib.pyplot as plt

ALPHA = BETHA = 1  # definied empirically

"""
DEFINING THE PROBLEM ======================================================================

pij = amount of pheromone between i-city and j-city
cost matrix 'pheromone_matrix'
ex: pheromone_matrix[i][j]

cij = distance between i-city and j-city
cost matrix 'cost_matrix'
ex: cost_matrix[i][j]

The DESIRE of moving from city i to city j is (pij**ALPHA) * (cij**BETHA)

Let 

S = SUM[ (pim**ALPHA) * (cim**BETHA) ], for all m-city allowed

be the sum of desires of moving from city i to all *allowed* cities

Thus, the probability P of moving from city i to city j is 

P = DESIRE/ S
"""


def update_pheromone(cost_matrix):
    pass


# Colony of Ants Optimization Algorithm
def ant_colony_optimization(cost_matrix):
    pass  # Implementar
