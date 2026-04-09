# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: text_delta.pyc (Python 3.11)

from typing import List, Optional
from _models import BaseModel
from annotation_delta import AnnotationDelta
__all__ = [
    'TextDelta']

class TextDelta(BaseModel):
    annotations: Optional[List[AnnotationDelta]] = None
    value: Optional[str] = None
