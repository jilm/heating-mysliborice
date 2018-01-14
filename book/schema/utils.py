# -*- coding: utf-8 -*-

from schema.canvas import canvas
import schema.components


def move(offset):
    canvas.move(offset)


def draw_symbol(label):
    # find the object to draw
    component = get_component(label)
    print('Component: {}, label: {}'.format(component.type, component.label))
    # look for connections that are already on
    term = component.get_terminals()
    term_full = list(('{}:{}'.format(label, t) for t in term))
    print(term_full)
    conn = list(
        c.a if c.b in term_full else c.b for c in schema.components.connections if c.a in term_full or c.b in term_full)
    print(conn)
    # choose appropriate coordinates
    # draw the symbol
    geom = component.draw_symbol()
    # store pins
    print(geom)
    for pin in geom['pins']:
        schema.components.terminals['{}:{}'.format(
            label, pin)] = geom['pins'][pin]
    # draw connections
    print(schema.components.terminals)
    pass


get_component = schema.components.get_component
