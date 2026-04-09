# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dis.pyc (Python 3.11)

'''Disassembler of Python byte code into mnemonics.'''
import sys
import types
import collections
import io
from opcode import *
from opcode import __all__ as _opcodes_all, _cache_format, _inline_cache_entries, _nb_ops, _specializations, _specialized_instructions
__all__ = [
    'code_info',
    'dis',
    'disassemble',
    'distb',
    'disco',
    'findlinestarts',
    'findlabels',
    'show_code',
    'get_instructions',
    'Instruction',
    'Bytecode'] + _opcodes_all
del _opcodes_all
_have_code = (types.MethodType, types.FunctionType, types.CodeType, classmethod, staticmethod, type)
FORMAT_VALUE = opmap['FORMAT_VALUE']
FORMAT_VALUE_CONVERTERS = ((None, ''), (str, 'str'), (repr, 'repr'), (ascii, 'ascii'))
MAKE_FUNCTION = opmap['MAKE_FUNCTION']
MAKE_FUNCTION_FLAGS = ('defaults', 'kwdefaults', 'annotations', 'closure')
LOAD_CONST = opmap['LOAD_CONST']
LOAD_GLOBAL = opmap['LOAD_GLOBAL']
BINARY_OP = opmap['BINARY_OP']
JUMP_BACKWARD = opmap['JUMP_BACKWARD']
CACHE = opmap['CACHE']
_all_opname = list(opname)
_all_opmap = dict(opmap)
_empty_slot = enumerate(_all_opname)()
for spec_op, specialized in zip(_empty_slot, _specialized_instructions):
    _all_opname[spec_op] = specialized
    _all_opmap[specialized] = spec_op
    deoptmap = _specializations.items()()
    
    def _try_compile(source, name):
        '''Attempts to compile the given source, first as an expression and
       then as a statement if the first approach fails.

       Utility function to accept strings in functions that otherwise
       expect code objects
    '''
        
        try:
            c = compile(source, name, 'eval')
        except SyntaxError:
            c = compile(source, name, 'exec')

        return c

    
    def dis(x = (lambda .0: pass# WARNING: Decompyle incomplete
), *, file, depth, show_caches, adaptive):
        '''Disassemble classes, methods, functions, and other compiled objects.

    With no argument, disassemble the last traceback.

    Compiled objects currently include generator objects, async generator
    objects, and coroutine objects, all of which store their code object
    in a special attribute.
    '''
        pass
    # WARNING: Decompyle incomplete

    
    def distb(tb = (lambda .0: pass# WARNING: Decompyle incomplete
), *, file, show_caches, adaptive):
        '''Disassemble a traceback (default: last traceback).'''
        pass
    # WARNING: Decompyle incomplete

    COMPILER_FLAG_NAMES = {
        1: 'OPTIMIZED',
        2: 'NEWLOCALS',
        4: 'VARARGS',
        8: 'VARKEYWORDS',
        16: 'NESTED',
        32: 'GENERATOR',
        64: 'NOFREE',
        128: 'COROUTINE',
        256: 'ITERABLE_COROUTINE',
        512: 'ASYNC_GENERATOR' }
    
    def pretty_flags(flags):
