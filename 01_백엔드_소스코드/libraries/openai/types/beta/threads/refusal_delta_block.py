# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: refusal_delta_block.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RefusalDeltaBlock']

class RefusalDeltaBlock(BaseModel):
    type: Literal['refusal'] = 'The refusal content that is part of a message.'
    refusal: Optional[str] = None
