# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_custom_tool_call_output.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from response_input_file import ResponseInputFile
from response_input_text import ResponseInputText
from response_input_image import ResponseInputImage
__all__ = [
    'ResponseCustomToolCallOutput',
    'OutputOutputContentList']
OutputOutputContentList: TypeAlias = Annotated[(Union[(ResponseInputText, ResponseInputImage, ResponseInputFile)], PropertyInfo(discriminator = 'type'))]

class ResponseCustomToolCallOutput(BaseModel):
    type: Literal['custom_tool_call_output'] = 'The output of a custom tool call from your code, being sent back to the model.'
    id: Optional[str] = None
