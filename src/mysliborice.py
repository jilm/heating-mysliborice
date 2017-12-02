# -*- coding: utf-8 -*-

import components as comp
import canvas

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

comp.Wire('=KK-BTH:1', '-B7:1')
comp.Wire('=KK-BTH:2', '-B7:4')

comp.components['=KK-BTH'].draw_symbol()
canvas.canvas.move((0.0, 12.0))
comp.Terminal(':1').draw_symbol()
canvas.canvas.text(':10', (-1.2, 0.0), 'nw')
canvas.canvas.move((0.0, 6.0))
comp.Terminal(':1').draw_symbol()
canvas.canvas.text(':9', (-1.2, 0.0), 'nw')
canvas.canvas.move((0.0, -30.0))
comp.Terminal(':1').draw_symbol()
canvas.canvas.text(':11', (-1.2, 0.0), 'nw')
canvas.canvas.move((0.0, -6.0))
comp.Terminal(':1').draw_symbol()
canvas.canvas.text(':12', (-1.2, 0.0), 'nw')
canvas.canvas.move((0.0, 18.0))
canvas.canvas.move((20.0, 0.0))
comp.components['-B7'].draw_symbol()
canvas.canvas.move((40.0, 0.0))
comp.components['-B3'].draw_symbol()
comp.begin_line()


comp.draw_connections()

