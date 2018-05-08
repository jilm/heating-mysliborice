# -*- coding: utf-8 -*-

import schema.latex_document as doc
from schema.frame import draw_frame
import schema.frame
from schema.scheme import PAPERS
import schema.scheme
from schema.resistor import draw_resistor_base
import schema.converter
import schema.resistor
import schema.elscheme
import schema.components

""" Analog input electrical scheme. """

with open('hm-ai.tex', mode='w', encoding='utf-8') as file:
    lat = doc.LatexDocument(file, PAPERS['A3L']['RAW_PAPER_SIZE'])
    lat.open()
    tikz = lat.begin_tikz()
    canvas = tikz.move()
    #tikz.open()
    canvas = draw_frame(canvas, PAPERS['A3L'])
    schema.frame.draw_description_field(
        canvas,
        description={
            'number' : 'HM-AI'
        }
    )
    canvas = schema.scheme.clip_margins(canvas, left=10.0, top=10.0, right=20.0, bottom=100.0)
    #sch = doc.Schema(tikz, PAPERS['A3L']['RAW_PAPER_SIZE'])
    #schema.resistor.draw_grid(sch, 4)
    elsch = schema.elscheme.ElectroScheme(canvas, None, None)
    elsch.draw_component(schema.components.PT100W4('aaa'), 'aaa')
    elsch.draw_h_mwire((-3,-2,2,3), (-2, -1, 1, 2))
    elsch.step(4*5, 0)
    elsch.draw_component(schema.components.P5310('bbb'), 'bbb')

    tikz.close()
    lat.close()
