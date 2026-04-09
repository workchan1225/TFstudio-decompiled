# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: abc.pyc (Python 3.11)

'''Abstract Base Classes (ABCs) according to PEP 3119.'''

def abstractmethod(funcobj):
    """A decorator indicating abstract methods.

    Requires that the metaclass is ABCMeta or derived from it.  A
    class that has a metaclass derived from ABCMeta cannot be
    instantiated unless all of its abstract methods are overridden.
    The abstract methods can be called using any of the normal
    'super' call mechanisms.  abstractmethod() may be used to declare
    abstract methods for properties and descriptors.

    Usage:

        class C(metaclass=ABCMeta):
            @abstractmethod
            def my_abstract_method(self, arg1, arg2, argN):
                ...
    """
    funcobj.__isabstractmethod__ = True
    return funcobj


class abstractclassmethod(classmethod):
    pass
# WARNING: Decompyle incomplete


class abstractstaticmethod(staticmethod):
    pass
# WARNING: Decompyle incomplete


class abstractproperty(property):
    """A decorator indicating abstract properties.

    Deprecated, use 'property' with 'abstractmethod' instead:

        class C(ABC):
            @property
            @abstractmethod
            def my_abstract_property(self):
                ...

    """
    __isabstractmethod__ = True


try:
    from _abc import get_cache_token, _abc_init, _abc_register, _abc_instancecheck, _abc_subclasscheck, _get_dump, _reset_registry, _reset_caches
    
    class ABCMeta(type):
        pass
    # WARNING: Decompyle incomplete

except ImportError:
    from _py_abc import ABCMeta, get_cache_token
    ABCMeta.__module__ = 'abc'


def update_abstractmethods(cls):
    '''Recalculate the set of abstract methods of an abstract class.

    If a class has had one of its abstract methods implemented after the
    class was created, the method will not be considered implemented until
    this function is called. Alternatively, if a new abstract method has been
    added to the class, it will only be considered an abstract method of the
    class after this function is called.

    This function should be called before any use is made of the class,
    usually in class decorators that add methods to the subject class.

    Returns cls, to allow usage as a class decorator.

    If cls is not an instance of ABCMeta, does nothing.
    '''
    if not hasattr(cls, '__abstractmethods__'):
        return cls
    abstracts = None()
    for scls in cls.__bases__:
        for name in getattr(scls, '__abstractmethods__', ()):
            value = getattr(cls, name, None)
            if getattr(value, '__isabstractmethod__', False):
                abstracts.add(name)
            for name, value in cls.__dict__.items():
                if getattr(value, '__isabstractmethod__', False):
                    abstracts.add(name)
                cls.__abstractmethods__ = frozenset(abstracts)
                return cls


def ABC():
    '''ABC'''
    __doc__ = 'Helper class that provides a standard way to create an ABC using\n    inheritance.\n    '
    __slots__ = ()

ABC = <NODE:27>(ABC, 'ABC', metaclass = ABCMeta)
