# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fields.pyc (Python 3.11)

import copy
import re
from collections import Counter as CollectionCounter, defaultdict, deque
from collections.abc import Callable, Hashable as CollectionsHashable, Iterable as CollectionsIterable
from typing import TYPE_CHECKING, Any, Counter, DefaultDict, Deque, Dict, ForwardRef, FrozenSet, Generator, Iterable, Iterator, List, Mapping, Optional, Pattern, Sequence, Set, Tuple, Type, TypeVar, Union
from typing_extensions import Annotated, Final
from pydantic.v1 import errors as errors_
from pydantic.v1.class_validators import Validator, make_generic_validator, prep_validators
from pydantic.v1.error_wrappers import ErrorWrapper
from pydantic.v1.errors import ConfigError, InvalidDiscriminator, MissingDiscriminator, NoneIsNotAllowedError
from pydantic.v1.types import Json, JsonWrapper
from pydantic.v1.typing import NoArgAnyCallable, convert_generics, display_as_type, get_args, get_origin, is_finalvar, is_literal_type, is_new_type, is_none_type, is_typeddict, is_typeddict_special, is_union, new_type_supertype
from pydantic.v1.utils import PyObjectStr, Representation, ValueItems, get_discriminator_alias_and_values, get_unique_discriminator_alias, lenient_isinstance, lenient_issubclass, sequence_like, smart_deepcopy
from pydantic.v1.validators import constant_validator, dict_validator, find_validators, validate_json
Required: Any = Ellipsis
T = TypeVar('T')

class UndefinedType:
    
    def __repr__(self = None):
        return 'PydanticUndefined'

    
    def __copy__(self = None):
        return self

    
    def __reduce__(self = None):
        return 'Undefined'

    
    def __deepcopy__(self = None, _ = None):
        return self


Undefined = UndefinedType()
if TYPE_CHECKING:
    from pydantic.v1.class_validators import ValidatorsList
    from pydantic.v1.config import BaseConfig
    from pydantic.v1.error_wrappers import ErrorList
    from pydantic.v1.types import ModelOrDc
    from pydantic.v1.typing import AbstractSetIntStr, MappingIntStrAny, ReprArgs
    ValidateReturn = Tuple[(Optional[Any], Optional[ErrorList])]
    LocStr = Union[(Tuple[(Union[(int, str)], ...)], str)]
    BoolUndefined = Union[(bool, UndefinedType)]

class FieldInfo(Representation):
    '''
    Captures extra information about a field.
    '''
    __slots__ = ('default', 'default_factory', 'alias', 'alias_priority', 'title', 'description', 'exclude', 'include', 'const', 'gt', 'ge', 'lt', 'le', 'multiple_of', 'allow_inf_nan', 'max_digits', 'decimal_places', 'min_items', 'max_items', 'unique_items', 'min_length', 'max_length', 'allow_mutation', 'repr', 'regex', 'discriminator', 'extra')
    __field_constraints__ = {
        'min_length': None,
        'max_length': None,
        'regex': None,
        'gt': None,
        'lt': None,
        'ge': None,
        'le': None,
        'multiple_of': None,
        'allow_inf_nan': None,
        'max_digits': None,
        'decimal_places': None,
        'min_items': None,
        'max_items': None,
        'unique_items': None,
        'allow_mutation': True }
    
    def __init__(self = None, default = None, **kwargs):
        self.default = default
        self.default_factory = kwargs.pop('default_factory', None)
        self.alias = kwargs.pop('alias', None)
    # WARNING: Decompyle incomplete

    
    def __repr_args__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def get_constraints(self = None):
        '''
        Gets the constraints set on the field by comparing the constraint value with its default value

        :return: the constraints set on field_info
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def update_from_config(self = None, from_config = None):
        '''
        Update this FieldInfo based on a dict from get_field_info, only fields which have not been set are dated.
        '''
        for attr_name, value in from_config.items():
            current_value = getattr(self, attr_name)
            if current_value is self.__field_constraints__.get(attr_name, None):
                setattr(self, attr_name, value)
                continue
            if attr_name == 'exclude':
                self.exclude = ValueItems.merge(value, current_value)
                continue
            if attr_name == 'include':
                self.include = ValueItems.merge(value, current_value, intersect = True)
            except AttributeError:
                self.extra.setdefault(attr_name, value)
                continue
            return None

    
    def _validate(self = None):
        pass
    # WARNING: Decompyle incomplete



def Field(default = None, *, default_factory, alias, title, description, exclude, include, const, gt, ge, lt, le, multiple_of, allow_inf_nan, max_digits, decimal_places, min_items, max_items, unique_items, min_length, max_length, allow_mutation, regex, discriminator, repr, **extra):
    '''
    Used to provide extra information about a field, either for the model schema or complex validation. Some arguments
    apply only to number fields (``int``, ``float``, ``Decimal``) and some apply only to ``str``.

    :param default: since this is replacing the field’s default, its first argument is used
      to set the default, use ellipsis (``...``) to indicate the field is required
    :param default_factory: callable that will be called when a default value is needed for this field
      If both `default` and `default_factory` are set, an error is raised.
    :param alias: the public name of the field
    :param title: can be any string, used in the schema
    :param description: can be any string, used in the schema
    :param exclude: exclude this field while dumping.
      Takes same values as the ``include`` and ``exclude`` arguments on the ``.dict`` method.
    :param include: include this field while dumping.
      Takes same values as the ``include`` and ``exclude`` arguments on the ``.dict`` method.
    :param const: this field is required and *must* take it\'s default value
    :param gt: only applies to numbers, requires the field to be "greater than". The schema
      will have an ``exclusiveMinimum`` validation keyword
    :param ge: only applies to numbers, requires the field to be "greater than or equal to". The
      schema will have a ``minimum`` validation keyword
    :param lt: only applies to numbers, requires the field to be "less than". The schema
      will have an ``exclusiveMaximum`` validation keyword
    :param le: only applies to numbers, requires the field to be "less than or equal to". The
      schema will have a ``maximum`` validation keyword
    :param multiple_of: only applies to numbers, requires the field to be "a multiple of". The
      schema will have a ``multipleOf`` validation keyword
    :param allow_inf_nan: only applies to numbers, allows the field to be NaN or infinity (+inf or -inf),
        which is a valid Python float. Default True, set to False for compatibility with JSON.
    :param max_digits: only applies to Decimals, requires the field to have a maximum number
      of digits within the decimal. It does not include a zero before the decimal point or trailing decimal zeroes.
    :param decimal_places: only applies to Decimals, requires the field to have at most a number of decimal places
      allowed. It does not include trailing decimal zeroes.
    :param min_items: only applies to lists, requires the field to have a minimum number of
      elements. The schema will have a ``minItems`` validation keyword
    :param max_items: only applies to lists, requires the field to have a maximum number of
      elements. The schema will have a ``maxItems`` validation keyword
    :param unique_items: only applies to lists, requires the field not to have duplicated
      elements. The schema will have a ``uniqueItems`` validation keyword
    :param min_length: only applies to strings, requires the field to have a minimum length. The
      schema will have a ``minLength`` validation keyword
    :param max_length: only applies to strings, requires the field to have a maximum length. The
      schema will have a ``maxLength`` validation keyword
    :param allow_mutation: a boolean which defaults to True. When False, the field raises a TypeError if the field is
      assigned on an instance.  The BaseModel Config must set validate_assignment to True
    :param regex: only applies to strings, requires the field match against a regular expression
      pattern string. The schema will have a ``pattern`` validation keyword
    :param discriminator: only useful with a (discriminated a.k.a. tagged) `Union` of sub models with a common field.
      The `discriminator` is the name of this common field to shorten validation and improve generated schema
    :param repr: show this field in the representation
    :param **extra: any additional keyword arguments will be added as is to the schema
    '''
    pass
# WARNING: Decompyle incomplete

SHAPE_SINGLETON = 1
SHAPE_LIST = 2
SHAPE_SET = 3
SHAPE_MAPPING = 4
SHAPE_TUPLE = 5
SHAPE_TUPLE_ELLIPSIS = 6
SHAPE_SEQUENCE = 7
SHAPE_FROZENSET = 8
SHAPE_ITERABLE = 9
SHAPE_GENERIC = 10
SHAPE_DEQUE = 11
SHAPE_DICT = 12
SHAPE_DEFAULTDICT = 13
SHAPE_COUNTER = 14
SHAPE_NAME_LOOKUP = {
    SHAPE_COUNTER: 'Counter[{}]',
    SHAPE_DEFAULTDICT: 'DefaultDict[{}]',
    SHAPE_DICT: 'Dict[{}]',
    SHAPE_DEQUE: 'Deque[{}]',
    SHAPE_ITERABLE: 'Iterable[{}]',
    SHAPE_FROZENSET: 'FrozenSet[{}]',
    SHAPE_SEQUENCE: 'Sequence[{}]',
    SHAPE_TUPLE_ELLIPSIS: 'Tuple[{}, ...]',
    SHAPE_SET: 'Set[{}]',
    SHAPE_LIST: 'List[{}]' }
MAPPING_LIKE_SHAPES: Set[int] = {
    SHAPE_DEFAULTDICT,
    SHAPE_DICT,
    SHAPE_MAPPING,
    SHAPE_COUNTER}

class ModelField(Representation):
    __slots__ = ('type_', 'outer_type_', 'annotation', 'sub_fields', 'sub_fields_mapping', 'key_field', 'validators', 'pre_validators', 'post_validators', 'default', 'default_factory', 'required', 'final', 'model_config', 'name', 'alias', 'has_alias', 'field_info', 'discriminator_key', 'discriminator_alias', 'validate_always', 'allow_none', 'shape', 'class_validators', 'parse_json')
    
    def __init__(self = None, *, name, type_, class_validators, model_config, default, default_factory, required, final, alias, field_info):
        self.name = name
        self.has_alias = alias is not None
    # WARNING: Decompyle incomplete

    
    def get_default(self = None):
        pass
    # WARNING: Decompyle incomplete

    _get_field_info = (lambda field_name = None, annotation = None, value = staticmethod, config = ('field_name', str, 'annotation', Any, 'value', Any, 'config', Type['BaseConfig'], 'return', Tuple[(FieldInfo, Any)]): field_info_from_config = config.get_field_info(field_name)field_info = None# WARNING: Decompyle incomplete
)()
    infer = (lambda cls = None, *, name: get_annotation_from_field_info = get_annotation_from_field_infoimport pydantic.v1.schema(field_info, value) = cls._get_field_info(name, annotation, value, config)required = Undefinedif value is Required:
required = Truevalue = Noneelif value is not Undefined:
required = Falseannotation = get_annotation_from_field_info(annotation, field_info, name, config.validate_assignment)cls(name = name, type_ = annotation, alias = field_info.alias, class_validators = class_validators, default = value, default_factory = field_info.default_factory, required = required, model_config = config, field_info = field_info))()
    
    def set_config(self = None, config = None):
        self.model_config = config
        info_from_config = config.get_field_info(self.name)
        config.prepare_field(self)
        new_alias = info_from_config.get('alias')
        if not info_from_config.get('alias_priority'):
            new_alias_priority = 0
            if new_alias:
                if self.field_info.alias_priority or new_alias_priority >= 0:
                    self.field_info.alias = new_alias
                    self.field_info.alias_priority = new_alias_priority
                    self.alias = new_alias
        new_exclude = info_from_config.get('exclude')
    # WARNING: Decompyle incomplete

    alt_alias = (lambda self = None: self.name != self.alias)()
    
    def prepare(self = None):
        '''
        Prepare the field but inspecting self.default, self.type_ etc.

        Note: this method is **not** idempotent (because _type_analysis is not idempotent),
        e.g. calling it it multiple times may modify the field and configure it incorrectly.
        '''
        self._set_default_and_type()
        if self.type_.__class__ is ForwardRef or self.type_.__class__ is DeferredType:
            return None
        None._type_analysis()
        if self.required is Undefined:
            self.required = True
    # WARNING: Decompyle incomplete

    
    def _set_default_and_type(self = None):
        '''
        Set the default value, infer the type if needed and check if `None` value is valid.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _type_analysis(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def prepare_discriminated_union_sub_fields(self = None):
        '''
        Prepare the mapping <discriminator key> -> <ModelField> and update `sub_fields`
        Note that this process can be aborted if a `ForwardRef` is encountered
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _create_sub_type(self = None, type_ = None, name = None, *, for_keys):
        (field_info, _) = self._get_field_info(name, type_, None, self.model_config)
        return self.__class__(type_ = type_, name = name, class_validators = class_validators, model_config = self.model_config, field_info = field_info)

    
    def populate_validators(self = None):
