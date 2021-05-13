import random
import numpy as np

from constants import *


class State:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.game_field = np.zeros([HEIGHT, WIDTH], dtype=int)
        self.snake = np.array([(0, 0), (1, 0)])
        self.game_field[0][1] = 1
        self.food = np.zeros(shape=(0, 2), dtype=int)
        self.add_food()
        self.snake_direction = 0, 1
        self.snake_alive = True
        self.direction_queue = []
        self.score = 0

    def add_food(self):
        """add food randomly"""
        random.seed(a=None, version=2)
        index_y = list(range(self.height))
        random.shuffle(index_y)
        for y in index_y:
            index_x = list(range(self.width))
            random.shuffle(index_x)
            for x in index_x:
                if self.game_field[y][x] == 0:
                    position = x, y
                    self.food = np.append(self.food, [position], axis=0)
                    self.game_field[y][x] = 2
                    return

    def move(self):
        """moving of the snake"""
        if not self.snake_alive:
            return

        # choose direction
        if self.direction_queue:
            new_direction = self.direction_queue[0]
            del self.direction_queue[0]
            old_x, old_y = self.snake_direction
            new_x, new_y = new_direction
            if (old_x, old_y) != (-new_x, -new_y):
                self.snake_direction = new_direction

        old_x, old_y = self.snake[len(self.snake) - 1]
        dir_x, dir_y = self.snake_direction
        new_x = old_x + dir_x
        new_y = old_y + dir_y

        # check if snake is in the wall
        if new_x < 0:
            self.snake_alive = False
            return
        if new_y < 0:
            self.snake_alive = False
            return
        if new_x >= self.width:
            self.snake_alive = False
            return
        if new_y >= self.height:
            self.snake_alive = False
            return

        # makes new head and check if is not in the snake
        new_head = new_x, new_y
        for x, y in self.snake:
            if new_head == (x, y):
                self.snake_alive = False
                return

        self.snake = np.append(self.snake, [new_head], axis=0)
        self.game_field[new_y][new_x] = 1

        # eats food
        for index in range(len(self.food)):
            if new_head[0] == self.food[index][0] and new_head[1] == self.food[index][1]:
                self.food = np.delete(self.food, index, 0)
                self.score += 1
                self.add_food()
                return

        # deletes tail
        self.snake = np.delete(self.snake, 0, 0)
        self.game_field[self.snake[0][1]][self.snake[0][0]] = 0
