# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_mcp_tool_result_block.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Literal
from _models import BaseModel
from beta_text_block import BetaTextBlock
__all__ = [
    'BetaMCPToolResultBlock']

class BetaMCPToolResultBlock(BaseModel):
    type: Literal['mcp_tool_result'] = 'BetaMCPToolResultBlock'
