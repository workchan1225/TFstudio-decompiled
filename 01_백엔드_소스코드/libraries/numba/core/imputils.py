# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: imputils.pyc (Python 3.11)

'''
Utilities to simplify the boilerplate for native lowering.
'''
import collections
import contextlib
import inspect
import functools
from enum import Enum
from numba.core import typing, types, utils, cgutils
from numba.core.typing.templates import BaseRegistryLoader

class Registry(object):
    '''
    A registry of function and attribute implementations.
    '''
    
    def __init__(self, name = ('unspecified',)):
        self.name = name
        self.functions = []
        self.getattrs = []
        self.setattrs = []
        self.casts = []
        self.constants = []

    
    def lower(self, func, *argtys):
        '''
        Decorate an implementation of *func* for the given argument types.
        *func* may be an actual global function object, or any
        pseudo-function supported by Numba, such as "getitem".

        The decorated implementation has the signature
        (context, builder, sig, args).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _decorate_attr(self, impl, ty, attr, impl_list, decorator):
        real_impl = decorator(impl, ty, attr)
        impl_list.append((real_impl, attr, real_impl.signature))
        return impl

    
    def lower_getattr(self, ty, attr):
        '''
        Decorate an implementation of __getattr__ for type *ty* and
        the attribute *attr*.

        The decorated implementation will have the signature
        (context, builder, typ, val).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def lower_getattr_generic(self, ty):
        """
        Decorate the fallback implementation of __getattr__ for type *ty*.

        The decorated implementation will have the signature
        (context, builder, typ, val, attr).  The implementation is
        called for attributes which haven't been explicitly registered
        with lower_getattr().
        """
        return self.lower_getattr(ty, None)

    
    def lower_setattr(self, ty, attr):
        '''
        Decorate an implementation of __setattr__ for type *ty* and
        the attribute *attr*.

        The decorated implementation will have the signature
        (context, builder, sig, args).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def lower_setattr_generic(self, ty):
        """
        Decorate the fallback implementation of __setattr__ for type *ty*.

        The decorated implementation will have the signature
        (context, builder, sig, args, attr).  The implementation is
        called for attributes which haven't been explicitly registered
        with lower_setattr().
        """
        return self.lower_setattr(ty, None)

    
    def lower_cast(self, fromty, toty):
        '''
        Decorate the implementation of implicit conversion between
        *fromty* and *toty*.

        The decorated implementation will have the signature
        (context, builder, fromty, toty, val).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def lower_constant(self, ty):
        '''
        Decorate the implementation for creating a constant of type *ty*.

        The decorated implementation will have the signature
        (context, builder, ty, pyval).
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return f'''Lowering Registry<{self.name}>'''



class RegistryLoader(BaseRegistryLoader):
    '''
    An incremental loader for a target registry.
    '''
    registry_items = ('functions', 'getattrs', 'setattrs', 'casts', 'constants')

builtin_registry = Registry('builtin_registry')
lower_builtin = builtin_registry.lower
lower_getattr = builtin_registry.lower_getattr
lower_getattr_generic = builtin_registry.lower_getattr_generic
lower_setattr = builtin_registry.lower_setattr
lower_setattr_generic = builtin_registry.lower_setattr_generic
lower_cast = builtin_registry.lower_cast
lower_constant = builtin_registry.lower_constant

def _decorate_getattr(impl, ty, attr):
    pass
# WARNING: Decompyle incomplete


def _decorate_setattr(impl, ty, attr):
    pass
# WARNING: Decompyle incomplete


def fix_returning_optional(context, builder, sig, status, retval):
    if isinstance(sig.return_type, types.Optional):
        value_type = sig.return_type.type
        optional_none = context.make_optional_none(builder, value_type)
        retvalptr = cgutils.alloca_once_value(builder, optional_none)
        builder.if_then(builder.not_(status.is_none))
        optional_value = context.make_optional_value(builder, value_type, retval)
        builder.store(optional_value, retvalptr)
        None(None, None)
    else:
        with None:
            if not None:
                pass
    retval = builder.load(retvalptr)
    return retval


def user_function(fndesc, libs):
    '''
    A wrapper inserting code calling Numba-compiled *fndesc*.
    '''
    pass
# WARNING: Decompyle incomplete


def user_generator(gendesc, libs):
    '''
    A wrapper inserting code calling Numba-compiled *gendesc*.
    '''
    pass
# WARNING: Decompyle incomplete


def iterator_impl(iterable_type, iterator_type):
    '''
    Decorator a given class as implementing *iterator_type*
    (by providing an `iternext()` method).
    '''
    pass
# WARNING: Decompyle incomplete


class _IternextResult(object):
    '''
    A result wrapper for iteration, passed by iternext_impl() into the
    wrapped function.
    '''
    __slots__ = ('_context', '_builder', '_pairobj')
    
    def __init__(self, context, builder, pairobj):
        self._context = context
        self._builder = builder
        self._pairobj = pairobj

    
    def set_exhausted(self):
        '''
        Mark the iterator as exhausted.
        '''
        self._pairobj.second = self._context.get_constant(types.boolean, False)

    
    def set_valid(self, is_valid = (True,)):
        '''
        Mark the iterator as valid according to *is_valid* (which must
        be either a Python boolean or a LLVM inst).
        '''
        if is_valid in (False, True):
            is_valid = self._context.get_constant(types.boolean, is_valid)
        self._pairobj.second = is_valid

    
    def yield_(self, value):
        '''
        Mark the iterator as yielding the given *value* (a LLVM inst).
        '''
        self._pairobj.first = value

    
    def is_valid(self):
        '''
        Return whether the iterator is marked valid.
        '''
        return self._context.get_argument_value(self._builder, types.boolean, self._pairobj.second)

    
    def yielded_value(self):
        """
        Return the iterator's yielded value, if any.
        """
        return self._pairobj.first



class RefType(Enum):
    '''
    Enumerate the reference type
    '''
    NEW = 1
    BORROWED = 2
    UNTRACKED = 3


def iternext_impl(ref_type = (None,)):
    '''
    Wrap the given iternext() implementation so that it gets passed
    an _IternextResult() object easing the returning of the iternext()
    result pair.

    ref_type: a numba.targets.imputils.RefType value, the reference type used is
    that specified through the RefType enum.

    The wrapped function will be called with the following signature:
        (context, builder, sig, args, iternext_result)
    '''
    pass
# WARNING: Decompyle incomplete


def call_getiter(context, builder, iterable_type, val):
    '''
    Call the `getiter()` implementation for the given *iterable_type*
    of value *val*, and return the corresponding LLVM inst.
    '''
    getiter_sig = typing.signature(iterable_type.iterator_type, iterable_type)
    getiter_impl = context.get_function('getiter', getiter_sig)
    return getiter_impl(builder, (val,))


def call_iternext(context, builder, iterator_type, val):
    '''
    Call the `iternext()` implementation for the given *iterator_type*
    of value *val*, and return a convenience _IternextResult() object
    reflecting the results.
    '''
    itemty = iterator_type.yield_type
    pair_type = types.Pair(itemty, types.boolean)
    iternext_sig = typing.signature(pair_type, iterator_type)
    iternext_impl = context.get_function('iternext', iternext_sig)
    val = iternext_impl(builder, (val,))
    pairobj = context.make_helper(builder, pair_type, val)
    return _IternextResult(context, builder, pairobj)


def call_len(context, builder, ty, val):
    """
    Call len() on the given value.  Return None if len() isn't defined on
    this type.
    """
    
    try:
        len_impl = context.get_function(len, typing.signature(types.intp, ty))
        return len_impl(builder, (val,))
    except NotImplementedError:
        return None


_ForIterLoop = collections.namedtuple('_ForIterLoop', ('value', 'do_break'))
for_iter = (lambda context, builder, iterable_type, val: pass# WARNING: Decompyle incomplete
)()

def impl_ret_new_ref(ctx, builder, retty, ret):
    '''
    The implementation returns a new reference.
    '''
    return ret


def impl_ret_borrowed(ctx, builder, retty, ret):
    '''
    The implementation returns a borrowed reference.
    This function automatically incref so that the implementation is
    returning a new reference.
    '''
    if ctx.enable_nrt:
        ctx.nrt.incref(builder, retty, ret)
    return ret


def impl_ret_untracked(ctx, builder, retty, ret):
    '''
    The return type is not a NRT object.
    '''
    return ret

force_error_model = (lambda context, model_name = ('numpy',): pass# WARNING: Decompyle incomplete
)()

def numba_typeref_ctor(*args, **kwargs):
    '''A stub for use internally by Numba when a call is emitted
    on a TypeRef.
    '''
    raise NotImplementedError('This function should not be executed.')
