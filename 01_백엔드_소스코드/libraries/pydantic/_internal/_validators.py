# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _validators.pyc (Python 3.11)

'''Validator functions for standard library types.

Import of this module is deferred since it contains imports of many standard library modules.
'''
from __future__ import annotations as _annotations
import collections.abc as collections
import math
import re
import typing
from collections.abc import Sequence
from decimal import Decimal
from fractions import Fraction
from ipaddress import IPv4Address, IPv4Interface, IPv4Network, IPv6Address, IPv6Interface, IPv6Network
from typing import Any, Callable, TypeVar, Union, cast
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError
import typing_extensions
from pydantic_core import PydanticCustomError, PydanticKnownError, core_schema
from typing_extensions import get_args, get_origin
from typing_inspection import typing_objects
from pydantic._internal._import_utils import import_cached_field_info
from pydantic.errors import PydanticSchemaGenerationError

def sequence_validator(input_value = None, validator = None):
    '''Validator for `Sequence` types, isinstance(v, Sequence) has already been called.'''
    value_type = type(input_value)
    if issubclass(value_type, (str, bytes)):
        raise PydanticCustomError('sequence_str', "'{type_name}' instances are not allowed as a Sequence value", {
            'type_name': value_type.__name__ })
    if value_type is tuple:
        input_value = list(input_value)
    v_list = validator(input_value)
    if value_type is list:
        return v_list
    if None(value_type, range):
        return v_list
    if None is tuple:
        return tuple(v_list)
    return value_type(v_list)


def import_string(value = None):
    if isinstance(value, str):
        
        try:
            return _import_string_logic(value)
        except ImportError:
            e = None
            raise PydanticCustomError('import_error', 'Invalid python path: {error}', {
                'error': str(e) }), e
            e = None
            del e
            return value



def _import_string_logic(dotted_path = None):
    """Inspired by uvicorn — dotted paths should include a colon before the final item if that item is not a module.
    (This is necessary to distinguish between a submodule and an attribute when there is a conflict.).

    If the dotted path does not include a colon and the final item is not a valid module, importing as an attribute
    rather than a submodule will be attempted automatically.

    So, for example, the following values of `dotted_path` result in the following returned values:
    * 'collections': <module 'collections'>
    * 'collections.abc': <module 'collections.abc'>
    * 'collections.abc:Mapping': <class 'collections.abc.Mapping'>
    * `collections.abc.Mapping`: <class 'collections.abc.Mapping'> (though this is a bit slower than the previous line)

    An error will be raised under any of the following scenarios:
    * `dotted_path` contains more than one colon (e.g., 'collections:abc:Mapping')
    * the substring of `dotted_path` before the colon is not a valid module in the environment (e.g., '123:Mapping')
    * the substring of `dotted_path` after the colon is not an attribute of the module (e.g., 'collections:abc123')
    """
    import_module = import_module
    import importlib
    components = dotted_path.strip().split(':')
    if len(components) > 2:
        raise ImportError(f'''Import strings should have at most one \':\'; received {dotted_path!r}''')
    module_path = components[0]
    if not module_path:
        raise ImportError(f'''Import strings should have a nonempty module name; received {dotted_path!r}''')
    
    try:
        module = import_module(module_path)
    except ModuleNotFoundError:
        e = None
        if '.' in module_path:
            (maybe_module_path, maybe_attribute) = dotted_path.strip().rsplit('.', 1)
            del e
            return None
        except ImportError:
            pass
        raise ImportError(f'''No module named {module_path!r}'''), e
        raise e
        None = None
        del e

    if len(components) > 1:
        attribute = components[1]
        
        try:
            return getattr(module, attribute)
        except AttributeError:
            e = None
            raise ImportError(f'''cannot import name {attribute!r} from {module_path!r}'''), e
            e = None
            del e
            return module



def pattern_either_validator(input_value = None):
    if isinstance(input_value, re.Pattern):
        return input_value
    if None(input_value, (str, bytes)):
        return compile_pattern(input_value)
    raise None('pattern_type', 'Input should be a valid pattern')


def pattern_str_validator(input_value = None):
    if isinstance(input_value, re.Pattern):
        if isinstance(input_value.pattern, str):
            return input_value
        raise None('pattern_str_type', 'Input should be a string pattern')
    if isinstance(input_value, str):
        return compile_pattern(input_value)
    if None(input_value, bytes):
        raise PydanticCustomError('pattern_str_type', 'Input should be a string pattern')
    raise PydanticCustomError('pattern_type', 'Input should be a valid pattern')


def pattern_bytes_validator(input_value = None):
    if isinstance(input_value, re.Pattern):
        if isinstance(input_value.pattern, bytes):
            return input_value
        raise None('pattern_bytes_type', 'Input should be a bytes pattern')
    if isinstance(input_value, bytes):
        return compile_pattern(input_value)
    if None(input_value, str):
        raise PydanticCustomError('pattern_bytes_type', 'Input should be a bytes pattern')
    raise PydanticCustomError('pattern_type', 'Input should be a valid pattern')

PatternType = TypeVar('PatternType', str, bytes)

def compile_pattern(pattern = None):
    
    try:
        return re.compile(pattern)
    except re.error:
        raise PydanticCustomError('pattern_regex', 'Input should be a valid regular expression')



def ip_v4_address_validator(input_value = None):
    if isinstance(input_value, IPv4Address):
        return input_value
    
    try:
        return IPv4Address(input_value)
    except ValueError:
        raise PydanticCustomError('ip_v4_address', 'Input is not a valid IPv4 address')



def ip_v6_address_validator(input_value = None):
    if isinstance(input_value, IPv6Address):
        return input_value
    
    try:
        return IPv6Address(input_value)
    except ValueError:
        raise PydanticCustomError('ip_v6_address', 'Input is not a valid IPv6 address')



def ip_v4_network_validator(input_value = None):
    '''Assume IPv4Network initialised with a default `strict` argument.

    See more:
    https://docs.python.org/library/ipaddress.html#ipaddress.IPv4Network
    '''
    if isinstance(input_value, IPv4Network):
        return input_value
    
    try:
        return IPv4Network(input_value)
    except ValueError:
        raise PydanticCustomError('ip_v4_network', 'Input is not a valid IPv4 network')



def ip_v6_network_validator(input_value = None):
    '''Assume IPv6Network initialised with a default `strict` argument.

    See more:
    https://docs.python.org/library/ipaddress.html#ipaddress.IPv6Network
    '''
    if isinstance(input_value, IPv6Network):
        return input_value
    
    try:
        return IPv6Network(input_value)
    except ValueError:
        raise PydanticCustomError('ip_v6_network', 'Input is not a valid IPv6 network')



def ip_v4_interface_validator(input_value = None):
    if isinstance(input_value, IPv4Interface):
        return input_value
    
    try:
        return IPv4Interface(input_value)
    except ValueError:
        raise PydanticCustomError('ip_v4_interface', 'Input is not a valid IPv4 interface')



def ip_v6_interface_validator(input_value = None):
    if isinstance(input_value, IPv6Interface):
        return input_value
    
    try:
        return IPv6Interface(input_value)
    except ValueError:
        raise PydanticCustomError('ip_v6_interface', 'Input is not a valid IPv6 interface')



def fraction_validator(input_value = None):
    if isinstance(input_value, Fraction):
        return input_value
    
    try:
        return Fraction(input_value)
    except ValueError:
        raise PydanticCustomError('fraction_parsing', 'Input is not a valid fraction')



def forbid_inf_nan_check(x = None):
    if not math.isfinite(x):
        raise PydanticKnownError('finite_number')
    return x


def _safe_repr(v = None):
    '''The context argument for `PydanticKnownError` requires a number or str type, so we do a simple repr() coercion for types like timedelta.

    See tests/test_types.py::test_annotated_metadata_any_order for some context.
    '''
    if isinstance(v, (int, float, str)):
        return v
    return None(v)


def greater_than_validator(x = None, gt = None):
    
    try:
        if not x > gt:
            raise PydanticKnownError('greater_than', {
                'gt': _safe_repr(gt) })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'gt\' to supplied value {x}''')



def greater_than_or_equal_validator(x = None, ge = None):
    
    try:
        if not x >= ge:
            raise PydanticKnownError('greater_than_equal', {
                'ge': _safe_repr(ge) })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'ge\' to supplied value {x}''')



def less_than_validator(x = None, lt = None):
    
    try:
        if not x < lt:
            raise PydanticKnownError('less_than', {
                'lt': _safe_repr(lt) })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'lt\' to supplied value {x}''')



def less_than_or_equal_validator(x = None, le = None):
    
    try:
        if not x <= le:
            raise PydanticKnownError('less_than_equal', {
                'le': _safe_repr(le) })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'le\' to supplied value {x}''')



def multiple_of_validator(x = None, multiple_of = None):
    
    try:
        if x % multiple_of:
            raise PydanticKnownError('multiple_of', {
                'multiple_of': _safe_repr(multiple_of) })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'multiple_of\' to supplied value {x}''')



def min_length_validator(x = None, min_length = None):
    
    try:
        if not len(x) >= min_length:
            raise PydanticKnownError('too_short', {
                'field_type': 'Value',
                'min_length': min_length,
                'actual_length': len(x) })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'min_length\' to supplied value {x}''')



def max_length_validator(x = None, max_length = None):
    
    try:
        if len(x) > max_length:
            raise PydanticKnownError('too_long', {
                'field_type': 'Value',
                'max_length': max_length,
                'actual_length': len(x) })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'max_length\' to supplied value {x}''')



def _extract_decimal_digits_info(decimal = None):
    """Compute the total number of digits and decimal places for a given [`Decimal`][decimal.Decimal] instance.

    This function handles both normalized and non-normalized Decimal instances.
    Example: Decimal('1.230') -> 4 digits, 3 decimal places

    Args:
        decimal (Decimal): The decimal number to analyze.

    Returns:
        tuple[int, int]: A tuple containing the number of decimal places and total digits.

    Though this could be divided into two separate functions, the logic is easier to follow if we couple the computation
    of the number of decimals and digits together.
    """
    pass
# WARNING: Decompyle incomplete


def max_digits_validator(x = None, max_digits = None):
    
    try:
        (_, num_digits) = _extract_decimal_digits_info(x)
        (_, normalized_num_digits) = _extract_decimal_digits_info(x.normalize())
        if num_digits > max_digits and normalized_num_digits > max_digits:
            raise PydanticKnownError('decimal_max_digits', {
                'max_digits': max_digits })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'max_digits\' to supplied value {x}''')



def decimal_places_validator(x = None, decimal_places = None):
    
    try:
        (decimal_places_, _) = _extract_decimal_digits_info(x)
        if decimal_places_ > decimal_places:
            (normalized_decimal_places, _) = _extract_decimal_digits_info(x.normalize())
            if normalized_decimal_places > decimal_places:
                raise PydanticKnownError('decimal_max_places', {
                    'decimal_places': decimal_places })
        return x
    except TypeError:
        raise TypeError(f'''Unable to apply constraint \'decimal_places\' to supplied value {x}''')



def deque_validator(input_value = None, handler = None):
    return collections.deque(handler(input_value), maxlen = getattr(input_value, 'maxlen', None))


def defaultdict_validator(input_value = None, handler = None, default_default_factory = None):
    if isinstance(input_value, collections.defaultdict):
        default_factory = input_value.default_factory
        return collections.defaultdict(default_factory, handler(input_value))
    return None.defaultdict(default_default_factory, handler(input_value))


def get_defaultdict_default_default_factory(values_source_type = None):
    pass
# WARNING: Decompyle incomplete


def validate_str_is_valid_iana_tz(value = None):
    if isinstance(value, ZoneInfo):
        return value
    
    try:
        return ZoneInfo(value)
    except (ZoneInfoNotFoundError, ValueError, TypeError):
        raise PydanticCustomError('zoneinfo_str', 'invalid timezone: {value}', {
            'value': value })


NUMERIC_VALIDATOR_LOOKUP: 'dict[str, Callable]' = {
    'gt': greater_than_validator,
    'ge': greater_than_or_equal_validator,
    'lt': less_than_validator,
    'le': less_than_or_equal_validator,
    'multiple_of': multiple_of_validator,
    'min_length': min_length_validator,
    'max_length': max_length_validator,
    'max_digits': max_digits_validator,
    'decimal_places': decimal_places_validator }
IpType = Union[(IPv4Address, IPv6Address, IPv4Network, IPv6Network, IPv4Interface, IPv6Interface)]
IP_VALIDATOR_LOOKUP: 'dict[type[IpType], Callable]' = {
    IPv6Interface: ip_v6_interface_validator,
    IPv4Interface: ip_v4_interface_validator,
    IPv6Network: ip_v6_network_validator,
    IPv4Network: ip_v4_network_validator,
    IPv6Address: ip_v6_address_validator,
    IPv4Address: ip_v4_address_validator }
MAPPING_ORIGIN_MAP: 'dict[Any, Any]' = {
    collections.abc.MutableMapping: dict,
    collections.abc.Mapping: dict,
    typing.MutableMapping: dict,
    typing.Mapping: dict,
    collections.Counter: collections.Counter,
    typing.Counter: collections.Counter,
    typing_extensions.OrderedDict: collections.OrderedDict,
    collections.OrderedDict: collections.OrderedDict,
    typing.OrderedDict: collections.OrderedDict,
    collections.defaultdict: collections.defaultdict,
    typing.DefaultDict: collections.defaultdict }
