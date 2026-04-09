# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_user_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'RealtimeConversationItemUserMessageParam',
    'Content']

def Content():
    '''Content'''
    type: "Literal['input_text', 'input_audio', 'input_image']" = 'Content'

Content = <NODE:27>(Content, 'Content', TypedDict, total = False)

def RealtimeConversationItemUserMessageParam():
    '''RealtimeConversationItemUserMessageParam'''
    status: "Literal['completed', 'incomplete', 'in_progress']" = 'A user message item in a Realtime conversation.'

RealtimeConversationItemUserMessageParam = <NODE:27>(RealtimeConversationItemUserMessageParam, 'RealtimeConversationItemUserMessageParam', TypedDict, total = False)
