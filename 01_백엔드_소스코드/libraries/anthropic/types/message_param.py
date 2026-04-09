# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Literal, Required, TypedDict
from content_block import ContentBlock
from text_block_param import TextBlockParam
from image_block_param import ImageBlockParam
from document_block_param import DocumentBlockParam
from thinking_block_param import ThinkingBlockParam
from tool_use_block_param import ToolUseBlockParam
from tool_result_block_param import ToolResultBlockParam
from search_result_block_param import SearchResultBlockParam
from server_tool_use_block_param import ServerToolUseBlockParam
from redacted_thinking_block_param import RedactedThinkingBlockParam
from web_search_tool_result_block_param import WebSearchToolResultBlockParam
__all__ = [
    'MessageParam']

def MessageParam():
    '''MessageParam'''
    role: "Required[Literal['user', 'assistant']]" = 'MessageParam'

MessageParam = <NODE:27>(MessageParam, 'MessageParam', TypedDict, total = False)
