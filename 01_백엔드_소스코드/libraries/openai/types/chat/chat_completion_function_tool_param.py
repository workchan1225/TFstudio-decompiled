# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_function_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from shared_params.function_definition import FunctionDefinition
__all__ = [
    'ChatCompletionFunctionToolParam']

def ChatCompletionFunctionToolParam():
    '''ChatCompletionFunctionToolParam'''
    type: "Required[Literal['function']]" = 'A function tool that can be used to generate a response.'

ChatCompletionFunctionToolParam = <NODE:27>(ChatCompletionFunctionToolParam, 'ChatCompletionFunctionToolParam', TypedDict, total = False)
