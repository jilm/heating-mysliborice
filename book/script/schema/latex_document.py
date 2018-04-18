# -*- coding: utf-8 -*-

""" It writes necessary latex document envelope. """

class LatexDocument:

    def __init__(self, file):
        """ Requires a file to write the otput. """
        self.file = file
        self.environment_stack = []
        self.open()

    def is_opened(self):
        return True if self.environment_stack else False

    def open(self):
        """ Write necessary latex document header into the file. """
        self.write_command('documentclass', args=['article'])
        self.write_command('usepackage', args=['tikz'])
        #self.file.write('\\usepackage[paperwidth={}mm, paperheight={}mm, left=0.3cm, right=0.3cm, top=0.3cm, bottom=0.3cm, hoffset=0cm]{{geometry}}\n'.format(self.paper_size[0], self.paper_size[1]))
        self.write_command('usepackage', arg1='utf8', args=['inputenc'])
        self.open_environment('document')

    def write_text(self, text):
        self.file.write(text)

    def write_command(self, command, arg1=None, args=None):
        str_arg1 = '' if arg1 is None else '[{0}]'.format(str(arg1))
        str_args = '' if args is None else '}{'.join([str(arg) for arg in args])
        self.file.write('\\{0}{1}{{{2}}}'.format(command, str_arg1, str_args))

    def open_environment(self, environment):
        self.write_command('begin', args=[environment])
        self.environment_stack.append(environment)

    def close_last_environment(self):
        if self.is_opened():
            self.write_command('end', args=[self.environment_stack.pop()])

    def close(self):
        while self.is_opened():
            self.close_last_environment()

class Path:

    def __init__(self):
        self.str_path = ''

    def get_path(self):
        return self.str_path

    def line_to(self, x, y)



class Tikz:

    def __init__(self, document):
        self.document = document

    def open(self):
        self.document.open_environment('tikzpicture')

    def close(self):
        self.document.close_last_environment()

    def draw(self, points, params=None, closed=False):
        self.document.write_command('draw')
        self.document.write_text(self.form_points(points))
        self.document.write_text(';')

    def form_points(self, points):
