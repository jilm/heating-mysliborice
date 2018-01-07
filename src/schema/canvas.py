# -*- coding: utf-8 -*-

"""Writes a Tikz output."""

import functools
import sys
from asyncio.queues import Queue

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

    def transform(self, transform):
        pass

    def write(self):
        pass


class Canvas(Writable):

    def __init__(self):
        self.writables = Queue()

    def move_to(self, x, y):
        sys.stdout.write('\draw ({},{})'.format(x, y))

    def line_to(self, x, y):
        sys.stdout.write(' -- ({},{})'.format(x, y))

    def close(self):
        sys.stdout.write('-- cycle;')


    def line(self, coordinates):
        """Draw line between all of the given coordinates.

        Coordinates must be given as a collection of x, y tuples."""
        form = ('({},{})'.format(x, y) for x, y in coordinates)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        print('\draw {};'.format(concat))

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

    def circle(self, center, radius):
        x, y = self.transform_point(center)
        r = radius * self.scale
        print('\draw ({},{}) circle ({});'.format(x, y, r))

canvas = Canvas()

# It allows to draw a line. Interanally it contains a list of tupels where
# the first character of the tuple determine the type of line and the meaning
# of the rest of the tuple.
class Path(Writable):

    def __init__(self):
        self.path = list()

    def transform(self, transform):
        pass

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


class Text(Writable):

    def transform(self, transform):
        pass

    def write(self):
        pass
