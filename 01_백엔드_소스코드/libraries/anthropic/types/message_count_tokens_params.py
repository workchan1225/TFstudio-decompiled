# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_count_tokens_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Required, TypedDict
from model_param import ModelParam
from message_param import MessageParam
from text_block_param import TextBlockParam
from tool_choice_param import ToolChoiceParam
from thinking_config_param import ThinkingConfigParam
from message_count_tokens_tool_param import MessageCountTokensToolParam
__all__ = [
    'MessageCountTokensParams']

def MessageCountTokensParams():
    '''MessageCountTokensParams'''
    tools: 'Iterable[MessageCountTokensToolParam]' = 'MessageCountTokensParams'

MessageCountTokensParams = <NODE:27>(MessageCountTokensParams, 'MessageCountTokensParams', TypedDict, total = False)
