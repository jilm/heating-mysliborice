
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
    t = I.scale(3.0, 4.0).transform(transf)
    symbol = Square(t)
    symbol.write(canvas)
    return transf.move(transf.transform_vector((3.0, 0.0)))

def write_pump(canvas, transf = I):
    symbol = Circle(transf)
    symbol.write(canvas)
    t = I.scale(-0.6, 0.6).transform(transf)
    symbol = Line(EQ_TRIANGLE, t)
    symbol.write(canvas)
    return transf.move(transf.transform_vector((1.5, 0.0)))

def write_mix_valve(canvas, transf = I):
    symbol = Line(MIX_VALVE, transf)
    symbol.write(canvas)
    t1 = transf.move(transf.transform_vector((1.5, 0.0)))
    t2 = transf.rotate_vect()
    t2 = t2.move(t2.transform_vector((1.5, 0.0)))
    return t1, t2

def write_corner(canvas, transf = I):
    symbol = Line(((-0.5, 0.0), (0.0, 0.0), (0.0, -0.5)), transf)
    symbol.write(canvas)
    transf = transf.rotate_vect()
    return transf.move(transf.transform_vector((1.5, 0.0)))

def write_radiator(canvas, transf = I):
    symbol = Square(I.scale(3.0, 4.0).transform(transf))
    symbol.write(canvas)
    return transf.move(transf.transform_vector((4.0, 0.0)))

def write_tee(canvas, t1, t2):
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

# Nakresli
canvas = Canvas()
transform = I
transform, t2 = write_mix_valve(canvas, transform)
transform = write_pump(canvas, transform)
transform = write_corner(canvas, transform)
transform = write_radiator(canvas, transform)
transform = write_corner(canvas, transform)
transform = write_tee(canvas, transform, t2)
transform, t2 = write_mix_valve(canvas, transform)
transform = write_pump(canvas, transform)
transform = write_corner(canvas, transform)
transform = write_heater(canvas, transform)
transform = write_corner(canvas, transform)
