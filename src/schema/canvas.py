# -*- coding: utf-8 -*-

import functools

text_positions = {
    'nw' : 'south east',
    'n' : 'south',
    'ne' : 'south west',
    'w' : 'east',
    'e' : 'west',
    'sw' : 'north east',
    's' : 'north',
    'se' : 'north west'
}

class Canvas:

    def __init__(self):
        self.scale = 1.0
        self.x_offset = 0.0
        self.y_offset = 0.0
        self.frame = None

    def line(self, coordinates):
        # transform given coordinates
        transform = list(((x*self.scale+self.x_offset, y*self.scale+self.y_offset) for x, y in coordinates))
        self.w_line(transform)

    def w_line(self, coordinates):
        # format into string
        form = ('({},{})'.format(x, y) for x, y in coordinates)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        print('\draw {};'.format(concat))

    def text(self, text, point, position=None):
        x = point[0]*self.scale+self.x_offset
        y = point[1]*self.scale+self.y_offset
        if position:
            anchor = 'anchor={}'.format(text_positions[position])
        else:
            anchor = ''
        print('\draw ({},{}) node[{}] {{{}}};'.format(x,y,anchor,text))

    def large_text(self, text, point, position=None):
        x, y = self.transform_point(point)
        if position:
            anchor = 'anchor={}'.format(text_positions[position])
        else:
            anchor = ''
        print('\draw ({},{}) node[{}] {{\large {}}};'.format(x,y,anchor,text))

    def small_text(self, text, point, position=None):
        x, y = self.transform_point(point)
        if position:
            anchor = 'anchor={}'.format(text_positions[position])
        else:
            anchor = ''
        print('\draw ({},{}) node[{}] {{\small {}}};'.format(x,y,anchor,text))

    def rect(self, x, y, width, height):
        self.line(((x, y), (x+width, y), (x+width, y+height), (x, y+height), (x, y)))

    def circle(self, center, radius):
        x, y = self.transform_point(center)
        r = radius * self.scale
        print('\draw ({},{}) circle ({});'.format(x, y, r))

    def set_scale(self, scale):
        self.scale = scale

    def scale(self, scale):
        self.scale *= scale

    def move(self, offset):
        self.x_offset += offset[0] * self.scale
        self.y_offset += offset[1] * self.scale

    def transform(self, coordinates):
        return list(((x*self.scale+self.x_offset, y*self.scale+self.y_offset) for x, y in coordinates))

    def transform_point(self, point):
        return point[0]*self.scale+self.x_offset, point[1]*self.scale+self.y_offset

    def union(self, coordinates):
        self.frame = ((
            min((x for x, y in coordinates)),
            min((y for x, y in coordinates)), (
            max((x for x, y in coordinates)),
            max((y for x, y in coordinates))
        )))
        print(self.frame)

    def put(self, key, coordinates):
        """ Puts given coordinates into internal dictionary under the given
        key. """
        pass



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

