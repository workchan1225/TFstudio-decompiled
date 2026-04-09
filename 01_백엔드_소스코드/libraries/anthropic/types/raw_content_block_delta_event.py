# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: raw_content_block_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from raw_content_block_delta import RawContentBlockDelta
__all__ = [
    'RawContentBlockDeltaEvent']

class RawContentBlockDeltaEvent(BaseModel):
    type: Literal['content_block_delta'] = 'RawContentBlockDeltaEvent'
