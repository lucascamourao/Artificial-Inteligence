# **Traveling Salesman Problem (TSP) Solver**  
### Implemented with Genetic Algorithm and Ant Colony Optimization  

This project provides an implementation of the **Traveling Salesman Problem (TSP)** using two powerful optimization algorithms:  
1. **Genetic Algorithm (GA)**  
2. **Ant Colony Optimization (ACO)**  

Both algorithms aim to solve the TSP efficiently, finding the shortest possible route that visits all cities exactly once and returns to the starting city.

---

## **1. Problem Overview**  

The **Traveling Salesman Problem** is one of the most famous combinatorial optimization problems.  
The objective is to:  
- Visit each city exactly **once**.  
- Return to the starting city.  
- Minimize the total travel cost (distance).  

Given `N` cities and a distance matrix, solving the TSP is NP-hard, so heuristic and metaheuristic algorithms such as GA and ACO are effective approaches.

---

## **2. Algorithms**  

### **Genetic Algorithm (GA)**  

Genetic Algorithm is an evolutionary optimization technique inspired by natural selection. It operates on a population of solutions, improving them over generations.  

**Steps of GA in this project:**  
1. **Initialization**: Randomly generate a population of routes.  
2. **Fitness Calculation**: Evaluate the total distance of each route.  
3. **Selection**: Choose the fittest routes for reproduction.  
4. **Crossover**: Combine routes (parents) to produce new offspring.  
5. **Mutation**: Randomly swap cities to maintain diversity.  
6. **Termination**: Stop after a defined number of generations or when no significant improvement occurs.  

---

### **Ant Colony Optimization (ACO)**  

ACO is a nature-inspired metaheuristic algorithm that simulates the foraging behavior of ants. Ants use pheromones to communicate, reinforcing paths with higher chances of being optimal.

**Steps of ACO in this project:**  
1. **Initialization**: Define pheromone levels and distances between cities.  
2. **Probability Calculation**: Use pheromones and distances to compute probabilities of moving to the next city.  
3. **Path Construction**: Simulate ants building complete paths by choosing cities probabilistically.  
4. **Pheromone Update**: Reinforce pheromones on better paths and evaporate others over time.  
5. **Best Solution**: Track the shortest path found.  

---

## **3. Project Information**  

- This is an Artificial Inteligence project from Federal University of Ceará.
- Implemented in Python and presented in December 18th, 2024.
- Made by Lucas Cabral Amador Mourão, Computer Science student. 

