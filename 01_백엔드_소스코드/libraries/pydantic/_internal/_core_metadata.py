# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _core_metadata.pyc (Python 3.11)

from __future__ import annotations as _annotations
from typing import TYPE_CHECKING, Any, TypedDict, cast
from warnings import warn
if TYPE_CHECKING:
    from config import JsonDict, JsonSchemaExtraCallable
    from _schema_generation_shared import GetJsonSchemaFunction

def CoreMetadata():
    '''CoreMetadata'''
    pydantic_internal_union_discriminator: 'str' = "A `TypedDict` for holding the metadata dict of the schema.\n\n    Attributes:\n        pydantic_js_functions: List of JSON schema functions that resolve refs during application.\n        pydantic_js_annotation_functions: List of JSON schema functions that don't resolve refs during application.\n        pydantic_js_prefer_positional_arguments: Whether JSON schema generator will\n            prefer positional over keyword arguments for an 'arguments' schema.\n            custom validation function. Only applies to before, plain, and wrap validators.\n        pydantic_js_updates: key / value pair updates to apply to the JSON schema for a type.\n        pydantic_js_extra: WIP, either key/value pair updates to apply to the JSON schema, or a custom callable.\n        pydantic_internal_union_tag_key: Used internally by the `Tag` metadata to specify the tag used for a discriminated union.\n        pydantic_internal_union_discriminator: Used internally to specify the discriminator value for a discriminated union\n            when the discriminator was applied to a `'definition-ref'` schema, and that reference was missing at the time\n            of the annotation application.\n\n    TODO: Perhaps we should move this structure to pydantic-core. At the moment, though,\n    it's easier to iterate on if we leave it in pydantic until we feel there is a semi-stable API.\n\n    TODO: It's unfortunate how functionally oriented JSON schema generation is, especially that which occurs during\n    the core schema generation process. It's inevitable that we need to store some json schema related information\n    on core schemas, given that we generate JSON schemas directly from core schemas. That being said, debugging related\n    issues is quite difficult when JSON schema information is disguised via dynamically defined functions.\n    "

CoreMetadata = <NODE:27>(CoreMetadata, 'CoreMetadata', TypedDict, total = False)

def update_core_metadata(core_metadata = None, *, pydantic_js_functions, pydantic_js_annotation_functions, pydantic_js_updates, pydantic_js_extra):
    PydanticJsonSchemaWarning = PydanticJsonSchemaWarning
    import json_schema
    core_metadata = cast(CoreMetadata, core_metadata)
    if pydantic_js_functions:
        core_metadata.setdefault('pydantic_js_functions', []).extend(pydantic_js_functions)
    if pydantic_js_annotation_functions:
        core_metadata.setdefault('pydantic_js_annotation_functions', []).extend(pydantic_js_annotation_functions)
# WARNING: Decompyle incomplete
