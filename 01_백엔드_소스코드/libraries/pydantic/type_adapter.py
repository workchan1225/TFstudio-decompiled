# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: type_adapter.pyc (Python 3.11)

'''Type adapter specification.'''
from __future__ import annotations as _annotations
import sys
import types
from collections.abc import Callable, Iterable
from dataclasses import is_dataclass
from types import FrameType
from typing import Any, Generic, Literal, TypeVar, cast, final, overload
from pydantic_core import CoreSchema, SchemaSerializer, SchemaValidator, Some
from typing_extensions import ParamSpec, is_typeddict
from pydantic.errors import PydanticUserError
from pydantic.main import BaseModel, IncEx
from _internal import _config, _generate_schema, _mock_val_ser, _namespace_utils, _repr, _typing_extra, _utils
from config import ConfigDict, ExtraValues
from errors import PydanticUndefinedAnnotation
from json_schema import DEFAULT_REF_TEMPLATE, GenerateJsonSchema, JsonSchemaKeyT, JsonSchemaMode, JsonSchemaValue
from plugin._schema_validator import PluggableSchemaValidator, create_schema_validator
T = TypeVar('T')
R = TypeVar('R')
P = ParamSpec('P')
TypeAdapterT = TypeVar('TypeAdapterT', bound = 'TypeAdapter')

def _getattr_no_parents(obj = None, attribute = None):
    '''Returns the attribute value without attempting to look up attributes from parent types.'''
    pass
# WARNING: Decompyle incomplete


def _type_has_config(type_ = None):
    '''Returns whether the type has config.'''
    if not _typing_extra.annotated_type(type_):
        type_ = type_
        
        try:
            if not issubclass(type_, BaseModel):
                if not is_dataclass(type_):
                    return is_typeddict(type_)
                except TypeError:
                    return False



def TypeAdapter():
    '''TypeAdapter'''
    pydantic_complete: 'bool' = '!!! abstract "Usage Documentation"\n        [`TypeAdapter`](../concepts/type_adapter.md)\n\n    Type adapters provide a flexible way to perform validation and serialization based on a Python type.\n\n    A `TypeAdapter` instance exposes some of the functionality from `BaseModel` instance methods\n    for types that do not have such methods (such as dataclasses, primitive types, and more).\n\n    **Note:** `TypeAdapter` instances are not types, and cannot be used as type annotations for fields.\n\n    Args:\n        type: The type associated with the `TypeAdapter`.\n        config: Configuration for the `TypeAdapter`, should be a dictionary conforming to\n            [`ConfigDict`][pydantic.config.ConfigDict].\n\n            !!! note\n                You cannot provide a configuration when instantiating a `TypeAdapter` if the type you\'re using\n                has its own config that cannot be overridden (ex: `BaseModel`, `TypedDict`, and `dataclass`). A\n                [`type-adapter-config-unused`](../errors/usage_errors.md#type-adapter-config-unused) error will\n                be raised in this case.\n        _parent_depth: Depth at which to search for the [parent frame][frame-objects]. This frame is used when\n            resolving forward annotations during schema building, by looking for the globals and locals of this\n            frame. Defaults to 2, which will result in the frame where the `TypeAdapter` was instantiated.\n\n            !!! note\n                This parameter is named with an underscore to suggest its private nature and discourage use.\n                It may be deprecated in a minor version, so we only recommend using it if you\'re comfortable\n                with potential change in behavior/support. It\'s default value is 2 because internally,\n                the `TypeAdapter` class makes another call to fetch the frame.\n        module: The module that passes to plugin if provided.\n\n    Attributes:\n        core_schema: The core schema for the type.\n        validator: The schema validator for the type.\n        serializer: The schema serializer for the type.\n        pydantic_complete: Whether the core schema for the type is successfully built.\n\n    ??? tip "Compatibility with `mypy`"\n        Depending on the type used, `mypy` might raise an error when instantiating a `TypeAdapter`. As a workaround, you can explicitly\n        annotate your variable:\n\n        ```py\n        from typing import Union\n\n        from pydantic import TypeAdapter\n\n        ta: TypeAdapter[Union[str, int]] = TypeAdapter(Union[str, int])  # type: ignore[arg-type]\n        ```\n\n    ??? info "Namespace management nuances and implementation details"\n\n        Here, we collect some notes on namespace management, and subtle differences from `BaseModel`:\n\n        `BaseModel` uses its own `__module__` to find out where it was defined\n        and then looks for symbols to resolve forward references in those globals.\n        On the other hand, `TypeAdapter` can be initialized with arbitrary objects,\n        which may not be types and thus do not have a `__module__` available.\n        So instead we look at the globals in our parent stack frame.\n\n        It is expected that the `ns_resolver` passed to this function will have the correct\n        namespace for the type we\'re adapting. See the source code for `TypeAdapter.__init__`\n        and `TypeAdapter.rebuild` for various ways to construct this namespace.\n\n        This works for the case where this function is called in a module that\n        has the target of forward references in its scope, but\n        does not always work for more complex cases.\n\n        For example, take the following:\n\n        ```python {title="a.py"}\n        IntList = list[int]\n        OuterDict = dict[str, \'IntList\']\n        ```\n\n        ```python {test="skip" title="b.py"}\n        from a import OuterDict\n\n        from pydantic import TypeAdapter\n\n        IntList = int  # replaces the symbol the forward reference is looking for\n        v = TypeAdapter(OuterDict)\n        v({\'x\': 1})  # should fail but doesn\'t\n        ```\n\n        If `OuterDict` were a `BaseModel`, this would work because it would resolve\n        the forward reference within the `a.py` namespace.\n        But `TypeAdapter(OuterDict)` can\'t determine what module `OuterDict` came from.\n\n        In other words, the assumption that _all_ forward references exist in the\n        module we are being called from is not technically always true.\n        Although most of the time it is and it works fine for recursive models and such,\n        `BaseModel`\'s behavior isn\'t perfect either and _can_ break in similar ways,\n        so there is no right or wrong between the two.\n\n        But at the very least this behavior is _subtly_ different from `BaseModel`\'s.\n    '
    __init__ = (lambda self = None, type = None, *, config, _parent_depth: pass)()
    __init__ = (lambda self = None, type = None, *, config, _parent_depth: pass)()
    
    def __init__(self = None, type = None, *, config, _parent_depth, module):
        pass
    # WARNING: Decompyle incomplete

    
    def _fetch_parent_frame(self = None):
        frame = sys._getframe(self._parent_depth)
        if frame.f_globals.get('__name__') == 'typing':
            return frame.f_back

    
    def _init_core_attrs(self = None, ns_resolver = None, force = None, raise_errors = (False,)):
        '''Initialize the core schema, validator, and serializer for the type.

        Args:
            ns_resolver: The namespace resolver to use when building the core schema for the adapted type.
            force: Whether to force the construction of the core schema, validator, and serializer.
                If `force` is set to `False` and `_defer_build` is `True`, the core schema, validator, and serializer will be set to mocks.
            raise_errors: Whether to raise errors if initializing any of the core attrs fails.

        Returns:
            `True` if the core schema, validator, and serializer were successfully initialized, otherwise `False`.

        Raises:
            PydanticUndefinedAnnotation: If `PydanticUndefinedAnnotation` occurs in`__get_pydantic_core_schema__`
                and `raise_errors=True`.
        '''
        if force and self._defer_build:
            _mock_val_ser.set_type_adapter_mocks(self)
            self.pydantic_complete = False
            return False
        
        try:
            self.core_schema = _getattr_no_parents(self._type, '__pydantic_core_schema__')
            self.validator = _getattr_no_parents(self._type, '__pydantic_validator__')
            self.serializer = _getattr_no_parents(self._type, '__pydantic_serializer__')
            if isinstance(self.core_schema, _mock_val_ser.MockCoreSchema) and isinstance(self.validator, _mock_val_ser.MockValSer) or isinstance(self.serializer, _mock_val_ser.MockValSer):
                raise AttributeError()
        except AttributeError:
            config_wrapper = _config.ConfigWrapper(self._config)
            schema_generator = _generate_schema.GenerateSchema(config_wrapper, ns_resolver = ns_resolver)
            core_schema = schema_generator.generate_schema(self._type)
        except PydanticUndefinedAnnotation:
            if raise_errors:
                raise 
            _mock_val_ser.set_type_adapter_mocks(self)
            return False

        self.core_schema = schema_generator.clean_schema(core_schema)

    _defer_build = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    _model_config = (lambda self = None:
