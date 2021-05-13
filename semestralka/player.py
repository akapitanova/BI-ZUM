import pyglet

from pathlib import Path
from snake import State
from constants import *

state = State()
window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
state.width = window.width // TILE_SIZE
state.height = window.height // TILE_SIZE

snake_tiles = {}
TILES_DIR = Path('snake-tiles')

for path in TILES_DIR.glob('*.png'):
    snake_tiles[path.stem] = pyglet.image.load(path)
apple_image = pyglet.image.load('img/apple.png')


def make_snake(snake):
    """makes snake from images"""
    new_snake = []
    for index in range(len(snake)):
        if index == 0:
            fr = "tail"
        else:
            if snake[index][0] > snake[index-1][0]:
                fr = "left"
            elif snake[index][0] < snake[index-1][0]:
                fr = "right"
            elif (snake[index][0] == snake[index-1][0]) and (snake[index][1] < snake[index-1][1]):
                fr = "top"
            elif (snake[index][0] == snake[index-1][0]) and (snake[index][1] > snake[index-1][1]):
                fr = "bottom"
        if index == len(snake)-1:
            to = "head"
        else:
            if snake[index][0] > snake[index+1][0]:
                to = "left"
            elif snake[index][0] < snake[index+1][0]:
                to = "right"
            elif (snake[index][0] == snake[index+1][0]) and (snake[index][1] < snake[index+1][1]):
                to = "top"
            elif (snake[index][0] == snake[index+1][0]) and (snake[index][1] > snake[index+1][1]):
                to = "bottom"
        new_snake.append((snake[index][0], snake[index][1], fr, to))
    return new_snake

@window.event
def on_draw():
    window.clear()
    pyglet.gl.glEnable(pyglet.gl.GL_BLEND)
    pyglet.gl.glBlendFunc(pyglet.gl.GL_SRC_ALPHA, pyglet.gl.GL_ONE_MINUS_SRC_ALPHA)
    new_snake = make_snake(state.snake)
    for x, y, fr, to in new_snake:
        if fr == 'head' and not state.snake_alive:
            fr = 'dead'
        if to == 'head' and not state.snake_alive:
            to = 'dead'
        snake_tiles[fr + '-' + to].blit(x * TILE_SIZE, y * TILE_SIZE,
                     width=TILE_SIZE, height=TILE_SIZE)
    for x, y in state.food:
        apple_image.blit(x * TILE_SIZE, y * TILE_SIZE, width = TILE_SIZE, height = TILE_SIZE)
    label = pyglet.text.Label(str(state.score),
                              font_size=SCORE_FONT_SIZE,
                              x=window.width // 2, y=window.height,
                              anchor_x='center', anchor_y='top')
    label.draw()


def move(dt):
    state.move()


@window.event
def on_key_press(symbol, mod):
    if symbol == pyglet.window.key.LEFT:
        new_direction = -1, 0
        state.direction_queue.append(new_direction)
        return
    if symbol == pyglet.window.key.RIGHT:
        new_direction = 1, 0
        state.direction_queue.append(new_direction)
        return
    if symbol == pyglet.window.key.DOWN:
        new_direction = 0, -1
        state.direction_queue.append(new_direction)
        return
    if symbol == pyglet.window.key.UP:
        new_direction = 0, 1
        state.direction_queue.append(new_direction)
        return
    else:
        return


pyglet.clock.schedule_interval(move, TIME_TO_MOVE)
pyglet.app.run()
