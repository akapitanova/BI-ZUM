import pyglet
import constants

from constants import *

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
label = pyglet.text.Label('Press A to play',
                          font_size=FONT_SIZE,
                          bold=True,
                          color=LABEL_COLOR,
                          x=MAIN_LABEL_X, y=MAIN_LABEL_Y,
                          anchor_x='center', anchor_y='center')
label1 = pyglet.text.Label('Press B for PC player',
                           font_size=FONT_SIZE,
                           bold=True,
                           color=LABEL_COLOR,
                           x=MAIN_LABEL_X, y=MAIN_LABEL1_Y,
                           anchor_x='center', anchor_y='center')
snake_image = pyglet.image.load('img/animals.png')


@window.event
def on_key_press(symbol, mod):
    if symbol == pyglet.window.key.A:
        window.close()
        import player
        player
    if symbol == pyglet.window.key.B:
        window.close()
        import pc_player_menu
        pc_player_menu
    else:
        return


@window.event
def on_draw():
    window.clear()
    label.draw()
    label1.draw()
    snake_image.blit(SNAKE_IMAGE_X, SNAKE_IMAGE_Y, width=SNAKE_IMAGE_WIDTH, height=SNAKE_IMAGE_HEIGHT)


pyglet.app.run()
