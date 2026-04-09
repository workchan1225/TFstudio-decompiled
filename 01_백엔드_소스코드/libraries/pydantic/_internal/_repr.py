# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _repr.pyc (Python 3.11)

'''Tools to provide pretty/human-readable display of objects.'''
from __future__ import annotations as _annotations
import types
from collections.abc import Callable, Collection, Generator, Iterable
from typing import TYPE_CHECKING, Any, ForwardRef, cast
import typing_extensions
from typing_extensions import TypeAlias
from typing_inspection import typing_objects
from typing_inspection.introspection import is_union_origin
from  import _typing_extra
if TYPE_CHECKING:
    ReprArgs: 'TypeAlias' = Iterable[tuple[(str | None, Any)]]
    RichReprResult: 'TypeAlias' = Iterable[Any | tuple[Any] | tuple[(str, Any)] | tuple[(str, Any, Any)]]

class PlainRepr(str):
    """String class where repr doesn't include quotes. Useful with Representation when you want to return a string
    representation of something that is valid (or pseudo-valid) python.
    """
    
    def __repr__(self = None):
        return str(self)



class Representation:
    __slots__ = ()
    
    def __repr_args__(self = None):
        """Returns the attributes to show in __str__, __repr__, and __pretty__ this is generally overridden.

        Can either return:
        * name - value pairs, e.g.: `[('foo_name', 'foo'), ('bar_name', ['b', 'a', 'r'])]`
        * or, just values, e.g.: `[(None, 'foo'), (None, ['b', 'a', 'r'])]`
        """
        pass
    # WARNING: Decompyle incomplete

    
    def __repr_name__(self = None):
        """Name of the instance's class, used in __repr__."""
        return self.__class__.__name__

    
    def __repr_recursion__(self = None, object = None):
        '''Returns the string representation of a recursive object.'''
        return f'''<Recursion on {type(object).__name__} with id={id(object)}>'''

    
    def __repr_str__(self = None, join_str = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(self.__repr_args__()())

    
    def __pretty__(self = None, fmt = None, **kwargs):
        '''Used by devtools (https://python-devtools.helpmanual.io/) to pretty print objects.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __rich_repr__(self = None):
        '''Used by Rich (https://rich.readthedocs.io/en/stable/pretty.html) to pretty print objects.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        return self.__repr_str__(' ')

    
    def __repr__(self = None):
        return f'''{self.__repr_name__()}({self.__repr_str__(', ')})'''



def display_as_type(obj = None):
    '''Pretty representation of a type, should be as close as possible to the original type definition string.

    Takes some logic from `typing._type_repr`.
    '''
    if isinstance(obj, (types.FunctionType, types.BuiltinFunctionType)):
        return obj.__name__
    if None is ...:
        return '...'
    if None(obj, Representation):
        return repr(obj)
    if None(obj, ForwardRef) or typing_objects.is_typealiastype(obj):
        return str(obj)
    if not None(obj, (_typing_extra.typing_base, _typing_extra.WithArgsTypes, type)):
        obj = obj.__class__
    if is_union_origin(typing_extensions.get_origin(obj)):
        args = ', '.join(map(display_as_type, typing_extensions.get_args(obj)))
        return f'''Union[{args}]'''
    if None(obj, _typing_extra.WithArgsTypes):
        if typing_objects.is_literal(typing_extensions.get_origin(obj)):
            args = ', '.join(map(repr, typing_extensions.get_args(obj)))
        else:
            args = ', '.join(map(display_as_type, typing_extensions.get_args(obj)))
        
        try:
            return f'''{obj.__qualname__}[{args}]'''
        except AttributeError:
            return 
            if isinstance(obj, type):
                return obj.__qualname__
            return None(obj).replace('typing.', '').replace('typing_extensions.', '')
