## Pathfinding Algorithms Implementation

### Overview
This project implements various **pathfinding algorithms** for navigating through a grid-based environment. The program loads a **map**, processes the **start and end positions**, and applies different search algorithms to find the optimal path.

The implemented algorithms include:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Random Search**
- **Greedy Search**
- **A* (A-Star) Search**

### Features
- **Multiple search algorithms** to explore different pathfinding strategies.
- **Interactive menu** for selecting the preferred algorithm.
- **Map loading and visualization** with real-time updates.
- **Path reconstruction** to display the shortest path found.
- **Performance metrics** such as the number of expanded nodes.

### Requirements
- Python 3.x
- Required modules: `sys`, `os`, `re`, `time`, `random`, `collections`

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/pathfinding-algorithms.git
   cd pathfinding-algorithms

# Travelling Salesman Problem (TSP)

## Problem Definition

The **Travelling Salesman Problem (TSP)** is an optimization problem where a salesman must visit all cities **exactly once** and return to the starting point while minimizing travel costs.

### Assumptions:
- The problem is formulated in **Euclidean space**.
- The distance matrix **C** is **symmetric**, meaning:  
  **c(i,j) = c(j,i)**.
- The **triangle inequality** holds:  
  **c(i,k) ≤ c(i,j) + c(j,k)** for all **i, j, k** in the set of cities.

## Graph Representation

The problem can be represented as an **undirected graph** **G = (V, A)**, where:
- **V** is the set of cities.
- **A** is the set of edges with non-negative weights corresponding to distances.

The goal is to find the **shortest Hamiltonian cycle**, a path that visits each city **exactly once** and returns to the start.

---

## Solving TSP using the Hill-Climbing Algorithm

### Key Objectives:
- Design and implement a **suitable encoding method** for TSP.
- Define an **objective function** to evaluate the quality of solutions.
- Explore different **neighborhood variants** for state transitions.
- Implement a method for **enumerating neighboring states**.
- Introduce a mechanism to **escape local optima**, such as **random restarts**.

---

### Algorithm Configuration

The following parameters can be adjusted:

- **Input File**: Specifies the dataset containing city distances.
- **Starting City**: Defines the city where the route begins.
- **Neighbor Selection Variant**:
  - **Variant 1**: Swaps two random cities in the path.
  - **Variant 2**: Swaps only adjacent cities.
- **Maximum Iterations**: Controls the limit for optimization steps.
- **Maximum Restarts**: Defines the number of attempts to escape local optima.

---

### Implementation Details

#### Steps:
1. **Load Data** – Reads the distance matrix from a dataset.
2. **Initialize Solution** – Generates a random route covering all cities.
3. **Generate Neighboring Solutions**:
   - **Method 1**: Swaps two randomly selected cities.
   - **Method 2**: Swaps only adjacent cities.
4. **Evaluate Solutions** – Computes the total distance for each path.
5. **Select the Best Neighbor** – Chooses the shortest route among generated neighbors.
6. **Iterate Until Convergence** – Repeats the process until no better solution is found.
7. **Handle Local Optima** – Uses restart strategies if the algorithm gets stuck.

---

### Conclusion

This project demonstrates two distinct algorithmic approaches:

1. **Pathfinding Algorithms** – Used for navigating a **grid-based environment**.
2. **Hill-Climbing Optimization** – Applied to solve the **Travelling Salesman Problem (TSP)**.

Each algorithm showcases a unique method of searching and optimizing solutions for **complex computational problems**.
