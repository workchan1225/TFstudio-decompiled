# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_tool_result_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from beta_text_block_param import BetaTextBlockParam
from beta_image_block_param import BetaImageBlockParam
from beta_search_result_block_param import BetaSearchResultBlockParam
from beta_tool_reference_block_param import BetaToolReferenceBlockParam
from beta_request_document_block_param import BetaRequestDocumentBlockParam
from beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
__all__ = [
    'BetaToolResultBlockParam',
    'Content']
Content: 'TypeAlias' = Union[(BetaTextBlockParam, BetaImageBlockParam, BetaSearchResultBlockParam, BetaRequestDocumentBlockParam, BetaToolReferenceBlockParam)]

def BetaToolResultBlockParam():
    '''BetaToolResultBlockParam'''
    is_error: 'bool' = 'BetaToolResultBlockParam'

BetaToolResultBlockParam = <NODE:27>(BetaToolResultBlockParam, 'BetaToolResultBlockParam', TypedDict, total = False)
