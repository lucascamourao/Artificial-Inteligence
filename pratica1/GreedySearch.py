"""
Greedy search: There are informations such as the straight-line distance to the city. So, basically, the algorithm's starting point sees the ramifications
(childs), like a tree, of this point. The closest to the destination is the chosen. It repetes until it finds the end (distance zero). 
OBS: Not necessarily this search finds the best (less cost, for example) path.

A* search: Utilizes the function f(n) = g(n) + h(n)
Let g(n), from Uniform Cost Seach, be the function that chooses the next node to expand based on the total path length from the start to the current node.
Let h(n), from Greedy Seach, be the function that makes its choice based on the heuristic estimate of the path length from the current node to the goal.
OBS: A* search always finds the best path because, even after finding a good path to the goal, it just stops when there are no change to find a better one. 

Links: 
https://www.youtube.com/watch?v=HMAHrQHmrUQ
https://www.youtube.com/watch?v=iTJvWfmp1vw
https://github.com/hassanzadehmahdi/Romanian-problem-using-Astar-and-GBFS/blob/main/README.md
"""

import queue

# import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        # they both are not in the graph
        if (node1 not in self.graph) and (node2 not in self.graph):
            self.graph[node1] = [[node2, weight]]
            self.graph[node2] = [[node1, weight]]

        elif node1 not in self.graph:
            self.graph[node1] = [[node2, weight]]

            connections = self.graph.get(node2)
            connections.append([node1, weight])
            self.graph.update({node2: connections})

        elif node2 not in self.graph:
            self.graph[node2] = [[node1, weight]]

            connections = self.graph.get(node1)
            connections.append([node2, weight])
            self.graph.update({node1: connections})

        else:
            connections = self.graph.get(node1)
            connections.append([node2, weight])
            self.graph.update({node1: connections})

            connections = self.graph.get(node2)
            connections.append([node1, weight])
            self.graph.update({node2: connections})


# Getting heuristics
def getHeuristics():
    # mapping the name of the city with the value (straight-line distance to the goal)
    heuristics = {}

    with open("heuristics.txt") as h:
        for line in h:
            cityName, value = line.strip().split(" ")
            heuristics[cityName] = int(value)
            # {... "cityname": value, ...}

    if heuristics == []:
        print("Error! Empty file?")

    return heuristics


# Getting cities location
def getCity():
    # dictionary with the name of the city (string) as key and [coordinates] as value
    city = {}
    # dictionary with id (int) of the city as key and the name of the city as value (string), starting from 1 to n cities
    cityID = {}
    id = 1
    # cities.txt gives the location (x, y) of the city
    with open("cities.txt") as c:
        for line in c:
            cityName, x, y = line.strip().split(" ")
            coordinates = [int(x), int(y)]
            city[cityName] = coordinates

            cityID[id] = cityName
            id += 1

    return city, cityID


# Creating the map (graph) of the city
def createGraph():
    graph = Graph()
    with open("citiesGraph.txt") as cg:
        for line in cg:
            city1, city2, cost = line.strip().split(" ")
            graph.add_edge(city1, city2, int(cost))
    return graph


# Greedy Best First Search Algorithm
def GBFS(startNode, heuristics, graph, goalNode="Bucharest"):
    priorityQueue = queue.PriorityQueue()
    priorityQueue.put((heuristics[startNode], startNode))

    path = []
    visited = set()

    while not priorityQueue.empty():
        current = priorityQueue.get()[1]
        if current in visited:
            continue

        path.append(current)
        visited.add(current)

        if current == goalNode:
            break

        for neighbor, _ in graph.graph.get(current, []):
            if neighbor not in visited:
                priorityQueue.put((heuristics[neighbor], neighbor))

    return path


# A* Search Algorithm
def Astar(startNode, heuristics, graph, goalNode="Bucharest"):
    priorityQueue = queue.PriorityQueue()
    priorityQueue.put(
        (heuristics[startNode], (startNode, 0))
    )  # (f(n), (current, g(n)))

    came_from = {}  # Para rastrear o caminho
    g_costs = {startNode: 0}  # Custos mínimos conhecidos
    visited = set()

    while not priorityQueue.empty():
        _, (current, g_cost) = priorityQueue.get()

        if current in visited:
            continue
        visited.add(current)

        if current == goalNode:
            break

        for neighbor, cost in graph.graph.get(current, []):
            new_g_cost = g_cost + cost
            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                f_cost = new_g_cost + heuristics[neighbor]
                priorityQueue.put((f_cost, (neighbor, new_g_cost)))
                came_from[neighbor] = current

    # Reconstruindo o caminho
    path = []
    current = goalNode
    while current in came_from or current == startNode:
        path.insert(0, current)
        current = came_from.get(current)

    return path


def main():
    heuristic = getHeuristics()
    graph = createGraph()
    city, cityID = getCity()

    for i, j in cityID.items():
        print(i, j)

    while True:
        goal = int(input("Enter your goal (0 for exit): \n"))

        if goal == 0:
            break

        cityName = cityID[goal]

        gbfs = GBFS(cityName, heuristic, graph)
        astar = Astar(cityName, heuristic, graph)
        print("GBFS => ", gbfs)
        print("ASTAR => ", astar)


main()
