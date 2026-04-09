# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

import abc
import math
import re
import warnings
from datetime import date
from decimal import Decimal, InvalidOperation
from enum import Enum
from pathlib import Path
from types import new_class
from typing import TYPE_CHECKING, Any, Callable, ClassVar, Dict, FrozenSet, List, Optional, Pattern, Set, Tuple, Type, TypeVar, Union, cast, overload
from uuid import UUID
from weakref import WeakSet
from pydantic.v1 import errors
from pydantic.v1.datetime_parse import parse_date
from pydantic.v1.utils import import_string, update_not_none
from pydantic.v1.validators import bytes_validator, constr_length_validator, constr_lower, constr_strip_whitespace, constr_upper, decimal_validator, float_finite_validator, float_validator, frozenset_validator, int_validator, list_validator, number_multiple_validator, number_size_validator, path_exists_validator, path_validator, set_validator, str_validator, strict_bytes_validator, strict_float_validator, strict_int_validator, strict_str_validator
__all__ = [
    'NoneStr',
    'NoneBytes',
    'StrBytes',
    'NoneStrBytes',
    'StrictStr',
    'ConstrainedBytes',
    'conbytes',
    'ConstrainedList',
    'conlist',
    'ConstrainedSet',
    'conset',
    'ConstrainedFrozenSet',
    'confrozenset',
    'ConstrainedStr',
    'constr',
    'PyObject',
    'ConstrainedInt',
    'conint',
    'PositiveInt',
    'NegativeInt',
    'NonNegativeInt',
    'NonPositiveInt',
    'ConstrainedFloat',
    'confloat',
    'PositiveFloat',
    'NegativeFloat',
    'NonNegativeFloat',
    'NonPositiveFloat',
    'FiniteFloat',
    'ConstrainedDecimal',
    'condecimal',
    'UUID1',
    'UUID3',
    'UUID4',
    'UUID5',
    'FilePath',
    'DirectoryPath',
    'Json',
    'JsonWrapper',
    'SecretField',
    'SecretStr',
    'SecretBytes',
    'StrictBool',
    'StrictBytes',
    'StrictInt',
    'StrictFloat',
    'PaymentCardNumber',
    'ByteSize',
    'PastDate',
    'FutureDate',
    'ConstrainedDate',
    'condate']
NoneStr = Optional[str]
NoneBytes = Optional[bytes]
StrBytes = Union[(str, bytes)]
NoneStrBytes = Optional[StrBytes]
OptionalInt = Optional[int]
OptionalIntFloat = Union[(OptionalInt, float)]
OptionalIntFloatDecimal = Union[(OptionalIntFloat, Decimal)]
OptionalDate = Optional[date]
StrIntFloat = Union[(str, int, float)]
if TYPE_CHECKING:
    from typing_extensions import Annotated
    from pydantic.v1.dataclasses import Dataclass
    from pydantic.v1.main import BaseModel
    from pydantic.v1.typing import CallableGenerator
    ModelOrDc = Type[Union[(BaseModel, Dataclass)]]
T = TypeVar('T')
_DEFINED_TYPES: 'WeakSet[type]' = WeakSet()
_registered = (lambda typ = None: pass)()
_registered = (lambda typ = None: pass)()

def _registered(typ = None):
    _DEFINED_TYPES.add(typ)
    return typ


class ConstrainedNumberMeta(type):
    
    def __new__(cls = None, name = None, bases = None, dct = ('name', str, 'bases', Any, 'dct', Dict[(str, Any)], 'return', 'ConstrainedInt')):
        new_cls = cast('ConstrainedInt', type.__new__(cls, name, bases, dct))
    # WARNING: Decompyle incomplete



def ConstrainedInt():
    '''ConstrainedInt'''
    strict: bool = False
    gt: OptionalInt = None
    ge: OptionalInt = None
    lt: OptionalInt = None
    le: OptionalInt = None
    multiple_of: OptionalInt = None
    __modify_schema__ = (lambda cls = None, field_schema = None: update_not_none(field_schema, exclusiveMinimum = cls.gt, exclusiveMaximum = cls.lt, minimum = cls.ge, maximum = cls.le, multipleOf = cls.multiple_of))()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()

ConstrainedInt = <NODE:27>(ConstrainedInt, 'ConstrainedInt', int, metaclass = ConstrainedNumberMeta)

def conint(*, strict, gt, ge, lt, le, multiple_of):
    namespace = dict(strict = strict, gt = gt, ge = ge, lt = lt, le = le, multiple_of = multiple_of)
    return type('ConstrainedIntValue', (ConstrainedInt,), namespace)


def ConstrainedFloat():
    '''ConstrainedFloat'''
    strict: bool = False
    gt: OptionalIntFloat = None
    ge: OptionalIntFloat = None
    lt: OptionalIntFloat = None
    le: OptionalIntFloat = None
    multiple_of: OptionalIntFloat = None
    allow_inf_nan: Optional[bool] = None
    __modify_schema__ = (lambda cls = None, field_schema = None: update_not_none(field_schema, exclusiveMinimum = cls.gt, exclusiveMaximum = cls.lt, minimum = cls.ge, maximum = cls.le, multipleOf = cls.multiple_of)if field_schema.get('exclusiveMinimum') == -(math.inf):
del field_schema['exclusiveMinimum']if field_schema.get('minimum') == -(math.inf):
del field_schema['minimum']if field_schema.get('exclusiveMaximum') == math.inf:
del field_schema['exclusiveMaximum']if field_schema.get('maximum') == math.inf:
del field_schema['maximum']None)()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()

ConstrainedFloat = <NODE:27>(ConstrainedFloat, 'ConstrainedFloat', float, metaclass = ConstrainedNumberMeta)

def confloat(*, strict, gt, ge, lt, le, multiple_of, allow_inf_nan):
    namespace = dict(strict = strict, gt = gt, ge = ge, lt = lt, le = le, multiple_of = multiple_of, allow_inf_nan = allow_inf_nan)
    return type('ConstrainedFloatValue', (ConstrainedFloat,), namespace)


class ConstrainedBytes(bytes):
    strip_whitespace = False
    to_upper = False
    to_lower = False
    min_length: OptionalInt = None
    max_length: OptionalInt = None
    strict: bool = False
    __modify_schema__ = (lambda cls = None, field_schema = None: update_not_none(field_schema, minLength = cls.min_length, maxLength = cls.max_length))()
    __get_validators__ = (lambda cls = None: pass# WARNING: Decompyle incomplete
)()


def conbytes(*, strip_whitespace, to_upper, to_lower, min_length, max_length, strict):
    namespace = dict(strip_whitespace = strip_whitespace, to_upper = to_upper, to_lower = to_lower, min_length = min_length, max_length = max_length, strict = strict)
    return _registered(type('ConstrainedBytesValue', (ConstrainedBytes,), namespace))


class ConstrainedStr(str):
    strip_whitespace = False
    to_upper = False
    to_lower = False
    min_length: OptionalInt = None
    max_length: OptionalInt = None
    curtail_length: OptionalInt = None
    regex: Optional[Union[(str, Pattern[str])]] = None
    strict = False
    __modify_schema__ = (lambda cls = None, field_schema = None:
