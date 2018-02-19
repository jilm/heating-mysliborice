# -*- coding: utf-8 -*-

from schema.canvas import Square
from schema.canvas import Canvas
from schema.canvas import StandaloneCanvas
from schema.canvas import Line
from schema.vector import I

PAPERS = {
    'A4L' : {},
    'A4P' : {},
    'A3L' : {
        'DRAWING_FRAME_SIZE' : (400.0, 277.0),
        'GRID_FRAME_SIZE' : (420.0, 297.0),
        'OUTER_FRAME_SIZE' : (430.0, 307.0),
        'RAW_PAPER_SIZE' : (436.0, 313.0),
        'GRID' : (3, 2)
    },
    'A3P' : {
        'DRAWING_FRAME_SIZE' : (287.0, 410.0),
        'GRID_FRAME_SIZE' : (297.0, 420.0),
        'OUTER_FRAME_SIZE' : (307.0, 430.0),
        'RAW_PAPER_SIZE' : (313.0, 436.0),
        'GRID' : (3, 4)
    }
}

LINE_WIDTHS = {
    'TINY' : 0.35,
    'NORMAL' : 0.5,
    'BOLD' : 0.7
}

class Scheme:

    def __init__(self, canvas, paper='A3L'):
        self.canvas = canvas
        self.canvas.setPaperSize(PAPERS[paper]['RAW_PAPER_SIZE'])
        self.canvas.unit = 'mm'
        self.canvas.open()
        self.paper = PAPERS[paper]
        self.t = I
        self.t_stack = list()
        self.draw_frame()

    def push(self):
        self.t_stack.append(self.t)

    def pop(self):
        self.t = self.t_stack.pop()

    def draw_rect(self, size, line='NORMAL'):
        self.canvas.set_line_width(LINE_WIDTHS[line])
        Square(self.t.r_scale(size[0], size[1])).write(self.canvas)

    def move(self, x, y):
        self.t = self.t.r_move(x, y)

    def draw_hline(self, x, y, size, line='NORMAL'):
        self.canvas.set_line_width(LINE_WIDTHS[line])
        Line(((x, y), (x+size, y)), self.t).write(self.canvas)

    def draw_vline(self, x, y, size, line='NORMAL'):
        self.canvas.set_line_width(LINE_WIDTHS[line])
        Line(((x, y), (x, y+size)), self.t).write(self.canvas)

    def draw_circle(self, r, x, y):
        pass

    def draw_frame(self):
        # Vykres velikosti A3
        # Vykresovy list
        drawing_frame_size = self.paper['DRAWING_FRAME_SIZE']
        grid_frame_size = self.paper['GRID_FRAME_SIZE']
        outer_frame_size = self.paper['OUTER_FRAME_SIZE']
        self.draw_rect(outer_frame_size, 'TINY') # draw outer frame
        self.draw_rect(grid_frame_size, 'TINY')  #
        self.draw_rect(drawing_frame_size)
        # draw center marks
        x, y = grid_frame_size
        x, y = 0.5 * x, 0.5 * y
        size = grid_frame_size[0] - drawing_frame_size[0]
        self.draw_hline(x, 0, -size)
        self.draw_hline(-x, 0, size)
        self.draw_vline(0, y, -size)
        self.draw_vline(0, -y, size)
        # draw grid
        hgrid, vgrid = self.paper['GRID']
        size = 0.5 * size
        dist = 0.5 * grid_frame_size[0] / hgrid
        for i in range(hgrid - 1):
            self.draw_vline((i+1)*dist, y, -size)
            self.draw_vline(-dist*(i+1), y, -size)
            self.draw_vline((i+1)*dist, -y, size)
            self.draw_vline(-dist*(i+1), -y, size)

        dist = 0.5 * grid_frame_size[1] / vgrid
        for i in range(vgrid - 1):
            self.draw_hline(x, (i+1)*dist, -size)
            self.draw_hline(x, -dist*(i+1), -size)
            self.draw_hline(-x, (i+1)*dist, size)
            self.draw_hline(-x, -dist*(i+1), size)
        # draw cut marks
        cut_points = (
            (0.0, 0.0),
            (10.0, 0.0),
            (10.0, 2.0),
            (2.0, 2.0),
            (2.0, 10.0),
            (0.0, 10.0),
            (0.0, 0.0)
        )
        x = 0.5 * grid_frame_size[0]
        y = 0.5 * grid_frame_size[1]
        self.canvas.set_line_width(LINE_WIDTHS['TINY'])
        Line(cut_points, self.t.r_move(-x, -y)).write(self.canvas)
        Line(cut_points, self.t.r_scale(1.0, -1.0).r_move(-x, -y)).write(self.canvas)
        Line(cut_points, self.t.r_scale(-1.0, 1.0).r_move(-x, -y)).write(self.canvas)
        Line(cut_points, self.t.r_scale(-1.0, -1.0).r_move(-x, -y)).write(self.canvas)
        # Description field
        DESC_FIELD_SIZE = (170.0, 50.0)
        self.push()
        self.move(
            0.5 * (drawing_frame_size[0] - DESC_FIELD_SIZE[0]),
            0.5 * (DESC_FIELD_SIZE[1] - drawing_frame_size[1])
        )
        self.draw_rect(DESC_FIELD_SIZE)
        self.pop()
        # Nazev vykresu
        # Cislo vykresu
        # List / listu
        # Projekt
        # Realizator
        # projektant
        # schvalil
        # nakreslil
        # datum
        # meritko
        # zmenove pole
        # Move drawing coordinates
        self.move(0.0, 0.5 * DESC_FIELD_SIZE[1])




class ScaledScheme(Scheme):

    def __init__(self, canvas, scale=1.0, paper='A3L'):
        Scheme.__init__(self, canvas, paper=paper)
        self.scale = scale
        self.t = self.t.r_scale(scale, scale)



