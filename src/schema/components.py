# -*- coding: utf-8 -*-

from schema.canvas import canvas
import schema.symbols as sym

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

    def __init__(self, label):
        self.label = label
        register(self)

class PT100(Component):

    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2')

    def __init__(self, label):
        super().__init__(label)

    def draw_symbol(self):
        canvas.draw_thermistor1()
        terminals['{}:1'.format(self.label)] = canvas.transform_point((19.0, 5.0))
        terminals['{}:2'.format(self.label)] = canvas.transform_point((19.0, -5.0))
        canvas.move((30.0, 0.0))

# four wire
class PT100W4(Component):

    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2', ':3', ':4')

    def __init__(self, label):
        super().__init__(label)

    def draw_symbol(self):
        sym.draw_thermistor()
        canvas.line(((10.0, 6.0), (10.0, 18.0), (19.0, 18.0)))
        canvas.line(((10.0, -6.0), (10.0, -18.0), (19.0, -18.0)))
        canvas.line(((10.0, 6.0), (16.0, 12.0), (19.0, 12.0)))
        canvas.line(((10.0, -6.0), (16.0, -12.0), (19.0, -12.0)))
        canvas.text(self.label, (10.0, 24.0), 'n')
        canvas.text(self.type, (10.0, -24.0), 's')
        terminals['{}:1'.format(self.label)] = canvas.transform_point((19.0, 18.0))
        terminals['{}:2'.format(self.label)] = canvas.transform_point((19.0, 12.0))
        canvas.move((30.0, 0.0))

class Terminal(Component):

    type = "PT100"
    short = "Thermistor"
    label_base = "BT"
    terminals = (':1', ':2', ':3', ':4')

    def __init__(self, label):
        super().__init__(label)

    def draw_symbol(self):
        canvas.circle((0.0, 0.0), 1.2)
        canvas.line(((-1.2, -1.2), (1.2, 1.2)))

class TerminalBlock(Component):

    type = 'Terminal Block'

    def __init__(self, label):
        super().__init__(label)

    def draw_symbol(self, part):
        canvas.circle((0.0, 0.0), 1.2)
        canvas.line(((-1.2, -1.2), (1.2, 1.2)))
        canvas.small_text(part, (-1.2, 0.0), 'nw')
        terminals['{}{}'.format(self.label, part)] = canvas.transform_point((1.2, 0.0))

class P5310(Component):

    type = 'P5310'
    manufacturer = 'JSP'
    short = 'Převodní teplota na proudovou smyčku.'
    temp_range = (0.0, 60.0)    # rozsah teplot [degC]
    out_range = (4e-3, 20e-3)   # rozsah výstupních proudů [A]
    terminals = (':1', ':2', ':3', ':4', ':5', ':6', ':7', ':8')
    dimensions = (17.0, 62.0, 63.0)  # rozmery [mm]

    def __init__(self, label):
        super().__init__(label)

    def draw_symbol(self):
        canvas.rect(0.0, -22.0, 18.0, 44.0)
        canvas.line(((0.0, -22.0), (18.0, 22.0)))
        canvas.large_text('R', (6.0, 10.6))
        canvas.large_text('I', (12.0, -10.6))
        canvas.small_text('1', (0.0, 18.0), 'nw')
        canvas.small_text('2', (0.0, 12.0), 'nw')
        canvas.small_text('3', (0.0, -12.0), 'nw')
        canvas.small_text('4', (0.0, -18.0), 'nw')
        canvas.small_text('5', (18.0, 6.0), 'ne')
        canvas.small_text('6', (18.0, -6.0), 'ne')
        #symbols.draw_RI_converter()
        terminals['{}:1'.format(self.label)] = canvas.transform_point((0.0, 18.0))
        terminals['{}:2'.format(self.label)] = canvas.transform_point((0.0, 12.0))
        terminals['{}:3'.format(self.label)] = canvas.transform_point((0.0, -12.0))
        terminals['{}:4'.format(self.label)] = canvas.transform_point((0.0, -18.0))
        terminals['{}:5'.format(self.label)] = canvas.transform_point((18.0, 6.0))
        terminals['{}:6'.format(self.label)] = canvas.transform_point((18.0, -6.0))

class TQS3(Component):

    type = 'TQS3'
    short = 'Teplotní senzor'

    def __init__(self, label, spinel_address = 256):
        super().__init__(label)
        self.spinel_address = spinel_address

class Quido88(Component):

    type = 'Quido 8/8'
    short = 'Binary IOs and temperature measurement'

    def __init__(self, label, spinel_address):
        super().__init__(label)
        self.spinel_address = spinel_address

    def draw_symbol(self, part):
        if part in ('o1', 'o2', 'o3', 'o4', 'o5', 'o6', 'o7', 'o8'):
            geometry = sym.draw_switch()
            canvas.small_text('no{}'.format(part[1]), geometry['pins']['no'][0], 'ne')
            canvas.small_text('nc{}'.format(part[1]), geometry['pins']['nc'][0], 'ne')
            canvas.small_text('c{}'.format(part[1]), geometry['pins']['comm'][0], 'nw')



class AD4ETH(Component):

    type = 'AD4ETH'
    short = 'AD converter with ethernet connection'

    def __init__(self, label, ip, spinel_address = 256):
        super().__init__(label)

    def draw_symbol(self):
        canvas.small_text(':in1', (0.0, 6.0), 'nw')
        canvas.small_text(':gnd', (0.0, -6.0), 'nw')
        sym.draw_AD_converter()
        terminals['{}:in1'.format(self.label)] = canvas.transform_point((0.0, 6.0))
        terminals['{}:gnd'.format(self.label)] = canvas.transform_point((0.0, -6.0))

class DA2RS(Component):

    type = 'DA2RS'
    short = 'DA converter with RS485'

    def __init__(self, label, spinel_address):
        super().__init__(label)
        self.spinel_address = spinel_address

class GNOME485(Component):

    type = 'GNOME'
    short = 'RS485 to ETHERNET'

    def __init__(self, label, ip):
        super().__init__(label)
        self.ip = ip

class SENSYCON(Component):

    type = 'SENSYCON'
    short = 'PT100 to current converter'
    temp_range = (0, 100)       # rozsah teplot [degC]
    out_range = (4e-3, 20e-3)   # rozsah výstupních proudů [A]

    def __init__(self, label):
        super().__init__(label)

class Rele(Component):

    type = 'Rele'
    short = 'Rele'

    def __init__(self, label):
        super().__init__(label)

    def draw_symbol(self):
        geometry = sym.draw_rele1()

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

def draw_connections():
    for c in connections:
        if c.a in terminals.keys() and c.b in terminals.keys():
            canvas.w_line((terminals[c.a], terminals[c.b]))

def begin_line():
    canvas.move((0.0, -20.0))
