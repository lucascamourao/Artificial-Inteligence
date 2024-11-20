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
"""

import queue
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node1, node2, weight):
        if node1 not in self.graph:  # Check if the node is already added
            self.graph[node1] = {}  # If not, create the node
        self.graph[node1][node2] = weight  # Else, add a connection to its neighbor


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

    if graph == {}:
        print("Error! Empty file?")

    return graph


# Greedy Best First Search Algorithm
def GBFS(startNode, heuristics, graph, goalNode="Bucharest"):
    return


# Astar Algorithm
def Astar(startNode, heuristics, graph, goalNode="Bucharest"):
    return


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
