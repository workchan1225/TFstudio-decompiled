# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _typedattr.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, Mapping
from typing import Any, TypeVar, final, overload
from _exceptions import TypedAttributeLookupError
T_Attr = TypeVar('T_Attr')
T_Default = TypeVar('T_Default')
undefined = object()

def typed_attribute():
    '''Return a unique object, used to mark typed attributes.'''
    return object()


class TypedAttributeSet:
    pass
# WARNING: Decompyle incomplete


class TypedAttributeProvider:
    '''Base class for classes that wish to provide typed extra attributes.'''
    extra_attributes = (lambda self = None: { })()
    extra = (lambda self = None, attribute = None: pass)()
    extra = (lambda self = None, attribute = None, default = overload: pass)()
    extra = (lambda self = None, attribute = None, default = final: try:
getter = self.extra_attributes[attribute]except KeyError:
if default is undefined:
raise TypedAttributeLookupError('Attribute not found'), Nonegetter())()
