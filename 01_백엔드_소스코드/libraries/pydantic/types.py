# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

__doc__ = 'The types module contains custom types used by pydantic.'
from __future__ import annotations as _annotations
import base64
import dataclasses as _dataclasses
import re
from collections.abc import Hashable, Iterator
from datetime import date, datetime
from decimal import Decimal
from enum import Enum
from pathlib import Path
from re import Pattern
from types import ModuleType
from typing import TYPE_CHECKING, Annotated, Any, Callable, ClassVar, Generic, Literal, TypeVar, Union, cast
from uuid import UUID
import annotated_types
from annotated_types import BaseMetadata, MaxLen, MinLen
from pydantic_core import CoreSchema, PydanticCustomError, SchemaSerializer, core_schema
from typing_extensions import Protocol, TypeAlias, TypeAliasType, deprecated, get_args, get_origin
from typing_inspection.introspection import is_union_origin
from _internal import _fields, _internal_dataclass, _utils, _validators
from _migration import getattr_migration
from annotated_handlers import GetCoreSchemaHandler, GetJsonSchemaHandler
from errors import PydanticUserError
from json_schema import JsonSchemaValue
from warnings import PydanticDeprecatedSince20
if TYPE_CHECKING:
    from _internal._core_metadata import CoreMetadata
__all__ = ('Strict', 'StrictStr', 'SocketPath', 'conbytes', 'conlist', 'conset', 'confrozenset', 'constr', 'ImportString', 'conint', 'PositiveInt', 'NegativeInt', 'NonNegativeInt', 'NonPositiveInt', 'confloat', 'PositiveFloat', 'NegativeFloat', 'NonNegativeFloat', 'NonPositiveFloat', 'FiniteFloat', 'condecimal', 'UUID1', 'UUID3', 'UUID4', 'UUID5', 'UUID6', 'UUID7', 'UUID8', 'FilePath', 'DirectoryPath', 'NewPath', 'Json', 'Secret', 'SecretStr', 'SecretBytes', 'StrictBool', 'StrictBytes', 'StrictInt', 'StrictFloat', 'PaymentCardNumber', 'ByteSize', 'PastDate', 'FutureDate', 'PastDatetime', 'FutureDatetime', 'condate', 'AwareDatetime', 'NaiveDatetime', 'AllowInfNan', 'EncoderProtocol', 'EncodedBytes', 'EncodedStr', 'Base64Encoder', 'Base64Bytes', 'Base64Str', 'Base64UrlBytes', 'Base64UrlStr', 'GetPydanticSchema', 'StringConstraints', 'Tag', 'Discriminator', 'JsonValue', 'OnErrorOmit', 'FailFast')
T = TypeVar('T')
Strict = <NODE:12>()
StrictBool = Annotated[(bool, Strict())]

def conint(*, strict, gt, ge, lt, le, multiple_of):
    '''
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `conint` returns a type, which doesn\'t play well with static analysis tools.

        === ":x: Don\'t do this"
            ```python
            from pydantic import BaseModel, conint

            class Foo(BaseModel):
                bar: conint(strict=True, gt=0)
            ```

        === ":white_check_mark: Do this"
            ```python
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[int, Field(strict=True, gt=0)]
            ```

    A wrapper around `int` that allows for additional constraints.

    Args:
        strict: Whether to validate the integer in strict mode. Defaults to `None`.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.

    Returns:
        The wrapped integer type.

    ```python
    from pydantic import BaseModel, ValidationError, conint

    class ConstrainedExample(BaseModel):
        constrained_int: conint(gt=1)

    m = ConstrainedExample(constrained_int=2)
    print(repr(m))
    #> ConstrainedExample(constrained_int=2)

    try:
        ConstrainedExample(constrained_int=0)
    except ValidationError as e:
        print(e.errors())
        \'\'\'
        [
            {
                \'type\': \'greater_than\',
                \'loc\': (\'constrained_int\',),
                \'msg\': \'Input should be greater than 1\',
                \'input\': 0,
                \'ctx\': {\'gt\': 1},
                \'url\': \'https://errors.pydantic.dev/2/v/greater_than\',
            }
        ]
        \'\'\'
    ```

    '''
    pass
# WARNING: Decompyle incomplete

PositiveInt = Annotated[(int, annotated_types.Gt(0))]
NegativeInt = Annotated[(int, annotated_types.Lt(0))]
NonPositiveInt = Annotated[(int, annotated_types.Le(0))]
NonNegativeInt = Annotated[(int, annotated_types.Ge(0))]
StrictInt = Annotated[(int, Strict())]
AllowInfNan = <NODE:12>()

def confloat(*, strict, gt, ge, lt, le, multiple_of, allow_inf_nan):
    '''
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `confloat` returns a type, which doesn\'t play well with static analysis tools.

        === ":x: Don\'t do this"
            ```python
            from pydantic import BaseModel, confloat

            class Foo(BaseModel):
                bar: confloat(strict=True, gt=0)
            ```

        === ":white_check_mark: Do this"
            ```python
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[float, Field(strict=True, gt=0)]
            ```

    A wrapper around `float` that allows for additional constraints.

    Args:
        strict: Whether to validate the float in strict mode.
        gt: The value must be greater than this.
        ge: The value must be greater than or equal to this.
        lt: The value must be less than this.
        le: The value must be less than or equal to this.
        multiple_of: The value must be a multiple of this.
        allow_inf_nan: Whether to allow `-inf`, `inf`, and `nan`.

    Returns:
        The wrapped float type.

    ```python
    from pydantic import BaseModel, ValidationError, confloat

    class ConstrainedExample(BaseModel):
        constrained_float: confloat(gt=1.0)

    m = ConstrainedExample(constrained_float=1.1)
    print(repr(m))
    #> ConstrainedExample(constrained_float=1.1)

    try:
        ConstrainedExample(constrained_float=0.9)
    except ValidationError as e:
        print(e.errors())
        \'\'\'
        [
            {
                \'type\': \'greater_than\',
                \'loc\': (\'constrained_float\',),
                \'msg\': \'Input should be greater than 1\',
                \'input\': 0.9,
                \'ctx\': {\'gt\': 1.0},
                \'url\': \'https://errors.pydantic.dev/2/v/greater_than\',
            }
        ]
        \'\'\'
    ```
    '''
    pass
# WARNING: Decompyle incomplete

PositiveFloat = Annotated[(float, annotated_types.Gt(0))]
NegativeFloat = Annotated[(float, annotated_types.Lt(0))]
NonPositiveFloat = Annotated[(float, annotated_types.Le(0))]
NonNegativeFloat = Annotated[(float, annotated_types.Ge(0))]
StrictFloat = Annotated[(float, Strict(True))]
FiniteFloat = Annotated[(float, AllowInfNan(False))]

def conbytes(*, min_length, max_length, strict):
    '''A wrapper around `bytes` that allows for additional constraints.

    Args:
        min_length: The minimum length of the bytes.
        max_length: The maximum length of the bytes.
        strict: Whether to validate the bytes in strict mode.

    Returns:
        The wrapped bytes type.
    '''
    pass
# WARNING: Decompyle incomplete

StrictBytes = Annotated[(bytes, Strict())]
StringConstraints = <NODE:12>()

def constr(*, strip_whitespace, to_upper, to_lower, strict, min_length, max_length, pattern):
    '''
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`StringConstraints`][pydantic.types.StringConstraints] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `constr` returns a type, which doesn\'t play well with static analysis tools.

        === ":x: Don\'t do this"
            ```python
            from pydantic import BaseModel, constr

            class Foo(BaseModel):
                bar: constr(strip_whitespace=True, to_upper=True, pattern=r\'^[A-Z]+$\')
            ```

        === ":white_check_mark: Do this"
            ```python
            from typing import Annotated

            from pydantic import BaseModel, StringConstraints

            class Foo(BaseModel):
                bar: Annotated[
                    str,
                    StringConstraints(
                        strip_whitespace=True, to_upper=True, pattern=r\'^[A-Z]+$\'
                    ),
                ]
            ```

    A wrapper around `str` that allows for additional constraints.

    ```python
    from pydantic import BaseModel, constr

    class Foo(BaseModel):
        bar: constr(strip_whitespace=True, to_upper=True)

    foo = Foo(bar=\'  hello  \')
    print(foo)
    #> bar=\'HELLO\'
    ```

    Args:
        strip_whitespace: Whether to remove leading and trailing whitespace.
        to_upper: Whether to turn all characters to uppercase.
        to_lower: Whether to turn all characters to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern to validate the string against.

    Returns:
        The wrapped string type.
    '''
    return Annotated[(str, StringConstraints(strip_whitespace = strip_whitespace, to_upper = to_upper, to_lower = to_lower, strict = strict, min_length = min_length, max_length = max_length, pattern = pattern))]

StrictStr = Annotated[(str, Strict())]
HashableItemType = TypeVar('HashableItemType', bound = Hashable)

def conset(item_type = None, *, min_length, max_length):
