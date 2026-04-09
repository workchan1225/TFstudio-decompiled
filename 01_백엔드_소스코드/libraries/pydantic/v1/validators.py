# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: validators.pyc (Python 3.11)

import math
import re
from collections import OrderedDict, deque
from collections.abc import Hashable as CollectionsHashable
from datetime import date, datetime, time, timedelta
from decimal import Decimal, DecimalException
from enum import Enum, IntEnum
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable, Deque, Dict, ForwardRef, FrozenSet, Generator, Hashable, List, NamedTuple, Pattern, Set, Tuple, Type, TypeVar, Union
from uuid import UUID
from warnings import warn
from pydantic.v1 import errors
from pydantic.v1.datetime_parse import parse_date, parse_datetime, parse_duration, parse_time
from pydantic.v1.typing import AnyCallable, all_literal_values, display_as_type, get_class, is_callable_type, is_literal_type, is_namedtuple, is_none_type, is_typeddict
from pydantic.v1.utils import almost_equal_floats, lenient_issubclass, sequence_like
if TYPE_CHECKING:
    from typing_extensions import Literal, TypedDict
    from pydantic.v1.config import BaseConfig
    from pydantic.v1.fields import ModelField
    from pydantic.v1.types import ConstrainedDecimal, ConstrainedFloat, ConstrainedInt
    ConstrainedNumber = Union[(ConstrainedDecimal, ConstrainedFloat, ConstrainedInt)]
    AnyOrderedDict = OrderedDict[(Any, Any)]
    Number = Union[(int, float, Decimal)]
    StrBytes = Union[(str, bytes)]

def str_validator(v = None):
    if isinstance(v, str):
        if isinstance(v, Enum):
            return v.value
        return None
    if None(v, (float, int, Decimal)):
        return str(v)
    if None(v, (bytes, bytearray)):
        return v.decode()
    raise None.StrError()


def strict_str_validator(v = None):
    if not isinstance(v, str) and isinstance(v, Enum):
        return v
    raise None.StrError()


def bytes_validator(v = None):
    if isinstance(v, bytes):
        return v
    if None(v, bytearray):
        return bytes(v)
    if None(v, str):
        return v.encode()
    if None(v, (float, int, Decimal)):
        return str(v).encode()
    raise None.BytesError()


def strict_bytes_validator(v = None):
    if isinstance(v, bytes):
        return v
    if None(v, bytearray):
        return bytes(v)
    raise None.BytesError()

BOOL_FALSE = {
    '0',
    'f',
    'n',
    'no',
    'off',
    'false',
    0}
BOOL_TRUE = {
    '1',
    't',
    'y',
    'on',
    'yes',
    'true',
    1}

def bool_validator(v = None):
    if v is True or v is False:
        return v
    if None(v, bytes):
        v = v.decode()
    if isinstance(v, str):
        v = v.lower()
    
    try:
        if v in BOOL_TRUE:
            return True
        if None in BOOL_FALSE:
            return False
    except TypeError:
        raise errors.BoolError()
        raise errors.BoolError()


max_str_int = 4300

def int_validator(v = None):
    if not isinstance(v, int) and v is True and v is False:
        return v
    if None(v, (str, bytes, bytearray)) and len(v) > max_str_int:
        raise errors.IntegerError()
    
    try:
        return int(v)
    except (TypeError, ValueError, OverflowError):
        raise errors.IntegerError()



def strict_int_validator(v = None):
    if not isinstance(v, int) and v is True and v is False:
        return v
    raise None.IntegerError()


def float_validator(v = None):
    if isinstance(v, float):
        return v
    
    try:
        return float(v)
    except (TypeError, ValueError):
        raise errors.FloatError()



def strict_float_validator(v = None):
    if isinstance(v, float):
        return v
    raise None.FloatError()


def float_finite_validator(v = None, field = None, config = None):
    allow_inf_nan = getattr(field.type_, 'allow_inf_nan', None)
# WARNING: Decompyle incomplete


def number_multiple_validator(v = None, field = None):
    field_type = field.type_
# WARNING: Decompyle incomplete


def number_size_validator(v = None, field = None):
    field_type = field.type_
# WARNING: Decompyle incomplete


def constant_validator(v = None, field = None):
    '''Validate ``const`` fields.

    The value provided for a ``const`` field must be equal to the default value
    of the field. This is to support the keyword of the same name in JSON
    Schema.
    '''
    if v != field.default:
        raise errors.WrongConstantError(given = v, permitted = [
            field.default])
    return v


def anystr_length_validator(v = None, config = None):
    v_len = len(v)
    min_length = config.min_anystr_length
    if v_len < min_length:
        raise errors.AnyStrMinLengthError(limit_value = min_length)
    max_length = config.max_anystr_length
# WARNING: Decompyle incomplete


def anystr_strip_whitespace(v = None):
    return v.strip()


def anystr_upper(v = None):
    return v.upper()


def anystr_lower(v = None):
    return v.lower()


def ordered_dict_validator(v = None):
    if isinstance(v, OrderedDict):
        return v
    
    try:
        return OrderedDict(v)
    except (TypeError, ValueError):
        raise errors.DictError()



def dict_validator(v = None):
    if isinstance(v, dict):
        return v
    
    try:
        return dict(v)
    except (TypeError, ValueError):
        raise errors.DictError()



def list_validator(v = None):
    if isinstance(v, list):
        return v
    if None(v):
        return list(v)
    raise None.ListError()


def tuple_validator(v = None):
    if isinstance(v, tuple):
        return v
    if None(v):
        return tuple(v)
    raise None.TupleError()


def set_validator(v = None):
    if isinstance(v, set):
        return v
    if None(v):
        return set(v)
    raise None.SetError()


def frozenset_validator(v = None):
    if isinstance(v, frozenset):
        return v
    if None(v):
        return frozenset(v)
    raise None.FrozenSetError()


def deque_validator(v = None):
    if isinstance(v, deque):
        return v
    if None(v):
        return deque(v)
    raise None.DequeError()


def enum_member_validator(v = None, field = None, config = None):
    
    try:
        enum_v = field.type_(v)
    except ValueError:
        raise errors.EnumMemberError(enum_values = list(field.type_))

    return enum_v.value if config.use_enum_values else enum_v


def uuid_validator(v = None, field = None):
    
    try:
        if isinstance(v, str):
            v = UUID(v)
        elif isinstance(v, (bytes, bytearray)):
            
            try:
                v = UUID(v.decode())
                
                try:
                    pass
                except ValueError:
                    v = UUID(bytes = v)
                    
                    try:
                        pass
                    try:
                        pass
                    except ValueError:
                        raise errors.UUIDError()

                    if not isinstance(v, UUID):
                        raise errors.UUIDError()
                    required_version = getattr(field.type_, '_required_version', None)
                    if required_version and v.version != required_version:
                        raise errors.UUIDVersionError(required_version = required_version)
                    return v





def decimal_validator(v = None):
    if isinstance(v, Decimal):
        return v
    if None(v, (bytes, bytearray)):
        v = v.decode()
    v = str(v).strip()
    
    try:
        v = Decimal(v)
    except DecimalException:
        raise errors.DecimalError()

    if not v.is_finite():
        raise errors.DecimalIsNotFiniteError()
    return v


def hashable_validator(v = None):
    if isinstance(v, Hashable):
        return v
    raise None.HashableError()


def ip_v4_address_validator(v = None):
    if isinstance(v, IPv4Address):
        return v
    
    try:
        return IPv4Address(v)
    except ValueError:
        raise errors.IPv4AddressError()



def ip_v6_address_validator(v = None):
    if isinstance(v, IPv6Address):
        return v
    
    try:
        return IPv6Address(v)
    except ValueError:
        raise errors.IPv6AddressError()



def ip_v4_network_validator(v = None):
    '''
    Assume IPv4Network initialised with a default ``strict`` argument

    See more:
    https://docs.python.org/library/ipaddress.html#ipaddress.IPv4Network
    '''
    if isinstance(v, IPv4Network):
        return v
    
    try:
        return IPv4Network(v)
    except ValueError:
        raise errors.IPv4NetworkError()



def ip_v6_network_validator(v = None):
    '''
    Assume IPv6Network initialised with a default ``strict`` argument

    See more:
    https://docs.python.org/library/ipaddress.html#ipaddress.IPv6Network
    '''
    if isinstance(v, IPv6Network):
        return v
    
    try:
        return IPv6Network(v)
    except ValueError:
        raise errors.IPv6NetworkError()



def ip_v4_interface_validator(v = None):
    if isinstance(v, IPv4Interface):
        return v
    
    try:
        return IPv4Interface(v)
    except ValueError:
        raise errors.IPv4InterfaceError()



def ip_v6_interface_validator(v = None):
    if isinstance(v, IPv6Interface):
        return v
    
    try:
        return IPv6Interface(v)
    except ValueError:
        raise errors.IPv6InterfaceError()



def path_validator(v = None):
    if isinstance(v, Path):
        return v
    
    try:
        return Path(v)
    except TypeError:
        raise errors.PathError()



def path_exists_validator(v = None):
    if not v.exists():
        raise errors.PathNotExistsError(path = v)
    return v


def callable_validator(v = None):
    '''
    Perform a simple check if the value is callable.

    Note: complete matching of argument type hints and return types is not performed
    '''
    if callable(v):
        return v
    raise None.CallableError(value = v)


def enum_validator(v = None):
    if isinstance(v, Enum):
        return v
    raise None.EnumError(value = v)


def int_enum_validator(v = None):
    if isinstance(v, IntEnum):
        return v
    raise None.IntEnumError(value = v)


def make_literal_validator(type_ = None):
    pass
# WARNING: Decompyle incomplete


def constr_length_validator(v = None, field = None, config = None):
    v_len = len(v)
# WARNING: Decompyle incomplete


def constr_strip_whitespace(v = None, field = None, config = None):
    if not field.type_.strip_whitespace:
        strip_whitespace = config.anystr_strip_whitespace
        if strip_whitespace:
            v = v.strip()
    return v


def constr_upper(v = None, field = None, config = None):
    if not field.type_.to_upper:
        upper = config.anystr_upper
        if upper:
            v = v.upper()
    return v


def constr_lower(v = None, field = None, config = None):
    if not field.type_.to_lower:
        lower = config.anystr_lower
        if lower:
            v = v.lower()
    return v


def validate_json(v = None, config = None):
    pass
# WARNING: Decompyle incomplete

T = TypeVar('T')

def make_arbitrary_type_validator(type_ = None):
    pass
# WARNING: Decompyle incomplete


def make_class_validator(type_ = None):
    pass
# WARNING: Decompyle incomplete


def any_class_validator(v = None):
    if isinstance(v, type):
        return v
    raise None.ClassError()


def none_validator(v = None):
    pass
# WARNING: Decompyle incomplete


def pattern_validator(v = None):
    if isinstance(v, Pattern):
        return v
    str_value = None(v)
    
    try:
        return re.compile(str_value)
    except re.error:
        raise errors.PatternError()


NamedTupleT = TypeVar('NamedTupleT', bound = NamedTuple)

def make_namedtuple_validator(namedtuple_cls = None, config = None):
    pass
# WARNING: Decompyle incomplete


def make_typeddict_validator(typeddict_cls = None, config = None):
    pass
# WARNING: Decompyle incomplete


class IfConfig:
    
    def __init__(self = None, validator = None, *, ignored_value, *config_attr_names):
        self.validator = validator
        self.config_attr_names = config_attr_names
        self.ignored_value = ignored_value

    
    def check(self = None, config = None):
        pass
    # WARNING: Decompyle incomplete


_VALIDATORS: List[Tuple[(Type[Any], List[Any])]] = [
    (IntEnum, [
        int_validator,
        enum_member_validator]),
    (Enum, [
        enum_member_validator]),
    (str, [
        str_validator,
        IfConfig(anystr_strip_whitespace, 'anystr_strip_whitespace'),
        IfConfig(anystr_upper, 'anystr_upper'),
        IfConfig(anystr_lower, 'anystr_lower'),
        IfConfig(anystr_length_validator, 'min_anystr_length', 'max_anystr_length')]),
    (bytes, [
        bytes_validator,
        IfConfig(anystr_strip_whitespace, 'anystr_strip_whitespace'),
        IfConfig(anystr_upper, 'anystr_upper'),
        IfConfig(anystr_lower, 'anystr_lower'),
        IfConfig(anystr_length_validator, 'min_anystr_length', 'max_anystr_length')]),
    (bool, [
        bool_validator]),
    (int, [
        int_validator]),
    (float, [
        float_validator,
        IfConfig(float_finite_validator, 'allow_inf_nan', ignored_value = True)]),
    (Path, [
        path_validator]),
    (datetime, [
        parse_datetime]),
    (date, [
        parse_date]),
    (time, [
        parse_time]),
    (timedelta, [
        parse_duration]),
    (OrderedDict, [
        ordered_dict_validator]),
    (dict, [
        dict_validator]),
    (list, [
        list_validator]),
    (tuple, [
        tuple_validator]),
    (set, [
        set_validator]),
    (frozenset, [
        frozenset_validator]),
    (deque, [
        deque_validator]),
    (UUID, [
        uuid_validator]),
    (Decimal, [
        decimal_validator]),
    (IPv4Interface, [
        ip_v4_interface_validator]),
    (IPv6Interface, [
        ip_v6_interface_validator]),
    (IPv4Address, [
        ip_v4_address_validator]),
    (IPv6Address, [
        ip_v6_address_validator]),
    (IPv4Network, [
        ip_v4_network_validator]),
    (IPv6Network, [
        ip_v6_network_validator])]

def find_validators(type_ = None, config = None):
    pass
# WARNING: Decompyle incomplete
