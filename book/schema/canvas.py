# -*- coding: utf-8 -*-

"""Writes a Tikz output."""

import functools
import sys
from asyncio.queues import Queue
from schema.vector import Transform
from schema.vector import I

text_positions = {
    'nw': 'south east',
    'n': 'south',
    'ne': 'south west',
    'w': 'east',
    'e': 'west',
    'sw': 'north east',
    's': 'north',
    'se': 'north west'
}

TEXT_SIZE = {
    'normal': '',
    'small': '\small',
    'large': '\large'
}


class Writable:

    def write(self):
        pass

class Transformable:

    def transform(self, transf):
        self.transf = self.transf.transform(transf)

class Canvas(Writable):

    def __init__(self):
        self.writables = Queue()

    def move_to(self, x, y):
        sys.stdout.write('\draw ({},{})'.format(x, y))

    def line_to(self, x, y):
        sys.stdout.write(' -- ({},{})'.format(x, y))

    def close(self):
        sys.stdout.write('-- cycle;')


    def line(self, points):
        """
        Draw strait line between all of the given points.
        Points must be given in the form of collection of x, y tuples.
        """
        form = ('({},{})'.format(x, y) for x, y in points)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        print('\draw {};'.format(concat))

    def closed_line(self, points):
        """
        Draw strait line between all of the given points, moreover, it connects
        the first and the last point by a line. Points must be given in the
        form of collection of x, y tuples.
        """
        form = ('({},{})'.format(x, y) for x, y in points)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        print('\draw {} -- cycle;'.format(concat))

    def text(self, text, point, position=None, size=None):
        """Draw given text at given position."""
        x, y = point
        if position is not None:
            anchor = 'anchor={}'.format(text_positions[position])
        else:
            anchor = ''
        if size is not None and size in TEXT_SIZE:
            size_value = TEXT_SIZE[size]
        else:
            size_value = ''
        print('\draw ({},{}) node[{}] {{{} {}}};'.format(
            x, y, anchor, size_value, text))


    def rect(self, x, y, width, height):
        self.line(((x, y), (x + width, y), (x + width,
                                            y + height), (x, y + height), (x, y)))

    def circle(self, x, y, radius):
        print('\draw ({},{}) circle ({});'.format(x, y, radius))

canvas = Canvas()

# It allows to draw a line. Interanally it contains a list of tupels where
# the first character of the tuple determine the type of line and the meaning
# of the rest of the tuple.
class Path:

    def __init__(self):
        self.path = list()

    def transform(self, transform):
        for i, seg in enumerate(self.path):
            if seg[0] in ('M', 'L'):
                x, y = transform.transform_point((seg[1], seg[2]))
                self.path[i] = (seg[0], x, y)

    def write(self, canvas):
        for seg in self.path:
            if seg[0] == 'M':
                canvas.move_to(seg[1], seg[2])
            elif seg[0] == 'L':
                canvas.line_to(seg[1], seg[2])
            elif seg[0] == 'Z':
                canvas.close()

    def line_to(self, point):
        x, y = point
        self.path.append(('L', x, y))

    def move_to(self, point):
        x, y = point
        self.path.append(('M', x, y))

    def close(self):
        self.path.append(('Z'))

class Line(Transformable):

    def __init__(self, points, transf = I):
        self.points = points
        self.transf = transf

    def write(self, canvas):
        canvas.line(
            self.transf.transform_points(self.points)
        )

class Circle(Transformable):

    def __init__(self, transf = I):
        self.transf = transf

    def write(self, canvas):
        cx, cy = self.transf.transform_point((0.0, 0.0))
        r, temp = self.transf.transform_vector((0.5, 0.0))
        canvas.circle(cx, cy, r)

class Text(Transformable):

    def write(self):
        pass

class Square(Transformable):

    POINTS = [
            (-0.5, -0.5),
            (0.5, -0.5),
            (0.5, 0.5),
            (-0.5, 0.5)
        ]

    def __init__(self, transf = I):
        self.transf = transf

    def write(self, canvas):
        canvas.closed_line(
            self.transf.transform_points(Square.POINTS)
        )
