# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_code_execution_result_block.pyc (Python 3.11)

from typing import List
from typing_extensions import Literal
from _models import BaseModel
from beta_code_execution_output_block import BetaCodeExecutionOutputBlock
__all__ = [
    'BetaCodeExecutionResultBlock']

class BetaCodeExecutionResultBlock(BaseModel):
    type: Literal['code_execution_result'] = 'BetaCodeExecutionResultBlock'
