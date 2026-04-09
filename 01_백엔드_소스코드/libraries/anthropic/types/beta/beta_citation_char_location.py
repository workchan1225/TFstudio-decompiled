# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_citation_char_location.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaCitationCharLocation']

class BetaCitationCharLocation(BaseModel):
    document_index: int = 'BetaCitationCharLocation'
    end_char_index: int = None
    type: Literal['char_location'] = None
