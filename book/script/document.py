# -*- coding: utf-8 -*-

#import plus_204_TK
#import plus_000_TK
#import eq_OT2_TK_H
#import eq_OT1_TK_H
from schema.components import TQS3
from schema.components import PT100W4
from schema.components import Quido88
from schema.components import AD4ETH
from schema.components import DA2RS
from schema.components import GNOME485
from schema.components import SENSYCON
from schema.components import P5310
from schema.components import Rele
from schema.components import Component

def real_to_latex(prefix, number, exponent, unit):
    return '${}{}\\:\\rm {}$'.format(prefix, round(number / 10**exponent) * 10**exponent, unit)


objects = {
    '+204-TK': TQS3(),      # senzor teploty v podkroví
    '+000-TK': TQS3(),      # senzor venkovní teploty
    '=KK-TK': PT100W4(''),    # senzor teploty horké vody na výstupu z krbových kamen
    '-B1': Quido88(),
    '-B2': Quido88(),
    '-B3': AD4ETH('-B3',    # AD prevodnik
        spinel_address = 254,
        ip = '192.168.1.110'
    ),
    # DA převodník pro směšovací ventil
    '-B4': DA2RS(
        label = '-B4',
        spinel_address = 54
    ),
    '-B5': GNOME485(
        label = '-B5',
        ip = '192.168.1.111'
    ),
    '-B6': SENSYCON(
        label = '-B6'
    ),
    '-B7': P5310(
        label = '-B7'
    ),
    '-K1': Rele(''),
    '-K2': Rele(''),
    '-K3': Rele(''),
    '-K4': Rele(''),
    '-K5': Rele(''),
    '-K6': Rele(''),
    '-K7': Rele(''),
    '-K8': Rele(''),
    '-K9': Rele(''),
    # Třífázový jistič
    '-FA1': Component('-FA1'),
    # Jednofázový jistič
    '-FA2': Component('-FA2'),
    # Skříňka napájení
    '=A1': Component('=A1'),
    # Rozváděč řízení
    '=A2': Component('=A2'),
    # Napájecí zdroj
    '-U1': Component('-U1'),
    # Napájecí zdroj
    '-U2': Component('-U2'),

}

# popis teplotních měření

#documents = [
#    plus_000_TK.DOCUMENT,
#    plus_204_TK.DOCUMENT,
#    eq_OT2_TK_H.DOCUMENT,
#    eq_OT1_TK_H.DOCUMENT
#]

#desc = '\\par{}'.join(doc['desc'] for doc in documents if 'desc' in doc)

# napájení 12V DC

powered_components = ['+204-TK', '+000-TK', '-B1', '-B2', '-B3', '-B4', '-B5', '-B6', '-B7', '-K1', '-K2', '-K3', '-K4', '-K5', '-K6', '-K7', '-K8', '-K9']
# Soucet pres vsechny komponenty
for key in powered_components:
    objects[key].power_supply_u = 12.0
# Tabulka prikonu jednotlivych komponent
#print('\\\\\n'.join([' & '.join((key, objects[key].type, real_to_latex('', objects[key].get_power()*1000, 1, 'mW'))) for key in powered_components]))
#print(sum(objects[key].get_power() for key in powered_components))


# položkový seznam prvků
#print('\\\\\n'.join([' & '.join((key, objects[key].type)) for key in objects]))

#component_tab = '\\\\\n'.join(
#    ' & '.join((comp.label, comp.type, doc['short']))
#    for doc in documents if 'components' in doc for comp in doc['components'])

#print(desc)
#print(component_tab)