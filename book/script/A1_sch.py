# -*- coding: utf-8 -*-

from schema.canvas import Square
from schema.canvas import Canvas
from schema.canvas import StandaloneCanvas
from schema.canvas import Line
from schema.vector import I
from schema.scheme import Scheme
from schema.scheme import ScaledScheme

MODULE_WIDTH = 17.5 # mm
VERTICAL_CONTENT_DISTANCE = 150.0 # mm

class CabinetPosition:

    def __init__(self, n_modules):
        self.n_modules = n_modules
        self.content = list()

    def draw_face_view(self, scheme):
        width = self.n_modules * MODULE_WIDTH
        scheme.draw_hline(-0.5 * width, 0.0, width, line='TINY')
        scheme.push()
        scheme.move(-0.5 * width, 0.0)
        for c in self.content:
            scheme.move(0.5 * c.dimensions[0], 0.0)
            c.draw_face_view(scheme)
            scheme.move(0.5 * c.dimensions[0], 0.0)
        scheme.pop()

    def put(self, module):
        self.content.append(module)


class Cabinet:

    dimensions = (360.0, 540.0)
    n_positions = 3
    n_modules = (16, 16, 16)

    def __init__(self):
        self.content = list([CabinetPosition(n) for n in self.n_modules])

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)
        scheme.push()
        scheme.move(0.0, (self.n_positions-1) * VERTICAL_CONTENT_DISTANCE * 0.5)
        for p in self.content:
            p.draw_face_view(scheme)
            scheme.move(0.0, -VERTICAL_CONTENT_DISTANCE)
        scheme.pop()



class Quido88:

    dimensions = (137.4, 96.5, 20)

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)
        #scheme.draw_circl/e(3.2, (64.45, 40.0))
        #scheme.draw_circle(3.2, (-64.45, 40.0))
        #scheme.draw_circle(3.2, (64.45, -40.0))
        #scheme.draw_circle(3.2, (-64.45, -40.0))
        
class P5310:

    dimensions = (17.0, 62.0)

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)
        
class Finder4031:        

    dimensions = (15.8, 78.6, 82.0,)

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)
        scheme.draw_rect((12.4, 29.0))        
        
class GNOME485:        

    dimensions = (42.0, 57.0, 25.0,)

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)



canvas = StandaloneCanvas()
scheme = ScaledScheme(canvas, scale=0.5, paper='A3P')
a1 = Cabinet()

a1.content[0].put(Quido88())
a1.content[0].put(Quido88())
for i in range(9):
    a1.content[1].put(Finder4031())
a1.content[1].put(GNOME485())    
    
a1.draw_face_view(scheme)
canvas.close()
