# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: create_embedding_response.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
from embedding import Embedding
__all__ = [
    'CreateEmbeddingResponse',
    'Usage']

class Usage(BaseModel):
    total_tokens: int = 'The usage information for the request.'


class CreateEmbeddingResponse(BaseModel):
    usage: Usage = 'CreateEmbeddingResponse'
