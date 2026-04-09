# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _fields.pyc (Python 3.11)

'''Private logic related to fields (the `Field()` function and `FieldInfo` class), and arguments to `Annotated`.'''
from __future__ import annotations as _annotations
import dataclasses
import warnings
from collections.abc import Mapping
from functools import cache
from inspect import Parameter, ismethoddescriptor, signature
from re import Pattern
from typing import TYPE_CHECKING, Any, Callable, TypeVar
from pydantic_core import PydanticUndefined
from typing_extensions import TypeIs
from typing_inspection.introspection import AnnotationSource
from pydantic import PydanticDeprecatedSince211
from pydantic.errors import PydanticUserError
from aliases import AliasGenerator
from  import _generics, _typing_extra
from _config import ConfigWrapper
from _docs_extraction import extract_docstrings_from_cls
from _import_utils import import_cached_base_model, import_cached_field_info
from _namespace_utils import NsResolver
from _repr import Representation
from _utils import can_be_positional, get_first_not_none
if TYPE_CHECKING:
    from annotated_types import BaseMetadata
    from fields import FieldInfo
    from main import BaseModel
    from _dataclasses import PydanticDataclass, StandardDataclass
    from _decorators import DecoratorInfos

class PydanticMetadata(Representation):
    '''Base class for annotation markers like `Strict`.'''
    __slots__ = ()


def pydantic_general_metadata(**metadata):
    '''Create a new `_PydanticGeneralMetadata` class with the given metadata.

    Args:
        **metadata: The metadata to add.

    Returns:
        The new `_PydanticGeneralMetadata` class.
    '''
    return _general_metadata_cls()(metadata)

_general_metadata_cls = (lambda : BaseMetadata = BaseMetadataimport annotated_types
class _PydanticGeneralMetadata(BaseMetadata, PydanticMetadata):
'''Pydantic general metadata like `max_digits`.'''

def __init__(self = None, metadata = None):
self.__dict__ = metadata_PydanticGeneralMetadata)()

def _check_protected_namespaces(protected_namespaces = None, ann_name = None, bases = None, cls_name = ('protected_namespaces', 'tuple[str | Pattern[str], ...]', 'ann_name', 'str', 'bases', 'tuple[type[Any], ...]', 'cls_name', 'str', 'return', 'None')):
    BaseModel = import_cached_base_model()
    for protected_namespace in protected_namespaces:
        ns_violation = False
        if isinstance(protected_namespace, Pattern):
            ns_violation = protected_namespace.match(ann_name) is not None
        elif isinstance(protected_namespace, str):
            ns_violation = ann_name.startswith(protected_namespace)
        if ns_violation:
            for b in bases:
                if hasattr(b, ann_name):
                    if not issubclass(b, BaseModel) or ann_name in getattr(b, '__pydantic_fields__', { }):
                        raise ValueError(f'''Field {ann_name!r} conflicts with member {getattr(b, ann_name)} of protected namespace {protected_namespace!r}.''')
                valid_namespaces = []
                for pn in protected_namespaces:
                    if isinstance(pn, Pattern):
                        if not pn.match(ann_name):
                            valid_namespaces.append(f'''re.compile({pn.pattern!r})''')
                        continue
                    if not ann_name.startswith(pn):
                        valid_namespaces.append(f'''\'{pn}\'''')
            valid_namespaces_str = f'''({', '.join(valid_namespaces)}{',)' if len(valid_namespaces) == 1 else ')'}'''
            warnings.warn(f'''Field {ann_name!r} in {cls_name!r} conflicts with protected namespace {protected_namespace!r}.\n\nYou may be able to solve this by setting the \'protected_namespaces\' configuration to {valid_namespaces_str}.''', UserWarning, stacklevel = 5)
        return None


def _update_fields_from_docstrings(cls = None, fields = None, use_inspect = None):
    fields_docs = extract_docstrings_from_cls(cls, use_inspect = use_inspect)
# WARNING: Decompyle incomplete


def _apply_field_title_generator_to_field_info(title_generator = None, field_name = None, field_info = None):
    pass
# WARNING: Decompyle incomplete


def _apply_alias_generator_to_field_info(alias_generator = None, field_name = None, field_info = None):
    '''Apply an alias generator to aliases on a `FieldInfo` instance if appropriate.

    Args:
        alias_generator: A callable that takes a string and returns a string, or an `AliasGenerator` instance.
        field_name: The name of the field from which to generate the alias.
        field_info: The `FieldInfo` instance to which the alias generator is (maybe) applied.
    '''
    pass
# WARNING: Decompyle incomplete


def update_field_from_config(config_wrapper = None, field_name = None, field_info = None):
    '''Update the `FieldInfo` instance from the configuration set on the model it belongs to.

    This will apply the title and alias generators from the configuration.

    Args:
        config_wrapper: The configuration from the model.
        field_name: The field name the `FieldInfo` instance is attached to.
        field_info: The `FieldInfo` instance to update.
    '''
    pass
# WARNING: Decompyle incomplete

_deprecated_method_names = {
    'copy',
    'dict',
    'json',
    '_iter',
    '_calculate_keys',
    '_copy_and_set_values'}
_deprecated_classmethod_names = {
    'schema',
    'from_orm',
    'validate',
    'construct',
    'parse_obj',
    'parse_raw',
    '_get_value',
    'parse_file',
    'schema_json',
    'update_forward_refs'}

def collect_model_fields(cls = None, config_wrapper = None, ns_resolver = None, *, typevars_map):
    """Collect the fields and class variables names of a nascent Pydantic model.

    The fields collection process is *lenient*, meaning it won't error if string annotations
    fail to evaluate. If this happens, the original annotation (and assigned value, if any)
    is stored on the created `FieldInfo` instance.

    The `rebuild_model_fields()` should be called at a later point (e.g. when rebuilding the model),
    and will make use of these stored attributes.

    Args:
        cls: BaseModel or dataclass.
        config_wrapper: The config wrapper instance.
        ns_resolver: Namespace resolver to use when getting model annotations.
        typevars_map: A dictionary mapping type variables to their concrete types.

    Returns:
        A two-tuple containing model fields and class variables names.

    Raises:
        NameError:
            - If there is a conflict between a field name and protected namespaces.
            - If there is a field other than `root` in `RootModel`.
            - If a field shadows an attribute in the parent model.
    """
    pass
# WARNING: Decompyle incomplete


def rebuild_model_fields(cls = None, *, config_wrapper, ns_resolver, typevars_map):
    """Rebuild the (already present) model fields by trying to reevaluate annotations.

    This function should be called whenever a model with incomplete fields is encountered.

    Raises:
        NameError: If one of the annotations failed to evaluate.

    Note:
        This function *doesn't* mutate the model fields in place, as it can be called during
        schema generation, where you don't want to mutate other model's fields.
    """
    FieldInfo_ = import_cached_field_info()
    rebuilt_fields = { }
    ns_resolver.push(cls)
# WARNING: Decompyle incomplete


def collect_dataclass_fields(cls = None, *, config_wrapper, ns_resolver, typevars_map):
    '''Collect the fields of a dataclass.

    Args:
        cls: dataclass.
        config_wrapper: The config wrapper instance.
        ns_resolver: Namespace resolver to use when getting dataclass annotations.
            Defaults to an empty instance.
        typevars_map: A dictionary mapping type variables to their concrete types.

    Returns:
        The dataclass fields.
    '''
    FieldInfo_ = import_cached_field_info()
    fields = { }
    if not ns_resolver:
        ns_resolver = NsResolver()
        dataclass_fields = cls.__dataclass_fields__
        for base in reversed(cls.__mro__):
            if not dataclasses.is_dataclass(base):
                continue
            ns_resolver.push(base)
            for ann_name, dataclass_field in dataclass_fields.items():
                base_anns = _typing_extra.safe_get_annotations(base)
                if ann_name not in base_anns:
                    continue
                (globalns, localns) = ns_resolver.types_namespace
                (ann_type, evaluated) = _typing_extra.try_eval_type(dataclass_field.type, globalns, localns)
                if _typing_extra.is_classvar_annotation(ann_type):
                    continue
                if dataclass_field.init and dataclass_field.default is dataclasses.MISSING and dataclass_field.default_factory is dataclasses.MISSING:
                    continue
                if isinstance(dataclass_field.default, FieldInfo_):
                    if dataclass_field.default.init_var:
                        if dataclass_field.default.init is False:
                            raise PydanticUserError(f'''Dataclass field {ann_name} has init=False and init_var=True, but these are mutually exclusive.''', code = 'clashing-init-and-init-var')
                        continue
                    field_info = FieldInfo_.from_annotated_attribute(ann_type, dataclass_field.default, _source = AnnotationSource.DATACLASS)
                    field_info._original_assignment = dataclass_field.default
                else:
                    field_info = FieldInfo_.from_annotated_attribute(ann_type, dataclass_field, _source = AnnotationSource.DATACLASS)
                    field_info._original_assignment = dataclass_field
                if not evaluated:
                    field_info._complete = False
                    field_info._original_annotation = ann_type
                fields[ann_name] = field_info
                update_field_from_config(config_wrapper, ann_name, field_info)
                if field_info.default is not PydanticUndefined and isinstance(getattr(cls, ann_name, field_info), FieldInfo_):
                    setattr(cls, ann_name, field_info.default)
                None(None, None)
            with None:
                if not ns_resolver:
                    pass
            if typevars_map:
                for field in fields.values():
                    field.apply_typevars_map(typevars_map)
                    if config_wrapper.use_attribute_docstrings:
                        _update_fields_from_docstrings(cls, fields, use_inspect = not hasattr(cls, '__is_pydantic_dataclass__'))
    return fields


def rebuild_dataclass_fields(cls = None, *, config_wrapper, ns_resolver, typevars_map):
    """Rebuild the (already present) dataclass fields by trying to reevaluate annotations.

    This function should be called whenever a dataclass with incomplete fields is encountered.

    Raises:
        NameError: If one of the annotations failed to evaluate.

    Note:
        This function *doesn't* mutate the dataclass fields in place, as it can be called during
        schema generation, where you don't want to mutate other dataclass's fields.
    """
    FieldInfo_ = import_cached_field_info()
    rebuilt_fields = { }
    ns_resolver.push(cls)
# WARNING: Decompyle incomplete


def is_valid_field_name(name = None):
    return not name.startswith('_')


def is_valid_privateattr_name(name = None):
