# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: misc.pyc (Python 3.11)

from numba.core.types.abstract import Callable, Literal, Type, Hashable
from numba.core.types.common import Dummy, IterableType, Opaque, SimpleIteratorType
from numba.core.typeconv import Conversion
from numba.core.errors import TypingError, LiteralTypingError
from numba.core.ir import UndefinedType
from numba.core.utils import get_hashable_key

class PyObject(Dummy):
    '''
    A generic CPython object.
    '''
    
    def is_precise(self):
        return False



class Phantom(Dummy):
    '''
    A type that cannot be materialized.  A Phantom cannot be used as
    argument or return type.
    '''
    pass


class Undefined(Dummy):
    '''
    A type that is left imprecise.  This is used as a temporaray placeholder
    during type inference in the hope that the type can be later refined.
    '''
    
    def is_precise(self):
        return False



class UndefVar(Dummy):
    '''
    A type that is created by Expr.undef to represent an undefined variable.
    This type can be promoted to any other type.
    This is introduced to handle Python 3.12 LOAD_FAST_AND_CLEAR.
    '''
    
    def can_convert_to(self, typingctx, other):
        return Conversion.promote



class RawPointer(Opaque):
    '''
    A raw pointer without any specific meaning.
    '''
    pass


class StringLiteral(Dummy, Literal):
    
    def can_convert_to(self, typingctx, other):
        if isinstance(other, UnicodeType):
            return Conversion.safe


Literal.ctor_map[str] = StringLiteral

def unliteral(lit_type):
    '''
    Get base type from Literal type.
    '''
    if hasattr(lit_type, '__unliteral__'):
        return lit_type.__unliteral__()
    return None(lit_type, 'literal_type', lit_type)


def literal(value):
    '''Returns a Literal instance or raise LiteralTypingError
    '''
    ty = type(value)
    if isinstance(value, Literal):
        msg = 'the function does not accept a Literal type; got {} ({})'
        raise ValueError(msg.format(value, ty))
    
    try:
        ctor = Literal.ctor_map[ty]
        return ctor(value)
    except KeyError:
        raise LiteralTypingError('{} cannot be used as a literal'.format(ty))



def maybe_literal(value):
    '''Get a Literal type for the value or None.
    '''
    
    try:
        return literal(value)
    except LiteralTypingError:
        return None



class Omitted(Opaque):
    pass
# WARNING: Decompyle incomplete


class VarArg(Type):
    pass
# WARNING: Decompyle incomplete


class Module(Dummy):
    pass
# WARNING: Decompyle incomplete


class MemInfoPointer(Type):
    pass
# WARNING: Decompyle incomplete


class CPointer(Type):
    pass
# WARNING: Decompyle incomplete


class EphemeralPointer(CPointer):
    """
    Type class for pointers which aren't guaranteed to last long - e.g.
    stack-allocated slots.  The data model serializes such pointers
    by copying the data pointed to.
    """
    pass


class EphemeralArray(Type):
    pass
# WARNING: Decompyle incomplete


class Object(Type):
    pass
# WARNING: Decompyle incomplete


class Optional(Type):
    pass
# WARNING: Decompyle incomplete


class NoneType(Opaque):
    '''
    The type for None.
    '''
    
    def unify(self, typingctx, other):
        '''
        Turn anything to a Optional type;
        '''
        if isinstance(other, (Optional, NoneType)):
            return other
        return None(other)



class EllipsisType(Opaque):
    '''
    The type for the Ellipsis singleton.
    '''
    pass


class ExceptionClass(Phantom, Callable):
    pass
# WARNING: Decompyle incomplete


class ExceptionInstance(Phantom):
    pass
# WARNING: Decompyle incomplete


class SliceType(Type):
    pass
# WARNING: Decompyle incomplete


class SliceLiteral(SliceType, Literal):
    
    def __init__(self, value):
        self._literal_init(value)
        name = 'Literal[slice]({})'.format(value)
    # WARNING: Decompyle incomplete

    key = (lambda self: sl = self.literal_value(sl.start, sl.stop, sl.step))()

Literal.ctor_map[slice] = SliceLiteral

class ClassInstanceType(Type):
    pass
# WARNING: Decompyle incomplete


class ClassType(Opaque, Callable):
    pass
# WARNING: Decompyle incomplete


class DeferredType(Type):
    pass
# WARNING: Decompyle incomplete


class ClassDataType(Type):
    pass
# WARNING: Decompyle incomplete


class ContextManager(Phantom, Callable):
    pass
# WARNING: Decompyle incomplete


class UnicodeType(Hashable, IterableType):
    pass
# WARNING: Decompyle incomplete


class UnicodeIteratorType(SimpleIteratorType):
    pass
# WARNING: Decompyle incomplete
