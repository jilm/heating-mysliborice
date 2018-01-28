# -*- coding: utf-8 -*-

from schema.vector import I
from schema.canvas import Canvas, Line, Circle, Square

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
    """Common predecessor for each component. Label of each component must
    be uniqe acros the project."""

    type = 'Component'
    short = 'Komponenta systému topení.'

    def __init__(self, label):
        self.label = label
        register(self)

    def get_terminals(self):
        return ()

    def get(self, key):
        return None


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


class Terminal(Component):

    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2', ':3', ':4')

    def __init__(self, label):
        super().__init__(label)

class TerminalBlock(Component):

    type = 'Terminal Block'

    def __init__(self, label):
        super().__init__(label)


class P5310(Component):

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

class TempMeasurement:

    def __init__(self, termistor, converter):
        self.termistor = termistor
        self.converter = converter

class TQS3:

    type = 'TQS3'
    short = 'Teplotní senzor'
    power_supply_u = (10.0, 30.0)         # povolene napajeci napeti
    power_supply_i = (2.0e-3, 3.0e-3)     # max odber ze zdroje

    def __init__(self):
        pass

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

class Quido88(Component):

    type = 'Quido 8/8'
    short = 'Binary IOs and temperature measurement'
    allow_power_supply_u = (8.0, 30.0)
    power_supply_i = (0.041, 0.283)

    def __init__(self):
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

class AD4ETH(Component):

    type = 'AD4ETH'
    short = 'AD converter with ethernet connection'
    channels = 4
    power_supply_u = (8.0, 30.0)
    power_supply_i = 170.0e-3
    size = (104.0e-3, 55.0e-3, 24.0e-3)
    input_range = (4.0e-3, 20.0e-3)

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


class DA2RS(Component):

    type = 'DA2RS'
    short = 'DA converter with RS485'
    channels = 2
    power_supply_u = (8.0, 30.0)
    power_supply_i = 90.0e-3

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

class GNOME485(Component):

    type = 'GNOME'
    short = 'RS485 to ETHERNET'
    power_supply_u = (9.0, 18.0)
    power_supply_i = 80.0e-3

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

class SENSYCON(Component):

    type = 'SENSYCON'
    short = 'PT100 to current converter'
    temp_range = (0, 100)       # rozsah teplot [degC]
    out_range = (4e-3, 20e-3)   # rozsah výstupních proudů [A]
    power_supply_u = 12.0
    power_supply_i = 20.0e-3

    def __init__(self, label):
        super().__init__(label)

    def get_power(self):
        return self.power_supply_u * self.power_supply_i


class Rele(Component):

    type = 'Rele'
    short = 'Rele'

    def __init__(self, label):
        super().__init__(label)

    def get_power(self):
        return 12.0 * 12.0 / 220.0

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
            Line([
                (0.0, 0.0),
                (EQ_TRIANGLE_H, 0.5
                .6+33333333333333
                ),
                (EQ_TRIANGLE_H, -0.5),
                (-EQ_TRIANGLE_H, 0.5),
                (-EQ_TRIANGLE_H, -0.5),
                (0.0, 0.0)
            ], t).write(canvas)
            Line([(EQ_TRIANGLE_H, 0), (EQ_TRIANGLE_H, 1.0)], t).write(canvas)
            Line([(-EQ_TRIANGLE_H, 0), (EQ_TRIANGLE_H, -1.0)], t).write(canvas)
        return t.r_move(-0.5, 0.0), t.r_move(0.5, 0.0)

