
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
    transf = I.scale(3.0, 4.0).transform(transf)
    symbol = Square(transf)
    symbol.write(canvas)
    return [
        transf.move((3.0, 1.5))
    ]

def write_pump(canvas, transf = I):
    symbol = Circle(transf)
    symbol.write(canvas)
    return transf.move((1.5, 0.0))

def write_mix_valve(canvas, transf = I):
    symbol = Line(MIX_VALVE, transf)
    symbol.write(canvas)
    return transf.move((1.5, 0.0))

def write_corner(canvas, transf = I):
    symbol = Line(((-0.5, 0.0), (0.0, 0.0), (0.0, -0.5)), transf)
    symbol.write(canvas)
    return transf.rotate_vect().move((1.5, 0.0))


# Schematicky blokovy diagram topeni v podkrovi

# Krbova kamna

# Cerpadlo krbovych kamen

# Termostaticky regulacni ventil

# Smesovaci ventil

# Cerpadlo do topeni

# Topeni


# Nakresli
canvas = Canvas()
transform = I
transform = write_pump(canvas, transform)
transform = write_mix_valve(canvas, transform)
transform = write_corner(canvas, transform)
transform = write_mix_valve(canvas, transform)


