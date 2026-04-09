# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_call_incoming_webhook_event.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeCallIncomingWebhookEvent',
    'Data',
    'DataSipHeader']

class DataSipHeader(BaseModel):
    value: str = 'A header from the SIP Invite.'


class Data(BaseModel):
    sip_headers: List[DataSipHeader] = 'Event data payload.'


class RealtimeCallIncomingWebhookEvent(BaseModel):
    type: Literal['realtime.call.incoming'] = 'Sent when Realtime API Receives a incoming SIP call.'
    object: Optional[Literal['event']] = None
