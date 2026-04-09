# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_retrieve_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ConversationItemRetrieveEventParam']

def ConversationItemRetrieveEventParam():
    '''ConversationItemRetrieveEventParam'''
    event_id: 'str' = "\n    Send this event when you want to retrieve the server's representation of a specific item in the conversation history. This is useful, for example, to inspect user audio after noise cancellation and VAD.\n    The server will respond with a `conversation.item.retrieved` event,\n    unless the item does not exist in the conversation history, in which case the\n    server will respond with an error.\n    "

ConversationItemRetrieveEventParam = <NODE:27>(ConversationItemRetrieveEventParam, 'ConversationItemRetrieveEventParam', TypedDict, total = False)
