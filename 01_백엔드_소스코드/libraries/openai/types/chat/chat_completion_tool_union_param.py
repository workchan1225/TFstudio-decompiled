# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_tool_union_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from chat_completion_custom_tool_param import ChatCompletionCustomToolParam
from chat_completion_function_tool_param import ChatCompletionFunctionToolParam
__all__ = [
    'ChatCompletionToolUnionParam']
ChatCompletionToolUnionParam: 'TypeAlias' = Union[(ChatCompletionFunctionToolParam, ChatCompletionCustomToolParam)]
