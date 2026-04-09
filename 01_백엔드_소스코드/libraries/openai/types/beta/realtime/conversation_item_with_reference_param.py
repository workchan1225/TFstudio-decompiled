# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_with_reference_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable
from typing_extensions import Literal, TypedDict
__all__ = [
    'ConversationItemWithReferenceParam',
    'Content']

def Content():
    '''Content'''
    type: "Literal['input_text', 'input_audio', 'item_reference', 'text']" = 'Content'

Content = <NODE:27>(Content, 'Content', TypedDict, total = False)

def ConversationItemWithReferenceParam():
    '''ConversationItemWithReferenceParam'''
    type: "Literal['message', 'function_call', 'function_call_output', 'item_reference']" = 'ConversationItemWithReferenceParam'

ConversationItemWithReferenceParam = <NODE:27>(ConversationItemWithReferenceParam, 'ConversationItemWithReferenceParam', TypedDict, total = False)
