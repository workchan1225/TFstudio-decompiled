# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: citation_char_location.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CitationCharLocation']

class CitationCharLocation(BaseModel):
    document_index: int = 'CitationCharLocation'
    end_char_index: int = None
    type: Literal['char_location'] = None
