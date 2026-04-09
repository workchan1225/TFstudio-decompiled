# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable
from typing_extensions import Literal, TypedDict
from conversation_item_content_param import ConversationItemContentParam
__all__ = [
    'ConversationItemParam']

def ConversationItemParam():
    '''ConversationItemParam'''
    type: "Literal['message', 'function_call', 'function_call_output']" = 'ConversationItemParam'

ConversationItemParam = <NODE:27>(ConversationItemParam, 'ConversationItemParam', TypedDict, total = False)
