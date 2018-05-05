# -*- coding: utf-8 -*-

GRID_SIZE = 4.0 # minimal distance between two parallel wires
RATIO = 4.0 / 12.0    # resistor width / height ratio
HEIGHT = 2.3 * GRID_SIZE
WIDTH = RATIO * HEIGHT
PIN1 = ((0.0, 0.5 * HEIGHT), (0.0, 1.0))
PIN2 = ((0.0, -0.5 * HEIGHT), (0.0, 1.0))
CROSS_LINE_SIZE = 0.7 * WIDTH
CROSS_LINE = ((-CROSS_LINE_SIZE, -CROSS_LINE_SIZE), (CROSS_LINE_SIZE, CROSS_LINE_SIZE))

def draw_resistor_base(canvas):
    canvas.draw_rect(WIDTH, HEIGHT, style='normal')

def draw_thermistor_var(canvas):
    MF = 0.8
    MFGS = MF * GRID_SIZE
    canvas.draw_line((
        (MFGS, MFGS),
        (-MFGS, -MFGS),
        (-2.0 * MFGS, -MFGS)), style='tiny')
    canvas.text('$\\vartheta$', point=(-1.5 * MFGS, -MFGS), position='n')

def draw_grid(canvas, size):
    abs_size = (size // 2) * GRID_SIZE * 3 + GRID_SIZE
    canvas.draw_hline(-0.5*abs_size, 0, abs_size, style='grid')
    canvas.draw_vline(0, -0.5*abs_size, abs_size, style='grid')
    for i in range(1,size):
        canvas.draw_hline(-0.5*abs_size, i*GRID_SIZE, abs_size, style='grid')
        canvas.draw_hline(-0.5*abs_size, -i*GRID_SIZE, abs_size, style='grid')
        canvas.draw_vline(i*GRID_SIZE, -0.5*abs_size, abs_size, style='grid')
        canvas.draw_vline(-i*GRID_SIZE, -0.5*abs_size, abs_size, style='grid')

def draw_pin4(canvas):
    y1 = 0.5 * HEIGHT
    y2 = (HEIGHT // GRID_SIZE) * GRID_SIZE
    y3 = y2 + GRID_SIZE
    canvas.draw_line(((0.0, y1), (0.0, y3)), style='normal')
    canvas.draw_line(((0.0, -y1), (0.0, -y3)), style='normal')
    canvas.draw_line(((0.0, y1), (GRID_SIZE, y2)), style='normal')
    canvas.draw_line(((0.0, -y1), (GRID_SIZE, -y2)), style='normal')

def draw_thermistor_block(canvas):
    # draw rectangle
    #canvas.line(RECT.get_points())
    # draw pins
    # draw variable symbol
    #canvas.line(CROSS_LINE)
    # draw theta letter
    #canvas.text('$\sigma$', (2.5, -5.0))
    # draw envelope rectangle
    #canvas.line(vector.Rect())
    pass

