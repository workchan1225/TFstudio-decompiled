# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _dataclasses.pyc (Python 3.11)

'''Private logic for creating pydantic dataclasses.'''
from __future__ import annotations as _annotations
import copy
import dataclasses
import sys
import warnings
from collections.abc import Generator
from contextlib import contextmanager
from functools import partial
from typing import TYPE_CHECKING, Any, ClassVar, Protocol, cast
from pydantic_core import ArgsKwargs, SchemaSerializer, SchemaValidator, core_schema
from typing_extensions import TypeAlias, TypeIs
from errors import PydanticUndefinedAnnotation
from fields import FieldInfo
from plugin._schema_validator import PluggableSchemaValidator, create_schema_validator
from warnings import PydanticDeprecatedSince20
from  import _config, _decorators
from _fields import collect_dataclass_fields
from _generate_schema import GenerateSchema, InvalidSchemaError
from _generics import get_standard_typevars_map
from _mock_val_ser import set_dataclass_mocks
from _namespace_utils import NsResolver
from _signature import generate_pydantic_signature
from _utils import LazyClassAttribute
if TYPE_CHECKING:
    from _typeshed import DataclassInstance as StandardDataclass
    from config import ConfigDict
    
    class PydanticDataclass(Protocol, StandardDataclass):
        __pydantic_validator__: 'ClassVar[SchemaValidator | PluggableSchemaValidator]' = 'A protocol containing attributes only available once a class has been decorated as a Pydantic dataclass.\n\n        Attributes:\n            __pydantic_config__: Pydantic-specific configuration settings for the dataclass.\n            __pydantic_complete__: Whether dataclass building is completed, or if there are still undefined fields.\n            __pydantic_core_schema__: The pydantic-core schema used to build the SchemaValidator and SchemaSerializer.\n            __pydantic_decorators__: Metadata containing the decorators defined on the dataclass.\n            __pydantic_fields__: Metadata about the fields defined on the dataclass.\n            __pydantic_serializer__: The pydantic-core SchemaSerializer used to dump instances of the dataclass.\n            __pydantic_validator__: The pydantic-core SchemaValidator used to validate instances of the dataclass.\n        '
        __pydantic_fields_complete__ = (lambda cls = None: pass)()


def set_dataclass_fields(cls = None, config_wrapper = None, ns_resolver = None):
    '''Collect and set `cls.__pydantic_fields__`.

    Args:
        cls: The class.
        config_wrapper: The config wrapper instance.
        ns_resolver: Namespace resolver to use when getting dataclass annotations.
    '''
    typevars_map = get_standard_typevars_map(cls)
    fields = collect_dataclass_fields(cls, ns_resolver = ns_resolver, typevars_map = typevars_map, config_wrapper = config_wrapper)
    cls.__pydantic_fields__ = fields


def complete_dataclass(cls = None, config_wrapper = None, *, raise_errors, ns_resolver, _force_build):
    '''Finish building a pydantic dataclass.

    This logic is called on a class which has already been wrapped in `dataclasses.dataclass()`.

    This is somewhat analogous to `pydantic._internal._model_construction.complete_model_class`.

    Args:
        cls: The class.
        config_wrapper: The config wrapper instance.
        raise_errors: Whether to raise errors, defaults to `True`.
        ns_resolver: The namespace resolver instance to use when collecting dataclass fields
            and during schema building.
        _force_build: Whether to force building the dataclass, no matter if
            [`defer_build`][pydantic.config.ConfigDict.defer_build] is set.

    Returns:
        `True` if building a pydantic dataclass is successfully completed, `False` otherwise.

    Raises:
        PydanticUndefinedAnnotation: If `raise_error` is `True` and there is an undefined annotations.
    '''
    original_init = cls.__init__
    
    def __init__(__dataclass_self__ = None, *args, **kwargs):
        __tracebackhide__ = True
        s = __dataclass_self__
        s.__pydantic_validator__.validate_python(ArgsKwargs(args, kwargs), self_instance = s)

    __init__.__qualname__ = f'''{cls.__qualname__}.__init__'''
    cls.__init__ = __init__
    cls.__pydantic_config__ = config_wrapper.config_dict
    set_dataclass_fields(cls, config_wrapper = config_wrapper, ns_resolver = ns_resolver)
    if _force_build and config_wrapper.defer_build:
        set_dataclass_mocks(cls)
        return False
    if None(cls, '__post_init_post_parse__'):
        warnings.warn('Support for `__post_init_post_parse__` has been dropped, the method will not be called', PydanticDeprecatedSince20)
    typevars_map = get_standard_typevars_map(cls)
    gen_schema = GenerateSchema(config_wrapper, ns_resolver = ns_resolver, typevars_map = typevars_map)
    cls.__signature__ = LazyClassAttribute('__signature__', partial(generate_pydantic_signature, init = original_init, fields = cls.__pydantic_fields__, validate_by_name = config_wrapper.validate_by_name, extra = config_wrapper.extra, is_dataclass = True))
    
    try:
        schema = gen_schema.generate_schema(cls)
    except PydanticUndefinedAnnotation:
        e = None
        if raise_errors:
            raise 
        set_dataclass_mocks(cls, f'''`{e.name}`''')
        e = None
        del e
        return False
        e = None
        del e

    core_config = config_wrapper.core_config(title = cls.__name__)
    
    try:
        schema = gen_schema.clean_schema(schema)
    except InvalidSchemaError:
        set_dataclass_mocks(cls)
        return False

    cls = cast('type[PydanticDataclass]', cls)
    cls.__pydantic_core_schema__ = schema
    cls.__pydantic_validator__ = create_schema_validator(schema, cls, cls.__module__, cls.__qualname__, 'dataclass', core_config, config_wrapper.plugin_settings)
    cls.__pydantic_serializer__ = SchemaSerializer(schema, core_config)
    cls.__pydantic_complete__ = True
    return True


def is_stdlib_dataclass(cls = None):
    '''Returns `True` if the class is a stdlib dataclass and *not* a Pydantic dataclass.

    Unlike the stdlib `dataclasses.is_dataclass()` function, this does *not* include subclasses
    of a dataclass that are themselves not dataclasses.

    Args:
        cls: The class.

    Returns:
        `True` if the class is a stdlib dataclass, `False` otherwise.
    '''
    if '__dataclass_fields__' in cls.__dict__:
        pass
    return not hasattr(cls, '__pydantic_validator__')


def as_dataclass_field(pydantic_field = None):
    field_args = {
        'default': pydantic_field }
# WARNING: Decompyle incomplete

DcFields: 'TypeAlias' = dict[(str, dataclasses.Field[Any])]
patch_base_fields = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()
