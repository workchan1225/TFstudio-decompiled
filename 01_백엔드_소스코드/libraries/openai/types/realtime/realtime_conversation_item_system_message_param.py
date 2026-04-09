# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_conversation_item_system_message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'RealtimeConversationItemSystemMessageParam',
    'Content']

def Content():
    '''Content'''
    type: "Literal['input_text']" = 'Content'

Content = <NODE:27>(Content, 'Content', TypedDict, total = False)

def RealtimeConversationItemSystemMessageParam():
    '''RealtimeConversationItemSystemMessageParam'''
    status: "Literal['completed', 'incomplete', 'in_progress']" = '\n    A system message in a Realtime conversation can be used to provide additional context or instructions to the model. This is similar but distinct from the instruction prompt provided at the start of a conversation, as system messages can be added at any point in the conversation. For major changes to the conversation\'s behavior, use instructions, but for smaller updates (e.g. "the user is now asking about a different topic"), use system messages.\n    '

RealtimeConversationItemSystemMessageParam = <NODE:27>(RealtimeConversationItemSystemMessageParam, 'RealtimeConversationItemSystemMessageParam', TypedDict, total = False)
