# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _completions.pyc (Python 3.11)

from __future__ import annotations
import json
import logging
from typing import TYPE_CHECKING, Any, Iterable, cast
from typing_extensions import TypeVar, TypeGuard, assert_never
import pydantic
from _tools import PydanticFunctionTool
from _types import Omit, omit
from _utils import is_dict, is_given
from _compat import PYDANTIC_V1, model_parse_json
from _models import construct_type_unchecked
from _pydantic import is_basemodel_type, to_strict_json_schema, is_dataclass_like_type
from types.chat import ParsedChoice, ChatCompletion, ParsedFunction, ParsedChatCompletion, ChatCompletionMessage, ParsedFunctionToolCall, ParsedChatCompletionMessage, ChatCompletionToolUnionParam, ChatCompletionFunctionToolParam, completion_create_params
from _exceptions import LengthFinishReasonError, ContentFilterFinishReasonError
from types.shared_params import FunctionDefinition
from types.chat.completion_create_params import ResponseFormat as ResponseFormatParam
from types.chat.chat_completion_message_function_tool_call import Function
ResponseFormatT = TypeVar('ResponseFormatT', default = None)
_default_response_format: 'None' = None
log: 'logging.Logger' = logging.getLogger('openai.lib.parsing')

def is_strict_chat_completion_tool_param(tool = None):
    '''Check if the given tool is a strict ChatCompletionFunctionToolParam.'''
    if not tool['type'] == 'function':
        return False
    if None['function'].get('strict') is not True:
        return False


def select_strict_chat_completion_tools(tools = None):
