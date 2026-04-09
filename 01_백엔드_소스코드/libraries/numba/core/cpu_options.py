# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cpu_options.pyc (Python 3.11)

'''
Defines CPU Options for use in the CPU target
'''
from abc import ABCMeta, abstractmethod

def AbstractOptionValue():
    '''AbstractOptionValue'''
    __doc__ = 'Abstract base class for custom option values.\n    '
    encode = (lambda self = None: pass)()
    
    def __repr__(self = None):
        return f'''{self.__class__.__name__}({self.encode()})'''


AbstractOptionValue = <NODE:27>(AbstractOptionValue, 'AbstractOptionValue', metaclass = ABCMeta)

class FastMathOptions(AbstractOptionValue):
    '''
    Options for controlling fast math optimization.
    '''
    
    def __init__(self, value):
        valid_flags = {
            'afn',
            'nsz',
            'arcp',
            'fast',
            'ninf',
            'nnan',
            'reassoc',
            'contract'}
        if isinstance(value, FastMathOptions):
            self.flags = value.flags.copy()
            return None
        if None is True:
            self.flags = {
                'fast'}
            return None
        if None is False:
            self.flags = set()
            return None
        if None(value, set):
            invalid = value - valid_flags
            if invalid:
                raise ValueError('Unrecognized fastmath flags: %s' % invalid)
            self.flags = value
            return None
        if None(value, dict):
            invalid = set(value.keys()) - valid_flags
            if invalid:
                raise ValueError('Unrecognized fastmath flags: %s' % invalid)
            self.flags = value.items()()
            return None
        msg = None
        raise ValueError(msg)

    
    def __bool__(self):
        return bool(self.flags)

    __nonzero__ = __bool__
    
    def encode(self = None):
        return str(self.flags)

    
    def __eq__(self, other):
        if type(other) is type(self):
            return self.flags == other.flags



class ParallelOptions(AbstractOptionValue):
    '''
    Options for controlling auto parallelization.
    '''
    __slots__ = ('enabled', 'comprehension', 'reduction', 'inplace_binop', 'setitem', 'numpy', 'stencil', 'fusion', 'prange')
    
    def __init__(self, value):
        if isinstance(value, bool):
            self.enabled = value
            self.comprehension = value
            self.reduction = value
            self.inplace_binop = value
            self.setitem = value
            self.numpy = value
            self.stencil = value
            self.fusion = value
            self.prange = value
            return None
        if None(value, dict):
            self.enabled = True
            self.comprehension = value.pop('comprehension', True)
            self.reduction = value.pop('reduction', True)
            self.inplace_binop = value.pop('inplace_binop', True)
            self.setitem = value.pop('setitem', True)
            self.numpy = value.pop('numpy', True)
            self.stencil = value.pop('stencil', True)
            self.fusion = value.pop('fusion', True)
            self.prange = value.pop('prange', True)
            if value:
                msg = 'Unrecognized parallel options: %s' % value.keys()
                raise NameError(msg)
            return None
        if None(value, ParallelOptions):
            self.enabled = value.enabled
            self.comprehension = value.comprehension
            self.reduction = value.reduction
            self.inplace_binop = value.inplace_binop
            self.setitem = value.setitem
            self.numpy = value.numpy
            self.stencil = value.stencil
            self.fusion = value.fusion
            self.prange = value.prange
            return None
        msg = None
        raise ValueError(msg)

    
    def _get_values(self):
        '''Get values as dictionary.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __eq__(self, other):
        if type(other) is type(self):
            return self._get_values() == other._get_values()

    
    def encode(self = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self._get_values().items()())



class InlineOptions(AbstractOptionValue):
    '''
    Options for controlling inlining
    '''
    
    def __init__(self, value):
        ok = False
        if isinstance(value, str):
            if value in ('always', 'never'):
                ok = True
            else:
                ok = hasattr(value, '__call__')
        if ok:
            self._inline = value
            return None
        msg = None % value
        raise ValueError(msg)

    is_never_inline = (lambda self: self._inline == 'never')()
    is_always_inline = (lambda self: self._inline == 'always')()
    has_cost_model = (lambda self:
