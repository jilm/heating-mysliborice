# -*- coding: utf-8 -*-

"""Writes a Tikz output."""

import functools

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


class Canvas:

    def __init__(self):
        pass

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
