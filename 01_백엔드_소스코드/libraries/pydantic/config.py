# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

'''Configuration for Pydantic models.'''
from __future__ import annotations as _annotations
import warnings
from re import Pattern
from typing import TYPE_CHECKING, Any, Callable, Literal, TypeVar, Union, cast, overload
from typing_extensions import TypeAlias, TypedDict, Unpack, deprecated
from _migration import getattr_migration
from aliases import AliasGenerator
from errors import PydanticUserError
from warnings import PydanticDeprecatedSince211
if TYPE_CHECKING:
    from _internal._generate_schema import GenerateSchema as _GenerateSchema
    from fields import ComputedFieldInfo, FieldInfo
__all__ = ('ConfigDict', 'with_config')
JsonValue: 'TypeAlias' = Union[(int, float, str, bool, None, list['JsonValue'], 'JsonDict')]
JsonDict: 'TypeAlias' = dict[(str, JsonValue)]
JsonEncoder = Callable[([
    Any], Any)]
JsonSchemaExtraCallable: 'TypeAlias' = Union[(Callable[([
    JsonDict], None)], Callable[([
    JsonDict,
    type[Any]], None)])]
ExtraValues = Literal[('allow', 'ignore', 'forbid')]

def ConfigDict():
    '''ConfigDict'''
    url_preserve_empty_path: 'bool' = 'A TypedDict for configuring Pydantic behaviour.'

ConfigDict = <NODE:27>(ConfigDict, 'ConfigDict', TypedDict, total = False)
_TypeT = TypeVar('_TypeT', bound = type)
with_config = (lambda *: pass)()()
with_config = (lambda config = None: pass)()
with_config = (lambda : pass)()

def with_config(config = None, **kwargs):
    '''!!! abstract "Usage Documentation"
        [Configuration with other types](../concepts/config.md#configuration-on-other-supported-types)

    A convenience decorator to set a [Pydantic configuration](config.md) on a `TypedDict` or a `dataclass` from the standard library.

    Although the configuration can be set using the `__pydantic_config__` attribute, it does not play well with type checkers,
    especially with `TypedDict`.

    !!! example "Usage"

        ```python
        from typing_extensions import TypedDict

        from pydantic import ConfigDict, TypeAdapter, with_config

        @with_config(ConfigDict(str_to_lower=True))
        class TD(TypedDict):
            x: str

        ta = TypeAdapter(TD)

        print(ta.validate_python({\'x\': \'ABC\'}))
        #> {\'x\': \'abc\'}
        ```

    /// deprecated-removed | v2.11 v3
    Passing `config` as a keyword argument.
    ///

    /// version-changed | v2.11
    Keyword arguments can be provided directly instead of a config dictionary.
    ///
    '''
    pass
# WARNING: Decompyle incomplete

__getattr__ = getattr_migration(__name__)
