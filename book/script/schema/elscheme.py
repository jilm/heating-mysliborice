# -*- coding: utf-8 -*-

from schema.canvas import Square
from schema.canvas import Canvas
from schema.canvas import StandaloneCanvas
from schema.canvas import Line
from schema.vector import I
from schema.symbols import EQ_TRIANGLE
from schema.scheme import Scheme
import schema.scheme

class ElectroScheme:

    """ The layer of the electric scheme. It is dedicated to help you to
    draw a scheme according to the habits of this field. It should work
    like this: you put some component, or a group of components and it
    helps you to place other components and draw wires between them.

    Each electrical scheme contains information of the components that
    have already been placed on. The position of the reference point,
    orientation and position of connectors are such information.
    The component is referenced by the label.

    So, the process could look like that:
    sch.draw_component('-B1')
    sch.move(1,0)
    sch.draw_component('-K2')
    sch.draw_wire('-B1:1', '-K2:5')
    """

    def __init__(self, canvas, offset, size):
        #self.t = self.t.r_scale(2.84526)
        #self.handlers = {}
        self.canvas = canvas
        self.row = schema.scheme.clip_top(self.canvas, 20.0)
        pass

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
        #self.canvas.text(text, self.t.transform_point((-0.1, 0.0)), position = 'w', size = 'small')
        return handle

    def draw_component(self, component, label):
        component.draw_electrical_symbol(self.row)
        #component = get_component(label)
        #_ = component.draw_el_symbol(self)
        #self.put(label, _)
        pass

    def step(self, x=0, y=0):
        self.row = self.row.move((x, y))


    def draw_h_mwire(self, left, right):
        pass

    def draw_h_wire(self, index_left, index_right):
