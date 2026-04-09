# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: assistant_response_format_option_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypeAlias
from shared_params.response_format_text import ResponseFormatText
from shared_params.response_format_json_object import ResponseFormatJSONObject
from shared_params.response_format_json_schema import ResponseFormatJSONSchema
__all__ = [
    'AssistantResponseFormatOptionParam']
AssistantResponseFormatOptionParam: 'TypeAlias' = Union[(Literal['auto'], ResponseFormatText, ResponseFormatJSONObject, ResponseFormatJSONSchema)]
