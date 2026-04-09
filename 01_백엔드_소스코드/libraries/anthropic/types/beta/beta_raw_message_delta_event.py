# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_raw_message_delta_event.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from beta_container import BetaContainer
from beta_stop_reason import BetaStopReason
from beta_message_delta_usage import BetaMessageDeltaUsage
from beta_context_management_response import BetaContextManagementResponse
__all__ = [
    'BetaRawMessageDeltaEvent',
    'Delta']

class Delta(BaseModel):
    container: Optional[BetaContainer] = None
    stop_reason: Optional[BetaStopReason] = None
    stop_sequence: Optional[str] = None


class BetaRawMessageDeltaEvent(BaseModel):
    usage: BetaMessageDeltaUsage = None
