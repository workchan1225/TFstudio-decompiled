# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _responses.pyc (Python 3.11)

from __future__ import annotations
import json
from typing import TYPE_CHECKING, Any, List, Iterable, cast
from typing_extensions import TypeVar, assert_never
import pydantic
from _tools import ResponsesPydanticFunctionTool
from _types import Omit
from _utils import is_given
from _compat import PYDANTIC_V1, model_parse_json
from _models import construct_type_unchecked
from _pydantic import is_basemodel_type, is_dataclass_like_type
from _completions import solve_response_format_t, type_to_response_format_param
from types.responses import Response, ToolParam, ParsedContent, ParsedResponse, FunctionToolParam, ParsedResponseOutputItem, ParsedResponseOutputText, ResponseFunctionToolCall, ParsedResponseOutputMessage, ResponseFormatTextConfigParam, ParsedResponseFunctionToolCall
from types.chat.completion_create_params import ResponseFormat
TextFormatT = TypeVar('TextFormatT', default = None)

def type_to_text_format_param(type_ = None):
    response_format_dict = type_to_response_format_param(type_)
# WARNING: Decompyle incomplete


def parse_response(*, text_format, input_tools, response):
    solved_t = solve_response_format_t(text_format)
    output_list = []
# WARNING: Decompyle incomplete


def parse_text(text = None, text_format = None):
    if not is_given(text_format):
        return None
    if None(text_format):
        return cast(TextFormatT, model_parse_json(text_format, text))
    if None(text_format):
        if PYDANTIC_V1:
            raise TypeError(f'''Non BaseModel types are only supported with Pydantic v2 - {text_format}''')
        return pydantic.TypeAdapter(text_format).validate_json(text)
    raise None(f'''Unable to automatically parse response format type {text_format}''')


def get_input_tool_by_name(*, input_tools, name):
    for tool in input_tools:
        if tool['type'] == 'function' and tool.get('name') == name:
            
            return None, tool
        return None


def parse_function_tool_arguments(*, input_tools, function_call):
    pass
# WARNING: Decompyle incomplete
