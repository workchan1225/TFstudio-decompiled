# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: properties.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Generic, TypeVar, cast, overload
_T = TypeVar('_T')
_U = TypeVar('_U')
if TYPE_CHECKING:
    from collections.abc import Callable
    from typing import Any, Protocol
    from typing_extensions import Self, TypeAlias
    _GetterCallable: 'TypeAlias' = Callable[(..., _T)]
    _GetterClassMethod: 'TypeAlias' = classmethod[(Any, [], _T)]
    _SetterCallable: 'TypeAlias' = Callable[([
        type[Any],
        _T], None)]
    _SetterClassMethod: 'TypeAlias' = classmethod[(Any, [
        _T], None)]
    
    def _ClassPropertyAttribute():
        '''_ClassPropertyAttribute'''
        
        def __get__(self = None, obj = None, objtype = None):
            pass

        
        def __set__(self = None, obj = None, value = None):
            pass


    _ClassPropertyAttribute = <NODE:27>(_ClassPropertyAttribute, '_ClassPropertyAttribute', Protocol[_T])

def NonDataProperty():
    '''NonDataProperty'''
    __doc__ = "Much like the property builtin, but only implements __get__,\n    making it a non-data property, and can be subsequently reset.\n\n    See http://users.rcn.com/python/download/Descriptor.htm for more\n    information.\n\n    >>> class X(object):\n    ...   @NonDataProperty\n    ...   def foo(self):\n    ...     return 3\n    >>> x = X()\n    >>> x.foo\n    3\n    >>> x.foo = 4\n    >>> x.foo\n    4\n\n    '...' below should be 'jaraco.classes' but for pytest-dev/pytest#3396\n    >>> X.foo\n    <....properties.NonDataProperty object at ...>\n    "
    
    def __init__(self = None, fget = None):
        pass
    # WARNING: Decompyle incomplete

    __get__ = (lambda self = None, obj = None, objtype = overload: pass)()
    __get__ = (lambda self = None, obj = None, objtype = overload: pass)()
    
    def __get__(self = None, obj = None, objtype = None):
        pass
    # WARNING: Decompyle incomplete


NonDataProperty = <NODE:27>(NonDataProperty, 'NonDataProperty', Generic[(_T, _U)])

def classproperty():
    '''classproperty'''
    fset: '_ClassPropertyAttribute[_SetterClassMethod[_T] | None]' = "\n    Like @property but applies at the class level.\n\n\n    >>> class X(metaclass=classproperty.Meta):\n    ...   val = None\n    ...   @classproperty\n    ...   def foo(cls):\n    ...     return cls.val\n    ...   @foo.setter\n    ...   def foo(cls, val):\n    ...     cls.val = val\n    >>> X.foo\n    >>> X.foo = 3\n    >>> X.foo\n    3\n    >>> x = X()\n    >>> x.foo\n    3\n    >>> X.foo = 4\n    >>> x.foo\n    4\n\n    Setting the property on an instance affects the class.\n\n    >>> x.foo = 5\n    >>> x.foo\n    5\n    >>> X.foo\n    5\n    >>> vars(x)\n    {}\n    >>> X().foo\n    5\n\n    Attempting to set an attribute where no setter was defined\n    results in an AttributeError:\n\n    >>> class GetOnly(metaclass=classproperty.Meta):\n    ...   @classproperty\n    ...   def foo(cls):\n    ...     return 'bar'\n    >>> GetOnly.foo = 3\n    Traceback (most recent call last):\n    ...\n    AttributeError: can't set attribute\n\n    It is also possible to wrap a classmethod or staticmethod in\n    a classproperty.\n\n    >>> class Static(metaclass=classproperty.Meta):\n    ...   @classproperty\n    ...   @classmethod\n    ...   def foo(cls):\n    ...     return 'foo'\n    ...   @classproperty\n    ...   @staticmethod\n    ...   def bar():\n    ...     return 'bar'\n    >>> Static.foo\n    'foo'\n    >>> Static.bar\n    'bar'\n\n    *Legacy*\n\n    For compatibility, if the metaclass isn't specified, the\n    legacy behavior will be invoked.\n\n    >>> class X:\n    ...   val = None\n    ...   @classproperty\n    ...   def foo(cls):\n    ...     return cls.val\n    ...   @foo.setter\n    ...   def foo(cls, val):\n    ...     cls.val = val\n    >>> X.foo\n    >>> X.foo = 3\n    >>> X.foo\n    3\n    >>> x = X()\n    >>> x.foo\n    3\n    >>> X.foo = 4\n    >>> x.foo\n    4\n\n    Note, because the metaclass was not specified, setting\n    a value on an instance does not have the intended effect.\n\n    >>> x.foo = 5\n    >>> x.foo\n    5\n    >>> X.foo  # should be 5\n    4\n    >>> vars(x)  # should be empty\n    {'foo': 5}\n    >>> X().foo  # should be 5\n    4\n    "
    
    class Meta(type):
        pass
    # WARNING: Decompyle incomplete

    
    def __init__(self = None, fget = None, fset = None):
        self.fget = self._ensure_method(fget)
        self.fset = fset
        if fset:
            self.setter(fset)
            return None

    
    def __get__(self = None, instance = None, owner = None):
        return self.fget.__get__(None, owner)()

    
    def __set__(self = None, owner = None, value = None):
        if not self.fset:
            raise AttributeError("can't set attribute")
        if type(owner) is not classproperty.Meta:
            owner = type(owner)
        return self.fset.__get__(None, cast('type[object]', owner))(value)

    
    def setter(self = None, fset = None):
        self.fset = self._ensure_method(fset)
        return self

    _ensure_method = (lambda cls = None, fn = overload: pass)()()
    _ensure_method = (lambda cls = None, fn = overload: pass)()()
    _ensure_method = (lambda cls = None, fn = None: needs_method = not isinstance(fn, (classmethod, staticmethod))classmethod(fn) if needs_method else fn)()

classproperty = <NODE:27>(classproperty, 'classproperty', Generic[_T])
