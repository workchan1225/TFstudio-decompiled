# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit_response_output_text.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'ChatKitResponseOutputText',
    'Annotation',
    'AnnotationFile',
    'AnnotationFileSource',
    'AnnotationURL',
    'AnnotationURLSource']

class AnnotationFileSource(BaseModel):
    type: Literal['file'] = 'File attachment referenced by the annotation.'


class AnnotationFile(BaseModel):
    type: Literal['file'] = 'Annotation that references an uploaded file.'


class AnnotationURLSource(BaseModel):
    url: str = 'URL referenced by the annotation.'


class AnnotationURL(BaseModel):
    type: Literal['url'] = 'Annotation that references a URL.'

Annotation: TypeAlias = Annotated[(Union[(AnnotationFile, AnnotationURL)], PropertyInfo(discriminator = 'type'))]

class ChatKitResponseOutputText(BaseModel):
    type: Literal['output_text'] = 'Assistant response text accompanied by optional annotations.'
