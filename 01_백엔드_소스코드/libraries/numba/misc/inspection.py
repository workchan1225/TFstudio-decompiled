# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: inspection.pyc (Python 3.11)

'''Miscellaneous inspection tools
'''
from tempfile import NamedTemporaryFile, TemporaryDirectory
import os
import warnings
from numba.core.errors import NumbaWarning

def disassemble_elf_to_cfg(elf, mangled_symbol):
    '''
    Gets the CFG of the disassembly of an ELF object, elf, at mangled name,
    mangled_symbol, and renders it appropriately depending on the execution
    environment (terminal/notebook).
    '''
    pass
# WARNING: Decompyle incomplete
