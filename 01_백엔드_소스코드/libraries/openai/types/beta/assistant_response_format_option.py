# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_response_format_option.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from shared.response_format_text import ResponseFormatText
from shared.response_format_json_object import ResponseFormatJSONObject
from shared.response_format_json_schema import ResponseFormatJSONSchema
__all__ = [
    'AssistantResponseFormatOption']
AssistantResponseFormatOption: TypeAlias = Union[(Literal['auto'], ResponseFormatText, ResponseFormatJSONObject, ResponseFormatJSONSchema)]
