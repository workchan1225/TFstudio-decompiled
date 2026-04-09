# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_json_schema.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Optional
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ResponseFormatJSONSchema',
    'JSONSchema']

def JSONSchema():
    '''JSONSchema'''
    strict: 'Optional[bool]' = 'Structured Outputs configuration options, including a JSON Schema.'

JSONSchema = <NODE:27>(JSONSchema, 'JSONSchema', TypedDict, total = False)

def ResponseFormatJSONSchema():
    '''ResponseFormatJSONSchema'''
    type: "Required[Literal['json_schema']]" = 'JSON Schema response format.\n\n    Used to generate structured JSON responses.\n    Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).\n    '

ResponseFormatJSONSchema = <NODE:27>(ResponseFormatJSONSchema, 'ResponseFormatJSONSchema', TypedDict, total = False)
