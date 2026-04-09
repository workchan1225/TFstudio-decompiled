# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decorators.pyc (Python 3.11)

import re
import warnings
from numba.core import typing, sigutils
from numba.pycc.compiler import ExportEntry
export_registry = []

def export(prototype):
    pass
# WARNING: Decompyle incomplete


def exportmany(prototypes):
    pass
# WARNING: Decompyle incomplete


def process_input_files(inputs):
    '''
    Read input source files for execution of legacy @export / @exportmany
    decorators.
    '''
    for ifile in inputs:
        fin = open(ifile)
        exec(compile(fin.read(), ifile, 'exec'))
        None(None, None)
    with None:
        if not None:
            pass
    continue


def clear_export_registry():
    export_registry[:] = []

re_symbol = re.compile('[_a-z][_a-z0-9]*', re.I)

def parse_prototype(text):
    '''Separate the symbol and function-type in a a string with
    "symbol function-type" (e.g. "mult float(float, float)")

    Returns
    ---------
    (symbol_string, functype_string)
    '''
    m = re_symbol.match(text)
    if not m:
        raise ValueError('Invalid function name for export prototype')
    s = m.start(0)
    e = m.end(0)
    symbol = text[s:e]
    functype = text[e + 1:]
    return (symbol, functype)
