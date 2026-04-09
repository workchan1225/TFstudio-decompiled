# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_json_object.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ResponseFormatJSONObject']

def ResponseFormatJSONObject():
    '''ResponseFormatJSONObject'''
    type: "Required[Literal['json_object']]" = 'JSON object response format.\n\n    An older method of generating JSON responses.\n    Using `json_schema` is recommended for models that support it. Note that the\n    model will not generate JSON without a system or user message instructing it\n    to do so.\n    '

ResponseFormatJSONObject = <NODE:27>(ResponseFormatJSONObject, 'ResponseFormatJSONObject', TypedDict, total = False)
