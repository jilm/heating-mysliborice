# -*- coding: utf-8 -*-

import canvas

components = {}
terminals = {}
connections = list()

def register(component):
    components[component.label] = component

def register_connection(connection):
    connections.append(connection)

class Gate:
    pass

class ResistorGate(Gate):
    pass

class Component:

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
        canvas.draw_thermistor()
        terminals['{}:1'.format(self.label)] = (10.0, 9.0)
        terminals['{}:2'.format(self.label)] = (10.0, -9.0)

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
        canvas.draw_RI_converter()
        terminals['{}:1'.format(self.label)] = (0.0, 2.0)
        terminals['{}:4'.format(self.label)] = (0.0, -2.0)

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

class AD4ETH(Component):

    type = 'AD4ETH'
    short = 'AD converter with ethernet connection'

    def __init__(self, label, ip, spinel_address = 256):
        super().__init__(label)

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
            canvas.canvas.line((terminals[c.a], terminals[c.b]))

