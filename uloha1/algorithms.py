from collections import deque
from graph import *
import random


def heuristics(x, end):
    return ((x[0] - end[1])**2 + (x[1] - end[0])**2)**0.5


def A_star(map, start, end):
    opened = []
    dist = {}
    prev = {}
    priority = {}
    closed = set()
    expanded = 0
    opened.append((start[1], start[0]))
    expanded += 1
    priority[(start[1], start[0])] = heuristics((start[1], start[0]), end)
    dist[(start[1], start[0])] = 0
    while len(opened):
        min_node = opened[0]
        for node in opened:
            if priority[node] < priority[min_node]:
                min_node = node
        x = min_node
        write_symbol_in_map('$', x[0], x[1], map)
        render(map)
        if x[0] is end[1] and x[1] is end[0]:
            return render_path(reconstructed_path(prev, x), map, expanded)
        for y in neighbours(map, x):
            if y not in closed:
                d = dist[x] + 1
                write_symbol_in_map('#', y[0], y[1], map)
                if y not in opened or d < dist[y]:
                    dist[y] = d
                    prev[y] = x
                    if y not in opened:
                        opened.append(y)
                        expanded += 1
                        priority[y] = d + heuristics(y, end)
                    else:
                        priority[y] = d + heuristics(y, end)
        render(map)
        opened.remove(x)
        del priority[x]
        closed.add(x)
        write_symbol_in_map('C', x[0], x[1], map)
        render(map)
    return


def greedy_search(map, start, end):
    open = []
    prev = {}
    closed = set()
    expanded = 0
    open.append((start[1], start[0]))
    expanded += 1
    while len(open):
        heu = (heuristics(open[0], end), open[0])
        for node in open:
            if heuristics(node, end) < heu[0]:
                heu = (heuristics(node, end), node)
        x = heu[1]
        write_symbol_in_map('$', x[0], x[1], map)
        render(map)
        if x[0] is end[1] and x[1] is end[0]:
            return render_path(reconstructed_path(prev, x), map, expanded)
        for y in neighbours(map, x):
            if y not in open and y not in closed:
                write_symbol_in_map('#', y[0], y[1], map)
                open.append(y)
                expanded += 1
                prev[y] = x
        open.remove(x)
        closed.add(x)
        render(map)
        write_symbol_in_map('C', x[0], x[1], map)
        render(map)
    return


def bfs(map, start, end):
    opened = deque([])
    closed = set()
    prev = {}
    expanded = 0
    opened.append((start[1], start[0]))
    expanded += 1
    while len(opened):
        x = opened.popleft()
        write_symbol_in_map('$', x[0], x[1], map)
        render(map)
        if x[0] is end[1] and x[1] is end[0]:
            return render_path(reconstructed_path(prev, x), map, expanded)
        for y in neighbours(map, x):
            if y not in opened and y not in closed:
                write_symbol_in_map('#', y[0], y[1], map)
                opened.append(y)
                expanded += 1
                prev[y] = x
        render(map)
        closed.add(x)
        write_symbol_in_map('C', x[0], x[1], map)
        render(map)
    return


def dfs(map, start, end):
    open = [(start[1], start[0])]
    closed = set()
    prev = {}
    expanded = 1
    while len(open):
        x = open.pop()
        write_symbol_in_map('$', x[0], x[1], map)
        render(map)
        if x[0] is end[1] and x[1] is end[0]:
            return render_path(reconstructed_path(prev, x), map, expanded)
        for y in neighbours(map, x):
            if y not in open and y not in closed:
                write_symbol_in_map('#', y[0], y[1], map)
                open.append(y)
                expanded += 1
                prev[y] = x
        closed.add(x)
        render(map)
        write_symbol_in_map('C', x[0], x[1], map)
        render(map)
    return


def random_search(map, start, end):
    open = {(start[1], start[0])}
    closed = set()
    prev = {}
    expanded = 1
    while len(open):
        x = random.sample(open, 1)[0]
        write_symbol_in_map('$', x[0], x[1], map)
        render(map)
        if x[0] is end[1] and x[1] is end[0]:
            return render_path(reconstructed_path(prev, x), map, expanded)
        for y in neighbours(map, x):
            if y not in open and y not in closed:
                write_symbol_in_map('#', y[0], y[1], map)
                open.add(y)
                expanded += 1
                prev[y] = x
        open.remove(x)
        closed.add(x)
        render(map)
        write_symbol_in_map('C', x[0], x[1], map)
        render(map)
    return







