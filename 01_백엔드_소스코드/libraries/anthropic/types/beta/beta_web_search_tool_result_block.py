# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_web_search_tool_result_block.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from beta_web_search_tool_result_block_content import BetaWebSearchToolResultBlockContent
__all__ = [
    'BetaWebSearchToolResultBlock']

class BetaWebSearchToolResultBlock(BaseModel):
    type: Literal['web_search_tool_result'] = 'BetaWebSearchToolResultBlock'
