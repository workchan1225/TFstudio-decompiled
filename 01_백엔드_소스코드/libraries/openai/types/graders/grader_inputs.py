# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grader_inputs.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from responses.response_input_text import ResponseInputText
from responses.response_input_audio import ResponseInputAudio
__all__ = [
    'GraderInputs',
    'GraderInputItem',
    'GraderInputItemOutputText',
    'GraderInputItemInputImage']

class GraderInputItemOutputText(BaseModel):
    type: Literal['output_text'] = 'A text output from the model.'


class GraderInputItemInputImage(BaseModel):
    type: Literal['input_image'] = 'An image input block used within EvalItem content arrays.'
    detail: Optional[str] = None

GraderInputItem: TypeAlias = Union[(str, ResponseInputText, GraderInputItemOutputText, GraderInputItemInputImage, ResponseInputAudio)]
GraderInputs: TypeAlias = List[GraderInputItem]
