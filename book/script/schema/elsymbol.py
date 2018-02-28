# -*- coding: utf-8 -*-

def draw_temp_sensor(scheme):
    """ Draw electrical symbol of a thermistor. """
    scheme.draw_rectangle((RESISTOR_RATIO, 1.0), style='contour') 
    scheme.draw_line(((0.4, 0.4), (-0.4, -0.4), (-0.7, -0.4)), style='aux')
    scheme.draw_text('$\\vartheta$', offset=(-0.55, -0.4), position='n')

