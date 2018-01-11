
from schema.canvas import Path
from schema.canvas import Canvas
from schema.canvas import Circle
from schema.canvas import Line
from schema.canvas import Square
from schema.vector import Transform
from schema.vector import I

GS = 1.5 # zakladni velikost nejakeho domneleho gridu

ALIGNMENTS = {
    'left' : 1.0,
    'center': 0.0,
    'right': -1.0
}

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

VALVE = Transform().scale(0.5).transform_points([
    (0.0, 0.0),
    (EQ_TRIANGLE_H, 0.5),
    (EQ_TRIANGLE_H, -0.5),
    (-EQ_TRIANGLE_H, 0.5),
    (-EQ_TRIANGLE_H, -0.5),
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

#def write_fork(canvas, t = I):
#    width = GS
#    Line(((0.3, 0.0), (width - 0.3, 0.0)), t).write(canvas)
#    Line(((width - 0.3, 1.25*GS), (0.5*width, 1.25*GS), (0.5*width, -1.25*GS), (width - 0.3, -1.25*GS)), t).write(canvas)
#    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, 1.25*GS)).transform(t)).write(canvas)
#    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, 0.0)).transform(t)).write(canvas)
#    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, -1.25*GS)).transform(t)).write(canvas)
#    return [
#        I.move((width, 1.25 * GS)).transform(t),
#        I.move((width, 0.0)).transform(t),
#        I.move((width, -1.25 * GS)).transform(t)
#    ]

def write_arrow(canvas, t = I):
    width = GS
    Line(((0.3, 0.0), (width - 0.3, 0.0)), t).write(canvas)
    Line(EQ_TRIANGLE, I.scale(-0.3, 0.3).move((width - 0.3, 0.0)).transform(t)).write(canvas)
    return t.move(t.transform_vector((width, 0.0)))

def write_switch(canvas, t = I, labels = None, align = 'left'):
    t = t.r_move(0.5 * ALIGNMENTS[align], 0.0)
    OVER = 3.0 / 20.0   # zobacek kontaktu
    EQA = 1.0 - OVER    # Strana rovnostranneho trojuhelnika
    EQH = 0.866 * EQA   # EQH - vyska rovnostranneho trojuhhlnika

    Line([
        (-0.5, 0.0),
        (-0.5 * EQH, 0.0),
        (0.5 * EQH * 0.866, 0.5 - 0.5 * OVER)
    ], t).write(canvas)
    # kontakt
    Line([
        (0.5 * EQH - 0.5 * OVER, OVER),
        (0.5 * EQH - 0.5 * OVER, 0.0),
        (0.5, 0.0)
    ], t).write(canvas)

    if labels is not None:
        canvas.text(labels[0], t.transform_point((-0.5, 0.0)), 'nw', 'small')
        canvas.text(labels[1], t.transform_point((0.5, 0.0)), 'ne', 'small')

    return t.r_move(0.5 * ALIGNMENTS[align], 0.0)

def write_change_over_switch(canvas, t = I, labels = None):

    if canvas is None:
        return t.r_move(-0.5, 0.0), t.r_move(0.5, 0.5), t.r_move(0.5, -0.5)

    #t = t.r_move(0.5, 0.0)
    OVER = 3.0 / 20.0   # zobacek kontaktu
    EQA = 1.0 - OVER    # Strana rovnostranneho trojuhelnika
    EQH = 0.866 * EQA   # EQH - vyska rovnostranneho trojuhhlnika

    Line([
        (-0.5, 0.0),
        (-0.5 * EQH, 0.0),
        (0.5 * EQH, 0.5 - 0.5 * OVER)
    ], t).write(canvas)
    # kontakty
    Line([
        (0.5 * EQH - 0.5 * OVER, 0.5 - OVER),
        (0.5 * EQH - 0.5 * OVER, 0.5),
        (0.5, 0.5)
    ], t).write(canvas)
    Line([
        (0.5 * EQH - 0.5 * OVER, -0.5 + OVER),
        (0.5 * EQH - 0.5 * OVER, -0.5),
        (0.5, -0.5)
    ], t).write(canvas)

    if labels is not None:
        canvas.text(labels[0], t.transform_point((-0.5 * EQH, 0.0)), 'nw', 'small')
        canvas.text(labels[1], t.transform_point((0.5 * EQH - 0.5 * OVER, 0.5)), 'ne', 'small')
        canvas.text(labels[2], t.transform_point((0.5 * EQH - 0.5 * OVER, -0.5)), 'se', 'small')

    return t.r_move(-0.5, 0.0), t.r_move(0.5, 0.5), t.r_move(0.5, -0.5)

def write_coil(canvas = None, t = I, labels = None):
    if canvas is not None:
        WH_RATIO = 3.0 / 4.0
        Square(t.r_scale(WH_RATIO, 1.0)).write(canvas)
        Line([(-0.5, 0.0), (-0.5 * WH_RATIO, 0.0)], t).write(canvas)
        Line([(0.5, 0.0), (0.5 * WH_RATIO, 0.0)], t).write(canvas)
        if labels is not None:
            canvas.text(labels[0], t.transform_point((-0.5 * WH_RATIO, 0.0)), 'nw', 'small')
            canvas.text(labels[1], t.transform_point((0.5 * WH_RATIO, 0.0)), 'ne', 'small')
    return t.r_move(-0.5, 0.0), t.r_move(0.5, 0.0)

def write_coil_solenid(canvas = None, t = I, labels = None):
    if canvas is not None:
        Line(VALVE, t.r_scale(0.5).r_move(0.0, 0.35)).write(canvas)
    return write_coil(canvas, t, labels)


def write_rele(canvas = None, t = I, labels = None):
    coil_labels = labels[0:2] if labels is not None else None
    switch_labels = labels[2:] if labels is not None else None
    tc1, tc2 = write_coil(canvas,  t, labels = coil_labels)
    ts0, ts1, ts2 = write_change_over_switch(canvas, t.r_move(0.0, -1.5), labels = switch_labels)
    return tc1, tc2, ts0, ts1, ts2

def write_wire(canvas, t = I, scale = 1.0):
    if canvas is not None:
        Line([(0.0, 0.0), (1.0 * scale, 0.0)], t).write(canvas)
    return t, t.r_move(1.0 * scale, 0.0)

def write_gnd(canvas, t = I):
    Line([
        (-0.5, 0.0),
        (0.5, 0.0),
        (0.0, -0.5),
        (-0.5, 0.0)
    ], t.r_scale(0.5).r_move(0.0, -0.5)).write(canvas)
    Line([(0.0, 0.0), (0.0, -0.25)], t).write(canvas)
    canvas.text('GND', t.transform_point((0.0, -0.25)), position = 'ne', size = 'small')

def write_n(canvas, t = I):
    Line([ (0.0, 0.0), (0.0, -0.25) ], t).write(canvas)
    Line([ (-0.25, -0.25), (0.25, -0.25) ], t).write(canvas)

def write_terminal(canvas, t = I, align = 'left'):
    SCALE = 0.20
    t = t.r_move(0.5 * SCALE * ALIGNMENTS[align], 0.0)
    t_scaled = t.r_scale(SCALE)
    Circle(t_scaled).write(canvas)
    Line([(-0.5, -0.5), (0.5, 0.5)], t_scaled).write(canvas)
    return t.r_move(0.5 * SCALE * ALIGNMENTS[align], 0.0)

def write_disconnect_terminal(canvas, t = I):
    WIDTH = 1.5
    if canvas is not None:
        write_terminal(canvas, t.r_move(-0.5*WIDTH, 0.0))
        write_terminal(canvas, t.r_move(0.5*WIDTH, 0.0), align='right')
        write_switch(canvas, t.r_move(0.75, 0.0).r_scale(0.75), align = 'center')
    return t.r_move(-0.5*WIDTH, 0.0), t.r_move(0.5*WIDTH, 0.0)

def write_ref(canvas, t = I, text = ''):
    Line([ (-0.1, 0.0), (0.0, 0.0) ], t).write(canvas)
    Line([
        (-0.1, 0.20),
        (-0.1, -0.20),
        (-1.0, -0.20),
        (-0.4*0.866-1.0, 0.0),
        (-1.0, 0.20),
        (-0.1, 0.20)
    ], t).write(canvas)
    canvas.text(text, t.transform_point((-0.1, 0.0)), position = 'w', size = 'small')
    return t

def write_fork(canvas, t, scale = 1.0):
    Line([ (0.0, 0.0), (0.5, 0.0) ], t).write(canvas)
    Line([
        (1.0, 0.5 * scale),
        (0.5, 0.5 * scale),
        (0.5, -0.5 * scale),
        (1.0, -0.5 * scale)
    ], t).write(canvas)
    Circle(t.r_move(0.5, 0.0).r_scale(0.15)).write(canvas)
    return t.r_move(1.0, 0.5 * scale), t.r_move(1.0, -0.5 * scale)

def write_join(canvas, t1, t2, scale = 1.0):
    x1, y1 = t1.get_offset()
    x2, y2 = t2.get_offset()
    x = max((x1, x2)) + 0.5 * scale
    y = 0.5 * (y1 + y2)
    Line([
        (x1, y1),
        (x, y1),
        (x, y2),
        (x2, y2)
    ]).write(canvas)
    Line([
        (x, y),
        (x + 0.5 * scale, y)
    ]).write(canvas)
    return I.move_to((x + 0.5 * scale, y))

def diff(p1, p2):
    return p1[0] - p2[0], p1[1] - p2[1]

def get_t(write_fn, t1, i):
    t2 = write_fn(None)[i]
    x1, y1 = t1.get_offset()
    x2, y2 = t2.get_offset()
    dx, dy = x1 - x2, y1 - y2
    return I.r_move(dx, dy)

# Nakresli
canvas = Canvas()
transform = I

upper_label_line = 1.0
lower_label_line = -4.5
# Linie 1
t = write_ref(canvas, text = 'WD')
t1, t2 = write_wire(canvas, t)
# Quido kontakt
tq = get_t(write_change_over_switch, t2, 0)
t1, t2, t3 = write_change_over_switch(
    canvas = canvas,
    t = tq,
    labels = ['C1', 'NC1', 'NO1'])
canvas.text(
    text='-B1',
    point = (tq.get_offset()[0], upper_label_line),
    position = 'n')
t1, t2 = write_wire(canvas, t3, scale = 1.5)
# Civka rele
t_rele = t = get_t(write_rele, t2, 0)
t1, t2, tc1, tc2, tc3 = write_rele(
    canvas = canvas,
    t = t_rele,
    labels = ['A1', 'A2', '21', '', '14'])
canvas.text(
    text='-K1',
    point = (t_rele.get_offset()[0], upper_label_line),
    position = 'n')
t1, t2 = write_wire(canvas, t2)
write_gnd(canvas, t2)

# Linie 2
# rozpojovaci svorka
t1, t2 = write_disconnect_terminal(canvas, t_rele.r_move(0.0, -3.0))
canvas.text(
    text='-X1:1',
    point = (t_rele.get_offset()[0], lower_label_line),
    position = 'n')
# paralelni propojeni s kontaktem rele
tr = write_join(canvas, t2, tc3)
tl = write_join(canvas, tc1, t1, scale = -1.0)
# zleva pripoj fazi
t1, t2 = write_wire(canvas, tl, scale = -1.0)
write_ref(canvas, t2, text = 'L1')
# zprava pripoj solenoid
t1, t2 = write_wire(canvas, tr)
t_solenoid = get_t(write_coil, t2, 0)
t1, t2 = write_coil_solenid(
    canvas = canvas,
    t = t_solenoid)
canvas.text(
    text='-V1',
    point = (t_solenoid.get_offset()[0], lower_label_line),
    position = 'n')
t1, t2 = write_wire(canvas, t2)
write_n(canvas, t2)
