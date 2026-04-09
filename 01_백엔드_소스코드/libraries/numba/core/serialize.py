# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: serialize.pyc (Python 3.11)

'''
Serialization support for compiled functions.
'''
import sys
import abc
import io
import copyreg
import pickle
from numba import cloudpickle
from llvmlite import ir

def _rebuild_reduction(cls, *args):
    '''
    Global hook to rebuild a given class from its __reduce__ arguments.
    '''
    pass
# WARNING: Decompyle incomplete

_unpickled_memo = { }

def _numba_unpickle(address, bytedata, hashed):
    '''Used by `numba_unpickle` from _helperlib.c

    Parameters
    ----------
    address : int
    bytedata : bytes
    hashed : bytes

    Returns
    -------
    obj : object
        unpickled object
    '''
    key = (address, hashed)
    
    try:
        obj = _unpickled_memo[key]
    except KeyError:
        _unpickled_memo[key] = cloudpickle.loads(bytedata)
        obj = cloudpickle.loads(bytedata)

    return obj


def dumps(obj):
    '''Similar to `pickle.dumps()`. Returns the serialized object in bytes.
    '''
    pickler = NumbaPickler
    buf = io.BytesIO()
    p = pickler(buf, protocol = 4)
    p.dump(obj)
    pickled = buf.getvalue()
    None(None, None)


def runtime_build_excinfo_struct(static_exc, exc_args):
    (exc, static_args, locinfo) = cloudpickle.loads(static_exc)
    real_args = []
    exc_args_iter = iter(exc_args)
    for arg in static_args:
        if isinstance(arg, ir.Value):
            real_args.append(next(exc_args_iter))
            continue
        real_args.append(arg)
        return (exc, tuple(real_args), locinfo)

loads = cloudpickle.loads

class _CustomPickled:
    '''A wrapper for objects that must be pickled with `NumbaPickler`.

    Standard `pickle` will pick up the implementation registered via `copyreg`.
    This will spawn a `NumbaPickler` instance to serialize the data.

    `NumbaPickler` overrides the handling of this type so as not to spawn a
    new pickler for the object when it is already being pickled by a
    `NumbaPickler`.
    '''
    __slots__ = ('ctor', 'states')
    
    def __init__(self, ctor, states):
        self.ctor = ctor
        self.states = states

    
    def _reduce(self):
        return (_CustomPickled._rebuild, (self.ctor, self.states))

    _rebuild = (lambda cls, ctor, states: cls(ctor, states))()


def _unpickle__CustomPickled(serialized):
    '''standard unpickling for `_CustomPickled`.

    Uses `NumbaPickler` to load.
    '''
    (ctor, states) = loads(serialized)
    return _CustomPickled(ctor, states)


def _pickle__CustomPickled(cp):
    '''standard pickling for `_CustomPickled`.

    Uses `NumbaPickler` to dump.
    '''
    serialized = dumps((cp.ctor, cp.states))
    return (_unpickle__CustomPickled, (serialized,))

copyreg.pickle(_CustomPickled, _pickle__CustomPickled)

def custom_reduce(cls, states):
    '''For customizing object serialization in `__reduce__`.

    Object states provided here are used as keyword arguments to the
    `._rebuild()` class method.

    Parameters
    ----------
    states : dict
        Dictionary of object states to be serialized.

    Returns
    -------
    result : tuple
        This tuple conforms to the return type requirement for `__reduce__`.
    '''
    return (custom_rebuild, (_CustomPickled(cls, states),))


def custom_rebuild(custom_pickled):
    '''Customized object deserialization.

    This function is referenced internally by `custom_reduce()`.
    '''
    states = custom_pickled.states
    cls = custom_pickled.ctor
# WARNING: Decompyle incomplete


def is_serialiable(obj):
    '''Check if *obj* can be serialized.

    Parameters
    ----------
    obj : object

    Returns
    --------
    can_serialize : bool
    '''
    fout = io.BytesIO()
    pickler = NumbaPickler(fout)
    pickler.dump(obj)
    None(None, None)
    return True
    except pickle.PicklingError:
        None(None, None)
        return False
    with None:
        if not None:
            pass


def _no_pickle(obj):
    raise pickle.PicklingError(f'''Pickling of {type(obj)} is unsupported''')


def disable_pickling(typ):
    '''This is called on a type to disable pickling
    '''
    NumbaPickler.disabled_types.add(typ)
    return typ


class NumbaPickler(cloudpickle.CloudPickler):
    pass
# WARNING: Decompyle incomplete


def _custom_reduce__custompickled(cp):
    return cp._reduce()

NumbaPickler.dispatch_table[_CustomPickled] = _custom_reduce__custompickled

class ReduceMixin(abc.ABC):
    '''A mixin class for objects that should be reduced by the NumbaPickler
    instead of the standard pickler.
    '''
    _reduce_states = (lambda self: raise NotImplementedError)()
    _rebuild = (lambda cls: raise NotImplementedError)()()
    
    def _reduce_class(self):
        return self.__class__

    
    def __reduce__(self):
        return custom_reduce(self._reduce_class(), self._reduce_states())



class PickleCallableByPath:
    '''Wrap a callable object to be pickled by path to workaround limitation
    in pickling due to non-pickleable objects in function non-locals.

    Note:
    - Do not use this as a decorator.
    - Wrapped object must be a global that exist in its parent module and it
      can be imported by `from the_module import the_object`.

    Usage:

    >>> def my_fn(x):
    >>>     ...
    >>> wrapped_fn = PickleCallableByPath(my_fn)
    >>> # refer to `wrapped_fn` instead of `my_fn`
    '''
    
    def __init__(self, fn):
        self._fn = fn

    
    def __call__(self, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def __reduce__(self):
        return (type(self)._rebuild, (self._fn.__module__, self._fn.__name__))

    _rebuild = (lambda cls, modname, fn_path: cls(getattr(sys.modules[modname], fn_path)))()
