# -*- coding: utf-8 -*-

import schema.latex_document as doc
from schema.frame import draw_frame
from schema.scheme import PAPERS
from schema.resistor import draw_resistor_base
import schema.resistor
import schema.elscheme
import schema.components

""" Analog input electrical scheme. """

with open('hm-ai.tex', mode='w', encoding='utf-8') as file:
    lat = doc.LatexDocument(file)
    lat.open()
    tikz = doc.Tikz(lat)
    tikz.open()
    sch = doc.Schema(tikz, PAPERS['A3L']['RAW_PAPER_SIZE'])
    draw_frame(sch, PAPERS['A3L'])
    schema.resistor.draw_grid(sch, 4)
    elsch = schema.elscheme.ElectroScheme(sch, None, None)
    elsch.draw_component(schema.components.PT100W4('aaa'), 'aaa')
    tikz.close()
    lat.close()
