# -*- coding: utf-8 -*-

from schema.symbols import EQ_TRIANGLE
from schema.vector import I

""" Draw a frame on the schema object. """

GRID_LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm', 'n', 'p']
GRID_NUMBERS = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13']

def draw_frame(schema, geometry):
    #raw_size=canvas.get_size()
    # Vykresovy list
    drawing_frame_size = geometry['DRAWING_FRAME_SIZE']
    grid_frame_size = geometry['GRID_FRAME_SIZE']
    outer_frame_size = geometry['OUTER_FRAME_SIZE']
    schema.move_to(schema.get_center())
    schema.draw_rect(*outer_frame_size, style='tiny') # draw outer frame
    schema.draw_rect(*grid_frame_size, style='tiny')  #
    schema.draw_rect(*drawing_frame_size, style='normal')
    # draw center marks
    x, y = grid_frame_size
    x, y = 0.5 * x, 0.5 * y
    size = grid_frame_size[0] - drawing_frame_size[0]
    schema.draw_hline(x, 0, -size)
    schema.draw_hline(-x, 0, size)
    schema.draw_vline(0, y, -size)
    schema.draw_vline(0, -y, size)
    # center triangles
    schema.draw_line(
        I.r_move(x-5.0, 0.0).r_scale(-5.0, 5.0).transform_points(EQ_TRIANGLE)
    )
    schema.draw_line(
        I.r_move(0.0, -y+5.0).r_scale(-5.0, 5.0).rotate_vect().transform_points(EQ_TRIANGLE)
    )
    # draw grid
    y = 0.5 * grid_frame_size[1]
    hgrid, vgrid = geometry['GRID']
    size = 0.5 * size
    dist = 0.5 * grid_frame_size[0] / hgrid
    for i in range(hgrid - 1):
        x = (i+1)*dist
        schema.draw_vline(x, y, -size)
        schema.draw_vline(-x, y, -size)
        schema.draw_vline(x, -y, size)
        schema.draw_vline(-x, -y, size)
        schema.text(GRID_NUMBERS[hgrid - 1 - i]
                , (-x + 0.5*dist,y - 0.5*size), size='large')
        schema.text(GRID_NUMBERS[hgrid + i]
                , (x - 0.5*dist,y - 0.5*size), size='large')
        schema.text(GRID_NUMBERS[hgrid - 1 - i]
                , (-x + 0.5*dist, - y + 0.5*size), size='large')
        schema.text(GRID_NUMBERS[hgrid + i]
                , (x - 0.5*dist, - y + 0.5*size), size='large')
    schema.text(GRID_NUMBERS[0]
        , (-(hgrid - 0.5)*dist,y - 0.5*size), size='large')
    schema.text(GRID_NUMBERS[hgrid*2-1]
        , ((hgrid - 0.5)*dist,y - 0.5*size), size='large')
    schema.text(GRID_NUMBERS[0]
        , (-(hgrid - 0.5)*dist, -y + 0.5*size), size='large')
    schema.text(GRID_NUMBERS[hgrid*2-1]
        , ((hgrid - 0.5)*dist, - y + 0.5*size), size='large')

    dist = 0.5 * grid_frame_size[1] / vgrid
    x = 0.5 * grid_frame_size[0]
    for i in range(vgrid - 1):
        x = 0.5 * grid_frame_size[0]
        y = (i + 1) * dist
        schema.draw_hline(x, y, -size)
        schema.draw_hline(x, -y, -size)
        schema.draw_hline(-x, y, size)
        schema.draw_hline(-x, -y, size)
        x = x - 0.5 * size
        y = (i + 0.5) * dist
        schema.text(GRID_LETTERS[vgrid-1-i], (x, y), size='large')
        schema.text(GRID_LETTERS[vgrid-1-i], (-x, y), size='large')
        schema.text(GRID_LETTERS[vgrid+i], (x, -y), size='large')
        schema.text(GRID_LETTERS[vgrid+i], (-x, -y), size='large')
    x = 0.5 * (grid_frame_size[0] - size)
    y = (vgrid - 0.5) * dist
    schema.text(GRID_LETTERS[0], (x, y), size='large')
    schema.text(GRID_LETTERS[0], (-x, y), size='large')
    schema.text(GRID_LETTERS[2*vgrid-1], (x, -y), size='large')
    schema.text(GRID_LETTERS[2*vgrid-1], (-x, -y), size='large')
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
    x = 0.5 * grid_frame_size[0] + 2.0
    y = 0.5 * grid_frame_size[1] + 2.0
    schema.draw_line(I.r_scale(1.0, 1.0).r_move(-x, -y).transform_points(cut_points))
    schema.draw_line(I.r_scale(1.0, -1.0).r_move(-x, -y).transform_points(cut_points))
    schema.draw_line(I.r_scale(-1.0, 1.0).r_move(-x, -y).transform_points(cut_points))
    schema.draw_line(I.r_scale(-1.0, -1.0).r_move(-x, -y).transform_points(cut_points))

    return
