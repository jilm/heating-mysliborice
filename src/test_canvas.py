# -*- coding: utf-8 -*-

import canvas

canvas.canvas.line(((0.0, 5.0), (15.0, 5.0)))
canvas.canvas.line(((0.0, 10.0), (15.0, 10.0)))
canvas.canvas.line(((5.0, 0.0), (5.0, 15.0)))
canvas.canvas.line(((10.0, 0.0), (10.0, 15.0)))
canvas.canvas.text('SW', (5.0, 5.0), 'sw')
canvas.canvas.text('S', (7.5, 5.0), 's')
canvas.canvas.text('SE', (10.0, 5.0), 'se')
canvas.canvas.text('W', (5.0, 7.5), 'w')
canvas.canvas.text('0', (7.5, 7.5))
canvas.canvas.text('E', (10.0, 7.5), 'e')
canvas.canvas.text('NW', (5.0, 10.0), 'nw')
canvas.canvas.text('N', (7.5, 10.0), 'n')
canvas.canvas.text('NE', (10.0, 10.0), 'ne')