# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_store_file.pyc (Python 3.11)

from typing import Dict, Union, Optional
from typing_extensions import Literal
from _models import BaseModel
from file_chunking_strategy import FileChunkingStrategy
__all__ = [
    'VectorStoreFile',
    'LastError']

class LastError(BaseModel):
    message: str = 'The last error associated with this vector store file.\n\n    Will be `null` if there are no errors.\n    '


class VectorStoreFile(BaseModel):
    created_at: int = 'A list of files attached to a vector store.'
    vector_store_id: str = None
    attributes: Optional[Dict[(str, Union[(str, float, bool)])]] = None
    chunking_strategy: Optional[FileChunkingStrategy] = None
