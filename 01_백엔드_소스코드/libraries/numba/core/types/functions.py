# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: functions.pyc (Python 3.11)

import traceback
from collections import namedtuple, defaultdict
import itertools
import logging
import textwrap
from shutil import get_terminal_size
from abstract import Callable, DTypeSpec, Dummy, Literal, Type, weakref
from common import Opaque
from misc import unliteral
from numba.core import errors, utils, types, config
from numba.core.typeconv import Conversion
_logger = logging.getLogger(__name__)
_termcolor = errors.termcolor()
_FAILURE = namedtuple('_FAILURE', 'template matched error literal')
_termwidth = get_terminal_size().columns
_header_lead = 'No implementation of function'
_header_template = _header_lead + ' {the_function} found for signature:\n \n >>> {fname}({signature})\n \nThere are {ncandidates} candidate implementations:'
_reason_template = '\n" - Of which {nmatches} did not match due to:\n\n'

def _wrapper(tmp, indent = (0,)):
    return textwrap.indent(tmp, ' ' * indent, (lambda line: True))

_overload_template = "- Of which {nduplicates} did not match due to:\n{kind} {inof} function '{function}': File: {file}: Line {line}.\n  With argument(s): '({args})':"
_err_reasons = {
    'specific_error': 'Rejected as the implementation raised a specific error:\n{}' }

def _bt_as_lines(bt):
    '''
    Converts a backtrace into a list of lines, squashes it a bit on the way.
    '''
    pass
# WARNING: Decompyle incomplete


def argsnkwargs_to_str(args, kwargs):
    buf = tuple(args)()
    (lambda .0: [ '{}={}'.format(k, v) for k, v in .0 ])(kwargs.items()())
    return ', '.join(buf)


class _ResolutionFailures(object):
    '''Collect and format function resolution failures.
    '''
    
    def __init__(self, context, function_type, args, kwargs, depth = (0,)):
        self._context = context
        self._function_type = function_type
        self._args = args
        self._kwargs = kwargs
        self._failures = defaultdict(list)
        self._depth = depth
        self._max_depth = 5
        self._scale = 2

    
    def __len__(self):
        return len(self._failures)

    
    def add_error(self, calltemplate, matched, error, literal):
        '''
        Args
        ----
        calltemplate : CallTemplate
        error : Exception or str
            Error message
        '''
        isexc = isinstance(error, Exception)
        errclazz = '%s: ' % type(error).__name__ if isexc else ''
        key = '{}{}'.format(errclazz, str(error))
        self._failures[key].append(_FAILURE(calltemplate, matched, error, literal))

    
    def format(self):
        '''Return a formatted error message from all the gathered errors.
        '''
        indent = ' ' * self._scale
        argstr = argsnkwargs_to_str(self._args, self._kwargs)
        ncandidates = (lambda .0: [ len(x) for x in .0 ])(self._failures.values()())
        tykey = self._function_type.typing_key
        fname = getattr(tykey, '__name__', None)
        is_external_fn_ptr = isinstance(self._function_type, ExternalFunctionPointer)
    # WARNING: Decompyle incomplete

    
    def format_error(self, error):
        '''Format error message or exception
        '''
        if isinstance(error, Exception):
            return '{}: {}'.format(type(error).__name__, error)
        return None.format(error)

    
    def get_loc(self, classtemplate, error):
        '''Get source location information from the error message.
        '''
        if isinstance(error, Exception) or hasattr(error, '__traceback__'):
            frame_list = traceback.extract_tb(error.__traceback__)
            if len(frame_list) != 0:
                frame = frame_list[-1]
                return '{}:{}'.format(frame[0], frame[1])
            return None
        return None

    
    def raise_error(self):
        for faillist in self._failures.values():
            for fail in faillist:
                if isinstance(fail.error, errors.ForceLiteralArg):
                    raise fail.error
                raise errors.TypingError(self.format())



def _unlit_non_poison(ty):
    '''Apply unliteral(ty) and raise a TypingError if type is Poison.
    '''
    out = unliteral(ty)
    if isinstance(out, types.Poison):
        m = f'''Poison type used in arguments; got {out}'''
        raise errors.TypingError(m)
    return out


class BaseFunction(Callable):
    pass
# WARNING: Decompyle incomplete


class Function(Opaque, BaseFunction):
    '''
    Type class for builtin functions implemented by Numba.
    '''
    pass


class BoundFunction(Opaque, Callable):
    pass
# WARNING: Decompyle incomplete


class MakeFunctionLiteral(Opaque, Literal):
    pass


class _PickleableWeakRef(weakref.ref):
    '''
    Allow a weakref to be pickled.

    Note that if the object referred to is not kept alive elsewhere in the
    pickle, the weakref will immediately expire after being constructed.
    '''
    
    def __getnewargs__(self):
        obj = self()
    # WARNING: Decompyle incomplete



class WeakType(Type):
    '''
    Base class for types parametered by a mortal object, to which only
    a weak reference is kept.
    '''
    
    def _store_object(self, obj):
        self._wr = _PickleableWeakRef(obj)

    
    def _get_object(self):
        obj = self._wr()
    # WARNING: Decompyle incomplete

    key = (lambda self: self._wr)()
    
    def __eq__(self, other):
