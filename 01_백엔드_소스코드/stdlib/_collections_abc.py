# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _collections_abc.pyc (Python 3.11)

'''Abstract Base Classes (ABCs) for collections, according to PEP 3119.

Unit tests are in test_collections.
'''
from abc import ABCMeta, abstractmethod
import sys
GenericAlias = type(list[int])
EllipsisType = type(...)

def _f():
    pass

FunctionType = type(_f)
del _f
__all__ = [
    'Awaitable',
    'Coroutine',
    'AsyncIterable',
    'AsyncIterator',
    'AsyncGenerator',
    'Hashable',
    'Iterable',
    'Iterator',
    'Generator',
    'Reversible',
    'Sized',
    'Container',
    'Callable',
    'Collection',
    'Set',
    'MutableSet',
    'Mapping',
    'MutableMapping',
    'MappingView',
    'KeysView',
    'ItemsView',
    'ValuesView',
    'Sequence',
    'MutableSequence',
    'ByteString']
__name__ = 'collections.abc'
bytes_iterator = type(iter(b''))
bytearray_iterator = type(iter(bytearray()))
dict_keyiterator = type(iter({ }.keys()))
dict_valueiterator = type(iter({ }.values()))
dict_itemiterator = type(iter({ }.items()))
list_iterator = type(iter([]))
list_reverseiterator = type(iter(reversed([])))
range_iterator = type(iter(range(0)))
longrange_iterator = type(iter(range(1 << 1000)))
set_iterator = type(iter(set()))
str_iterator = type(iter(''))
tuple_iterator = type(iter(()))
zip_iterator = type(iter(zip()))
dict_keys = type({ }.keys())
dict_values = type({ }.values())
dict_items = type({ }.items())
mappingproxy = type(type.__dict__)
generator = type((lambda : pass# WARNING: Decompyle incomplete
)())

async def _coro():
    pass
# WARNING: Decompyle incomplete

_coro = _coro()
coroutine = type(_coro)
_coro.close()
del _coro

def _ag():
    pass
# WARNING: Decompyle incomplete

_ag = _ag()
async_generator = type(_ag)
del _ag

def _check_methods(C, *methods):
    mro = C.__mro__
# WARNING: Decompyle incomplete


def Hashable():
    '''Hashable'''
    __slots__ = ()
    __hash__ = (lambda self: 0)()
    __subclasshook__ = (lambda cls, C: if cls is Hashable:
_check_methods(C, '__hash__'))()

Hashable = <NODE:27>(Hashable, 'Hashable', metaclass = ABCMeta)

def Awaitable():
    '''Awaitable'''
    __slots__ = ()
    __await__ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    __subclasshook__ = (lambda cls, C: if cls is Awaitable:
_check_methods(C, '__await__'))()
    __class_getitem__ = classmethod(GenericAlias)

Awaitable = <NODE:27>(Awaitable, 'Awaitable', metaclass = ABCMeta)

class Coroutine(Awaitable):
    __slots__ = ()
    send = (lambda self, value: raise StopIteration)()
    throw = (lambda self, typ, val, tb = (None, None): pass# WARNING: Decompyle incomplete
)()
    
    def close(self):
        '''Raise GeneratorExit inside coroutine.
        '''
        
        try:
            self.throw(GeneratorExit)
            raise RuntimeError('coroutine ignored GeneratorExit')
        except (GeneratorExit, StopIteration):
            return None


    __subclasshook__ = (lambda cls, C: if cls is Coroutine:
_check_methods(C, '__await__', 'send', 'throw', 'close'))()

Coroutine.register(coroutine)

def AsyncIterable():
    '''AsyncIterable'''
    __slots__ = ()
    __aiter__ = (lambda self: AsyncIterator())()
    __subclasshook__ = (lambda cls, C: if cls is AsyncIterable:
_check_methods(C, '__aiter__'))()
    __class_getitem__ = classmethod(GenericAlias)

AsyncIterable = <NODE:27>(AsyncIterable, 'AsyncIterable', metaclass = ABCMeta)

class AsyncIterator(AsyncIterable):
    __slots__ = ()
    __anext__ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self):
        return self

    __subclasshook__ = (lambda cls, C: if cls is AsyncIterator:
_check_methods(C, '__anext__', '__aiter__'))()


class AsyncGenerator(AsyncIterator):
    __slots__ = ()
    
    async def __anext__(self):
        '''Return the next item from the asynchronous generator.
        When exhausted, raise StopAsyncIteration.
        '''
        pass
    # WARNING: Decompyle incomplete

    asend = (lambda self, value: pass# WARNING: Decompyle incomplete
)()
    athrow = (lambda self, typ, val, tb = (None, None): pass# WARNING: Decompyle incomplete
)()
    
    async def aclose(self):
        '''Raise GeneratorExit inside coroutine.
        '''
        pass
    # WARNING: Decompyle incomplete

    __subclasshook__ = (lambda cls, C: if cls is AsyncGenerator:
_check_methods(C, '__aiter__', '__anext__', 'asend', 'athrow', 'aclose'))()

AsyncGenerator.register(async_generator)

def Iterable():
    '''Iterable'''
    __slots__ = ()
    __iter__ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    __subclasshook__ = (lambda cls, C: if cls is Iterable:
_check_methods(C, '__iter__'))()
    __class_getitem__ = classmethod(GenericAlias)

Iterable = <NODE:27>(Iterable, 'Iterable', metaclass = ABCMeta)

class Iterator(Iterable):
    __slots__ = ()
    __next__ = (lambda self: raise StopIteration)()
    
    def __iter__(self):
        return self

    __subclasshook__ = (lambda cls, C: if cls is Iterator:
_check_methods(C, '__iter__', '__next__'))()

Iterator.register(bytes_iterator)
Iterator.register(bytearray_iterator)
Iterator.register(dict_keyiterator)
Iterator.register(dict_valueiterator)
Iterator.register(dict_itemiterator)
Iterator.register(list_iterator)
Iterator.register(list_reverseiterator)
Iterator.register(range_iterator)
Iterator.register(longrange_iterator)
Iterator.register(set_iterator)
Iterator.register(str_iterator)
Iterator.register(tuple_iterator)
Iterator.register(zip_iterator)

class Reversible(Iterable):
    __slots__ = ()
    __reversed__ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    __subclasshook__ = (lambda cls, C: if cls is Reversible:
_check_methods(C, '__reversed__', '__iter__'))()


class Generator(Iterator):
    __slots__ = ()
    
    def __next__(self):
        '''Return the next item from the generator.
        When exhausted, raise StopIteration.
        '''
        return self.send(None)

    send = (lambda self, value: raise StopIteration)()
    throw = (lambda self, typ, val, tb = (None, None): pass# WARNING: Decompyle incomplete
)()
    
    def close(self):
        '''Raise GeneratorExit inside generator.
        '''
        
        try:
            self.throw(GeneratorExit)
            raise RuntimeError('generator ignored GeneratorExit')
        except (GeneratorExit, StopIteration):
            return None


    __subclasshook__ = (lambda cls, C: if cls is Generator:
_check_methods(C, '__iter__', '__next__', 'send', 'throw', 'close'))()

Generator.register(generator)

def Sized():
    '''Sized'''
    __slots__ = ()
    __len__ = (lambda self: 0)()
    __subclasshook__ = (lambda cls, C: if cls is Sized:
_check_methods(C, '__len__'))()

Sized = <NODE:27>(Sized, 'Sized', metaclass = ABCMeta)

def Container():
    '''Container'''
    __slots__ = ()
    __contains__ = (lambda self, x: False)()
    __subclasshook__ = (lambda cls, C: if cls is Container:
_check_methods(C, '__contains__'))()
    __class_getitem__ = classmethod(GenericAlias)

Container = <NODE:27>(Container, 'Container', metaclass = ABCMeta)

class Collection(Container, Iterable, Sized):
    __slots__ = ()
    __subclasshook__ = (lambda cls, C: if cls is Collection:
_check_methods(C, '__len__', '__iter__', '__contains__'))()


class _CallableGenericAlias(GenericAlias):
    pass
# WARNING: Decompyle incomplete


def _is_param_expr(obj):
    '''Checks if obj matches either a list of types, ``...``, ``ParamSpec`` or
    ``_ConcatenateGenericAlias`` from typing.py
    '''
    pass
# WARNING: Decompyle incomplete


def _type_repr(obj):
    """Return the repr() of an object, special-casing types (internal helper).

    Copied from :mod:`typing` since collections.abc
    shouldn't depend on that module.
    """
    if isinstance(obj, GenericAlias):
        return repr(obj)
    if None(obj, type):
        if obj.__module__ == 'builtins':
            return obj.__qualname__
        return f'''{None.__module__}.{obj.__qualname__}'''
    if None is Ellipsis:
        return '...'
    if None(obj, FunctionType):
        return obj.__name__
    return None(obj)


def Callable():
    '''Callable'''
    __slots__ = ()
    __call__ = (lambda self: False)()
    __subclasshook__ = (lambda cls, C: if cls is Callable:
_check_methods(C, '__call__'))()
    __class_getitem__ = classmethod(_CallableGenericAlias)

Callable = <NODE:27>(Callable, 'Callable', metaclass = ABCMeta)

class Set(Collection):
    '''A set is a finite, iterable container.

    This class provides concrete generic implementations of all
    methods except for __contains__, __iter__ and __len__.

    To override the comparisons (presumably for speed, as the
    semantics are fixed), redefine __le__ and __ge__,
    then the other operations will automatically follow suit.
    '''
    __slots__ = ()
    
    def __le__(self, other):
        if not isinstance(other, Set):
            return NotImplemented
        if None(self) > len(other):
            return False
        for elem in None:
            if elem not in other:
                return False
            return True

    
    def __lt__(self, other):
