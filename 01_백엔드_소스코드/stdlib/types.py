# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

"""
Define names for built-in types that aren't directly accessible as a builtin.
"""
import sys

def _f():
    pass

FunctionType = type(_f)
LambdaType = type((lambda : pass))
CodeType = type(_f.__code__)
MappingProxyType = type(type.__dict__)
SimpleNamespace = type(sys.implementation)

def _cell_factory():
    pass
# WARNING: Decompyle incomplete

CellType = type(_cell_factory())

def _g():
    pass
# WARNING: Decompyle incomplete

GeneratorType = type(_g())

async def _c():
    pass
# WARNING: Decompyle incomplete

_c = _c()
CoroutineType = type(_c)
_c.close()

def _ag():
    pass
# WARNING: Decompyle incomplete

_ag = _ag()
AsyncGeneratorType = type(_ag)

class _C:
    
    def _m(self):
        pass


MethodType = type(_C()._m)
BuiltinFunctionType = type(len)
BuiltinMethodType = type([].append)
WrapperDescriptorType = type(object.__init__)
MethodWrapperType = type(object().__str__)
MethodDescriptorType = type(str.join)
ClassMethodDescriptorType = type(dict.__dict__['fromkeys'])
ModuleType = type(sys)

try:
    raise TypeError
except TypeError:
    exc = None
    TracebackType = type(exc.__traceback__)
    FrameType = type(exc.__traceback__.tb_frame)
    exc = None
    del exc
except:
    exc = None
    del exc

GetSetDescriptorType = type(FunctionType.__code__)
MemberDescriptorType = type(FunctionType.__globals__)
del sys
del _f
del _g
del _C
del _c
del _ag

def new_class(name, bases, kwds, exec_body = ((), None, None)):
    '''Create a class object dynamically using the appropriate metaclass.'''
    resolved_bases = resolve_bases(bases)
    (meta, ns, kwds) = prepare_class(name, resolved_bases, kwds)
# WARNING: Decompyle incomplete


def resolve_bases(bases):
    '''Resolve MRO entries dynamically as specified by PEP 560.'''
    new_bases = list(bases)
    updated = False
    shift = 0
    for i, base in enumerate(bases):
        if isinstance(base, type):
            continue
        if not hasattr(base, '__mro_entries__'):
            continue
        new_base = base.__mro_entries__(bases)
        updated = True
        if not isinstance(new_base, tuple):
            raise TypeError('__mro_entries__ must return a tuple')
        new_bases[i + shift:i + shift + 1] = new_base
        shift += len(new_base) - 1
        if not updated:
            return bases
        return None(new_bases)


def prepare_class(name, bases, kwds = ((), None)):
    """Call the __prepare__ method of the appropriate metaclass.

    Returns (metaclass, namespace, kwds) as a 3-tuple

    *metaclass* is the appropriate metaclass
    *namespace* is the prepared class namespace
    *kwds* is an updated copy of the passed in kwds argument with any
    'metaclass' entry removed. If no kwds argument is passed in, this will
    be an empty dict.
    """
    pass
# WARNING: Decompyle incomplete


def _calculate_meta(meta, bases):
    '''Calculate the most derived metaclass.'''
    winner = meta
    for base in bases:
        base_meta = type(base)
        if issubclass(winner, base_meta):
            continue
        if issubclass(base_meta, winner):
            winner = base_meta
            continue
        raise TypeError('metaclass conflict: the metaclass of a derived class must be a (non-strict) subclass of the metaclasses of all its bases')
        return winner


class DynamicClassAttribute:
    """Route attribute access on a class to __getattr__.

    This is a descriptor, used to define attributes that act differently when
    accessed through an instance and through a class.  Instance access remains
    normal, but access to an attribute through a class will be routed to the
    class's __getattr__ method; this is done by raising AttributeError.

    This allows one to have properties active on an instance, and have virtual
    attributes on the class with the same name.  (Enum used this between Python
    versions 3.4 - 3.9 .)

    Subclass from this to use a different method of accessing virtual attributes
    and still be treated properly by the inspect module. (Enum uses this since
    Python 3.10 .)

    """
    
    def __init__(self, fget, fset, fdel, doc = (None, None, None, None)):
