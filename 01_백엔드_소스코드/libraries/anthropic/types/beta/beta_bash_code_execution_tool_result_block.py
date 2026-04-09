# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_bash_code_execution_tool_result_block.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
from beta_bash_code_execution_result_block import BetaBashCodeExecutionResultBlock
from beta_bash_code_execution_tool_result_error import BetaBashCodeExecutionToolResultError
__all__ = [
    'BetaBashCodeExecutionToolResultBlock',
    'Content']
Content: TypeAlias = Union[(BetaBashCodeExecutionToolResultError, BetaBashCodeExecutionResultBlock)]

class BetaBashCodeExecutionToolResultBlock(BaseModel):
    type: Literal['bash_code_execution_tool_result'] = 'BetaBashCodeExecutionToolResultBlock'
