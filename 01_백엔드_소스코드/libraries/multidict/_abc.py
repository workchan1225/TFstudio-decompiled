# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _abc.pyc (Python 3.11)

import abc
from collections.abc import Iterable, Mapping, MutableMapping
from typing import TYPE_CHECKING, Protocol, TypeVar, Union, overload
if TYPE_CHECKING:
    from _multidict_py import istr
else:
    istr = str
_V = TypeVar('_V')
_V_co = TypeVar('_V_co', covariant = True)
_T = TypeVar('_T')

def SupportsKeys():
    '''SupportsKeys'''
    
    def keys(self = None):
        pass

    
    def __getitem__(self = None, key = None):
        pass


SupportsKeys = <NODE:27>(SupportsKeys, 'SupportsKeys', Protocol[_V_co])

def SupportsIKeys():
    '''SupportsIKeys'''
    
    def keys(self = None):
        pass

    
    def __getitem__(self = None, key = None):
        pass


SupportsIKeys = <NODE:27>(SupportsIKeys, 'SupportsIKeys', Protocol[_V_co])
MDArg = Union[(SupportsKeys[_V], SupportsIKeys[_V], Iterable[tuple[(str, _V)]], None)]

def MultiMapping():
    '''MultiMapping'''
    getall = (lambda self = None, key = None: pass)()
    getall = (lambda self = None, key = None, default = overload: pass)()
    getall = (lambda self = None, key = None, default = abc.abstractmethod: pass)()
    getone = (lambda self = None, key = None: pass)()
    getone = (lambda self = None, key = None, default = overload: pass)()
    getone = (lambda self = None, key = None, default = abc.abstractmethod: pass)()

MultiMapping = <NODE:27>(MultiMapping, 'MultiMapping', Mapping[(str, _V_co)])

def MutableMultiMapping():
    '''MutableMultiMapping'''
    add = (lambda self = None, key = None, value = abc.abstractmethod: pass)()
    extend = (lambda self = None, arg = None: pass)()
    merge = (lambda self = None, arg = None: pass)()
    popone = (lambda self = None, key = None: pass)()
    popone = (lambda self = None, key = None, default = overload: pass)()
    popone = (lambda self = None, key = None, default = abc.abstractmethod: pass)()
    popall = (lambda self = None, key = None: pass)()
    popall = (lambda self = None, key = None, default = overload: pass)()
    popall = (lambda self = None, key = None, default = abc.abstractmethod: pass)()

MutableMultiMapping = <NODE:27>(MutableMultiMapping, 'MutableMultiMapping', MultiMapping[_V], MutableMapping[(str, _V)])
