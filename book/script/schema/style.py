# -*- coding: utf-8 -*-

LINE_WIDTHS = {
    'TINY' : 0.18,
    'NORMAL' : 0.25,
    'BOLD' : 0.5
}

STYLE = {

    'aux' : {
        'line_width' : LINE_WIDTHS['TINY'],
        'line' : 'dashed',
        'filled' : False,
    },

    'tiny' : {
        'line_width' : LINE_WIDTHS['TINY'],
        'line' : 'solid',
        'filled' : False
    },

    'normal' : {
        'line width' : LINE_WIDTHS['NORMAL'],
        'line' : None,
        'filled' : False,
    },

    'bold' : {
        'line width' : LINE_WIDTHS['BOLD'],
        'line' : None,
        'filled' : False,
    },

    'filled' : {
        'line width' : LINE_WIDTHS['TINY'],
        'filled' : True,
        'line' : None
    },

    'warning' : {
        'line width' : LINE_WIDTHS['TINY'],
        'line' : 'dashed',
        'color' : 'red',
        'filled' : False
    },

    'axis' : {
        'line width' : LINE_WIDTHS['TINY'],
        'line' : 'on 7mm off 0.8mm on 0.6mm off 0.8mm',
        'filled' : False,
    },

    'grid' : {
        'line width' : LINE_WIDTHS['TINY'],
        'color' : 'red'
    }
}

def form_tikz_style(style):
    result = []
    if 'line width' in style:
        result.append('line width={0}mm'.format(style['line width']))
    if 'color' in style:
        result.append('color={}'.format(style['color']))
    return ','.join(result)