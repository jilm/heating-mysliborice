# -*- coding: utf-8 -*-

from schema.canvas import Square
from schema.canvas import Canvas
from schema.canvas import StandaloneCanvas
from schema.canvas import Line
from schema.vector import I
from schema.symbols import EQ_TRIANGLE
from schema.scheme import Scheme

class ElectroScheme(Scheme):

    def __init__(self, canvas, paper='A3L', description=None):
        super().__init__(canvas, paper, description)
        self.t = self.t.r_scale(2.84526)

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

    def get_handle(self):
        return self.t
