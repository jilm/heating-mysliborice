# -*- coding: utf-8 -*-

from schema.canvas import Square
from schema.canvas import Canvas
from schema.canvas import StandaloneCanvas
from schema.canvas import Line
from schema.vector import I
from schema.symbols import EQ_TRIANGLE
from schema.scheme import Scheme

class ElectroScheme(Scheme):

    """ The layer of the electric scheme. It is dedicated to help you to
    draw a scheme according to the habits in this field. It should work
    like this. You put some component, or a group of components and it
    helps you to place an draw a wires between those components. """

    def __init__(self, canvas, paper='A3L', description=None):
        super().__init__(canvas, paper, description)
        self.t = self.t.r_scale(2.84526)
        self.handlers = {}

    def write_ref(self, handle, text = ''):
        Line([ (-0.1, 0.0), (0.0, 0.0) ], handle).write(self.canvas)
        Line([
            (-0.1, 0.20),
            (-0.1, -0.20),
            (-1.0, -0.20),
            (-0.4*0.866-1.0, 0.0),
            (-1.0, 0.20),
            (-0.1, 0.20)
        ], handle).write(self.canvas)
        self.canvas.text(text, self.t.transform_point((-0.1, 0.0)), position = 'w', size = 'small')
        return handle

    def put(self, component):
        """ Draw given component on the scheme. """
        h = component.draw_electrical_scheme(self)
        self.handlers[component.get_label()] = h

    def draw_rectangle(self, size, offset=(0.0, 0.0), style='normal'):
        super().draw_rect(size, style)

    def draw_line(self, points, style):
        pass

    def draw_text(self, text, offset, orientation, style):
        pass
