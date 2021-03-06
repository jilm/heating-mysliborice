# -*- coding: utf-8 -*-

from schema.paper import PAPERS
from schema.vector import I
from schema.style import STYLE
from schema.style import form_tikz_style
from schema.scheme import LocalScheme
from schema.scheme import ClipRegion
import sys

""" Latex and Tikz document drivers. """

PAPER_MARGINS = 3.0 # mm

class Latex:

    """ It represents the lowest layer; the Latex document. """

    def __init__(self):
        """ Requires a file to write the otput. """
        self.environment_stack = []

    def is_opened(self):
        return True if self.environment_stack else False

    def write_text(self, text):
        sys.stdout.write(text)

    def write_command(self, command, arg1=None, args=None):
        str_arg1 = '' if arg1 is None else '[{0}]'.format(str(arg1))
        str_args = '' if args is None else '}{'.join([str(arg) for arg in args])
        self.write_text('\\{0}{1}{{{2}}}'.format(command, str_arg1, str_args))

    def open_environment(self, environment):
        self.write_command('begin', args=[environment])
        self.environment_stack.append(environment)

    def close_last_environment(self):
        if self.is_opened():
            self.write_command('end', args=[self.environment_stack.pop()])

    def close(self):
        while self.is_opened():
            self.close_last_environment()

    def form_params(self, param_dict):
        return ','.join(
            ['{}={}'.format(key, param_dict[key]) for key in param_dict.keys()]
        )

class LatexDocument:

    """ It represents the lowest layer; the Latex document. """

    def __init__(self, file, raw_paper_size):

        """ Requires a file to write the otput. """

        self.file = file
        self.environment_stack = []
        self.raw_paper_size = raw_paper_size
        #self.open()

    def is_opened(self):
        return True if self.environment_stack else False

    def open(self):

        """ Write necessary latex document header into the file. """

        self.write_command('documentclass', args=['article'])
        self.write_command('usepackage', args=['tikz'])
        self.write_command('usepackage', args=['geometry'])
        #self.file.write('\\usepackage[paperwidth={}mm, paperheight={}mm, left=0.3cm, right=0.3cm, top=0.3cm, bottom=0.3cm, hoffset=0cm]{{geometry}}\n'.format(self.paper_size[0], self.paper_size[1]))
        self.write_command('usepackage', arg1='utf8', args=['inputenc'])
        geometry_params = {
            'paperwidth' : '{0}mm'.format(self.raw_paper_size[0]),
            'paperheight' : '{0}mm'.format(self.raw_paper_size[1]),
            'top' : '{0}mm'.format(PAPER_MARGINS),
            'bottom' : '0mm',
            'left' : '{0}mm'.format(PAPER_MARGINS),
            'right' : '0mm',
        }
        self.write_command('geometry', args=([self.form_params(geometry_params)]))
        self.open_environment('document')

    def write_text(self, text):
        self.file.write(text)

    def write_command(self, command, arg1=None, args=None):
        str_arg1 = '' if arg1 is None else '[{0}]'.format(str(arg1))
        str_args = '' if args is None else '}{'.join([str(arg) for arg in args])
        self.write_text('\\{0}{1}{{{2}}}'.format(command, str_arg1, str_args))

    def open_environment(self, environment):
        self.write_command('begin', args=[environment])
        self.environment_stack.append(environment)

    def close_last_environment(self):
        if self.is_opened():
            self.write_command('end', args=[self.environment_stack.pop()])

    def close(self):
        while self.is_opened():
            self.close_last_environment()

    def form_params(self, param_dict):
        return ','.join(
            ['{}={}'.format(key, param_dict[key]) for key in param_dict.keys()]
        )

    def get_size(self):
        return (
            self.raw_paper_size[0] - 2 * PAPER_MARGINS,
            self.raw_paper_size[1] - 2 * PAPER_MARGINS
        )

    def begin_tikz(self):
        tikz = Tikz(self, self.get_size())
        tikz.open()
        return tikz

class Tikz:

    """ Encapsulates a Tikz environment. """

    def __init__(self, latex_document, size):
        self.document = latex_document
        self.unit = 'mm'
        self.clip_region = ClipRegion((0.0, 0.0), size)

    def open(self):
        self.document.write_command('noindent')
        for name, style in STYLE.items():
            self.document.write_command('tikzstyle', args=(name,))
            self.document.write_text('=[{}]'.format(form_tikz_style(style)))
        self.document.open_environment('tikzpicture')

    def close(self):
        self.document.close_last_environment()

    def draw_line(self, points, style=None):

        """
        Draw strait line between all of the given points.
        Points must be given in the form of collection of x, y tuples.
        """

        path = TikzPathBuilder()
        for p in points:
            path.line_to(p)
        self.document.write_command('draw', arg1=style)
        self.document.write_text(str(path))
        self.document.write_text(';')

    def draw_hline(self, x, y, size, style=None):
        self.draw_line((
                (x, y),
                (x + size, y)
            ),
            style = style
        )

    def draw_vline(self, x, y, size, style=None):
        self.draw_line((
                (x, y),
                (x, y + size)
            ),
            style = style
        )

    def draw_rect(self, width, height, offset=(0.0, 0.0), style=None):
        lt_point = (-0.5 * width + offset[0], -0.5 * height + offset[1])
        rb_point = (0.5 * width + offset[0], 0.5 * height + offset[1])
        path = TikzPathBuilder(lt_point)
        path.rectangle_to(rb_point)
        self.document.write_command('draw', arg1=style)
        self.document.write_text(str(path))
        self.document.write_text(';')

    def get_size(self):
        return self.clip_region.get_size()

    def text(self, text, point, size=None, position=None, style=None):

        """Draw given text at given position."""

        x, y = point
        path = TikzPathBuilder(point)
        path.node(text)
        #params = list()
        #if position is not None:
        #    params.append('anchor={}'.format(text_positions[position]))
        #if width is not None:
        #    params.append('text width={}{}'.format(width, self.unit))
        #if size is not None and size in TEXT_SIZE:
        #    size_value = TEXT_SIZE[size]
        #else:
        #    size_value = ''
        #if params:
        #    str_params = '[{}]'.format(','.join(params))
        #else:
        #    str_params = ''
        self.document.write_command('draw', arg1=style)
        self.document.write_text(str(path))
        self.document.write_text(';')

    def move(self, offset=(0.0, 0.0)):
        return LocalScheme(
            canvas=self,
            t=I.r_move(*offset),
            clip_region=self.clip_region
        )

class TikzPathBuilder:

    """ It helps to format tikz path. """

    def __init__(self, point=None, unit='mm'):
        self.unit = unit
        if point is not None:
            self.str_path = self.form_point(*point)
        else:
            self.str_path = None

    def line_to(self, point):
        if self.str_path is None:
            self.str_path = self.form_point(*point)
        else:
            self.str_path = '--'.join([self.str_path, self.form_point(*point)])

    def close_path(self):
        if self.str_path is not None:
            self.str_path = self.str_path.__add__('--cycle')

    def rectangle_to(self, point):
        if self.str_path is None:
            self.str_path = self.form_point(*point)
        else:
            self.str_path = ' rectangle '.join([
                self.str_path,
                self.form_point(*point)
            ])

    def node(self, label):
        if self.str_path is not None:
            self.str_path += ' node {{{0}}}'.format(label)

    def form_point(self, x, y):
        if self.unit is not None:
            return '({0}{2},{1}{2})'.format(x, y, self.unit)
        else:
            return '({0},{1})'.format(x, y)

    def __str__(self):
        return self.str_path


class TransformableScheme:

    def __init__(self, size):
        self.t = I
        self.size = size

    def move_to(self, point):
        self.t = self.t.move_to(point)

    def get_center(self):
        return (0.5 * self.size[0], 0.5 * self.size[1])

class Schema(TransformableScheme):

    """ This object represents the device independent layer on the Tikz. """

    def __init__(self, tikz, size):
        super().__init__(size)
        self.canvas = tikz

    def draw_rect(self, width, height, style=None):
        self.canvas.draw_rect(
            self.t.transform_point((-0.5 * width, -0.5 * height)),
            self.t.transform_point((0.5 * width, 0.5 * height)),
            style = style
        )

    def draw_line(self, points, style=None):
        self.canvas.draw_line(
            self.t.transform_points(points),
            style = style
        )

    def draw_hline(self, x, y, size, style=None):
        self.canvas.draw_line(
            self.t.transform_points((
                (x, y),
                (x + size, y)
            )),
            style = style
        )

    def draw_vline(self, x, y, size, style=None):
        self.canvas.draw_line(
            self.t.transform_points((
                (x, y),
                (x, y + size)
            )),
            style = style
        )

    def text(self, text, point, size=None, position=None):
        self.canvas.text(text, self.t.transform_point(point))