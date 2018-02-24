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

GRID_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p']
GRID_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

LINE_WIDTHS = {
    'TINY' : 0.18,
    'NORMAL' : 0.25,
    'BOLD' : 0.5
}

STYLE = {
    'aux' : {
        'line_width' : LINE_WIDTHS['TINY'],
        'line' : 'dashed',
    },
    'normal' : {
        'line_width' : LINE_WIDTHS['NORMAL'],
    },
    'bold' : {
        'line_width' : LINE_WIDTHS['NORMAL'],
    },
    'filled' : {
        'filled' : True,
    },
    'warning' : {
        'line_width' : LINE_WIDTHS['TINY'],
        'line' : 'dashed',
        'color' : 'red'
    },
    'axis' : {
        'line_width' : LINE_WIDTHS['TINY'],
        'line' : 'dashed',
    }
}

class Scheme:

    def __init__(self, canvas, paper='A3L', description=None):
        self.canvas = canvas
        self.canvas.setPaperSize(PAPERS[paper]['RAW_PAPER_SIZE'])
        self.canvas.unit = 'mm'
        self.canvas.open()
        self.paper = PAPERS[paper]
        self.t = I
        self.t_stack = list()
        self.description = description
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

    def draw_circle(self, radius, cx=0.0, cy=0.0):
        c = self.t.transform_point((cx, cy))
        r = self.t.transform_vector((radius, radius))[0]
        self.canvas.circle(c[0], c[1], r)

    def draw_hdimension(self, points, y):
        # draw auxiliary lines
        self.canvas.set_line_width(LINE_WIDTHS['TINY'])
        aux_points = [((x1, y1+2.0), (x1, y+2.0)) for x1, y1 in points]
        for p in aux_points:
            Line(p, self.t).write(self.canvas)
        # draw dimension line
        Line(((points[0][0], y), (points[-1][0], y)), self.t).write(self.canvas)
        # draw dimension mark
        for p in [(x, y) for x, _ in points[1:]]:
            self.draw_dimension_mark(self.t.r_move(p[0], p[1]))
        for p in [(x, y) for x, _ in points[0:-1]]:
            self.draw_dimension_mark(self.t.r_move(p[0], p[1]).r_scale(-1.0, 1.0))
        # write a dimension
        for i in range(len(points)-1):
            x1 = points[i][0]
            x2 = points[i+1][0]
            dim = x2 - x1
            self.canvas.text('{}'.format(dim), self.t.transform_point((0.5 *
            (x1 + x2), y)), 'n')

    def draw_vdimension(self, points, x):
        # draw auxiliary lines
        self.canvas.set_line_width(LINE_WIDTHS['TINY'])
        aux_points = [((x1-2.0, y1), (x-2.0, y1)) for x1, y1 in points]
        for p in aux_points:
            Line(p, self.t).write(self.canvas)
        # draw dimension line
        Line(((x, points[0][1]), (x, points[-1][1])), self.t).write(self.canvas)
        # draw dimension mark
        for p in [(x, y) for _, y in points[1:]]:
            self.draw_dimension_mark(self.t.r_move(p[0], p[1]).rotate_vect())
        for p in [(x, y) for _, y in points[0:-1]]:
            self.draw_dimension_mark(
                self.t.r_move(p[0], p[1]).r_scale(-1.0, 1.0).rotate_vect()
            )
        # write a dimension
        for i in range(len(points)-1):
            y1 = points[i][1]
            y2 = points[i+1][1]
            dim = y2 - y1
            self.canvas.text(
                '{}'.format(dim),
                self.t.transform_point((x, 0.5 * (y1 + y2))),
                'w'
            )


    def draw_dimension_mark(self, t):
        Line(((-4.0, 1.37), (0.0, 0.0), (-4.0, -1.37)), t).write(self.canvas)

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
        y = 0.5 * grid_frame_size[1]
        hgrid, vgrid = self.paper['GRID']
        size = 0.5 * size
        dist = 0.5 * grid_frame_size[0] / hgrid
        for i in range(hgrid - 1):
            x = (i+1)*dist
            self.draw_vline(x, y, -size)
            self.draw_vline(-x, y, -size)
            self.draw_vline(x, -y, size)
            self.draw_vline(-x, -y, size)
            self.canvas.text(GRID_NUMBERS[hgrid - 1 - i]
                , (-x + 0.5*dist,y - 0.5*size), size='large')
            self.canvas.text(GRID_NUMBERS[hgrid + i]
                , (x - 0.5*dist,y - 0.5*size), size='large')
            self.canvas.text(GRID_NUMBERS[hgrid - 1 - i]
                , (-x + 0.5*dist, - y + 0.5*size), size='large')
            self.canvas.text(GRID_NUMBERS[hgrid + i]
                , (x - 0.5*dist, - y + 0.5*size), size='large')
        self.canvas.text(GRID_NUMBERS[0]
            , (-(hgrid - 0.5)*dist,y - 0.5*size), size='large')
        self.canvas.text(GRID_NUMBERS[hgrid*2-1]
            , ((hgrid - 0.5)*dist,y - 0.5*size), size='large')
        self.canvas.text(GRID_NUMBERS[0]
            , (-(hgrid - 0.5)*dist, -y + 0.5*size), size='large')
        self.canvas.text(GRID_NUMBERS[hgrid*2-1]
            , ((hgrid - 0.5)*dist, - y + 0.5*size), size='large')

        dist = 0.5 * grid_frame_size[1] / vgrid
        x = 0.5 * grid_frame_size[0]
        for i in range(vgrid - 1):
            x = 0.5 * grid_frame_size[0]
            y = (i + 1) * dist
            self.draw_hline(x, y, -size)
            self.draw_hline(x, -y, -size)
            self.draw_hline(-x, y, size)
            self.draw_hline(-x, -y, size)
            x = x - 0.5 * size
            y = (i + 0.5) * dist
            self.canvas.text(GRID_LETTERS[vgrid-1-i], (x, y), size='large')
            self.canvas.text(GRID_LETTERS[vgrid-1-i], (-x, y), size='large')
            self.canvas.text(GRID_LETTERS[vgrid+i], (x, -y), size='large')
            self.canvas.text(GRID_LETTERS[vgrid+i], (-x, -y), size='large')
        x = 0.5 * (grid_frame_size[0] - size)
        y = (vgrid - 0.5) * dist
        self.canvas.text(GRID_LETTERS[0], (x, y), size='large')
        self.canvas.text(GRID_LETTERS[0], (-x, y), size='large')
        self.canvas.text(GRID_LETTERS[2*vgrid-1], (x, -y), size='large')
        self.canvas.text(GRID_LETTERS[2*vgrid-1], (-x, -y), size='large')
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
        if self.description is not None:
            # Cislo vykresu
            if 'number' in self.description:
                self.canvas.text(
                    self.description['number'],
                    self.t.transform_point((0, 0)),
                    size='huge'
                )
            # Nazev vykresu
            if 'name' in self.description:
                self.canvas.text(
                    self.description['name'],
                    self.t.transform_point((0, -10)),
                    size='huge'
                )
        # List / listu
        # Projekt
        # Realizator
        # projektant
        # schvalil
        # nakreslil
        # datum
        # meritko
        # zmenove pole
        self.pop()
        # Move drawing coordinates
        self.move(0.0, 0.5 * DESC_FIELD_SIZE[1])




class ScaledScheme(Scheme):

    def __init__(self, canvas, scale=1.0, paper='A3L', description=None):
        Scheme.__init__(self, canvas, paper=paper, description=description)
        self.scale = scale
        self.t = self.t.r_scale(scale, scale)




