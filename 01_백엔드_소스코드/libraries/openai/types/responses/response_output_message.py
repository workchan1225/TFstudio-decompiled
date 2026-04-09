# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_output_message.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from response_output_text import ResponseOutputText
from response_output_refusal import ResponseOutputRefusal
__all__ = [
    'ResponseOutputMessage',
    'Content']
Content: TypeAlias = Annotated[(Union[(ResponseOutputText, ResponseOutputRefusal)], PropertyInfo(discriminator = 'type'))]

class ResponseOutputMessage(BaseModel):
    type: Literal['message'] = 'An output message from the model.'
