# AI and Optimization Projects  

This repository contains three projects from a course BI-ZUM, focusing on **search algorithms, AI pathfinding, and optimization techniques**. Each project demonstrates a different approach to solving **complex computational problems** using **heuristic search, AI decision-making, and optimization strategies**.  

---

## 1️⃣ **[Pathfinding Algorithms Implementation](./uloha1/)**  
This project explores **pathfinding algorithms** for navigating a **grid-based environment**. It loads a **map**, processes the **start and end positions**, and applies **various search algorithms** to find the optimal path.  

## 2️⃣ **[Travelling Salesman Problem (TSP) using Hill-Climbing](./uloha2/)**  
This project solves the **Travelling Salesman Problem (TSP)** using the **Hill-Climbing algorithm**, an **iterative improvement method** for optimization problems. The goal is to find the shortest possible route that visits each city exactly once and returns to the starting point.  

## 3️⃣ **[Intelligent Snake Game AI](./semestralka/)**   
This project implements an **AI-controlled Snake agent** that intelligently **navigates a 2D grid**, collects food, and avoids collisions. The agent applies **heuristic search algorithms** to calculate the best moves, ensuring **long-term survival and strategic decision-making**.  
📄 **For detailed analysis and results, see this report: [dokumentace.pdf](./semestralka/dokumentace.pdf)**

---

## 🧭 Pathfinding Algorithms Implementation

### 📌 Overview
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

---

## 🚗 Travelling Salesman Problem (TSP)

### 📌 Overview

The **Travelling Salesman Problem (TSP)** is an optimization problem where a salesman must visit all cities **exactly once** and return to the starting point while minimizing travel costs.

#### Assumptions:
- The problem is formulated in **Euclidean space**.
- The distance matrix **C** is **symmetric**, meaning:  
  **c(i,j) = c(j,i)**.
- The **triangle inequality** holds:  
  **c(i,k) ≤ c(i,j) + c(j,k)** for all **i, j, k** in the set of cities.

### Graph Representation

The problem can be represented as an **undirected graph** **G = (V, A)**, where:
- **V** is the set of cities.
- **A** is the set of edges with non-negative weights corresponding to distances.

The goal is to find the **shortest Hamiltonian cycle**, a path that visits each city **exactly once** and returns to the start.

### Solving TSP using the Hill-Climbing Algorithm

### Key Objectives:
- Design and implement a **suitable encoding method** for TSP.
- Define an **objective function** to evaluate the quality of solutions.
- Explore different **neighborhood variants** for state transitions.
- Implement a method for **enumerating neighboring states**.
- Introduce a mechanism to **escape local optima**, such as **random restarts**.

### Algorithm Configuration

The following parameters can be adjusted:

- **Input File**: Specifies the dataset containing city distances.
- **Starting City**: Defines the city where the route begins.
- **Neighbor Selection Variant**:
  - **Variant 1**: Swaps two random cities in the path.
  - **Variant 2**: Swaps only adjacent cities.
- **Maximum Iterations**: Controls the limit for optimization steps.
- **Maximum Restarts**: Defines the number of attempts to escape local optima.

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

## 🐍 Intelligent Snake Game AI  

### 📌 Overview  
This project focuses on designing an **intelligent AI agent** for the classic **Snake game**. The goal is to create an **adaptive agent** that can navigate the game grid, collect food, and **avoid self-collisions** while maximizing survival time.  

The implemented agent follows **goal-based AI principles**, leveraging **heuristic search algorithms** for optimal pathfinding.  

### Problem Definition  
- The **Snake** moves on a **2D grid**, following a path where its **body trails behind the head**.  
- The objective is to **collect food (apples)**, growing in length with each consumption.  
- The challenge is to **avoid colliding with itself** or the game boundaries.  
- The environment is **partially observable** since the Snake only has limited information about the grid.  

### AI Agent Approach  
Instead of relying on a **basic reflex agent** (which makes **random moves** to avoid obstacles), the implemented agent:  
1. **Calculates an optimal path** to the apple using a selected search algorithm.  
2. **Follows the planned path** step by step, **minimizing the risk of getting trapped**.  
3. **Handles dead-end situations** by generating an **imaginary apple**—a temporary target that allows the Snake to maneuver until a real path to the actual apple becomes available.  

### Algorithms Used  
The AI agent is implemented using **heuristic search techniques**, including:  
- **A* Algorithm** (Optimal pathfinding with a heuristic)  
- **Dijkstra's Algorithm** (Uniform cost search)  
- **Greedy Search** (Fast but not always optimal)  

At the start of the game, the user selects which **algorithm** will control the Snake.  

### Implementation Details  
- **Language:** Python 🐍  
- **Visualization:** Implemented using **Pyglet**, a Python graphics library.  
- **Heuristic Used:** **Manhattan Distance** for evaluating path costs.  

### Pathfinding Strategy  
1. When an **apple appears**, the Snake calculates the best path using the chosen **search algorithm**.  
2. If no valid path exists (due to the Snake’s own body blocking it), the agent **creates an imaginary apple** at a reachable position to buy time.  
3. The Snake moves towards the **imaginary apple** until a real path to the actual apple is available.  
4. If the Snake becomes trapped with no escape, it **fails** and the game ends.  

---
