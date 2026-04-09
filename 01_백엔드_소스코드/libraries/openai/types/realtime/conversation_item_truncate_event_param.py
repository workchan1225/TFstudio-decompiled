# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: conversation_item_truncate_event_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'ConversationItemTruncateEventParam']

def ConversationItemTruncateEventParam():
    '''ConversationItemTruncateEventParam'''
    event_id: 'str' = "Send this event to truncate a previous assistant message’s audio.\n\n    The server\n    will produce audio faster than realtime, so this event is useful when the user\n    interrupts to truncate audio that has already been sent to the client but not\n    yet played. This will synchronize the server's understanding of the audio with\n    the client's playback.\n\n    Truncating audio will delete the server-side text transcript to ensure there\n    is not text in the context that hasn't been heard by the user.\n\n    If successful, the server will respond with a `conversation.item.truncated`\n    event.\n    "

ConversationItemTruncateEventParam = <NODE:27>(ConversationItemTruncateEventParam, 'ConversationItemTruncateEventParam', TypedDict, total = False)
