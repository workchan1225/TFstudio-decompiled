# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _transform.pyc (Python 3.11)

from __future__ import annotations
import io
import base64
import pathlib
from typing import Any, Mapping, TypeVar, cast
from datetime import date, datetime
from typing_extensions import Literal, get_args, override, get_type_hints as _get_type_hints
import anyio
import pydantic
from _utils import is_list, is_given, lru_cache, is_mapping, is_iterable, is_sequence
from _files import is_base64_file_input
from _compat import get_origin, is_typeddict
from _typing import is_list_type, is_union_type, extract_type_arg, is_iterable_type, is_required_type, is_sequence_type, is_annotated_type, strip_annotated_type
_T = TypeVar('_T')
PropertyFormat = Literal[('iso8601', 'base64', 'custom')]

class PropertyInfo:
    discriminator: 'str | None' = "Metadata class to be used in Annotated types to provide information about a given type.\n\n    For example:\n\n    class MyParams(TypedDict):\n        account_holder_name: Annotated[str, PropertyInfo(alias='accountHolderName')]\n\n    This means that {'account_holder_name': 'Robert'} will be transformed to {'accountHolderName': 'Robert'} before being sent to the API.\n    "
    
    def __init__(self = None, *, alias, format, format_template, discriminator):
        self.alias = alias
        self.format = format
        self.format_template = format_template
        self.discriminator = discriminator

    __repr__ = (lambda self = None: f'''{self.__class__.__name__}(alias=\'{self.alias}\', format={self.format}, format_template=\'{self.format_template}\', discriminator=\'{self.discriminator}\')''')()


def maybe_transform(data = None, expected_type = None):
    '''Wrapper over `transform()` that allows `None` to be passed.

    See `transform()` for more details.
    '''
    pass
# WARNING: Decompyle incomplete


def transform(data = None, expected_type = None):
    '''Transform dictionaries based off of type information from the given type, for example:

    ```py
    class Params(TypedDict, total=False):
        card_id: Required[Annotated[str, PropertyInfo(alias="cardID")]]


    transformed = transform({"card_id": "<my card ID>"}, Params)
    # {\'cardID\': \'<my card ID>\'}
    ```

    Any keys / data that does not have type information given will be included as is.

    It should be noted that the transformations that this function does are not represented in the type system.
    '''
    transformed = _transform_recursive(data, annotation = cast(type, expected_type))
    return cast(_T, transformed)

_get_annotated_type = (lambda type_ = None: if is_required_type(type_):
type_ = get_args(type_)[0]if is_annotated_type(type_):
type_)()

def _maybe_transform_key(key = None, type_ = None):
    '''Transform the given `data` based on the annotations provided in `type_`.

    Note: this function only looks at `Annotated` types that contain `PropertyInfo` metadata.
    '''
    annotated_type = _get_annotated_type(type_)
# WARNING: Decompyle incomplete


def _no_transform_needed(annotation = None):
