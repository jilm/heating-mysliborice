# -*- coding: utf-8 -*-

import io
from document import objects

def write_table(head, content, caption = '', label = ''):
    return '\n'.join([
        '\\begin{table}[h]',
        '\\centering',
        '\\begin{tabular}{r|l}',
        '\\\\\n'.join([' & '.join(row) for row in content]),
        '\\end{tabular}',
        '\\caption{{{}}}'.format(caption),
        '\\label{{{}}}'.format(label),
        '\\end{table}'
    ])

with io.open('build/component_list.tex', 'w', encoding="utf-8") as file:
    file.write(write_table(
        None,
        [(key, '({}) {}'.format(objects[key].type, objects[key].short)) for key in objects],
        caption = 'Výčet použitých komponent.',
        label = 'tab:component-list'
        )
    )