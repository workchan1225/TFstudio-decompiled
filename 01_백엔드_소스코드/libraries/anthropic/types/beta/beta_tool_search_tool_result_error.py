# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_tool_search_tool_result_error.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaToolSearchToolResultError']

class BetaToolSearchToolResultError(BaseModel):
    error_code: Literal[('invalid_tool_input', 'unavailable', 'too_many_requests', 'execution_time_exceeded')] = 'BetaToolSearchToolResultError'
    type: Literal['tool_search_tool_result_error'] = None
