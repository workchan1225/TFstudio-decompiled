# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_code_execution_tool_result_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_code_execution_tool_result_error_code import BetaCodeExecutionToolResultErrorCode
__all__ = [
    'BetaCodeExecutionToolResultError']

class BetaCodeExecutionToolResultError(BaseModel):
    type: Literal['code_execution_tool_result_error'] = 'BetaCodeExecutionToolResultError'
