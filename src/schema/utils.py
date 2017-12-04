# -*- coding: utf-8 -*-

from schema.canvas import canvas
import schema.components

def move(offset):
    canvas.move(offset)

def draw_symbol(label):
    # find the object to draw
    component = get_component(label)
    # look for connections that are already on
    terminals = component.get_terminals()

    # choose appropriate coordinates
    # draw the symbol
    # draw connections
    pass

get_component = schema.components.get_component
