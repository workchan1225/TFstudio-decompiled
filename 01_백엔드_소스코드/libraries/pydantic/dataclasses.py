# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dataclasses.pyc (Python 3.11)

'''Provide an enhanced dataclass that performs validation.'''
from __future__ import annotations as _annotations
import dataclasses
import functools
import sys
import types
from typing import TYPE_CHECKING, Any, Callable, Generic, Literal, NoReturn, TypeVar, overload
from warnings import warn
from typing_extensions import TypeGuard, dataclass_transform
from _internal import _config, _decorators, _mock_val_ser, _namespace_utils, _typing_extra
from _internal import _dataclasses as _pydantic_dataclasses
from _migration import getattr_migration
from config import ConfigDict
from errors import PydanticUserError
from fields import Field, FieldInfo, PrivateAttr
if TYPE_CHECKING:
    from _internal._dataclasses import PydanticDataclass
    from _internal._namespace_utils import MappingNamespace
__all__ = ('dataclass', 'rebuild_dataclass')
_T = TypeVar('_T')
if sys.version_info >= (3, 10):
    dataclass = (lambda *: pass)()()
    dataclass = (lambda _cls = None, *, init: pass)()()
else:
    dataclass = (lambda *: pass)()()
    dataclass = (lambda _cls = None, *, init: pass)()()
dataclass = (lambda _cls = None, *, init: pass# WARNING: Decompyle incomplete
)()

def _pydantic_fields_complete(cls = None):
    '''Return whether the fields where successfully collected (i.e. type hints were successfully resolves).

    This is a private property, not meant to be used outside Pydantic.
    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(cls.__pydantic_fields__.values()())

__getattr__ = getattr_migration(__name__)
if sys.version_info < (3, 11):
    
    def _call_initvar(*args, **kwargs):
        """This function does nothing but raise an error that is as similar as possible to what you'd get
        if you were to try calling `InitVar[int]()` without this monkeypatch. The whole purpose is just
        to ensure typing._type_check does not error if the type hint evaluates to `InitVar[<parameter>]`.
        """
        raise TypeError("'InitVar' object is not callable")

    dataclasses.InitVar.__call__ = _call_initvar

def rebuild_dataclass(cls = None, *, force, raise_errors, _parent_namespace_depth, _types_namespace):
    '''Try to rebuild the pydantic-core schema for the dataclass.

    This may be necessary when one of the annotations is a ForwardRef which could not be resolved during
    the initial attempt to build the schema, and automatic rebuilding fails.

    This is analogous to `BaseModel.model_rebuild`.

    Args:
        cls: The class to rebuild the pydantic-core schema for.
        force: Whether to force the rebuilding of the schema, defaults to `False`.
        raise_errors: Whether to raise errors, defaults to `True`.
        _parent_namespace_depth: The depth level of the parent namespace, defaults to 2.
        _types_namespace: The types namespace, defaults to `None`.

    Returns:
        Returns `None` if the schema is already "complete" and rebuilding was not required.
        If rebuilding _was_ required, returns `True` if rebuilding was successful, otherwise `False`.
    '''
    if force and cls.__pydantic_complete__:
        return None
# WARNING: Decompyle incomplete


def is_pydantic_dataclass(class_ = None):
    '''Whether a class is a pydantic dataclass.

    Args:
        class_: The class.

    Returns:
        `True` if the class is a pydantic dataclass, `False` otherwise.
    '''
    
    try:
        if '__is_pydantic_dataclass__' in class_.__dict__:
            pass
        return dataclasses.is_dataclass(class_)
    except AttributeError:
        return False
