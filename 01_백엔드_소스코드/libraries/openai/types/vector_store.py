# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_store.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
from shared.metadata import Metadata
__all__ = [
    'VectorStore',
    'FileCounts',
    'ExpiresAfter']

class FileCounts(BaseModel):
    total: int = 'FileCounts'


class ExpiresAfter(BaseModel):
    days: int = 'The expiration policy for a vector store.'


class VectorStore(BaseModel):
    file_counts: FileCounts = '\n    A vector store is a collection of processed files can be used by the `file_search` tool.\n    '
    last_active_at: Optional[int] = None
    usage_bytes: int = None
    expires_after: Optional[ExpiresAfter] = None
    expires_at: Optional[int] = None
