import sys

from algorithms import *
from graph import *


def menu():
    print("Hello, choose which algorithm do you want.")
    print("0 for Breadth-first search")
    print("1 for Depth-first search")
    print("2 for Random search")
    print("3 for Greedy search")
    print("4 for A*")
    print("")


def choice(choice, map, start, end):
    if int(choice) == 0:
        bfs(map, start, end)
    elif int(choice) == 1:
        dfs(map, start, end)
    elif int(choice) == 2:
        random_search(map, start, end)
    elif int(choice) == 3:
        greedy_search(map, start, end)
    elif int(choice) == 4:
        A_star(map, start, end)
    else:
        print("Bad choice, please try it again.")
        menu()
        choice = input('your choice: ')
        print(choice)
        choice(choice, map, start, end)
    return


def main():
    file = str(sys.argv[1])
    print(file)
    map, start, end = load_map(file)
    menu()
    my_choice = input('your choice: ')
    choice(my_choice, map, start, end)

main()