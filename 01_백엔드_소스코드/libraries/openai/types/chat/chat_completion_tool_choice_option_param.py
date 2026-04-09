# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_tool_choice_option_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypeAlias
from chat_completion_named_tool_choice_param import ChatCompletionNamedToolChoiceParam
from chat_completion_allowed_tool_choice_param import ChatCompletionAllowedToolChoiceParam
from chat_completion_named_tool_choice_custom_param import ChatCompletionNamedToolChoiceCustomParam
__all__ = [
    'ChatCompletionToolChoiceOptionParam']
ChatCompletionToolChoiceOptionParam: 'TypeAlias' = Union[(Literal[('none', 'auto', 'required')], ChatCompletionAllowedToolChoiceParam, ChatCompletionNamedToolChoiceParam, ChatCompletionNamedToolChoiceCustomParam)]
