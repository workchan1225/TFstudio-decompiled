# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from message_delta import MessageDelta
__all__ = [
    'MessageDeltaEvent']

class MessageDeltaEvent(BaseModel):
    object: Literal['thread.message.delta'] = 'Represents a message delta i.e.\n\n    any changed fields on a message during streaming.\n    '
