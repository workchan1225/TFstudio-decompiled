# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_chunking_strategy_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from auto_file_chunking_strategy_param import AutoFileChunkingStrategyParam
from static_file_chunking_strategy_object_param import StaticFileChunkingStrategyObjectParam
__all__ = [
    'FileChunkingStrategyParam']
FileChunkingStrategyParam: 'TypeAlias' = Union[(AutoFileChunkingStrategyParam, StaticFileChunkingStrategyObjectParam)]
