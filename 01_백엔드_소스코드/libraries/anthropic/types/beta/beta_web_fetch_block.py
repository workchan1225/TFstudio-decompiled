# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_fetch_block.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from beta_document_block import BetaDocumentBlock
__all__ = [
    'BetaWebFetchBlock']

class BetaWebFetchBlock(BaseModel):
    content: BetaDocumentBlock = 'BetaWebFetchBlock'
    url: str = None
