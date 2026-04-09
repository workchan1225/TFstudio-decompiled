# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_raw_message_stop_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaRawMessageStopEvent']

class BetaRawMessageStopEvent(BaseModel):
    type: Literal['message_stop'] = 'BetaRawMessageStopEvent'
