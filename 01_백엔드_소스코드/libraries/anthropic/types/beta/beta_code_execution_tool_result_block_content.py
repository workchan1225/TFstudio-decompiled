# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_code_execution_tool_result_block_content.pyc (Python 3.11)

from typing import Union
from typing_extensions import TypeAlias
from beta_code_execution_result_block import BetaCodeExecutionResultBlock
from beta_code_execution_tool_result_error import BetaCodeExecutionToolResultError
__all__ = [
    'BetaCodeExecutionToolResultBlockContent']
BetaCodeExecutionToolResultBlockContent: TypeAlias = Union[(BetaCodeExecutionToolResultError, BetaCodeExecutionResultBlock)]
