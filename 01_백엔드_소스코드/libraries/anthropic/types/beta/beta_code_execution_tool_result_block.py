# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_code_execution_tool_result_block.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_code_execution_tool_result_block_content import BetaCodeExecutionToolResultBlockContent
__all__ = [
    'BetaCodeExecutionToolResultBlock']

class BetaCodeExecutionToolResultBlock(BaseModel):
    type: Literal['code_execution_tool_result'] = 'BetaCodeExecutionToolResultBlock'
