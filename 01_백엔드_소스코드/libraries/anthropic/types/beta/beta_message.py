# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_message.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from model import Model
from _models import BaseModel
from beta_usage import BetaUsage
from beta_container import BetaContainer
from beta_stop_reason import BetaStopReason
from beta_content_block import BetaContentBlock, BetaContentBlock
from beta_context_management_response import BetaContextManagementResponse
__all__ = [
    'BetaMessage']

class BetaMessage(BaseModel):
    id: str = 'BetaMessage'
    content: List[BetaContentBlock] = None
    role: Literal['assistant'] = None
    stop_reason: Optional[BetaStopReason] = None
    usage: BetaUsage = None
