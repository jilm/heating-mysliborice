# -*- coding: utf-8 -*-

from schema.canvas import Square
from schema.canvas import Canvas
from schema.canvas import StandaloneCanvas
from schema.canvas import Line
from schema.vector import I
from schema.scheme import ScaledScheme

"""    Namaluje dispozicni usporadani rozvadece A1.    """

MODULE_WIDTH = 17.5 # mm
VERTICAL_CONTENT_DISTANCE = 150.0 # mm

# Vykreslí vlastní výkres

canvas = StandaloneCanvas()
scheme = ScaledScheme(canvas, scale=0.5, paper='A3P')

a1.draw_face_view(scheme)
canvas.close()
