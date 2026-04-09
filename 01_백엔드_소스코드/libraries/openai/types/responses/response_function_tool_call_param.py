# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_tool_call_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ResponseFunctionToolCallParam']

def ResponseFunctionToolCallParam():
    '''ResponseFunctionToolCallParam'''
    status: "Literal['in_progress', 'completed', 'incomplete']" = 'A tool call to run a function.\n\n    See the\n    [function calling guide](https://platform.openai.com/docs/guides/function-calling) for more information.\n    '

ResponseFunctionToolCallParam = <NODE:27>(ResponseFunctionToolCallParam, 'ResponseFunctionToolCallParam', TypedDict, total = False)
