# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typedlist.pyc (Python 3.11)

'''
Python wrapper that connects CPython interpreter to the Numba typed-list.

This is the code that is used when creating typed lists outside of a `@jit`
context and when returning a typed-list from a `@jit` decorated function. It
basically a Python class that has a Numba allocated typed-list under the hood
and uses `@jit` functions to access it. Since it inherits from MutableSequence
it should really quack like the CPython `list`.

'''
from collections.abc import MutableSequence
from numba.core.types import ListType
from numba.core.imputils import numba_typeref_ctor
from numba.core.dispatcher import Dispatcher
from numba.core import types, config, cgutils
from numba import njit, typeof
from numba.core.extending import overload, box, unbox, NativeValue, type_callable, overload_classmethod
from numba.typed import listobject
from numba.core.errors import TypingError, LoweringError
from numba.core.typing.templates import Signature
import typing as pt
Int_or_Slice = pt.Union[('pt.SupportsIndex', slice)]
T_co = pt.TypeVar('T_co', covariant = True)

def _Sequence():
    '''_Sequence'''
    
    def __getitem__(self = None, i = None):
        pass

    
    def __len__(self = None):
        pass


_Sequence = <NODE:27>(_Sequence, '_Sequence', pt.Protocol[T_co])
DEFAULT_ALLOCATED = listobject.DEFAULT_ALLOCATED
_make_list = (lambda itemty, allocated = (DEFAULT_ALLOCATED,): listobject._as_meminfo(listobject.new_list(itemty, allocated = allocated)))()
_length = (lambda l: len(l))()
_allocated = (lambda l: l._allocated())()
_is_mutable = (lambda l: l._is_mutable())()
_make_mutable = (lambda l: l._make_mutable())()
_make_immutable = (lambda l: l._make_immutable())()
_append = (lambda l, item: l.append(item))()
_setitem = (lambda l, i, item: l[i] = item)()
_getitem = (lambda l, i: l[i])()
_contains = (lambda l, item: item in l)()
_count = (lambda l, item: l.count(item))()
_pop = (lambda l, i: l.pop(i))()
_delitem = (lambda l, i: del l[i])()
_extend = (lambda l, iterable: l.extend(iterable))()
_insert = (lambda l, i, item: l.insert(i, item))()
_remove = (lambda l, item: l.remove(item))()
_clear = (lambda l: l.clear())()
_reverse = (lambda l: l.reverse())()
_copy = (lambda l: l.copy())()
_eq = (lambda t, o: t == o)()
_ne = (lambda t, o: t != o)()
_lt = (lambda t, o: t < o)()
_le = (lambda t, o: t <= o)()
_gt = (lambda t, o: t > o)()
_ge = (lambda t, o: t >= o)()
_index = (lambda l, item, start, end: l.index(item, start, end))()
_sort = (lambda l, key, reverse: l.sort(key, reverse))()

def _from_meminfo_ptr(ptr, listtype):
    return List(meminfo = ptr, lsttype = listtype)

T = pt.TypeVar('T')
T_or_ListT = pt.Union[(T, 'List[T]')]

def List():
    '''List'''
    __doc__ = 'A typed-list usable in Numba compiled functions.\n\n    Implements the MutableSequence interface.\n    '
    _legal_kwargs = [
        'lsttype',
        'meminfo',
        'allocated']
    
    def __new__(cls = None, *, lsttype, meminfo, allocated, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    empty_list = (lambda cls, item_type, allocated = (DEFAULT_ALLOCATED,): if config.DISABLE_JIT:
list()cls(lsttype = ListType(item_type), allocated = allocated))()
    
    def __init__(self, *args, **kwargs):
        '''
        For users, the constructor does not take any parameters.
        The keyword arguments are for internal use only.

        Parameters
        ----------
        args: iterable
            The iterable to initialize the list from
        lsttype : numba.core.types.ListType; keyword-only
            Used internally for the list type.
        meminfo : MemInfo; keyword-only
            Used internally to pass the MemInfo object when boxing.
        allocated: int; keyword-only
            Used internally to pre-allocate space for items
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_arg(self, lsttype, meminfo, allocated = (None, DEFAULT_ALLOCATED)):
        if not isinstance(lsttype, ListType):
            raise TypeError('*lsttype* must be a ListType')
    # WARNING: Decompyle incomplete

    _numba_type_ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _typed = (lambda self: self._list_type is not None)()
    _dtype = (lambda self: if not self._typed:
raise RuntimeError('invalid operation on untyped list')self._list_type.dtype)()
    
    def _initialise_list(self, item):
        lsttype = types.ListType(typeof(item))
        (self._list_type, self._opaque) = self._parse_arg(lsttype)

    
    def __len__(self = property):
        if not self._typed:
            return 0
        return None(self)

    
    def _allocated(self):
        if not self._typed:
            return DEFAULT_ALLOCATED
        return None(self)

    
    def _is_mutable(self):
        return _is_mutable(self)

    
    def _make_mutable(self):
        return _make_mutable(self)

    
    def _make_immutable(self):
        return _make_immutable(self)

    
    def __eq__(self, other):
        return _eq(self, other)

    
    def __ne__(self, other):
        return _ne(self, other)

    
    def __lt__(self, other):
        return _lt(self, other)

    
    def __le__(self, other):
        return _le(self, other)

    
    def __gt__(self, other):
        return _gt(self, other)

    
    def __ge__(self, other):
        return _ge(self, other)

    
    def append(self = None, item = None):
        if not self._typed:
            self._initialise_list(item)
        _append(self, item)

    __setitem__ = (lambda self = None, i = None, o = pt.overload: pass)()
    __setitem__ = (lambda self = None, s = None, o = pt.overload: pass)()
    
    def __setitem__(self = None, i = None, item = None):
        if not self._typed:
            self._initialise_list(item)
        _setitem(self, i, item)

    __getitem__ = (lambda self = None, i = None: pass)()
    __getitem__ = (lambda self = None, i = None: pass)()
    
    def __getitem__(self = None, i = None):
        if not self._typed:
            raise IndexError
        return _getitem(self, i)

    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __contains__(self = None, item = None):
        return _contains(self, item)

    
    def __delitem__(self = None, i = None):
        _delitem(self, i)

    
    def insert(self = None, i = None, item = None):
        if not self._typed:
            self._initialise_list(item)
        _insert(self, i, item)

    
    def count(self = None, item = None):
        return _count(self, item)

    
    def pop(self = None, i = None):
        return _pop(self, i)

    
    def extend(self = None, iterable = None):
        if len(iterable) == 0:
            return None
        if not None._typed:
            self._initialise_list(iterable[0])
        return _extend(self, iterable)

    
    def remove(self = None, item = None):
        return _remove(self, item)

    
    def clear(self):
        return _clear(self)

    
    def reverse(self):
        return _reverse(self)

    
    def copy(self):
        return _copy(self)

    
    def index(self = None, item = None, start = None, stop = (None, None)):
        return _index(self, item, start, stop)

    
    def sort(self, key, reverse = (None, False)):
        '''Sort the list inplace.

        See also ``list.sort()``
        '''
        if not callable(key) and isinstance(key, Dispatcher):
            key = njit(key)
        return _sort(self, key, reverse)

    
    def __str__(self):
        buf = []
        for x in self:
            buf.append('{}'.format(x))
            
            try:
                get_ipython
                preview = ', '.join(buf[:1000])
                suffix = ', ...' if len(buf) > 1000 else ''
                return '[{0}{1}]'.format(preview, suffix)
            except (NameError, IndexError):
                return 


    
    def __repr__(self):
        body = str(self)
        prefix = str(self._list_type) if self._typed else 'ListType[Undefined]'
        return '{prefix}({body})'.format(prefix = prefix, body = body)


List = <NODE:27>(List, 'List', MutableSequence, pt.Generic[T])
typedlist_empty = (lambda cls, item_type, allocated = (DEFAULT_ALLOCATED,): if cls.instance_type is not ListType:
None
def impl(cls, item_type, allocated = (None,)):
listobject.new_list(item_type, allocated = allocated)impl)()
box_lsttype = (lambda typ, val, c: context = c.contextbuilder = c.builderctor = cgutils.create_struct_proxy(typ)lstruct = ctor(context, builder, value = val)boxed_meminfo = c.box(types.MemInfoPointer(types.voidptr), lstruct.meminfo)modname = c.context.insert_const_string(c.builder.module, 'numba.typed.typedlist')typedlist_mod = c.pyapi.import_module(modname)fmp_fn = c.pyapi.object_getattr_string(typedlist_mod, '_from_meminfo_ptr')lsttype_obj = c.pyapi.unserialize(c.pyapi.serialize_object(typ))result_var = builder.alloca(c.pyapi.pyobj)builder.store(cgutils.get_null_value(c.pyapi.pyobj), result_var)builder.if_then(cgutils.is_not_null(builder, lsttype_obj))res = c.pyapi.call_function_objargs(fmp_fn, (boxed_meminfo, lsttype_obj))c.pyapi.decref(fmp_fn)c.pyapi.decref(typedlist_mod)c.pyapi.decref(boxed_meminfo)builder.store(res, result_var)None(None, None))()
unbox_listtype = (lambda typ, val, c:
