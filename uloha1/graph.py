import re
import time
import os


def extract_numbers_from_string(word):
    """
    Extract numbers from string word.
    Makes a list of axis x and y.
    """
    return [int(s) for s in re.findall(r"[\w']+", word) if s.isdigit()]


def write_symbol_in_map(symbol, row, column, map):
    """
    Writes a symbol in the specific place in the map.
    row = axe x
    column = axe y
    """
    map[row] = map[row][:column] + symbol + map[row][(column + 1):]
    return map


def load_map(file):
    """
    Loading file by lines. If the first char on the line is 's',
    string start is the line,
    If the first char on the line is 'e',
    string end is the line.
    Than axes from these strings will be separated with
    function extract_numbers_from_string.
    Otherwise the line is appended into map.
    """
    map = []
    start_row = ""
    end_row = ""
    with open(file, "r", encoding="utf-8") as f:
        for row in f.readlines():
            if row[0] == 's':
                start_row = row
            elif row[0] == 'e':
                end_row = row
            else:
                map.append(row)

    # read number of row and column, where 'S' should be put in the map
    start = extract_numbers_from_string(start_row)
    map = write_symbol_in_map('S', start[1], start[0], map)

    # read number of row and column, where 'E' should be put in the map
    end = extract_numbers_from_string(end_row)
    map = write_symbol_in_map('E', end[1], end[0], map)

    return map, start, end

def render(map):
    time.sleep(0.05)
    os.system('clear')

    print('\033[92m' + 'E end' + '\033[0m'
       + "\t" + '\033[94m' + '# Opened node' + '\033[0m'
       + "\t" + '\033[91m' + 'o Path' + '\033[0m'
       + "\t" + "X Wall"
       + "\t" + '\033[91m' + '$ current position' + '\033[0m'
       + "\t" + '\033[93m' + 'C closed nodes' + '\033[0m'
       + "\t" + "space Fresh node")
    print("---------------------------------------")

    for row in map:
        for c in row:
            if c == '#':
                print('\033[94m' + '#' + '\033[0m', end="")
            elif c == 'C':
                print('\033[93m' + 'C' + '\033[0m', end="")
            elif c == '$':
                print('\033[91m' + '$' + '\033[0m', end="")
            elif c == 'E':
                print('\033[92m' + 'E' + '\033[0m', end="")
            elif c == '+':
                print('\033[91m' + '+' + '\033[0m', end="")
            else:
                print(c, end="")
    return


def reconstructed_path(prev, x):
    path = []
    while x in prev:
        path.append(x)
        x = prev[x]
    path.append(x)
    return path


def render_path(path, mapa, expanded):
    counter = -1
    for node in path:
        write_symbol_in_map('+', node[0], node[1], mapa)
        counter += 1
    render(mapa)
    print("length of the path: " + str(counter))
    print("number of expanded nodes: " + str(expanded))
    return


def neighbours(map, x):
    list = []
    for row_number in range(len(map)):
        if row_number == (x[0] - 1):
            if map[row_number][x[1]] != 'X':
                list.append((row_number, x[1]))
        if row_number == x[0]:
            if x[1] > 0 and map[row_number][x[1] - 1] != 'X':
                list.append((row_number, x[1]-1))
            if x[1] < (len(map[row_number]) - 1) and map[row_number][x[1] + 1] != 'X':
                list.append((row_number, x[1]+1))
        if row_number == (x[0] + 1):
            if map[row_number][x[1]] != 'X':
                list.append((row_number, x[1]))
    return list