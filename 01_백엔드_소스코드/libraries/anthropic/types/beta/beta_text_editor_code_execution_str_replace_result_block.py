# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_text_editor_code_execution_str_replace_result_block.pyc (Python 3.11)

from typing import List, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaTextEditorCodeExecutionStrReplaceResultBlock']

class BetaTextEditorCodeExecutionStrReplaceResultBlock(BaseModel):
    lines: Optional[List[str]] = None
    new_lines: Optional[int] = None
    new_start: Optional[int] = None
    old_lines: Optional[int] = None
    type: Literal['text_editor_code_execution_str_replace_result'] = None
