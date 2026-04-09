# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_fetch_tool_result_error_block.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_web_fetch_tool_result_error_code import BetaWebFetchToolResultErrorCode
__all__ = [
    'BetaWebFetchToolResultErrorBlock']

class BetaWebFetchToolResultErrorBlock(BaseModel):
    type: Literal['web_fetch_tool_result_error'] = 'BetaWebFetchToolResultErrorBlock'
