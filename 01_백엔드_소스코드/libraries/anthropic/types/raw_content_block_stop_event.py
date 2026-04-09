# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: raw_content_block_stop_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RawContentBlockStopEvent']

class RawContentBlockStopEvent(BaseModel):
    type: Literal['content_block_stop'] = 'RawContentBlockStopEvent'
