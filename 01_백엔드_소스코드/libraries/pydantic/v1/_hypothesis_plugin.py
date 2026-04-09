# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _hypothesis_plugin.pyc (Python 3.11)

'''
Register Hypothesis strategies for Pydantic custom types.

This enables fully-automatic generation of test data for most Pydantic classes.

Note that this module has *no* runtime impact on Pydantic itself; instead it
is registered as a setuptools entry point and Hypothesis will import it if
Pydantic is installed.  See also:

https://hypothesis.readthedocs.io/en/latest/strategies.html#registering-strategies-via-setuptools-entry-points
https://hypothesis.readthedocs.io/en/latest/data.html#hypothesis.strategies.register_type_strategy
https://hypothesis.readthedocs.io/en/latest/strategies.html#interaction-with-pytest-cov
https://docs.pydantic.dev/usage/types/#pydantic-types

Note that because our motivation is to *improve user experience*, the strategies
are always sound (never generate invalid data) but sacrifice completeness for
maintainability (ie may be unable to generate some tricky but valid data).

Finally, this module makes liberal use of `# type: ignore[<code>]` pragmas.
This is because Hypothesis annotates `register_type_strategy()` with
`(T, SearchStrategy[T])`, but in most cases we register e.g. `ConstrainedInt`
to generate instances of the builtin `int` type which match the constraints.
'''
import contextlib
import datetime
import ipaddress
import json
import math
from fractions import Fraction
from typing import Callable, Dict, Type, Union, cast, overload
from hypothesis.strategies import strategies as st
import pydantic
import pydantic.color as pydantic
import pydantic.types as pydantic
from pydantic.v1.utils import lenient_issubclass

try:
    import email_validator
    
    def is_valid_email(s = None):
        
        try:
            email_validator.validate_email(s, check_deliverability = False)
            return True
        except email_validator.EmailNotValidError:
            return False


    st.register_type_strategy(pydantic.EmailStr, st.emails().filter(is_valid_email))
    st.register_type_strategy(pydantic.NameEmail, st.builds('{} <{}>'.format, st.from_regex('[A-Za-z0-9_]+( [A-Za-z0-9_]+){0,5}', fullmatch = True), st.emails().filter(is_valid_email)))
except ImportError:
    pass

None(st.sampled_from, (lambda .0: pass# WARNING: Decompyle incomplete
)(sorted(vars(math))()))
_color_regexes = '|'.join((pydantic.color.r_hex_short, pydantic.color.r_hex_long, pydantic.color.r_rgb, pydantic.color.r_rgba, pydantic.color.r_hsl, pydantic.color.r_hsla)).replace(pydantic.color._r_sl, '(?:(\\d\\d?(?:\\.\\d+)?|100(?:\\.0+)?)%)').replace(pydantic.color._r_alpha, '(?:(0(?:\\.\\d+)?|1(?:\\.0+)?|\\.\\d+|\\d{1,2}%))').replace(pydantic.color._r_255, '(?:((?:\\d|\\d\\d|[01]\\d\\d|2[0-4]\\d|25[0-4])(?:\\.\\d+)?|255(?:\\.0+)?))')
st.register_type_strategy(pydantic.color.Color, st.one_of(st.sampled_from(sorted(pydantic.color.COLORS_BY_NAME)), st.tuples(st.integers(0, 255), st.integers(0, 255), st.integers(0, 255), st.none() | st.floats(0, 1) | st.floats(0, 100).map('{}%'.format)), st.from_regex(_color_regexes, fullmatch = True)))

def add_luhn_digit(card_number = None):
    for digit in '0123456789':
        contextlib.suppress(Exception)
        pydantic.PaymentCardNumber.validate_luhn_check_digit(card_number + digit)
        None(None, None)
        
        return None, card_number + digit, 
        with None:
            if not None:
                pass
        raise AssertionError('Unreachable')

card_patterns = ('4[0-9]{14}', '5[12345][0-9]{13}', '3[47][0-9]{12}', '[0-26-9][0-9]{10,17}')
st.register_type_strategy(pydantic.PaymentCardNumber, st.from_regex('|'.join(card_patterns), fullmatch = True).map(add_luhn_digit))
st.register_type_strategy(pydantic.UUID1, st.uuids(version = 1))
st.register_type_strategy(pydantic.UUID3, st.uuids(version = 3))
st.register_type_strategy(pydantic.UUID4, st.uuids(version = 4))
st.register_type_strategy(pydantic.UUID5, st.uuids(version = 5))
st.register_type_strategy(pydantic.SecretBytes, st.binary().map(pydantic.SecretBytes))
st.register_type_strategy(pydantic.SecretStr, st.text().map(pydantic.SecretStr))
st.register_type_strategy(pydantic.IPvAnyAddress, st.ip_addresses())
st.register_type_strategy(pydantic.IPvAnyInterface, st.from_type(ipaddress.IPv4Interface) | st.from_type(ipaddress.IPv6Interface))
st.register_type_strategy(pydantic.IPvAnyNetwork, st.from_type(ipaddress.IPv4Network) | st.from_type(ipaddress.IPv6Network))
st.register_type_strategy(pydantic.StrictBool, st.booleans())
st.register_type_strategy(pydantic.StrictStr, st.text())
st.register_type_strategy(pydantic.FutureDate, st.dates(min_value = datetime.date.today() + datetime.timedelta(days = 1)))
st.register_type_strategy(pydantic.PastDate, st.dates(max_value = datetime.date.today() - datetime.timedelta(days = 1)))
RESOLVERS: Dict[(type, Callable[([
    type], st.SearchStrategy)])] = { }
_registered = (lambda typ = None: pass)()
_registered = (lambda typ = None: pass)()

def _registered(typ = None):
    pydantic.types._DEFINED_TYPES.add(typ)
    for supertype, resolver in RESOLVERS.items():
        if issubclass(typ, supertype):
            st.register_type_strategy(typ, resolver(typ))
            
            return None, typ
        raise NotImplementedError(f'''Unknown type {typ!r} has no resolver to register''')


def resolves(typ = None):
    pass
# WARNING: Decompyle incomplete

resolve_json = (lambda cls: pass# WARNING: Decompyle incomplete
)()
resolve_conbytes = (lambda cls: if not cls.min_length:
min_size = 0max_size = cls.max_lengthif not cls.strip_whitespace:
st.binary(min_size = min_size, max_size = max_size)repeats = None.format(min_size - 2 if min_size > 2 else 0, max_size - 2 if max_size or 0 > 2 else '')if min_size >= 2:
pattern = f'''\\W.{repeats}\\W'''elif min_size == 1:
pattern = f'''\\W(.{repeats}\\W)?'''# WARNING: Decompyle incomplete
)()
resolve_condecimal = (lambda cls: pass# WARNING: Decompyle incomplete
)()
resolve_confloat = (lambda cls: pass# WARNING: Decompyle incomplete
)()
resolve_conint = (lambda cls: pass# WARNING: Decompyle incomplete
)()
resolve_condate = (lambda cls: pass# WARNING: Decompyle incomplete
)()
resolve_constr = (lambda cls: pass# WARNING: Decompyle incomplete
)()
for typ in list(pydantic.types._DEFINED_TYPES):
    _registered(typ)
    pydantic.types._registered = _registered
    st.register_type_strategy(pydantic.Json, resolve_json)
    return None
