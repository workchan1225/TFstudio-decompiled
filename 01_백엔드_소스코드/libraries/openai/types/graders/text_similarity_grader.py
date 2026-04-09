# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_similarity_grader.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'TextSimilarityGrader']

class TextSimilarityGrader(BaseModel):
    type: Literal['text_similarity'] = 'A TextSimilarityGrader object which grades text based on similarity metrics.'
