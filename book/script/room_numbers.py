# -*- coding: utf-8 -*-

import io

ROOM_NUMBERS = [

    ('+100', 'Celé přízemí.'),
    ('+101', 'Kuchyně.'),
    ('+102', 'Obývací pokoj.'),
    ('+103', 'Ložnice I.'),
    ('+104', 'Ložnice II.'),
    ('+105', 'Chodba.'),
    ('+106', 'Koupelna.'),
    ('+107', 'Záchod.'),
    ('+108', 'Prádelna.'),
    ('+109', 'Botník.'),
    ('+110', 'Zádveří.'),
    ('+111', 'Schodiště.'),
    ('+112', 'Garáž.'),
    ('+113', 'Venkovní prostor vstupních dveří.'),
    ('+114', 'Venkovní prostor směrem do zahrady.'),
    ('+200', 'Celé podkroví.'),
    ('+201', 'Ložnice I.'),
    ('+202', 'Ložnice II.'),
    ('+203', 'Kuchyň a jídelna.'),
    ('+204', 'Obývací pokoj.'),
    ('+205', 'Koupelna.'),
    ('+206', 'Schodiště.'),
    ('+207', 'Technická místnost.')

]

def write_table(head, content, caption = '', label = ''):
    return '\n'.join([
        '\\begin{table}[h]',
        '\\begin{tabular}',
        '\\centering',
        '\\\\\n'.join([' & '.join(row) for row in content]),
        '\\caption{{{}}}'.format(caption),
        '\\label{{{}}}'.format(label),
        '\\end{tabular}',
        '\\end{table}'
    ])

with io.open('build/room_numbers.tex', 'w', encoding="utf-8") as file:
    file.write(write_table(
        None,
        #ROOM_NUMBERS,
        [(ROOM_NUMBERS[i][0], ROOM_NUMBERS[i][1], ROOM_NUMBERS[i+1][0], ROOM_NUMBERS[i+1][1]) for i in range(0, len(ROOM_NUMBERS)-1, 2)],
        caption = 'Označení místností domu.',
        label = 'tab:room-numbers'
        )
    )