# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_text_editor_code_execution_tool_result_error.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaTextEditorCodeExecutionToolResultError']

class BetaTextEditorCodeExecutionToolResultError(BaseModel):
    error_code: Literal[('invalid_tool_input', 'unavailable', 'too_many_requests', 'execution_time_exceeded', 'file_not_found')] = 'BetaTextEditorCodeExecutionToolResultError'
    type: Literal['text_editor_code_execution_tool_result_error'] = None
