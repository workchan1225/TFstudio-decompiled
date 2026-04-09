# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _proxy.pyc (Python 3.11)

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Iterable, cast
from typing_extensions import override
T = TypeVar('T')

def LazyProxy():
    '''LazyProxy'''
    __doc__ = 'Implements data methods to pretend that an instance is another instance.\n\n    This includes forwarding attribute access and other methods.\n    '
    
    def __getattr__(self = None, attr = None):
        proxied = self.__get_proxied__()
        if isinstance(proxied, LazyProxy):
            return proxied
        return None(proxied, attr)

    __repr__ = (lambda self = None: proxied = self.__get_proxied__()if isinstance(proxied, LazyProxy):
proxied.__class__.__name__None(self.__get_proxied__()))()
    __str__ = (lambda self = None: proxied = self.__get_proxied__()if isinstance(proxied, LazyProxy):
proxied.__class__.__name__None(proxied))()
    __dir__ = (lambda self = None: proxied = self.__get_proxied__()if isinstance(proxied, LazyProxy):
[]None.__dir__())()
    __class__ = (lambda self = None: try:
proxied = self.__get_proxied__()except Exception:
if issubclass(type(proxied), LazyProxy):
type(proxied)None.__class__)()()
    
    def __get_proxied__(self = None):
        return self.__load__()

    
    def __as_proxied__(self = None):
        '''Helper method that returns the current proxy, typed as the loaded object'''
        return cast(T, self)

    __load__ = (lambda self = None: pass)()

LazyProxy = <NODE:27>(LazyProxy, 'LazyProxy', Generic[T], ABC)
