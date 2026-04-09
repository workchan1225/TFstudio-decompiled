# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: citation_page_location.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CitationPageLocation']

class CitationPageLocation(BaseModel):
    document_index: int = 'CitationPageLocation'
    end_page_number: int = None
    type: Literal['page_location'] = None
