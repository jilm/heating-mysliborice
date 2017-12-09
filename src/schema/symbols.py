# -*- coding: utf-8 -*-

from schema.canvas import canvas

STEP = 6.0

def draw_resistor_base():
    canvas.rect(0.0, -6.0, 4.0, 12.0)
    canvas.line(((2.0, 6.0), (2.0, 9.0)))
    canvas.line(((2.0, -6.0), (2.0, -9.0)))

def draw_coil_base_lr():
    canvas.rect(0.0, -4.0, 12.0, 8.0)
    return {
        'dim' : ((0.0, -4.0), (12.0, 8.0)),
        'axes' : ((6.0, 0.0)),
        'pins' : {
            'a1' : ((6.0, -4.0), (0.0, -1.0)),
            'a2' : ((6.0, 4.0), (0.0, 1.0))
        }
    }


def draw_thermistor():
    canvas.line(((0.0, -5.0), (5.0, -5.0), (15.0, 5.0)))
    canvas.text('$\\vartheta$', (2.5, -5.0), 'n')
    canvas.move((8.0, 0.0))
    draw_resistor_base()
    canvas.move((-8.0, 0.0))
    #canvas.move((10.0, 0.0))

def draw_thermistor1():
    """ Zleva, doprava """
    canvas.line(((0.0, -5.0), (5.0, -5.0), (15.0, 5.0)))
    canvas.text('$\sigma$', (2.5, -5.0))
    canvas.move((8.0, 0.0))
    draw_resistor_base()
    canvas.move((-8.0, 0.0))
    canvas.line(((10.0, 9.0), (19.0, 9.0), (19.0, 5.0)))
    canvas.line(((10.0, -9.0), (19.0, -9.0), (19.0, -5.0)))

def draw_converter_base():
    canvas.rect(0.0, -9.0, 18.0, 18.0)
    canvas.line(((0.0, -9.0), (18.0, 9.0)))

def draw_converter_text(a, b):
    canvas.large_text(a, (6.0, 1.0))
    canvas.large_text(b, (12.0, -7.0))

def draw_RI_converter():
    draw_converter_base()
    draw_converter_text('R', 'I')

def draw_AD_converter():
    draw_converter_base()
    draw_converter_text('A', 'D')

def draw_triangle_base():
    """ Just triangle, it is a base for amplifier or comparator """
    canvas.line(((0.8, -6.0), (11.2, 0.0), (0.8, 6.0), (0.8, -6.0)))

def draw_hysteresys_symbol():
    canvas.line(((-2.0, -1.5), (1.0, -1.5), (1.0, 1.5)))
    canvas.line(((-1.0, -1.5), (-1.0, 1.5), (2.0, 1.5)))


def draw_coil_base_ud():
    canvas.rect(0.0, -6.0, 8.0, 12.0)

def get_coil_geometry():
    return {
        'dim' : ((0.0, -6.0), (8.0, 6.0)),
        'axes' : (4.0, 0.0),
        'pins' : {
            'a1' : ((0.0, 0.0), (-1.0, 0.0)),
            'a2' : ((8.0, 0.0), (1.0, 0.0))
        }
    }

def draw_switch():
    canvas.line(((0.0, 0.0), (2*STEP-2.0, STEP-1.0)))
    canvas.line(((2*STEP-3.0, STEP-3.0), (2*STEP-3.0, STEP), (2*STEP, STEP)))
    canvas.line(((2*STEP-3.0, 3.0-STEP), (2*STEP-3.0, -1.0*STEP), (2*STEP, -1.0*STEP)))

def get_switch_geometry():
    return {
        'dim' : ((0.0, -1.0*STEP), (2*STEP, STEP)),
        'x_axes' : (STEP),
        'y_axes' : (0.0),
        'pins' : {
            'comm' : ((0.0, 0.0), (-1.0, 0.0)),
            'nc' : ((2*STEP, STEP), (1.0, 0.0)),
            'no' : ((2*STEP, -1.0*STEP), (1.0, 0.0))
        }
    }

def draw_rele1():
    draw_coil_base_ud()
    canvas.move((0.0, -3.0 * STEP))
    draw_switch()

def get_rele1_geometry():
    coil_geom = get_coil_geometry()
    switch_geom = get_switch_geometry()
    return {
        'dim' : merge_rects(coil_geom['dim'], switch_geom['dim']),
        'pins' : dict({k: v for d in (coil_geom['pins'], switch_geom['pins']) for k, v in d.items()})
    }

def merge_rects(rect1, rect2):
    return (
        (min(rect1[0][0], rect2[0][0]), min(rect1[0][1], rect2[0][1])),
        (max(rect1[0][0], rect2[0][0]), max(rect1[0][1], rect2[0][1]))
    )
