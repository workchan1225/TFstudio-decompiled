# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: raw_message_start_event.pyc (Python 3.11)

from typing_extensions import Literal
from message import Message
from _models import BaseModel
__all__ = [
    'RawMessageStartEvent']

class RawMessageStartEvent(BaseModel):
    type: Literal['message_start'] = 'RawMessageStartEvent'
