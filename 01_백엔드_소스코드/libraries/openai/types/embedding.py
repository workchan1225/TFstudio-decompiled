# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: embedding.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'Embedding']

class Embedding(BaseModel):
    object: Literal['embedding'] = 'Represents an embedding vector returned by embedding endpoint.'
