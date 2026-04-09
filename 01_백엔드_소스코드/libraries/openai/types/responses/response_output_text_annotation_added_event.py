# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_text_annotation_added_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseOutputTextAnnotationAddedEvent']

class ResponseOutputTextAnnotationAddedEvent(BaseModel):
    type: Literal['response.output_text.annotation.added'] = 'Emitted when an annotation is added to output text content.'
