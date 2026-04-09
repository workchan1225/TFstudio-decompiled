# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: auto_file_chunking_strategy_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
__all__ = [
    'AutoFileChunkingStrategyParam']

def AutoFileChunkingStrategyParam():
    '''AutoFileChunkingStrategyParam'''
    type: "Required[Literal['auto']]" = 'The default strategy.\n\n    This strategy currently uses a `max_chunk_size_tokens` of `800` and `chunk_overlap_tokens` of `400`.\n    '

AutoFileChunkingStrategyParam = <NODE:27>(AutoFileChunkingStrategyParam, 'AutoFileChunkingStrategyParam', TypedDict, total = False)
