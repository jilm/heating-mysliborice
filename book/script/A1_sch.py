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
        'number' : 'HM-A1-DISP'
    }
)

a1 = get_component('=A1')
a1.draw_face_view(scheme)
canvas.close()
