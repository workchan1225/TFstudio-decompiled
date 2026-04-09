# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: raw_message_delta_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from stop_reason import StopReason
from message_delta_usage import MessageDeltaUsage
__all__ = [
    'RawMessageDeltaEvent',
    'Delta']

class Delta(BaseModel):
    stop_reason: Optional[StopReason] = None
    stop_sequence: Optional[str] = None


class RawMessageDeltaEvent(BaseModel):
    usage: MessageDeltaUsage = 'RawMessageDeltaEvent'
