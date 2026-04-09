# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_tool_call_output_item.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from response_input_file import ResponseInputFile
from response_input_text import ResponseInputText
from response_input_image import ResponseInputImage
__all__ = [
    'ResponseFunctionToolCallOutputItem',
    'OutputOutputContentList']
OutputOutputContentList: TypeAlias = Annotated[(Union[(ResponseInputText, ResponseInputImage, ResponseInputFile)], PropertyInfo(discriminator = 'type'))]

class ResponseFunctionToolCallOutputItem(BaseModel):
    type: Literal['function_call_output'] = 'ResponseFunctionToolCallOutputItem'
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None
