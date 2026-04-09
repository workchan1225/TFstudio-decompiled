# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_computer_tool_call_output_screenshot.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseComputerToolCallOutputScreenshot']

class ResponseComputerToolCallOutputScreenshot(BaseModel):
    type: Literal['computer_screenshot'] = 'A computer screenshot image used with the computer use tool.'
    file_id: Optional[str] = None
    image_url: Optional[str] = None
