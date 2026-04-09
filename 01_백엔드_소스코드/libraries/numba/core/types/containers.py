# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: containers.pyc (Python 3.11)

from collections.abc import Iterable
from collections.abc import Sequence as pySequence
from types import MappingProxyType
from abstract import ConstSized, Container, Hashable, MutableSequence, Sequence, Type, TypeRef, Literal, InitialValue, Poison
from common import Buffer, IterableType, SimpleIterableType, SimpleIteratorType
from misc import Undefined, unliteral, Optional, NoneType
from typeconv import Conversion
from errors import TypingError
from  import utils

class Pair(Type):
    pass
# WARNING: Decompyle incomplete


class BaseContainerIterator(SimpleIteratorType):
    pass
# WARNING: Decompyle incomplete


class BaseContainerPayload(Type):
    pass
# WARNING: Decompyle incomplete


class Bytes(Buffer):
    '''
    Type class for Python 3.x bytes objects.
    '''
    mutable = False
    slice_is_copy = False


class ByteArray(Buffer):
    '''
    Type class for bytearray objects.
    '''
    slice_is_copy = True


class PyArray(Buffer):
    '''
    Type class for array.array objects.
    '''
    slice_is_copy = True


class MemoryView(Buffer):
    '''
    Type class for memoryview objects.
    '''
    pass


def is_homogeneous(*tys):
    '''Are the types homogeneous?
    '''
    pass
# WARNING: Decompyle incomplete


class BaseTuple(Hashable, ConstSized):
    '''
    The base class for all tuple types (with a known size).
    '''
    from_types = (lambda cls, tys, pyclass = (None,): pass# WARNING: Decompyle incomplete
)()
    _make_homogeneous_tuple = (lambda cls, dtype, count: UniTuple(dtype, count))()
    _make_heterogeneous_tuple = (lambda cls, tys: Tuple(tys))()


class BaseAnonymousTuple(BaseTuple):
    '''
    Mixin for non-named tuples.
    '''
    
    def can_convert_to(self, typingctx, other):
        '''
        Convert this tuple to another one.  Note named tuples are rejected.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __unliteral__(self):
        return (lambda .0: [ unliteral(t) for t in .0 ])(self())



class _HomogeneousTuple(BaseTuple, Sequence):
    iterator_type = (lambda self: UniTupleIter(self))()
    
    def __getitem__(self, i):
        '''
        Return element at position i
        '''
        return self.dtype

    
    def __iter__(self):
        return iter([
            self.dtype] * self.count)

    
    def __len__(self):
        return self.count

    types = (lambda self: (self.dtype,) * self.count)()


class UniTuple(Sequence, _HomogeneousTuple, BaseAnonymousTuple):
    pass
# WARNING: Decompyle incomplete


class UniTupleIter(BaseContainerIterator):
    '''
    Type class for homogeneous tuple iterators.
    '''
    container_class = _HomogeneousTuple


class _HeterogeneousTuple(BaseTuple):
    
    def __getitem__(self, i):
        '''
        Return element at position i
        '''
        return self.types[i]

    
    def __len__(self):
        return len(self.types)

    
    def __iter__(self):
        return iter(self.types)

    is_types_iterable = (lambda types: if not isinstance(types, Iterable):
raise TypingError("Argument 'types' is not iterable"))()


class UnionType(Type):
    pass
# WARNING: Decompyle incomplete


class Tuple(_HeterogeneousTuple, BaseAnonymousTuple):
    pass
# WARNING: Decompyle incomplete


class _StarArgTupleMixin:
    _make_homogeneous_tuple = (lambda cls, dtype, count: StarArgUniTuple(dtype, count))()
    _make_heterogeneous_tuple = (lambda cls, tys: StarArgTuple(tys))()


class StarArgTuple(Tuple, _StarArgTupleMixin):
    '''To distinguish from Tuple() used as argument to a `*args`.
    '''
    
    def __new__(cls, types):
        pass
    # WARNING: Decompyle incomplete



class StarArgUniTuple(UniTuple, _StarArgTupleMixin):
    '''To distinguish from UniTuple() used as argument to a `*args`.
    '''
    pass


class BaseNamedTuple(BaseTuple):
    pass


class NamedUniTuple(BaseNamedTuple, _HomogeneousTuple):
    pass
# WARNING: Decompyle incomplete


class NamedTuple(BaseNamedTuple, _HeterogeneousTuple):
    pass
# WARNING: Decompyle incomplete


class List(InitialValue, MutableSequence):
    pass
# WARNING: Decompyle incomplete


class LiteralList(Hashable, ConstSized, Literal):
    '''A heterogeneous immutable list (basically a tuple with list semantics).
    '''
    mutable = False
    
    def __init__(self, literal_value):
        self.is_types_iterable(literal_value)
        self._literal_init(list(literal_value))
        self.types = tuple(literal_value)
        self.count = len(self.types)
        self.name = 'LiteralList({})'.format(literal_value)

    
    def __getitem__(self, i):
        '''
        Return element at position i
        '''
        return self.types[i]

    
    def __len__(self):
        return len(self.types)

    
    def __iter__(self):
        return iter(self.types)

    from_types = (lambda cls, tys: LiteralList(tys))()
    is_types_iterable = (lambda types: if not isinstance(types, Iterable):
raise TypingError("Argument 'types' is not iterable"))()
    iterator_type = (lambda self: ListIter(self))()
    
    def __unliteral__(self):
        return Poison(self)

    
    def unify(self, typingctx, other):
        '''
        Unify this with the *other* one.
        '''
        if isinstance(other, LiteralList) or self.count == other.count:
            tys = []
            for i1, i2 in zip(self.types, other.types):
                tys.append(typingctx.unify_pairs(i1, i2))
                if all(tys):
                    return LiteralList(tys)
                return None
                return None
                return None



class ListIter(BaseContainerIterator):
    '''
    Type class for list iterators.
    '''
    container_class = List


class ListPayload(BaseContainerPayload):
    '''
    Internal type class for the dynamically-allocated payload of a list.
    '''
    container_class = List


class Set(Container):
    pass
# WARNING: Decompyle incomplete


class SetIter(BaseContainerIterator):
    '''
    Type class for set iterators.
    '''
    container_class = Set


class SetPayload(BaseContainerPayload):
    '''
    Internal type class for the dynamically-allocated payload of a set.
    '''
    container_class = Set


class SetEntry(Type):
    pass
# WARNING: Decompyle incomplete


class ListType(IterableType):
    pass
# WARNING: Decompyle incomplete


class ListTypeIterableType(SimpleIterableType):
    pass
# WARNING: Decompyle incomplete


class ListTypeIteratorType(SimpleIteratorType):
    pass
# WARNING: Decompyle incomplete


def _sentry_forbidden_types(key, value):
    if isinstance(key, (Set, List)):
        raise TypingError('{} as key is forbidden'.format(key))
    if isinstance(value, (Set, List)):
        raise TypingError('{} as value is forbidden'.format(value))


class DictType(InitialValue, IterableType):
    pass
# WARNING: Decompyle incomplete


class LiteralStrKeyDict(Hashable, ConstSized, Literal):
    '''A Dictionary of string keys to heterogeneous values (basically a
    namedtuple with dict semantics).
    '''
    
    class FakeNamedTuple(pySequence):
        pass
    # WARNING: Decompyle incomplete

    mutable = False
    
    def __init__(self, literal_value, value_index = (None,)):
        self._literal_init(literal_value)
        self.value_index = value_index
        strkeys = literal_value.keys()()
        self.tuple_ty = self.FakeNamedTuple('_ntclazz', strkeys)
        tys = literal_value.values()()
        self.types = tuple(tys)
        self.count = len(self.types)
        self.fields = tuple(self.tuple_ty._fields)
        self.instance_class = self.tuple_ty
        self.name = 'LiteralStrKey[Dict]({})'.format(literal_value)

    
    def __unliteral__(self):
        return Poison(self)

    
    def unify(self, typingctx, other):
        '''
        Unify this with the *other* one.
        '''
        if isinstance(other, LiteralStrKeyDict):
            tys = []
            for k1, v1 in zip(self.literal_value.items(), other.literal_value.items()):
                (k2, v2) = None
                if k1 != k2:
                    return None
                None.append(typingctx.unify_pairs(v1, v2))
                if all(tys):
                    d = zip(self.literal_value.keys(), tys)()
                    return LiteralStrKeyDict(d)
                return None
                return None

    
    def __len__(self):
        return len(self.types)

    
    def __iter__(self):
        return iter(self.types)

    key = (lambda self: (self.tuple_ty._fields, self.types, str(self.literal_value)))()


class DictItemsIterableType(SimpleIterableType):
    pass
# WARNING: Decompyle incomplete


class DictKeysIterableType(SimpleIterableType):
    pass
# WARNING: Decompyle incomplete


class DictValuesIterableType(SimpleIterableType):
    pass
# WARNING: Decompyle incomplete


class DictIteratorType(SimpleIteratorType):
    pass
# WARNING: Decompyle incomplete


class StructRef(Type):
    pass
# WARNING: Decompyle incomplete


class StructRefPayload(Type):
    pass
# WARNING: Decompyle incomplete
