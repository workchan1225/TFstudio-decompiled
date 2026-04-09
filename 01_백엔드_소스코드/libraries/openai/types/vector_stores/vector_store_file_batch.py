# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_store_file_batch.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'VectorStoreFileBatch',
    'FileCounts']

class FileCounts(BaseModel):
    total: int = 'FileCounts'


class VectorStoreFileBatch(BaseModel):
    vector_store_id: str = 'A batch of files attached to a vector store.'
