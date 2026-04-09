# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_bash_code_execution_result_block.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
from beta_bash_code_execution_output_block import BetaBashCodeExecutionOutputBlock
__all__ = [
    'BetaBashCodeExecutionResultBlock']

class BetaBashCodeExecutionResultBlock(BaseModel):
    type: Literal['bash_code_execution_result'] = 'BetaBashCodeExecutionResultBlock'
