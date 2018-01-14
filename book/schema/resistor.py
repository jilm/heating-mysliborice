# -*- coding: utf-8 -*-

from schema.canvas import canvas
import vector

GS = 6.0 # minimal distance between two parallel wires
RATIO = 4.0 / 12.0    # width / height ratio
HEIGHT = 2.0 * GS
WIDTH = RATIO * HEIGHT
RECT = vector.Rect([(-0.5 * WIDTH, -0.5 * HEIGHT), (0.5 * WIDTH, 0.5 * HEIGHT)])
PIN1 = ((0.0, 0.5 * HEIGHT), (0.0, 1.0))
PIN2 = ((0.0, -0.5 * HEIGHT), (0.0, 1.0))
CROSS_LINE_SIZE = 0.7 * WIDTH
CROSS_LINE = ((-CROSS_LINE_SIZE, -CROSS_LINE_SIZE), (CROSS_LINE_SIZE, CROSS_LINE_SIZE))


def draw_thermistor_block():
    # draw rectangle
    canvas.line(RECT.get_points())
    # draw pins
    # draw variable symbol
    canvas.line(CROSS_LINE)
    # draw theta letter
    canvas.text('$\sigma$', (2.5, -5.0))
    # draw envelope rectangle 
    canvas.line(vector.Rect())
    
 
