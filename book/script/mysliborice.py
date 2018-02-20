# -*- coding: utf-8 -*-

import schema.components as comp
from schema.components import get_component

# Řídící počítač
comp.PC(
    label = '-B10',
    ip = '192.168.1.90'
)

# Ethernet hub
comp.Component(
    label = '-B11'
)

# Čidlo pro měření teploty vody na výstupu z kotle
comp.PT100W4(
    label = '=KK-BTH'
)

# Čidlo pro měření teploty horké vody v přízemí
comp.PT100W4(
    label = '=HP-BTH'
)


# Převodník na proudovou smyčku pro PT100 =HP-BTH
comp.P5310(
    label = '-B3',
)

# Senzor teploty v obývacím pokoji v podkroví
comp.TQS3(
     label =  '+204-BT',
     spinel_address = 50,
)

# Senzor venkovní teploty
comp.TQS3(
    label = '+0-BT',
    spinel_address = 51
)

# Binární IO,
comp.Quido88(
    label = '-B1',
    spinel_address = 52
)

# Binární IO,
comp.Quido88(
    label = '-B2',
    spinel_address = 53
),

# AD převodník, vstup 0: teplota kotle, vstup 1: horká větev v přízemí
comp.AD4ETH(
    label = '-B3',
    spinel_address = 254,
    ip = '192.168.1.110'
)

# DA převodník pro směšovací ventil
comp.DA2RS(
    label = '-B4',
    spinel_address = 54
)

comp.GNOME485(
    label = '-B5',
    ip = '192.168.1.111'
)

comp.SENSYCON(
    label = '-B6'
)

comp.P5310(
    label = '-B7'
)

comp.Rele('-K1')
comp.Rele('-K2')
comp.Rele('-K3')
comp.Rele('-K4')
comp.Rele('-K5')
comp.Rele('-K6')
comp.Rele('-K7')
comp.Rele('-K8')
comp.Rele('-K9')

# Třífázový jistič
comp.Component('-FA1')

# Jednofázový jistič
comp.Component('-FA2')

# Skříňka napájení
comp.Component('=A1')

# Rozváděč řízení
comp.Component('=A2')

# Napájecí zdroj
comp.Component('-U1')

# Napájecí zdroj
comp.Component('-U2')

comp.TerminalBlock('+112=A1-X1')

comp.Wire('=KK-BTH:1', '+112=A1-X1:9')
comp.Wire('=KK-BTH:2', '+112=A1-X1:10')
comp.Wire('=KK-BTH:3', '+112=A1-X1:11')
comp.Wire('=KK-BTH:4', '+112=A1-X1:12')

comp.Wire('-B7:1', '+112=A1-X1:9')
comp.Wire('-B7:2', '+112=A1-X1:10')
comp.Wire('-B7:3', '+112=A1-X1:11')
comp.Wire('-B7:4', '+112=A1-X1:12')

comp.Wire('-B3:in1', '-B7:6')

# Obsah rozvadece A1

a1 = comp.Cabinet('=A1')

a1.content[0].put(get_component('-B1')) # Quido
a1.content[0].put(get_component('-B2')) # Quido

for i in range(9): # Vystupni rele K1-9
    a1.content[1].put(get_component('-K{}'.format(i+1)))

a1.content[1].put(get_component('-B7')) # P5310
a1.content[1].put(get_component('-B6')) # Sensycon
a1.content[1].put(get_component('-B5')) # Gnome 485
# x1
x1 = comp.TerminalBlock('=A1-X1')
for i in range(3):
    x1.append(comp.Terminal('=A1-X1:{}'.format(i+1)))
a1.content[2].put(x1)
# x2
x2 = comp.TerminalBlock('=A1-X2')
for i in range(10):
    x2.append(comp.Terminal('=A1-X2:{}'.format(i+1)))
a1.content[2].put(x2)
# X3
x3 = comp.TerminalBlock('=A1-X3')
for i in range(4):
    x3.append(comp.Terminal('=A1-X3:{}'.format(i+1)))
a1.content[2].put(x3)
a1.content[2].put(get_component('-B3'))  # AD4ETH
a1.content[2].put(get_component('-B4'))  # DA2RS
