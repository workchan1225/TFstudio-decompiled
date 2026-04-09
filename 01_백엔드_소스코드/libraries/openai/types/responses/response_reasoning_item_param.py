# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_reasoning_item_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ResponseReasoningItemParam',
    'Summary',
    'Content']

def Summary():
    '''Summary'''
    type: "Required[Literal['summary_text']]" = 'A summary text from the model.'

Summary = <NODE:27>(Summary, 'Summary', TypedDict, total = False)

def Content():
    '''Content'''
    type: "Required[Literal['reasoning_text']]" = 'Reasoning text from the model.'

Content = <NODE:27>(Content, 'Content', TypedDict, total = False)

def ResponseReasoningItemParam():
    '''ResponseReasoningItemParam'''
    status: "Literal['in_progress', 'completed', 'incomplete']" = '\n    A description of the chain of thought used by a reasoning model while generating\n    a response. Be sure to include these items in your `input` to the Responses API\n    for subsequent turns of a conversation if you are manually\n    [managing context](https://platform.openai.com/docs/guides/conversation-state).\n    '

ResponseReasoningItemParam = <NODE:27>(ResponseReasoningItemParam, 'ResponseReasoningItemParam', TypedDict, total = False)
