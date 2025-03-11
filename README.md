# Pathfinding Algorithms Implementation

## Overview
This project implements various **pathfinding algorithms** for navigating through a grid-based environment. The program loads a **map**, processes the **start and end positions**, and applies different search algorithms to find the optimal path.

The implemented algorithms include:
- **Breadth-First Search (BFS)**
- **Depth-First Search (DFS)**
- **Random Search**
- **Greedy Search**
- **A* (A-Star) Search**

## Features
- **Multiple search algorithms** to explore different pathfinding strategies.
- **Interactive menu** for selecting the preferred algorithm.
- **Map loading and visualization** with real-time updates.
- **Path reconstruction** to display the shortest path found.
- **Performance metrics** such as the number of expanded nodes.

## Requirements
- Python 3.x
- Required modules: `sys`, `os`, `re`, `time`, `random`, `collections`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/pathfinding-algorithms.git
   cd pathfinding-algorithms


# Druhá domácí úloha: Nesystematické prohledávání stavového prostoru

## Symetrická úloha obchodního cestujícího (Symmetric Travelling Salesman Problem, TSP)

Je dána množina měst **W** a matice **C** vzdáleností mezi dvojicemi měst z **W**. Úkolem obchodního cestujícího je projít těmito městy a následně se vrátit do výchozího města s minimálními výdaji na cestu, přičemž každé město navštíví právě jednou.

Předpoklady:
- Úloha je formulována v **Euklidovském prostoru**.
- Matice **C** vzdáleností mezi městy je **symetrická**, tj. platí **c(i,j) = c(j,i)** (tj. cestující může mezi městy cestovat oběma směry).
- Platí **trojúhelníková nerovnost**:  
  **c(i,k) ≤ c(i,j) + c(j,k)** pro všechna **i, j, k** z **W**.

Z pohledu **teorie grafů** lze úlohu formulovat následovně:  
Nechť **G = (V, A)** je **neorientovaný graf**, kde:
- **V** je množina vrcholů (města).
- **A** je množina hran s nezápornými ohodnoceními odpovídajícími prvkům matice **C**.

Úkolem je nalézt **nejkratší Hamiltonovskou kružnici**, která projde všemi vrcholy právě jednou.

---

## Zadání úlohy: TSP pomocí algoritmu Hill-Climbing

Navrhněte a implementujte řešení problému **obchodního cestujícího** pomocí **hill-climbing algoritmu**.

### Dílčí úkoly:
- Navrhnout a implementovat **vhodné kódování** problému **TSP** resp. **N-královen** pro řešení pomocí **hill-climbing**.
- Navrhnout **účelovou funkci**.
- Definovat **různé varianty okolí** daného stavu.
- Implementovat metodu na **enumeraci stavů** v definovaném okolí.
- Implementovat nějakou metodu na **únik z lokálního extrému** (například **restarty**).

---

## Moje řešení

### **Nastavení**
Níže lze nastavit parametry algoritmu **Hill-Climbing**:

```python
fileName = 'distances-10.csv'  # Název souboru s daty
start = 'Praha'  # Startovní město

# Varianta výběru sousedů (1 nebo 2):
# 1 - Prohazuje dvě libovolná města v cestě
# 2 - Prohazuje pouze sousední města
neighboursVariant = 2

maxIter = 1000  # Maximální počet iterací
maxRestarts = 1000  # Maximální počet restartů (pro únik z lokálního extrému)
