import random
import constants

from constants import *
from alg import a_star, greedy_search, dijkstra, neighbours

UP, DOWN, RIGHT, LEFT = (0, 1, 2, 3)


class Snake:
    def __init__(self):
        self.body = [(0, 0), (0, 1)]
        self.length = len(self.body)
        self.is_alive = True

    def get_head(self):
        return self.body[self.length - 1]

    def get_tail(self):
        return self.body[0]

    def move(self, position, ate_apple):
        self.body.append(position)
        if not ate_apple:
            self.body.pop(0)
        else:
            self.length += 1


class State:
    def __init__(self, width, height):
        self.snake = Snake()
        self.width = width
        self.height = height
        self.food = []
        self.add_food()
        self.path = []
        self.score = 0

    def add_food(self):
        tries = self.width * self.height
        for i in range(tries):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y
            if (position not in self.snake.body) and (position not in self.food):
                self.food.append(position)
                return

    def add_imaginary_food(self):
        """used if is not any possible way to real apple"""
        for i in range(MAX_TRIES_FIND_SPACE):
            x = random.randrange(self.width)
            y = random.randrange(self.height)
            position = x, y
            if (position not in self.snake.body) and (position not in self.food):
                return position
        x = random.randrange(self.width)
        y = random.randrange(self.height)
        return x, y

    def check_snake_in_wall(self):
        head = self.snake.get_head()
        if head[0] >= self.width:
            return True
        elif head[1] >= self.height:
            return True
        elif head[0] < 0:
            return True
        elif head[1] < 0:
            return True
        else:
            return False

    def check_snake_in_body(self):
        head = self.snake.get_head()
        for segment_index in range(self.snake.length - 1):
            if self.snake.body[segment_index] == head:
                return True
        return False

    def kill_snake(self):
        head_neigh = neighbours(self.snake.body, self.snake.get_head(), self.width, self.height)
        if len(head_neigh) == 0:
            self.snake.is_alive = False
            return
        self.snake.move(head_neigh[0], False)

    def algorithm(self, food):
        if ALGORITHM is A_STAR:
            self.path = a_star(self.snake.body, self.snake.get_head(), food, self.width, self.height)
        elif ALGORITHM is DIJKSTRA:
            self.path = dijkstra(self.snake.body, self.snake.get_head(), food, self.width, self.height)
        elif ALGORITHM is GREEDY_SEARCH:
            self.path = greedy_search(self.snake.body, self.snake.get_head(), food, self.width, self.height)

    def eat_apple(self):
        self.snake.move(self.path[0], True)
        self.path.pop(0)
        self.food.pop(0)
        self.score += 1
        self.add_food()

    def eat_imaginary_food(self):
        counter = 0
        while len(self.path) == 0:
            if counter > MAX_TRIES_FIND_PATH:
                self.kill_snake()
                print("kill max")
                return
            imaginary_food = self.add_imaginary_food()
            self.algorithm(imaginary_food)

    def move(self):
        """moving of the snake"""

        if not self.snake.is_alive:
            return
            
        if self.path == "kill":
            self.algorithm(self.food[0])
            if len(self.path) == 0 or self.path == "kill":
                print("kill 0")
                self.path = "kill"
                self.kill_snake()
                return
        else:
            self.algorithm(self.food[0])

        if len(self.path) == 0 or self.path == "kill":
            self.eat_imaginary_food()
            if self.path == "kill":
                return

        if not self.snake.is_alive:
            return

        if self.path[0] == self.food[0]:
            self.eat_apple()
            self.algorithm(self.food[0])
            if self.path == "kill":
                return
        else:
            self.snake.move(self.path[0], False)
            self.path.pop(0)

        if self.check_snake_in_wall():
            self.snake.is_alive = False
            return

        # make new head and check if its position is allowed
        if self.check_snake_in_body():
            self.snake.is_alive = False
            return


