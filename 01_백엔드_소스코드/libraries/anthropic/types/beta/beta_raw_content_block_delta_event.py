# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_raw_content_block_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_raw_content_block_delta import BetaRawContentBlockDelta
__all__ = [
    'BetaRawContentBlockDeltaEvent']

class BetaRawContentBlockDeltaEvent(BaseModel):
    type: Literal['content_block_delta'] = 'BetaRawContentBlockDeltaEvent'
