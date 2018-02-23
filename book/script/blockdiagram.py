# -*- coding: utf-8 -*-

# Nakresli blokovy diagram vyhrivani podkrovi z krbovych kamen.

from schema.canvas import Path
from schema.canvas import Canvas
from schema.canvas import Circle
from schema.canvas import Line
from schema.canvas import Square
from schema.vector import Transform
from schema.vector import I

GS = 12.0 # zakladni velikost nejakeho domneleho gridu

# equilateral_triangle
EQ_TRIANGLE_H = 0.866 # height of the triangle
EQ_TRIANGLE_R = 0.289 # The radius of the inscribed circle
EQ_TRIANGLE = Transform().move((EQ_TRIANGLE_R - EQ_TRIANGLE_H, 0)).transform_points([
    (0.0, 0.0),
    (EQ_TRIANGLE_H, 0.5),
    (EQ_TRIANGLE_H, -0.5),
    (0.0, 0.0)
])

# Schematicka znacka smesovaciho ventilu
MIX_VALVE = Transform().scale(0.5).transform_points([
    (0.0, 0.0),
    (EQ_TRIANGLE_H, 0.5),
    (EQ_TRIANGLE_H, -0.5),
    (-EQ_TRIANGLE_H, 0.5),
    (-EQ_TRIANGLE_H, -0.5),
    (0.0, 0.0),
    (0.5, -EQ_TRIANGLE_H),
    (-0.5, -EQ_TRIANGLE_H),
    (0.0, 0.0)
])

# Schematicka znacka cerpadla
circle = Circle()
triangle = Line(Transform().scale(0.70).transform_points(EQ_TRIANGLE))

# Krbova kamna
def write_heater(canvas, transf = I):
    if canvas is not None:
        t = I.scale(2.0, 3.0).transform(transf)
        symbol = Square(t)
        symbol.write(canvas)
    return transf.r_move(-1.0, 0.0), transf.r_move(1.0, 0.0)

def write_pump(canvas, transf = I):
    if canvas is not None:
        symbol = Circle(transf)
        symbol.write(canvas)
        t = I.scale(-0.6, 0.6).transform(transf)
        symbol = Line(EQ_TRIANGLE, t)
        symbol.write(canvas)
    return transf.r_move(-0.5, 0.0), transf.r_move(0.5, 0.0)

def write_mix_valve(canvas, transf = I):
    if canvas is not None:
        symbol = Line(MIX_VALVE, transf)
        symbol.write(canvas)
    return transf.r_move(-0.5, 0.0), transf.r_move(0.5, 0.0), transf.rotate_vect().r_move(0.5, 0.0)

def write_corner(canvas, transf = I):
    if canvas is not None:
        symbol = Line(((-0.5, 0.0), (0.0, 0.0), (0.0, -0.5)), transf)
        symbol.write(canvas)
    return transf.r_move(-0.5, 0.0), transf.rotate_vect().r_move(0.5, 0.0)

def write_radiator(canvas, transf = I):
    if canvas is not None:
        symbol = Square(I.scale(2.0, 3.0).transform(transf))
        symbol.write(canvas)
    return transf.r_move(-1.0, 0.0), transf.r_move(1.0, 0.0)

def write_tee2(canvas, t1, t2):
    p1x, p1y = t1.transform_point((0.0, 0.0))
    v1x, v1y = t1.transform_vector((-1.0, 0.0))
    p2x, p2y = t2.transform_point((0.0, 0.0))
    v2x, v2y = t2.transform_vector((-1.0, 0.0))
    ox = p1x * v2x + p2x * v1x
    oy = p1y * v2y + p2y * v1y
    t = t1.move_to((ox, oy))
    symbol = Line(((-0.5, 0.0), (0.5, 0.0), (0.0, 0.0), (0.0, -0.5)), t)
    symbol.write(canvas)
    return t.move(t.transform_vector((1.5, 0.0)))

def write_tee(canvas, t = I):
    if canvas is not None:
        symbol = Line(((-0.5, 0.0), (0.5, 0.0), (0.0, 0.0), (0.0, -0.5)), t)
        symbol.write(canvas)
    return t.r_move(-0.5, 0.0), t.r_move(0.5, 0.0), t.rotate_vect().r_move(0.5, 0.0)

def write_wire(canvas, t = I, scale = 1.0):
    if canvas is not None:
        Line([(0.0, 0.0), (1.0 * scale, 0.0)], t).write(canvas)
    return t, t.r_move(1.0 * scale, 0.0)

def get_t(write_fn, t1, i = 0):
    t2 = write_fn(None, t1)[i]
    x1, y1 = t1.get_offset()
    x2, y2 = t2.get_offset()
    dx, dy = x1 - x2, y1 - y2
    return t1.move((dx, dy))


# Nakresli
canvas = Canvas()
transform = I
t1, t2, t3 = write_mix_valve(canvas, I)
canvas.text('=KKB-MV', t2.r_move(0.0, 1.0).get_offset(), 'n')
_, t2 = write_wire(canvas, t2)
_, t2 = write_pump(canvas, get_t(write_pump, t2))
canvas.text('=KKB-P', t2.r_move(0.0, 1.0).get_offset(), 'n')
_, t2 = write_corner(canvas, get_t(write_corner, t2))
_, t2 = write_wire(canvas, t2, 0.25)
_, t2 = write_radiator(canvas, get_t(write_radiator, t2))
canvas.text('=OT', t2.get_offset(), 'se')
_, t2 = write_wire(canvas, t2, 0.25)
_, t2 = write_corner(canvas, get_t(write_corner, t2))
_, t2 = write_wire(canvas, t2, -t3.get_offset()[1] + t2.get_offset()[0] - 1.0)
_, t2, t3 = write_tee(canvas, get_t(write_tee, t2))
write_wire(canvas, t3, 2.5)
_, t2 = write_wire(canvas, t2, 1.0)
_, t2, t3 = write_mix_valve(canvas, get_t(write_mix_valve, t2))
canvas.text('=KKA-MV', t2.r_move(0.0, 1.0).get_offset(), 's')
_, t2 = write_wire(canvas, t2)
_, t2 = write_pump(canvas, get_t(write_pump, t2))
canvas.text('=KKA-P', t2.r_move(0.0, 1.0).get_offset(), 's')
_, t2 = write_corner(canvas, get_t(write_corner, t2))
_, t2 = write_wire(canvas, t2, 0.25)
_, t2 = write_heater(canvas, get_t(write_heater, t2))
canvas.text('=KK', t2.get_offset(), 'nw')
_, t2 = write_wire(canvas, t2, 0.25)
_, t2 = write_corner(canvas, get_t(write_corner, t2))
_, t2 = write_wire(canvas, t2, 2.0)
_, t2, t3 = write_tee(canvas, t2.move_to((t3.get_offset()[0], t2.get_offset()[1])))
write_wire(canvas, t3, 2.5)
_, t2 = write_wire(canvas, t2, 1.0)


#transform, t2 = write_mix_valve(canvas, transform)
#transform = write_pump(canvas, transform)
#transform = write_corner(canvas, transform)
#transform = write_radiator(canvas, transform)
#transform = write_corner(canvas, transform)
#transform = write_tee(canvas, transform, t2)
#transform, t2 = write_mix_valve(canvas, transform)
#transform = write_pump(canvas, transform)
#transform = write_corner(canvas, transform)
#transform = write_heater(canvas, transform)
#transform = write_corner(canvas, transform)
