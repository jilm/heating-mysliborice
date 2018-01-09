
from schema.canvas import Path
from schema.canvas import Canvas
from schema.canvas import Circle
from schema.canvas import Line
from schema.canvas import Square
from schema.vector import Transform
from schema.vector import I
from schema.components import get_component

GS = 1.5 # zakladni velikost nejakeho domneleho gridu

RESISTOR_RATIO = 4.0 / 12.0

# equilateral_triangle
EQ_TRIANGLE_H = 0.866 # height of the triangle
EQ_TRIANGLE_R = 0.289 # The radius of the inscribed circle
EQ_TRIANGLE = Transform().move((EQ_TRIANGLE_R - EQ_TRIANGLE_H, 0)).transform_points([
    (0.0, 0.0),
    (EQ_TRIANGLE_H, 0.5),
    (EQ_TRIANGLE_H, -0.5),
    (0.0, 0.0)
])

# Symbol komparatoru
COMPARATOR_POINTS = [
    (-0.5, -0.5),
    (0.16, -0.5),
    (0.16, 0.5)
]

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

def write_temp_sensor(canvas, t = I):
    width = GS
    t = I.move((0.5 * width, 0.0)).transform(t)
    Square(I.scale(RESISTOR_RATIO, 1.0).move((0.0, 0.0)).transform(t)).write(canvas)
    Line(((0.4, 0.4), (-0.4, -0.4), (-0.7, -0.4)), t).write(canvas)
    # Square(I.scale(1.5, 1.5).transform(t)).write(canvas)
    canvas.text('$\\vartheta$', t.transform_point((-0.55, -0.4)), position='n')
    return I.move((0.2 * GS, 0.0)).transform(t)

def write_converter(labels, canvas, t = I):
    width = GS
    t = I.move((0.5 * width, 0.0)).transform(t)
    Square(I.scale(1.5, 1.5).transform(t)).write(canvas)
    Line(((-0.75, -0.75), (0.75, 0.75)), t).write(canvas)
    canvas.text(labels[0], t.transform_point((-0.35, 0.35)))
    canvas.text(labels[1], t.transform_point((0.35, -0.35)))
    return t.move(t.transform_vector((0.5*width, 0.0)))

def write_comparator(canvas, t = I):
    width = GS
    t = I.move((0.5 * width, 0.0)).transform(t)
    Line(COMPARATOR_POINTS, I.scale(0.3, 0.3).transform(t)).write(canvas)
    Line(COMPARATOR_POINTS, I.scale(-0.3, -0.3).transform(t)).write(canvas)
    Line(EQ_TRIANGLE, I.scale(-1.3, 1.3).transform(t)).write(canvas)
    return t.move(t.transform_vector((0.5 * GS, 0.0)))

def write_fork(canvas, t = I):
    width = GS
    Line(((0.3, 0.0), (width - 0.3, 0.0)), t).write(canvas)
    Line(((width - 0.3, 1.25*GS), (0.5*width, 1.25*GS), (0.5*width, -1.25*GS), (width - 0.3, -1.25*GS)), t).write(canvas)
    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, 1.25*GS)).transform(t)).write(canvas)
    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, 0.0)).transform(t)).write(canvas)
    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, -1.25*GS)).transform(t)).write(canvas)
    return [
        I.move((width, 1.25 * GS)).transform(t),
        I.move((width, 0.0)).transform(t),
        I.move((width, -1.25 * GS)).transform(t)
    ]

def write_arrow(canvas, t = I):
    width = GS
    Line(((0.3, 0.0), (width - 0.3, 0.0)), t).write(canvas)
    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, 0.0)).transform(t)).write(canvas)
    return t.move(t.transform_vector((width, 0.0)))


# Nakresli
canvas = Canvas()
transform = I

get_component('=KK-BTH')

[write_arrow(canvas,
    write_comparator(canvas, t)) for t in
    write_fork(canvas,
        write_converter('AD', canvas,
        write_arrow(canvas,
            write_converter('RI', canvas,
            write_arrow(canvas,
                write_temp_sensor(canvas, I)
            )
        )
    )))
]