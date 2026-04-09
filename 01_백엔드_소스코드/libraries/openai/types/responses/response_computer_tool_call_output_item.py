# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_computer_tool_call_output_item.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
from response_computer_tool_call_output_screenshot import ResponseComputerToolCallOutputScreenshot
__all__ = [
    'ResponseComputerToolCallOutputItem',
    'AcknowledgedSafetyCheck']

class AcknowledgedSafetyCheck(BaseModel):
    id: str = 'A pending safety check for the computer call.'
    code: Optional[str] = None
    message: Optional[str] = None


class ResponseComputerToolCallOutputItem(BaseModel):
    type: Literal['computer_call_output'] = 'ResponseComputerToolCallOutputItem'
    acknowledged_safety_checks: Optional[List[AcknowledgedSafetyCheck]] = None
    status: Optional[Literal[('in_progress', 'completed', 'incomplete')]] = None
