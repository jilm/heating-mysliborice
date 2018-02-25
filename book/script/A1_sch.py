# -*- coding: utf-8 -*-

import mysliborice
from schema.components import get_component
from schema.canvas import Square
from schema.canvas import Canvas
from schema.canvas import StandaloneCanvas
from schema.canvas import Line
from schema.vector import I
from schema.scheme import ScaledScheme

"""    Namaluje dispozicni usporadani rozvadece A1.    """


# Vykreslí vlastní výkres

canvas = StandaloneCanvas()
scheme = ScaledScheme(canvas, scale=0.5, paper='A3P',
    description = {
        'name' : 'Disp. uspořádání rozváděče =A1',
        'number' : 'HM-A1-DISP',
        'date' : '25.\,2.\,2018',
        'author' : 'jilm',
        'scale' : '2:1',
        'page' : '2'
    }
)

a1 = get_component('=A1')
a1.draw_face_view(scheme)
scheme.move(-75.0, -125.0)
scheme.draw_rect((150.0, 230.0), style='warning')
canvas.close()
