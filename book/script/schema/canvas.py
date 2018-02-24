# -*- coding: utf-8 -*-

""" Writes a Tikz output. """

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
    'large': '\large',
    'huge' : '\huge'
}


class Writable:

    def write(self):
        pass

class Transformable:

    def transform(self, transf):
        self.transf = self.transf.transform(transf)

class Canvas(Writable):

    """ Writes TIKZ output on std out. """

    def __init__(self):
        self.writables = Queue()
        self.unit=''
        self.opened = False
        self.closed = False
        self.line_width = 0.4

    def __str__(self):
        return 'This is a Canvas instance, opened: {}, closed: {}'.format(self.opened, self.closed)

    def set_line_width(self, width):
        self.line_width = width

    def open(self):
        """ It is called before the first character is written on the output. """
        self.opened = True

    def close(self):
        """ Should be called after the picture is finished. """
        if not self.opened:
            self.open()
        self.closed = True

    def write(self, text):
        """ Some kind of low level method. It is not inteded for direct use,
        it is called internaly. """
        if not self.opened:
            self.open()
        sys.stdout.write(text)

    def move_to(self, x, y):
        self.write('\draw {}'.format(self.form_point(x, y)))

    def line_to(self, x, y):
        self.write(' -- {}'.format(self.form_point(x, y)))

    def arc_to(self, angle1, angle2, radius):
        self.write(' arc ({}:{}:{}{})'.format(angle1, angle2, radius, self.unit))

    def close_path(self):
        self.write('-- cycle;')

    def line(self, points):
        """
        Draw strait line between all of the given points.
        Points must be given in the form of collection of x, y tuples.
        """
        form = ('({0}{2},{1}{2})'.format(x, y, self.unit) for x, y in points)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        self.write('\draw[{1}] {0};'.format(concat, self.form_draw_params()))

    def closed_line(self, points):
        """
        Draw strait line between all of the given points, moreover, it connects
        the first and the last point by a line. Points must be given in the
        form of collection of x, y tuples.
        """
        form = ('({0}{2},{1}{2})'.format(x, y, self.unit) for x, y in points)
        concat = functools.reduce(lambda a, b: '{} -- {}'.format(a, b), form)
        self.write('\draw[{1}] {0} -- cycle;'.format(concat, self.form_draw_params()))

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
        self.write('\draw {0} node[{1}] {{{2} {3}}};'.format(
            self.form_point(x, y), anchor, size_value, text))


    def rect(self, x, y, width, height):
        self.line(((x, y), (x + width, y), (x + width,
                                            y + height), (x, y + height), (x, y)))

    def circle(self, x, y, radius):
        self.write('\draw {} circle ({}{});'.format(self.form_point(x, y),
        radius, self.unit))

    def form_point(self, x, y):
        """ For internal use, it returns tikz string representation of the
        given coordinates. """
        return '({0}{2},{1}{2})'.format(x, y, self.unit)

    def form_points(self, points):
        form = (self.form_point(x, y) for x, y in points)
        return ' -- '.join(form)

    def form_draw_params(self):
        """ For internal use, it returns tikz string representation of the
        draw parameters. """
        return 'line width={}{}'.format(self.line_width, self.unit)


#canvas = Canvas()

class StandaloneCanvas(Canvas):

    def __init__(self):
        Canvas.__init__(self)

    def __str__(self):
        return '{}\n  Instance of a StandaloneCanvas'.format(Canvas.__str__(self))

    def open(self):
        Canvas.open(self)
        self.write('\\documentclass{article}')
        self.write('\\usepackage{tikz}')
        self.write('\\usepackage[paperwidth={}mm, paperheight={}mm, left=0.3cm, right=0.3cm, top=0.3cm, bottom=0.3cm, hoffset=0cm]{{geometry}}'.format(self.paper_size[0], self.paper_size[1]))
        self.write('\\begin{document}')
        self.write('\\noindent\\begin{tikzpicture}')

    def setPaperSize(self, size):
        self.paper_size = size

    def close(self):
        self.write('\\end{tikzpicture}')
        self.write('\\end{document}')
        Canvas.close(self)

# It allows to draw a line. Interanally it contains a list of tupels where
# the first character of the tuple determine the type of line and the meaning
# of the rest of the tuple.
class Path:

    def __init__(self, path=list()):
        self.path = path

    def transform(self, transform):
        for i, seg in enumerate(self.path):
            if seg[0] in ('M', 'L'):
                x, y = transform.transform_point((seg[1], seg[2]))
                self.path[i] = (seg[0], x, y)
            elif seg[0] == 'A':
                self.path[i] = (seg[0], seg[1], seg[2], transform.transform_vector((seg[3], seg[3]))[0])

    def write(self, canvas):
        for seg in self.path:
            if seg[0] == 'M':
                canvas.move_to(seg[1], seg[2])
            elif seg[0] == 'L':
                canvas.line_to(seg[1], seg[2])
            elif seg[0] == 'Z':
                canvas.close_path()
            elif seg[0] == 'A':
                canvas.arc_to(seg[1], seg[2], seg[3])
        canvas.close_path()

    def line_to(self, point):
        x, y = point
        self.path.append(('L', x, y))

    def move_to(self, point):
        x, y = point
        self.path.append(('M', x, y))

    def arc_to(self, angle1, angle2, radius):
        self.path.append(('A', angle1, angle2, radius))

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
