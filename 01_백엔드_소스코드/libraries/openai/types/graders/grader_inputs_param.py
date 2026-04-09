# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grader_inputs_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from responses.response_input_text_param import ResponseInputTextParam
from responses.response_input_audio_param import ResponseInputAudioParam
__all__ = [
    'GraderInputsParam',
    'GraderInputsParamItem',
    'GraderInputsParamItemOutputText',
    'GraderInputsParamItemInputImage']

def GraderInputsParamItemOutputText():
    '''GraderInputsParamItemOutputText'''
    type: "Required[Literal['output_text']]" = 'A text output from the model.'

GraderInputsParamItemOutputText = <NODE:27>(GraderInputsParamItemOutputText, 'GraderInputsParamItemOutputText', TypedDict, total = False)

def GraderInputsParamItemInputImage():
    '''GraderInputsParamItemInputImage'''
    detail: 'str' = 'An image input block used within EvalItem content arrays.'

GraderInputsParamItemInputImage = <NODE:27>(GraderInputsParamItemInputImage, 'GraderInputsParamItemInputImage', TypedDict, total = False)
GraderInputsParamItem: 'TypeAlias' = Union[(str, ResponseInputTextParam, GraderInputsParamItemOutputText, GraderInputsParamItemInputImage, ResponseInputAudioParam)]
GraderInputsParam: 'TypeAlias' = List[GraderInputsParamItem]
