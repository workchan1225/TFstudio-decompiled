# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_delete_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ConversationItemDeleteEventParam']

def ConversationItemDeleteEventParam():
    '''ConversationItemDeleteEventParam'''
    event_id: 'str' = 'Send this event when you want to remove any item from the conversation\n    history.\n\n    The server will respond with a `conversation.item.deleted` event,\n    unless the item does not exist in the conversation history, in which case the\n    server will respond with an error.\n    '

ConversationItemDeleteEventParam = <NODE:27>(ConversationItemDeleteEventParam, 'ConversationItemDeleteEventParam', TypedDict, total = False)
