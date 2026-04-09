# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_citation_annotation.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'FileCitationAnnotation',
    'FileCitation']

class FileCitation(BaseModel):
    file_id: str = 'FileCitation'


class FileCitationAnnotation(BaseModel):
    type: Literal['file_citation'] = '\n    A citation within the message that points to a specific quote from a specific File associated with the assistant or the message. Generated when the assistant uses the "file_search" tool to search files.\n    '
