# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: citation_content_block_location.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'CitationContentBlockLocation']

class CitationContentBlockLocation(BaseModel):
    document_index: int = 'CitationContentBlockLocation'
    end_block_index: int = None
    type: Literal['content_block_location'] = None
