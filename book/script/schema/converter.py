# -*- coding: utf-8 -*-

GRID_SIZE = 4.0 # minimal distance between two parallel wires
WIDTH = GRID_SIZE * 4

def draw_converter_base(canvas, height = 4):
    canvas.draw_rect(WIDTH, height * GRID_SIZE, style='normal')
    canvas.draw_line(
        points = (
            (-0.5*WIDTH, -0.5*height*GRID_SIZE),
            (0.5*WIDTH, 0.5*height*GRID_SIZE)
        ),
        style='tiny'
    )


