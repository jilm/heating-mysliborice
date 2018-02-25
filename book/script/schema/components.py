# -*- coding: utf-8 -*-

from schema.vector import I
from schema.canvas import Canvas, Line, Circle, Square, Path
from schema.scheme import Scheme
import itertools
from schema.symbols import EQ_TRIANGLE_H


"""   Třídy použitých komponent. """


components = {}
terminals = {}
connections = list()

def register(component):
    components[component.label] = component

def get_component(label):
    return components[label]

def register_connection(connection):
    connections.append(connection)


class Gate:
    pass


class ResistorGate(Gate):
    pass


class Component:

    """ Common predecessor for each component. Label of each component must
    be uniqe acros the project. """

    type = 'Component'
    short = 'Komponenta systému topení.'

    def __init__(self, label):
        self.label = label
        register(self)

    def get_terminals(self):
        return ()

    def get(self, key):
        return None

class DINAssembly:

    """ Base class for components that are dedicated to DIN assembly. """

    dimensions = (0.0, 0.0, 0.0)

    def get_dimensions(self):
        return self.dimensions

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.get_dimensions())

class PT100(Component):

    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2')
    kind = 'thermistor'

    def __init__(self, label):
        super().__init__(label)


class PT100W4(Component):

    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2', ':3', ':4')
    kind = 'thermistor'

    def __init__(self, label):
        super().__init__(label)


class Terminal(Component, DINAssembly):

    """ Jedna svorka. """

    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2', ':3', ':4')
    dimensions = (5.1, 60.0, 46.5)

    def __init__(self, label):
        super().__init__(label)


class TerminalBlock(Component, DINAssembly):

    """ Svorkovnice. """

    type = 'Terminal Block'

    def __init__(self, label):
        super().__init__(label)
        self.content = list()

    def append(self, terminal):
        self.content.append(terminal)

    def get_dimensions(self):
        return (
            sum([c.get_dimensions()[0] for c in self.content]),
            max([c.get_dimensions()[1] for c in self.content]),
            max([c.get_dimensions()[2] for c in self.content])
        )


class P5310(Component, DINAssembly):

    type = 'P5310'
    manufacturer = 'JSP'
    short = 'Převodník teploty na proudovou smyčku.'
    temp_range = (0.0, 60.0)    # rozsah teplot [degC]
    out_range = (4e-3, 20e-3)   # rozsah výstupních proudů [A]
    terminals = (':1', ':2', ':3', ':4', ':5', ':6', ':7', ':8')
    dimensions = (17.0, 62.0, 63.0)  # rozmery [mm]
    power_supply_u = 12.0
    power_supply_i = 20.0e-3

    def __init__(self, label):
        super().__init__(label)

    def write_block_symbol(self):
        pass

    def write_schema_symbol(self):
        pass

    def write_front_view(self):
        pass

    def get_power(self):
        return self.power_supply_u * self.power_supply_i

    def draw_face_view(self, scheme):
        scheme.draw_rect((12.4, 62))
        Line(
            ((6.2, 24.26), (8.5, 24.26), (8.5, -24.26), (6.2, -24.26)),
            scheme.t
        ).write(scheme.canvas)
        Line(
            ((-6.2, 24.26), (-8.5, 24.26), (-8.5, -24.26), (-6.2, -24.26)),
            scheme.t
        ).write(scheme.canvas)
        Line(((-6.2, 18.38), (6.2, 18.38)), scheme.t).write(scheme.canvas)
        Line(((-6.2, -18.38), (6.2, -18.38)), scheme.t).write(scheme.canvas)
        scheme.draw_rect((10.85, 35.28), 'TINY')
        scheme.draw_circle(2.325, cx=-2.7125, cy=31.0-2.725)
        scheme.draw_circle(2.325, cx=2.7125, cy=31.0-2.725)
        scheme.draw_circle(2.325, cx=-2.7125, cy=-31.0+2.725)
        scheme.draw_circle(2.325, cx=2.7125, cy=-31.0+2.725)

class TempMeasurement:

    def __init__(self, termistor, converter):
        self.termistor = termistor
        self.converter = converter

class TQS3(Component):

    type = 'TQS3'
    short = 'Teplotní senzor'
    power_supply_u = (10.0, 30.0)         # povolene napajeci napeti
    power_supply_i = (2.0e-3, 3.0e-3)     # max odber ze zdroje

    def __init__(self, label, spinel_address):
        super().__init__(label)

    def get_power(self):
        try:
            u = max(self.power_supply_u)
        except:
            u = self.power_supply_u
        try:
            i = max(self.power_supply_i)
        except:
            i = self.power_supply_i
        return u * i

    def write_power_supply_symbol(self, canvas = None, t = I, label = ''):
        if canvas is not None:
            Square(t.r_scale(2.0, 1.0)).write(canvas)
            canvas.text(self.type, t.transform_point((0.0, -0.5)), 's')
            canvas.text(label, t.transform_point((0.0, 0.5)), 'n')
            canvas.text('+', t.transform_point((-1.0, 0.0)), 'nw', 'small')
            canvas.text('-', t.transform_point((1.0, 0.0)), 'ne', 'small')
        return t.r_move(-1.0, 0.0), t.r_move(1.0, 0.0)

class Quido88(Component, DINAssembly):

    type = 'Quido 8/8'
    short = 'Binary IOs and temperature measurement'
    allow_power_supply_u = (8.0, 30.0)
    power_supply_i = (0.041, 0.283)
    dimensions = (137.4, 96.5, 20)

    def __init__(self, label, spinel_address):
        super().__init__(label)
        self.power_supply_u = self.allow_power_supply_u[1]

    def get_power(self):
        return self.power_supply_u * self.power_supply_i[1]

    def write_power_supply_symbol(self, canvas = None, t = I, label = ''):
        if canvas is not None:
            Square(t.r_scale(2.0, 1.0)).write(canvas)
            canvas.text(self.type, t.transform_point((0.0, -0.5)), 's')
            canvas.text(label, t.transform_point((0.0, 0.5)), 'n')
            canvas.text('PWR', t.transform_point((-1.0, 0.0)), 'nw', 'small')
            canvas.text('GND', t.transform_point((1.0, 0.0)), 'ne', 'small')
        return t.r_move(-1.0, 0.0), t.r_move(1.0, 0.0)

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)
        #scheme.draw_circl/e(3.2, (64.45, 40.0))
        #scheme.draw_circle(3.2, (-64.45, 40.0))
        #scheme.draw_circle(3.2, (64.45, -40.0))
        #scheme.draw_circle(3.2, (-64.45, -40.0))


class AD4ETH(Component, DINAssembly):

    type = 'AD4ETH'
    short = 'AD converter with ethernet connection'
    channels = 4
    power_supply_u = (8.0, 30.0)
    power_supply_i = 170.0e-3
    size = (104.0e-3, 55.0e-3, 24.0e-3)
    input_range = (4.0e-3, 20.0e-3)
    dimensions = (55.0 ,104.0 , 24.0)

    def __init__(self, label, ip, spinel_address=256):
        super().__init__(label)

    def get_power(self):
        return self.power_supply_u * self.power_supply_i

    def write_power_supply_symbol(self, canvas = None, t = I, label = ''):
        if canvas is not None:
            Square(t.r_scale(2.0, 1.0)).write(canvas)
            canvas.text(self.type, t.transform_point((0.0, -0.5)), 's')
            canvas.text(label, t.transform_point((0.0, 0.5)), 'n')
            canvas.text('+', t.transform_point((-1.0, 0.0)), 'nw', 'small')
            canvas.text('-', t.transform_point((1.0, 0.0)), 'ne', 'small')
        return t.r_move(-1.0, 0.0), t.r_move(1.0, 0.0)


class DA2RS(Component, DINAssembly):

    type = 'DA2RS'
    short = 'DA converter with RS485'
    channels = 2
    power_supply_u = (8.0, 30.0)
    power_supply_i = 90.0e-3
    dimensions = (55.0 ,104.0 , 24.0)

    def __init__(self, label, spinel_address):
        super().__init__(label)
        self.spinel_address = spinel_address

    def get_power(self):
        return self.power_supply_u * self.power_supply_i

    def write_power_supply_symbol(self, canvas = None, t = I, label = ''):
        if canvas is not None:
            Square(t.r_scale(2.0, 1.0)).write(canvas)
            canvas.text(self.type, t.transform_point((0.0, -0.5)), 's')
            canvas.text(label, t.transform_point((0.0, 0.5)), 'n')
            canvas.text('PWR', t.transform_point((-1.0, 0.0)), 'nw', 'small')
            canvas.text('GND', t.transform_point((1.0, 0.0)), 'ne', 'small')
        return t.r_move(-1.0, 0.0), t.r_move(1.0, 0.0)

class GNOME485(Component, DINAssembly):

    type = 'GNOME'
    short = 'RS485 to ETHERNET'
    power_supply_u = (9.0, 18.0)
    power_supply_i = 80.0e-3
    dimensions = (42.0, 57.0, 25.0)

    def __init__(self, label, ip):
        super().__init__(label)
        self.ip = ip

    def get_power(self):
        return self.power_supply_u * self.power_supply_i

    def write_power_supply_symbol(self, canvas = None, t = I, label = ''):
        if canvas is not None:
            Square(t.r_scale(2.0, 1.0)).write(canvas)
            canvas.text(self.type, t.transform_point((0.0, -0.5)), 's')
            canvas.text(label, t.transform_point((0.0, 0.5)), 'n')
            canvas.text('PWR', t.transform_point((-1.0, 0.0)), 'nw', 'small')
            canvas.text('GND', t.transform_point((1.0, 0.0)), 'ne', 'small')
        return t.r_move(-1.0, 0.0), t.r_move(1.0, 0.0)

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)

class SENSYCON(Component, DINAssembly):

    type = 'SENSYCON'
    short = 'PT100 to current converter'
    temp_range = (0, 100)       # rozsah teplot [degC]
    out_range = (4e-3, 20e-3)   # rozsah výstupních proudů [A]
    power_supply_u = 12.0
    power_supply_i = 20.0e-3
    dimensions = (17.0, 62.0, 63.0)  # rozmery [mm]


    def __init__(self, label):
        super().__init__(label)

    def get_power(self):
        return self.power_supply_u * self.power_supply_i


class Rele(Component, DINAssembly):

    type = 'Finder4031'
    short = 'Rele'
    dimensions = (15.8, 78.6, 82.0)

    def __init__(self, label):
        super().__init__(label)

    def get_power(self):
        return 12.0 * 12.0 / 220.0

    def draw_face_view(self, scheme):
        scheme.draw_rect(self.dimensions)
        scheme.draw_rect((12.4, 29.0),'TINY')



class PC(Component):

    type = 'PC'
    short = 'PC'

    def __init__(self, label, ip):
        super().__init__(label)
        self.ip = ip


class Wire:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        register_connection(self)

class Valve(Component):

    type = 'Valve'
    short = 'Valve'

    def write_schema_symbol(self, canvas = None, t = I):
        if canvas is not None:
            Line([(EQ_TRIANGLE_H, 0), (EQ_TRIANGLE_H, 1.0)], t).write(canvas)
            Line([(-EQ_TRIANGLE_H, 0), (EQ_TRIANGLE_H, -1.0)], t).write(canvas)
        return t.r_move(-0.5, 0.0), t.r_move(0.5, 0.0)

class Glue(DINAssembly):
    pass

class CabinetPosition:

    """ Jedna pozice uvnitr rozvadece, jedna DIN lista. """

    def __init__(self, n_modules):
        """ Parametr n_modules je celociselna hodnota, kolik komponent,
        s modulovou sirkou se da osadit na tuto DIN listu. """
        self.n_modules = n_modules
        self.content = list()

    def draw_face_view(self, scheme):
        """ Draw dhe face view into the given schema. The center of the
        drawing will be placed into the center of the coordinates system.
        """
        # draw the axis
        width = self.n_modules * Cabinet.MODULE_WIDTH
        scheme.draw_hline(-0.5 * width - 2*Cabinet.MODULE_WIDTH, 0.0, width + 4*Cabinet.MODULE_WIDTH, style='axis')
        # find the size of the whole drawing
        height = max([c.get_dimensions()[1] for c in self.content])
        occupied_width = sum([c.get_dimensions()[0] for c in self.content])
        n_glue = len([c for c in self.content if isinstance(c, Glue)])
        scheme.push()
        max_height = max([c.get_dimensions()[1] for c in self.content])
        scheme.move(-0.5 * width, 0.0)
        for c in self.content:
            if isinstance(c, Glue):
                scheme.move((width - occupied_width) / n_glue, 0.0)
            else:
                scheme.move(0.5 * c.get_dimensions()[0], 0.0)
                c.draw_face_view(scheme)
                # draw the label
                scheme.canvas.text(c.label, scheme.t.transform_point((0, 0.5 *
                height)), position = 'n')
                scheme.move(0.5 * c.get_dimensions()[0], 0.0)
        scheme.pop()

    def put(self, module):
        """ Přidá jedenu komponentu. """
        self.content.append(module)


class Cabinet(Component):

    """ Jeden rozváděč, který může dále obsahovat více pozic s DIN lištou. """

    dimensions = (360.0, 540.0)
    n_positions = 3
    n_modules = (16, 16, 16)
    MODULE_WIDTH = 17.5 # mm
    VERTICAL_CONTENT_DISTANCE = 150.0 # mm
    content_y = (120.0, 270.0, 420.0)

    def __init__(self, label):
        super().__init__(label)
        self.content = list([CabinetPosition(n) for n in self.n_modules])

    def draw_face_view(self, scheme):
        # outer frame of the cabinet
        scheme.draw_rect(self.dimensions)
        x, y = [0.5 * d - 4.0 for d in self.dimensions]
        path = Path(
            [
                ('M', x-36.0, y), ('L', -x+36.0, y),
                ('L', -x+36.0, y-13.0), ('A', 0.0, -90.0, 10.0),
                ('L', -x, y-23.0), ('L', -x, -y+23.0),
                ('L', -x+26.0, -y+23.0), ('A', 90.0, 0.0, 10.0),
                ('L', -x+36.0, -y), ('L', x-36.0, -y),
                ('L', x-36.0, -y+13.0), ('A', 180.0, 90.0, 10.0),
                ('L', x, -y+23.0), ('L', x, y-23.0),
                ('L', x-26.0, y-23.0), ('A', 270.0, 180.0, 10.0)
            ]
        )
        path.transform(scheme.t)
        path.write(scheme.canvas)
        # draw dimensions
        x, y = (0.5 * d for d in self.dimensions)
        scheme.draw_hdimension(((-x, y), (x, y)), y + 10)
        scheme.draw_vdimension(((-x, y), (-x, -y)), -x - 20)
        scheme.draw_vdimension(
            [(-x, -cy+y) for cy in itertools.chain((0, ), self.content_y)],
            -x - 10
        )
        # draw content of the cabinet
        scheme.push()
        scheme.move(0.0, (self.n_positions-1) * self.VERTICAL_CONTENT_DISTANCE * 0.5)
        for p in self.content:
            p.draw_face_view(scheme)
            scheme.move(0.0, -self.VERTICAL_CONTENT_DISTANCE)
        scheme.pop()
