# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_batch_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Iterable, Optional
from typing_extensions import Required, TypedDict
from _types import SequenceNotStr
from file_chunking_strategy_param import FileChunkingStrategyParam
__all__ = [
    'FileBatchCreateParams',
    'File']

def FileBatchCreateParams():
    '''FileBatchCreateParams'''
    files: 'Iterable[File]' = 'FileBatchCreateParams'

FileBatchCreateParams = <NODE:27>(FileBatchCreateParams, 'FileBatchCreateParams', TypedDict, total = False)

def File():
    '''File'''
    chunking_strategy: 'FileChunkingStrategyParam' = 'File'

File = <NODE:27>(File, 'File', TypedDict, total = False)
