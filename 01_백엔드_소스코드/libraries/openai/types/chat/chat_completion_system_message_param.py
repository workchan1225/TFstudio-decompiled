# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_system_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict
from chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
__all__ = [
    'ChatCompletionSystemMessageParam']

def ChatCompletionSystemMessageParam():
    '''ChatCompletionSystemMessageParam'''
    name: 'str' = '\n    Developer-provided instructions that the model should follow, regardless of\n    messages sent by the user. With o1 models and newer, use `developer` messages\n    for this purpose instead.\n    '

ChatCompletionSystemMessageParam = <NODE:27>(ChatCompletionSystemMessageParam, 'ChatCompletionSystemMessageParam', TypedDict, total = False)
