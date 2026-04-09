# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_raw_message_start_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_message import BetaMessage
__all__ = [
    'BetaRawMessageStartEvent']

class BetaRawMessageStartEvent(BaseModel):
    type: Literal['message_start'] = 'BetaRawMessageStartEvent'
