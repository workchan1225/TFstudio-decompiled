# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_search_tool_result_block.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
from web_search_tool_result_block_content import WebSearchToolResultBlockContent
__all__ = [
    'WebSearchToolResultBlock']

class WebSearchToolResultBlock(BaseModel):
    type: Literal['web_search_tool_result'] = 'WebSearchToolResultBlock'
