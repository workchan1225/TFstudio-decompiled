# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_store_search_response.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'VectorStoreSearchResponse',
    'Content']

class Content(BaseModel):
    type: Literal['text'] = 'Content'


class VectorStoreSearchResponse(BaseModel):
    score: float = None
