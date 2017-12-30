# -*- coding: utf-8 -*-

import pathlib

ARCH_DIR = '/cygdrive/C/Users/jilm/Documents/heating-mysliborice/rec/arch/'
WORK_DIR = '/cygdrive/C/Users/jilm/Documents/heating-mysliborice/rec/work/'
ARCH_PATH = pathlib.Path(ARCH_DIR)
WORK_PATH = pathlib.Path(WORK_DIR)

ARCH_VARIABLES = [

    {
        'arch-id': 'outdoor-temp',
        'arch-file': 'outtemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius',
        'plot-title': 'Venkovní teplota'
    },

    {
        'arch-id': 'heater-temp',
        'arch-file': 'heattemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius',
        'plot-color': 'red'
    },

    {
        'arch-id': 'attic-temp',
        'arch-file': 'attictemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'attic-hot-leg-temp',
        'arch-file': 'atthltemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'heater-on-temp',
        'arch-file': 'heatontemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'overheating-temp',
        'arch-file': 'heatovertemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'attic-cold-leg-temp',
        'arch-file': 'attcltemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'attic-request-temp',
        'arch-file': 'attrtemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'gf-hot-leg-temp',
        'arch-file': 'gfhltemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'heater-ready-temp',
        'arch-file': 'heatreadytemp',
        'archive': True,
        'datatype': 'real',
        'unit': 'Celsius'
    },

    {
        'arch-id': 'v1',
        'arch-file': 'v1',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'v2',
        'arch-file': 'v2',
        'archive': False,
        'datatype': 'bool'
    },

    {
        'arch-id': 'v3',
        'arch-file': 'v3',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'v4',
        'arch-file': 'v4',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'v5',
        'arch-file': 'v5',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'v6',
        'arch-file': 'v6',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'c1',
        'arch-file': 'c1',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'c2',
        'arch-file': 'c2',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'c3',
        'arch-file': 'c3',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'heater-ready',
        'arch-file': 'heatready',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'attic-request-hp',
        'arch-file': 'attreqhp',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'gf-request',
        'arch-file': 'gfreq',
        'archive': True,
        'datatype': 'bool'
    },

    {
        'arch-id': 'regul',
        'arch-file': 'regul',
        'archive': True,
        'datatype': 'real',
        'limits': (0.0, 1.0),
        'unit': '-'
    }


]

def data_from_file(filename):
    with open(filename, 'r') as f:
        yield f.readline()

PLOTS = {

    'outdoor-temp': {

        'title': 'Venkovní teplota',
        'daq': lambda x: data_from_file('outdoor-temp')


    }
}