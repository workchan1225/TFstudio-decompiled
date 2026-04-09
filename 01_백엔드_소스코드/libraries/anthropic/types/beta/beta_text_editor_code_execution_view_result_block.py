# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_text_editor_code_execution_view_result_block.pyc (Python 3.11)

from typing import Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaTextEditorCodeExecutionViewResultBlock']

class BetaTextEditorCodeExecutionViewResultBlock(BaseModel):
    file_type: Literal[('text', 'image', 'pdf')] = 'BetaTextEditorCodeExecutionViewResultBlock'
    num_lines: Optional[int] = None
    start_line: Optional[int] = None
    type: Literal['text_editor_code_execution_view_result'] = None
