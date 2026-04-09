# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_calls_step_details.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from tool_call import ToolCall
from _models import BaseModel
__all__ = [
    'ToolCallsStepDetails']

class ToolCallsStepDetails(BaseModel):
    type: Literal['tool_calls'] = 'Details of the tool call.'
