# -*- coding: utf-8 -*-

from schema.elscheme import ElectricalScheme
from schema.canvas import Canvas

""" Control system electrical scheme. """

# Create a canvas object according to required output format
canvas = Canvas()

# Create a sheet of paper
_ = StandaloneScheme(canvas)

# write a frame on the paper sheet
_ = FramedScheme(_)

# Create electrical schema object
schema = ElectricalScheme(_)

# Put all of the object on it


