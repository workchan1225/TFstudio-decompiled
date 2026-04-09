# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_create_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from conversation_item_param import ConversationItemParam
__all__ = [
    'ConversationItemCreateEventParam']

def ConversationItemCreateEventParam():
    '''ConversationItemCreateEventParam'''
    previous_item_id: 'str' = '\n    Add a new Item to the Conversation\'s context, including messages, function\n    calls, and function call responses. This event can be used both to populate a\n    "history" of the conversation and to add new items mid-stream, but has the\n    current limitation that it cannot populate assistant audio messages.\n\n    If successful, the server will respond with a `conversation.item.created`\n    event, otherwise an `error` event will be sent.\n    '

ConversationItemCreateEventParam = <NODE:27>(ConversationItemCreateEventParam, 'ConversationItemCreateEventParam', TypedDict, total = False)
