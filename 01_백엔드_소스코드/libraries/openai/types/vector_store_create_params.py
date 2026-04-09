# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_store_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
from shared_params.metadata import Metadata
from file_chunking_strategy_param import FileChunkingStrategyParam
__all__ = [
    'VectorStoreCreateParams',
    'ExpiresAfter']

def VectorStoreCreateParams():
    '''VectorStoreCreateParams'''
    name: 'str' = 'VectorStoreCreateParams'

VectorStoreCreateParams = <NODE:27>(VectorStoreCreateParams, 'VectorStoreCreateParams', TypedDict, total = False)

def ExpiresAfter():
    '''ExpiresAfter'''
    days: 'Required[int]' = 'The expiration policy for a vector store.'

ExpiresAfter = <NODE:27>(ExpiresAfter, 'ExpiresAfter', TypedDict, total = False)
