# -*- coding: utf-8 -*-

import canvas

STEP = 6.0

def draw_resistor_base():
    canvas.canvas.rect(0.0, -6.0, 4.0, 12.0)
    canvas.canvas.line(((2.0, 6.0), (2.0, 9.0)))
    canvas.canvas.line(((2.0, -6.0), (2.0, -9.0)))

def draw_thermistor():
    canvas.canvas.line(((0.0, -5.0), (5.0, -5.0), (15.0, 5.0)))
    canvas.canvas.text('$\\vartheta$', (2.5, -5.0), 'n')
    canvas.canvas.move((8.0, 0.0))
    draw_resistor_base()
    canvas.canvas.move((-8.0, 0.0))
    #canvas.move((10.0, 0.0))

def draw_thermistor1():
    """ Zleva, doprava """
    canvas.canvas.line(((0.0, -5.0), (5.0, -5.0), (15.0, 5.0)))
    canvas.canvas.text('$\sigma$', (2.5, -5.0))
    canvas.canvas.move((8.0, 0.0))
    draw_resistor_base()
    canvas.canvas.move((-8.0, 0.0))
    canvas.canvas.line(((10.0, 9.0), (19.0, 9.0), (19.0, 5.0)))
    canvas.canvas.line(((10.0, -9.0), (19.0, -9.0), (19.0, -5.0)))

def draw_converter_base():
    canvas.canvas.rect(0.0, -9.0, 18.0, 18.0)
    canvas.canvas.line(((0.0, -9.0), (18.0, 9.0)))

def draw_converter_text(a, b):
    canvas.canvas.large_text(a, (6.0, 1.0))
    canvas.canvas.large_text(b, (12.0, -7.0))

def draw_RI_converter():
    draw_converter_base()
    draw_converter_text('R', 'I')

def draw_AD_converter():
    draw_converter_base()
    draw_converter_text('A', 'D')

def draw_triangle_base():
    """ Just triangle, it is a base for amplifier or comparator """
    canvas.canvas.line(((0.8, -6.0), (11.2, 0.0), (0.8, 6.0), (0.8, -6.0)))

def draw_hysteresys_symbol():
    canvas.canvas.line(((-2.0, -1.5), (1.0, -1.5), (1.0, 1.5)))
    canvas.canvas.line(((-1.0, -1.5), (-1.0, 1.5), (2.0, 1.5)))

