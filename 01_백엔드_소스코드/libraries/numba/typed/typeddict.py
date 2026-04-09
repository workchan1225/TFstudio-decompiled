# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: typeddict.pyc (Python 3.11)

'''
Python wrapper that connects CPython interpreter to the numba dictobject.
'''
from collections.abc import MutableMapping, Iterable, Mapping
from numba.core.types import DictType
from numba.core.imputils import numba_typeref_ctor
from numba import njit, typeof
from numba.core import types, errors, config, cgutils
from numba.core.extending import overload, box, unbox, NativeValue, type_callable, overload_classmethod
from numba.typed import dictobject
from numba.core.typing import signature
_make_dict = (lambda keyty, valty, n_keys = (0,): dictobject._as_meminfo(dictobject.new_dict(keyty, valty, n_keys = n_keys)))()
_length = (lambda d: len(d))()
_setitem = (lambda d, key, value: d[key] = value)()
_getitem = (lambda d, key: d[key])()
_delitem = (lambda d, key: del d[key])()
_contains = (lambda d, key: key in d)()
_get = (lambda d, key, default: d.get(key, default))()
_setdefault = (lambda d, key, default: d.setdefault(key, default))()
_iter = (lambda d: list(d.keys()))()
_popitem = (lambda d: d.popitem())()
_copy = (lambda d: d.copy())()

def _from_meminfo_ptr(ptr, dicttype):
    d = Dict(meminfo = ptr, dcttype = dicttype)
    return d


class Dict(MutableMapping):
    '''A typed-dictionary usable in Numba compiled functions.

    Implements the MutableMapping interface.
    '''
    
    def __new__(cls, dcttype, meminfo, n_keys = (None, None, 0)):
        if config.DISABLE_JIT:
            return dict.__new__(dict)
        return None.__new__(cls)

    empty = (lambda cls, key_type, value_type, n_keys = (0,): if config.DISABLE_JIT:
dict()cls(dcttype = DictType(key_type, value_type), n_keys = n_keys))()
    
    def __init__(self, *args, **kwargs):
        '''
        For users, the constructor does not take any parameters.
        The keyword arguments are for internal use only.

        Parameters
        ----------
        dcttype : numba.core.types.DictType; keyword-only
            Used internally for the dictionary type.
        meminfo : MemInfo; keyword-only
            Used internally to pass the MemInfo object when boxing.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _parse_arg(self, dcttype, meminfo, n_keys = (None, 0)):
        if not isinstance(dcttype, DictType):
            raise TypeError('*dcttype* must be a DictType')
    # WARNING: Decompyle incomplete

    _numba_type_ = (lambda self: pass# WARNING: Decompyle incomplete
)()
    _typed = (lambda self: self._dict_type is not None)()
    
    def _initialise_dict(self, key, value):
        dcttype = types.DictType(typeof(key), typeof(value))
        (self._dict_type, self._opaque) = self._parse_arg(dcttype)

    
    def __getitem__(self, key):
        if not self._typed:
            raise KeyError(key)
        return _getitem(self, key)

    
    def __setitem__(self, key, value):
        if not self._typed:
            self._initialise_dict(key, value)
        return _setitem(self, key, value)

    
    def __delitem__(self, key):
        if not self._typed:
            raise KeyError(key)
        _delitem(self, key)

    
    def __iter__(self):
        if not self._typed:
            return iter(())
        return None(_iter(self))

    
    def __len__(self):
        if not self._typed:
            return 0
        return None(self)

    
    def __contains__(self, key):
        if len(self) == 0:
            return False
        return None(self, key)

    
    def __str__(self):
        buf = []
        for k, v in self.items():
            buf.append('{}: {}'.format(k, v))
            return '{{{0}}}'.format(', '.join(buf))

    
    def __repr__(self):
        body = str(self)
        prefix = str(self._dict_type)
        return '{prefix}({body})'.format(prefix = prefix, body = body)

    
    def get(self, key, default = (None,)):
        if not self._typed:
            return default
        return None(self, key, default)

    
    def setdefault(self, key, default = (None,)):
        pass
    # WARNING: Decompyle incomplete

    
    def popitem(self):
        if len(self) == 0:
            raise KeyError('dictionary is empty')
        return _popitem(self)

    
    def copy(self):
        return _copy(self)


typeddict_empty = (lambda cls, key_type, value_type, n_keys = (0,): if cls.instance_type is not DictType:
None
def impl(cls, key_type, value_type, n_keys = None):
dictobject.new_dict(key_type, value_type, n_keys = n_keys)impl)()
box_dicttype = (lambda typ, val, c: context = c.contextbuilder = c.builderctor = cgutils.create_struct_proxy(typ)dstruct = ctor(context, builder, value = val)boxed_meminfo = c.box(types.MemInfoPointer(types.voidptr), dstruct.meminfo)modname = c.context.insert_const_string(c.builder.module, 'numba.typed.typeddict')typeddict_mod = c.pyapi.import_module(modname)fmp_fn = c.pyapi.object_getattr_string(typeddict_mod, '_from_meminfo_ptr')dicttype_obj = c.pyapi.unserialize(c.pyapi.serialize_object(typ))result_var = builder.alloca(c.pyapi.pyobj)builder.store(cgutils.get_null_value(c.pyapi.pyobj), result_var)builder.if_then(cgutils.is_not_null(builder, dicttype_obj))res = c.pyapi.call_function_objargs(fmp_fn, (boxed_meminfo, dicttype_obj))c.pyapi.decref(fmp_fn)c.pyapi.decref(typeddict_mod)c.pyapi.decref(boxed_meminfo)builder.store(res, result_var)None(None, None))()
unbox_dicttype = (lambda typ, val, c: context = c.contextdict_type = c.pyapi.unserialize(c.pyapi.serialize_object(Dict))valtype = c.pyapi.object_type(val)same_type = c.builder.icmp_unsigned('==', valtype, dict_type)(then, orelse) = c.builder.if_else(same_type)thenmiptr = c.pyapi.object_getattr_string(val, '_opaque')mip_type = types.MemInfoPointer(types.voidptr)native = c.unbox(mip_type, miptr)mi = native.valueargtypes = (mip_type, typeof(typ))
def convert(mi, typ):
dictobject._from_meminfo(mi, typ)# WARNING: Decompyle incomplete
)()
typeddict_call = (lambda context: 
def typer(arg = (None,)):
pass# WARNING: Decompyle incomplete
typer)()
impl_numba_typeref_ctor = (lambda cls: pass# WARNING: Decompyle incomplete
)()
