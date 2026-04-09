# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _discriminated_union.pyc (Python 3.11)

from __future__ import annotations as _annotations
from collections.abc import Hashable, Sequence
from typing import TYPE_CHECKING, Any, cast
from pydantic_core import CoreSchema, core_schema
from errors import PydanticUserError
from  import _core_utils
from _core_utils import CoreSchemaField
if TYPE_CHECKING:
    from types import Discriminator
    from _core_metadata import CoreMetadata

class MissingDefinitionForUnionRef(Exception):
    pass
# WARNING: Decompyle incomplete


def set_discriminator_in_metadata(schema = None, discriminator = None):
    metadata = cast('CoreMetadata', schema.setdefault('metadata', { }))
    metadata['pydantic_internal_union_discriminator'] = discriminator


def apply_discriminator(schema = None, discriminator = None, definitions = None):
