from constants import *


def reconstructed_path(prev, x):
    """reverse path and deletes start node"""
    path = []
    while x in prev:
        path.append(x)
        x = prev[x]
    path.append(x)
    path = path[::-1]
    path.pop(0)
    return path


def neighbours(snake, x, width, height):
    """returns list of x' neighboring nodes"""
    x_neighbours = []
    columns = width
    rows = height
    # upper neighbour
    if x[1] + 1 < rows:
        if (x[0], x[1] + 1) not in snake:
            x_neighbours.append((x[0], x[1] + 1))
    # bottom
    if x[1] - 1 >= 0:
        if (x[0], x[1] - 1) not in snake:
            x_neighbours.append((x[0], x[1] - 1))
    # right
    if x[0] + 1 < columns:
        if (x[0] + 1, x[1]) not in snake:
            x_neighbours.append((x[0] + 1, x[1]))
    # left
    if x[0] - 1 >= 0:
        if (x[0] - 1, x[1]) not in snake:
            x_neighbours.append((x[0] - 1, x[1]))

    return x_neighbours


def heuristics(x, end, width, height):
    """counts heuristics from current node to apple"""
    heu_x = abs(x[0] - end[0])
    heu_y = abs(x[1] - end[1])
    if x[0] == 0 or x[1] == 0:
        return heu_x + heu_y + SIDE_PENALTY
    if x[0] == width - 1 or x[1] == height - 1:
        return heu_x + heu_y + SIDE_PENALTY
    if x[0] == 1 or x[1] == 1:
        return heu_x + heu_y + NEXT_SIDE_PENALTY
    if x[0] == width - 2 or x[1] == height - 2:
        return heu_x + heu_y + NEXT_SIDE_PENALTY
    return heu_x + heu_y


def a_star(snake, start, end, width, height):
    """returns path from snake head to apple"""
    open_nodes = []
    dist = {}
    prev = {}
    priority = {}
    closed = set()
    open_nodes.append(start)
    priority[start] = heuristics(start, end, width, height)
    dist[start] = 0
    while len(open_nodes):
        min_node = open_nodes[0]
        for node in open_nodes:
            if priority[node] < priority[min_node]:
                min_node = node
        x = min_node
        if x[0] == end[0] and x[1] == end[1]:
            return reconstructed_path(prev, x)
        neigh = neighbours(snake, x, width, height)

        if len(neigh) == 0:
            return "kill"

        for y in neigh:
            if y not in closed:
                d = dist[x] + 1
                if y not in open_nodes or d < dist[y]:
                    dist[y] = d
                    prev[y] = x
                    if y not in open_nodes:
                        open_nodes.append(y)
                        priority[y] = d + heuristics(y, end, width, height)
                    else:
                        priority[y] = d + heuristics(y, end, width, height)
        open_nodes.remove(x)
        del priority[x]
        closed.add(x)
    return []


def greedy_search(snake, start, end, width, height):
    open_nodes = []
    prev = {}
    closed = set()
    open_nodes.append(start)
    while len(open_nodes):
        heu = (heuristics(open_nodes[0], end, width, height), open_nodes[0])
        for node in open_nodes:
            node_heuristics = heuristics(node, end, width, height)
            if node_heuristics < heu[0]:
                heu = (node_heuristics, node)
        x = heu[1]
        if x[0] is end[0] and x[1] is end[1]:
            return reconstructed_path(prev, x)

        neigh = neighbours(snake, x, width, height)

        if len(neigh) == 0:
            return "kill"

        for y in neigh:
            if y not in open_nodes and y not in closed:
                open_nodes.append(y)
                prev[y] = x
        open_nodes.remove(x)
        closed.add(x)
    return []


def dijkstra(snake, start, end, width, height):
    open_nodes = []
    prev = {}
    dist = {}
    open_nodes.append(start)
    dist[start] = 0
    while len(open_nodes):
        min_node = open_nodes[0]
        for node in open_nodes:
            if dist[node] < dist[min_node]:
                min_node = node
        x = min_node
        if x[0] is end[0] and x[1] is end[1]:
            return reconstructed_path(prev, x)

        neigh = neighbours(snake, x, width, height)

        if len(neigh) == 0:
            return "kill"

        for y in neigh:
            d = dist[x] + 1
            if y not in dist or d < dist[y]:
                if y not in dist:
                    open_nodes.append(y)
                dist[y] = d
                prev[y] = x
        open_nodes.remove(x)
    return []

