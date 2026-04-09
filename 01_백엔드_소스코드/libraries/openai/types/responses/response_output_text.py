# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_text.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ResponseOutputText',
    'Annotation',
    'AnnotationFileCitation',
    'AnnotationURLCitation',
    'AnnotationContainerFileCitation',
    'AnnotationFilePath',
    'Logprob',
    'LogprobTopLogprob']

class AnnotationFileCitation(BaseModel):
    type: Literal['file_citation'] = 'A citation to a file.'


class AnnotationURLCitation(BaseModel):
    url: str = 'A citation for a web resource used to generate a model response.'


class AnnotationContainerFileCitation(BaseModel):
    type: Literal['container_file_citation'] = 'A citation for a container file used to generate a model response.'


class AnnotationFilePath(BaseModel):
    type: Literal['file_path'] = 'A path to a file.'

Annotation: TypeAlias = Annotated[(Union[(AnnotationFileCitation, AnnotationURLCitation, AnnotationContainerFileCitation, AnnotationFilePath)], PropertyInfo(discriminator = 'type'))]

class LogprobTopLogprob(BaseModel):
    logprob: float = 'The top log probability of a token.'


class Logprob(BaseModel):
    top_logprobs: List[LogprobTopLogprob] = 'The log probability of a token.'


class ResponseOutputText(BaseModel):
    type: Literal['output_text'] = 'A text output from the model.'
    logprobs: Optional[List[Logprob]] = None
