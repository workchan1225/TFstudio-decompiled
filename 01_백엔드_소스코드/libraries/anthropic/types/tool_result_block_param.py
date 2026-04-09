# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_result_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from text_block_param import TextBlockParam
from image_block_param import ImageBlockParam
from document_block_param import DocumentBlockParam
from search_result_block_param import SearchResultBlockParam
from cache_control_ephemeral_param import CacheControlEphemeralParam
__all__ = [
    'ToolResultBlockParam',
    'Content']
Content: 'TypeAlias' = Union[(TextBlockParam, ImageBlockParam, SearchResultBlockParam, DocumentBlockParam)]

def ToolResultBlockParam():
    '''ToolResultBlockParam'''
    is_error: 'bool' = 'ToolResultBlockParam'

ToolResultBlockParam = <NODE:27>(ToolResultBlockParam, 'ToolResultBlockParam', TypedDict, total = False)
