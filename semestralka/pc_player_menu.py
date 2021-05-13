import pyglet

import constants
from constants import *

window = pyglet.window.Window(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)

label_press = pyglet.text.Label('Press A ',
                                font_size=FONT_SIZE,
                                bold=True,
                                color=PRESS_LABEL_COLOR,
                                x=LABEL_PRESS_X, y=LABEL_Y,
                                anchor_x='left', anchor_y='center')

label = pyglet.text.Label('for A*',
                          font_size=FONT_SIZE,
                          bold=True,
                          color=LABEL_COLOR,
                          x=LABEL_X, y=LABEL_Y,
                          anchor_x='left', anchor_y='center')

label1_press = pyglet.text.Label('Press B ',
                                 font_size=FONT_SIZE,
                                 bold=True,
                                 color=PRESS_LABEL_COLOR,
                                 x=LABEL_PRESS_X, y=LABEL1_Y,
                                 anchor_x='left', anchor_y='center')

label1 = pyglet.text.Label('for Dijkstra',
                           font_size=FONT_SIZE,
                           bold=True,
                           color=LABEL_COLOR,
                           x=LABEL_X, y=LABEL1_Y,
                           anchor_x='left', anchor_y='center')

label2_press = pyglet.text.Label('Press C ',
                                 font_size=FONT_SIZE,
                                 bold=True,
                                 color=PRESS_LABEL_COLOR,
                                 x=LABEL_PRESS_X, y=LABEL2_Y,
                                 anchor_x='left', anchor_y='center')

label2 = pyglet.text.Label('for Greedy search',
                           font_size=FONT_SIZE,
                           bold=True,
                           color=LABEL_COLOR,
                           x=LABEL_X, y=LABEL2_Y,
                           anchor_x='left', anchor_y='center')


@window.event
def on_key_press(symbol, mod):
    if symbol == pyglet.window.key.A:
        window.close()
        constants.ALGORITHM = A_STAR
        import pc_player
        pc_player
    if symbol == pyglet.window.key.B:
        window.close()
        constants.ALGORITHM = DIJKSTRA
        import pc_player
        pc_player
    if symbol == pyglet.window.key.C:
        window.close()
        constants.ALGORITHM = GREEDY_SEARCH
        import pc_player
        pc_player
    else:
        return


@window.event
def on_draw():
    window.clear()
    label_press.draw()
    label.draw()
    label1_press.draw()
    label1.draw()
    label2_press.draw()
    label2.draw()


pyglet.app.run()
