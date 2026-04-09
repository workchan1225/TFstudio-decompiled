# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_developer_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict
from chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
__all__ = [
    'ChatCompletionDeveloperMessageParam']

def ChatCompletionDeveloperMessageParam():
    '''ChatCompletionDeveloperMessageParam'''
    name: 'str' = '\n    Developer-provided instructions that the model should follow, regardless of\n    messages sent by the user. With o1 models and newer, `developer` messages\n    replace the previous `system` messages.\n    '

ChatCompletionDeveloperMessageParam = <NODE:27>(ChatCompletionDeveloperMessageParam, 'ChatCompletionDeveloperMessageParam', TypedDict, total = False)
