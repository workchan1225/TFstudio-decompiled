# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: asnumbatype.pyc (Python 3.11)

import inspect
import typing as py_typing
from numba.core.typing.typeof import typeof
from numba.core import errors, types
from numba.core.utils import PYVERSION

class AsNumbaTypeRegistry:
    '''
    A registry for Python types. It stores a lookup table for simple cases
    (e.g. ``int``) and a list of functions for more complicated cases (e.g.
    generics like ``List[int]``).

    Python types are used in Python type annotations, and in instance checks.
    Therefore, this registry supports determining the Numba type of Python type
    annotations at compile time, along with determining the type of classinfo
    arguments to ``isinstance()``.

    This registry is not used dynamically on instances at runtime; to check the
    type of an object at runtime, use ``numba.typeof``.
    '''
    
    def __init__(self):
        self.lookup = (0, 0, complex(0), 'numba', True, None)()
        self.functions = [
            self._builtin_infer,
            self._numba_type_infer]

    
    def _numba_type_infer(self, py_type):
        if isinstance(py_type, types.Type):
            return py_type

    
    def _builtin_infer(self, py_type):
        if PYVERSION in ((3, 14),):
            if not isinstance(py_type, (py_typing.Union, py_typing._GenericAlias)):
                return None
        if PYVERSION in ((3, 10), (3, 11), (3, 12), (3, 13)):
            if not isinstance(py_type, py_typing._GenericAlias):
                return None
        raise NotImplementedError(PYVERSION)
        if getattr(py_type, '__origin__', None) is py_typing.Union:
            if len(py_type.__args__) != 2:
                raise errors.TypingError('Cannot type Union of more than two types')
            (arg_1_py, arg_2_py) = py_type.__args__
            if arg_2_py is type(None):
                return types.Optional(self.infer(arg_1_py))
            if None is type(None):
                return types.Optional(self.infer(arg_2_py))
            raise None.TypingError(f'''Cannot type Union that is not an Optional (neither type type {arg_2_py} is not NoneType''')
        if getattr(py_type, '__origin__', None) is list:
            (element_py,) = py_type.__args__
            return types.ListType(self.infer(element_py))
        if None(py_type, '__origin__', None) is dict:
            (key_py, value_py) = py_type.__args__
            return types.DictType(self.infer(key_py), self.infer(value_py))
        if None(py_type, '__origin__', None) is set:
            (element_py,) = py_type.__args__
            return types.Set(self.infer(element_py))
        if None(py_type, '__origin__', None) is tuple:
            tys = tuple(map(self.infer, py_type.__args__))
            return types.BaseTuple.from_types(tys)

    
    def register(self, func_or_py_type, numba_type = (None,)):
        '''
        Add support for new Python types (e.g. user-defined JitClasses) to the
        registry. For a simple pair of a Python type and a Numba type, this can
        be called as a function ``register(py_type, numba_type)``. If more
        complex logic is required (e.g. for generic types), ``register`` can be
        used as a decorator for a function that takes a Python type as input
        and returns a Numba type or ``None``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def try_infer(self, py_type):
        '''
        Try to determine the Numba type of a given Python type. We first
        consider the lookup dictionary. If ``py_type`` is not there, we iterate
        through the registered functions until one returns a Numba type.  If
        type inference fails, return ``None``.
        '''
        result = self.lookup.get(py_type, None)
    # WARNING: Decompyle incomplete

    
    def infer(self, py_type):
        result = self.try_infer(py_type)
    # WARNING: Decompyle incomplete

    
    def __call__(self, py_type):
        return self.infer(py_type)


as_numba_type = AsNumbaTypeRegistry()
