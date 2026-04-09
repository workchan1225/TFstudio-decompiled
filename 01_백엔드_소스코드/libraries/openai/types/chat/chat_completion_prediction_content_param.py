# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chat_completion_prediction_content_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict
from chat_completion_content_part_text_param import ChatCompletionContentPartTextParam
__all__ = [
    'ChatCompletionPredictionContentParam']

def ChatCompletionPredictionContentParam():
    '''ChatCompletionPredictionContentParam'''
    type: "Required[Literal['content']]" = '\n    Static predicted output content, such as the content of a text file that is\n    being regenerated.\n    '

ChatCompletionPredictionContentParam = <NODE:27>(ChatCompletionPredictionContentParam, 'ChatCompletionPredictionContentParam', TypedDict, total = False)
