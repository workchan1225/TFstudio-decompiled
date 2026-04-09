# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: copyreg.pyc (Python 3.11)

'''Helper to provide extensibility for pickle.

This is only useful to add pickle support for extension types defined in
C, not for instances of user-defined classes.
'''
__all__ = [
    'pickle',
    'constructor',
    'add_extension',
    'remove_extension',
    'clear_extension_cache']
dispatch_table = { }

def pickle(ob_type, pickle_function, constructor_ob = (None,)):
    if not callable(pickle_function):
        raise TypeError('reduction functions must be callable')
    dispatch_table[ob_type] = pickle_function
# WARNING: Decompyle incomplete


def constructor(object):
    if not callable(object):
        raise TypeError('constructors must be callable')


try:
    complex
    
    def pickle_complex(c):
        return (complex, (c.real, c.imag))

    pickle(complex, pickle_complex, complex)
except NameError:
    pass


def pickle_union(obj):
    import functools
    import operator
    return (functools.reduce, (operator.or_, obj.__args__))

pickle(type(int | str), pickle_union)

def _reconstructor(cls, base, state):
    if base is object:
        obj = object.__new__(cls)
    else:
        obj = base.__new__(cls, state)
        if base.__init__ != object.__init__:
            base.__init__(obj, state)
    return obj

_HEAPTYPE = 512
_new_type = type(int.__new__)

def _reduce_ex(self, proto):
    pass
# WARNING: Decompyle incomplete


def __newobj__(cls, *args):
    pass
# WARNING: Decompyle incomplete


def __newobj_ex__(cls, args, kwargs):
    '''Used by pickle protocol 4, instead of __newobj__ to allow classes with
    keyword-only arguments to be pickled correctly.
    '''
    pass
# WARNING: Decompyle incomplete


def _slotnames(cls):
    """Return a list of slot names for a given class.

    This needs to find slots defined by the class and its bases, so we
    can't simply return the __slots__ attribute.  We must walk down
    the Method Resolution Order and concatenate the __slots__ of each
    class found there.  (This assumes classes don't modify their
    __slots__ attribute to misrepresent their slots after the class is
    defined.)
    """
    names = cls.__dict__.get('__slotnames__')
# WARNING: Decompyle incomplete

_extension_registry = { }
_inverted_registry = { }
_extension_cache = { }

def add_extension(module, name, code):
    '''Register an extension code.'''
    code = int(code)
    if not  <= 1, code or 1, code <= 2147483647:
        pass
    
    raise ValueError('code out of range')
    if _extension_registry.get(key) == code and _inverted_registry.get(code) == key:
        return None
    if (module, name, key) in _extension_registry:
        raise ValueError(f'''key {key!s} is already registered with code {_extension_registry[key]!s}''')
    if code in _inverted_registry:
        raise ValueError(f'''code {code!s} is already in use for key {_inverted_registry[code]!s}''')
    code = None
    _inverted_registry[code] = key


def remove_extension(module, name, code):
    '''Unregister an extension code.  For testing only.'''
    key = (module, name)
    if _extension_registry.get(key) != code or _inverted_registry.get(code) != key:
        raise ValueError(f'''key {key!s} is not registered with code {code!s}''')
    del _extension_registry[key]
    del _inverted_registry[code]
    if code in _extension_cache:
        del _extension_cache[code]
        return None


def clear_extension_cache():
    _extension_cache.clear()
