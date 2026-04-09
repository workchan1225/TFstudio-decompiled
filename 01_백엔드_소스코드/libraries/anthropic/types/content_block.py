# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: content_block.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from text_block import TextBlock
from thinking_block import ThinkingBlock
from tool_use_block import ToolUseBlock
from server_tool_use_block import ServerToolUseBlock
from redacted_thinking_block import RedactedThinkingBlock
from web_search_tool_result_block import WebSearchToolResultBlock
__all__ = [
    'ContentBlock']
ContentBlock: TypeAlias = Annotated[(Union[(TextBlock, ThinkingBlock, RedactedThinkingBlock, ToolUseBlock, ServerToolUseBlock, WebSearchToolResultBlock)], PropertyInfo(discriminator = 'type'))]
