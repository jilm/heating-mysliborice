# -*- coding: utf-8 -*-

import functools

class Canvas:
    def __init__(self):
        self.scale = 1.0
        self.x_offset = 0.0
        self.y_offset = 0.0
        self.frame = None
    def line(self, coordinates):
        # transform given coordinates
        transform = list(((x*self.scale+self.x_offset, y*self.scale+self.y_offset) for x, y in coordinates))
        # format into string
        form = ('({},{})'.format(x, y) for x, y in transform)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        print('\draw {};'.format(concat))
    def text(self, text, point):
        x = point[0]*self.scale+self.x_offset
        y = point[1]*self.scale+self.y_offset
        print('\draw ({},{}) node[anchor=south] {{{}}};'.format(x,y,text))
    def rect(self, x, y, width, height):
        self.line(((x, y), (x+width, y), (x+width, y+height), (x, y+height), (x, y)))
    def set_scale(self, scale):
        self.scale = scale
    def scale(self, scale):
        self.scale *= scale
    def move(self, offset):
        self.x_offset += offset[0] * self.scale
        self.y_offset += offset[1] * self.scale
    def union(self, coordinates):
        self.frame = ((
            min((x for x, y in coordinates)),
            min((y for x, y in coordinates)), (
            max((x for x, y in coordinates)),
            max((y for x, y in coordinates))
        )))
        print(self.frame)

canvas = Canvas()
canvas.set_scale(0.075)

def draw_resistor_base():
    canvas.rect(0.0, -6.0, 4.0, 12.0)
    canvas.line(((2.0, 6.0), (2.0, 9.0)))
    canvas.line(((2.0, -6.0), (2.0, -9.0)))

def draw_thermistor():
    canvas.line(((0.0, -5.0), (5.0, -5.0), (15.0, 5.0)))
    canvas.text('$\sigma$', (2.5, -5.0))
    canvas.move((8.0, 0.0))
    draw_resistor_base()
    canvas.move((-8.0, 0.0))
    #canvas.move((10.0, 0.0))

def draw_converter_base():
    canvas.rect(0.0, -6.0, 12.0, 12.0)
    canvas.line(((0.0, -6.0), (12.0, 6.0)))

def draw_converter_text(a, b):
    canvas.text(a, (4.0, 0.0))
    canvas.text(b, (8.0, -6.0))

def draw_RI_converter():
    draw_converter_base()
    draw_converter_text('R', 'I')

def draw_AD_converter():
    draw_converter_base()
    draw_converter_text('A', 'D')

def draw_triangle_base():
    """ Just triangle, it is a base for amplifier or comparator """
    canvas.line(((0.8, -6.0), (11.2, 0.0), (0.8, 6.0), (0.8, -6.0)))

def draw_hysteresys_symbol():
    canvas.line(((-2.0, -1.5), (1.0, -1.5), (1.0, 1.5)))
    canvas.line(((-1.0, -1.5), (-1.0, 1.5), (2.0, 1.5)))


draw_thermistor()
draw_RI_converter()
canvas.move((20.0, 0.0))
draw_AD_converter()
