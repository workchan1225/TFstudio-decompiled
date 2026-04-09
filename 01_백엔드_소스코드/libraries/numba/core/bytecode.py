# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bytecode.pyc (Python 3.11)

import sys
from collections import namedtuple, OrderedDict
import dis
import inspect
import itertools
from types import CodeType, ModuleType
from numba.core import errors, utils, serialize
from numba.core.utils import PYVERSION
if PYVERSION in ((3, 12), (3, 13), (3, 14)):
    from opcode import _inline_cache_entries
    INSTR_LEN = 2
elif PYVERSION in ((3, 10), (3, 11)):
    pass
else:
    raise NotImplementedError(PYVERSION)
opcode_info = namedtuple('opcode_info', [
    'argsize'])
_ExceptionTableEntry = namedtuple('_ExceptionTableEntry', 'start end target depth lasti')
_FIXED_OFFSET = 2

def get_function_object(obj):
    '''
    Objects that wraps function should provide a "__numba__" magic attribute
    that contains a name of an attribute that contains the actual python
    function object.
    '''
    attr = getattr(obj, '__numba__', None)
    if attr:
        return getattr(obj, attr)


def get_code_object(obj):
    '''Shamelessly borrowed from llpython'''
    return getattr(obj, '__code__', getattr(obj, 'func_code', None))


def _as_opcodes(seq):
    lst = []
# WARNING: Decompyle incomplete

JREL_OPS = frozenset(dis.hasjrel)
JABS_OPS = frozenset(dis.hasjabs)
JUMP_OPS = JREL_OPS | JABS_OPS
TERM_OPS = frozenset(_as_opcodes([
    'RETURN_VALUE',
    'RAISE_VARARGS']))
EXTENDED_ARG = dis.EXTENDED_ARG
HAVE_ARGUMENT = dis.HAVE_ARGUMENT

class ByteCodeInst(object):
    '''
    Attributes
    ----------
    - offset:
        byte offset of opcode
    - opcode:
        opcode integer value
    - arg:
        instruction arg
    - lineno:
        -1 means unknown
    '''
    __slots__ = ('offset', 'next', 'opcode', 'opname', 'arg', 'lineno')
    
    def __init__(self, offset, opcode, arg, nextoffset):
        self.offset = offset
        self.next = nextoffset
        self.opcode = opcode
        self.opname = dis.opname[opcode]
        self.arg = arg
        self.lineno = -1

    is_jump = (lambda self: self.opcode in JUMP_OPS)()
    is_terminator = (lambda self: self.opcode in TERM_OPS)()
    
    def get_jump_target(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '%s(arg=%s, lineno=%d)' % (self.opname, self.arg, self.lineno)

    block_effect = (lambda self: if self.opname.startswith('SETUP_'):
1if None.opname == 'POP_BLOCK':
-1)()

CODE_LEN = 1
ARG_LEN = 1
NO_ARG_LEN = 1
OPCODE_NOP = dis.opname.index('NOP')
if PYVERSION in ((3, 13), (3, 14)):
    
    def _unpack_opargs(code):
        pass
    # WARNING: Decompyle incomplete

elif PYVERSION in ((3, 10), (3, 11), (3, 12)):
    
    def _unpack_opargs(code):
        '''
        Returns a 4-int-tuple of
        (bytecode offset, opcode, argument, offset of next bytecode).
        '''
        pass
    # WARNING: Decompyle incomplete

else:
    raise NotImplementedError(PYVERSION)

def _patched_opargs(bc_stream):
    '''Patch the bytecode stream.

    - Adds a NOP bytecode at the start to avoid jump target being at the entry.
    '''
    pass
# WARNING: Decompyle incomplete


class ByteCodeIter(object):
    
    def __init__(self, code):
        self.code = code
        self.iter = iter(_patched_opargs(_unpack_opargs(self.code.co_code)))

    
    def __iter__(self):
        return self

    
    def _fetch_opcode(self):
        return next(self.iter)

    
    def next(self):
        (offset, opcode, arg, nextoffset) = self._fetch_opcode()
        return (offset, ByteCodeInst(offset = offset, opcode = opcode, arg = arg, nextoffset = nextoffset))

    __next__ = next
    
    def read_arg(self, size):
        buf = 0
        for i in range(size):
            (_offset, byte) = next(self.iter)
            buf |= byte << 8 * i
            return buf



class _ByteCode(object):
    '''
    The decoded bytecode of a function, and related information.
    '''
    __slots__ = ('func_id', 'co_names', 'co_varnames', 'co_consts', 'co_cellvars', 'co_freevars', 'exception_entries', 'table', 'labels')
    
    def __init__(self, func_id):
        code = func_id.code
        labels = (lambda .0: pass# WARNING: Decompyle incomplete
)(dis.findlabels(code.co_code)())
        labels.add(0)
        table = OrderedDict(ByteCodeIter(code))
        self._compute_lineno(table, code)
        self.func_id = func_id
        self.co_names = code.co_names
        self.co_varnames = code.co_varnames
        self.co_consts = code.co_consts
        self.co_cellvars = code.co_cellvars
        self.co_freevars = code.co_freevars
        self.table = table
        self.labels = sorted(labels)

    _compute_lineno = (lambda cls, table, code: pass# WARNING: Decompyle incomplete
)()
    
    def __iter__(self):
        return iter(self.table.values())

    
    def __getitem__(self, offset):
        return self.table[offset]

    
    def __contains__(self, offset):
        return offset in self.table

    
    def dump(self):
        pass
    # WARNING: Decompyle incomplete

    _compute_used_globals = (lambda cls, func, table, co_consts, co_names: d = { }globs = func.__globals__builtins = globs.get('__builtins__', utils.builtins)if isinstance(builtins, ModuleType):
builtins = builtins.__dict__for inst in table.values():
if inst.opname == 'LOAD_GLOBAL':
name = co_names[_fix_LOAD_GLOBAL_arg(inst.arg)]if name not in d:
value = globs[name]else:
except KeyError:
value = builtins[name]d[name] = valuefor co in co_consts:
if isinstance(co, CodeType):
subtable = OrderedDict(ByteCodeIter(co))d.update(cls._compute_used_globals(func, subtable, co.co_consts, co.co_names))d)()
    
    def get_used_globals(self):
        '''
        Get a {name: value} map of the globals used by this code
        object and any nested code objects.
        '''
        return self._compute_used_globals(self.func_id.func, self.table, self.co_consts, self.co_names)



def _fix_LOAD_GLOBAL_arg(arg):
    if PYVERSION in ((3, 11), (3, 12), (3, 13), (3, 14)):
        return arg >> 1
    if None in ((3, 10),):
        return arg
    raise None(PYVERSION)


class ByteCodePy311(_ByteCode):
    pass
# WARNING: Decompyle incomplete


class ByteCodePy312(ByteCodePy311):
    pass
# WARNING: Decompyle incomplete

if PYVERSION == (3, 11):
    ByteCode = ByteCodePy311
elif PYVERSION in ((3, 12), (3, 13), (3, 14)):
    ByteCode = ByteCodePy312
elif PYVERSION < (3, 11):
    ByteCode = _ByteCode
else:
    raise NotImplementedError(PYVERSION)

class FunctionIdentity(serialize.ReduceMixin):
    """
    A function's identity and metadata.

    Note this typically represents a function whose bytecode is
    being compiled, not necessarily the top-level user function
    (the two might be distinct).
    """
    _unique_ids = itertools.count(1)
    from_function = (lambda cls, pyfunc: func = get_function_object(pyfunc)code = get_code_object(func)pysig = utils.pysignature(func)if not code:
raise errors.ByteCodeSupportError('%s does not provide its bytecode' % func)try:
func_qualname = func.__qualname__except AttributeError:
func_qualname = func.__name__self = cls()self.func = funcself.func_qualname = func_qualnameself.func_name = func_qualname.split('.')[-1]self.code = codeself.module = inspect.getmodule(func)# WARNING: Decompyle incomplete
)()
    
    def derive(self):
        '''Copy the object and increment the unique counter.
        '''
        return self.from_function(self.func)

    
    def _reduce_states(self):
        '''
        NOTE: part of ReduceMixin protocol
        '''
        return dict(pyfunc = self.func)

    _rebuild = (lambda cls, pyfunc: cls.from_function(pyfunc))()
