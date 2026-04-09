# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_assistant_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'RealtimeConversationItemAssistantMessageParam',
    'Content']

def Content():
    '''Content'''
    type: "Literal['output_text', 'output_audio']" = 'Content'

Content = <NODE:27>(Content, 'Content', TypedDict, total = False)

def RealtimeConversationItemAssistantMessageParam():
    '''RealtimeConversationItemAssistantMessageParam'''
    status: "Literal['completed', 'incomplete', 'in_progress']" = 'An assistant message item in a Realtime conversation.'

RealtimeConversationItemAssistantMessageParam = <NODE:27>(RealtimeConversationItemAssistantMessageParam, 'RealtimeConversationItemAssistantMessageParam', TypedDict, total = False)
