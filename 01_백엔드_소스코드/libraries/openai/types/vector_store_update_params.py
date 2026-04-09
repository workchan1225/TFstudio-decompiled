# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: vector_store_update_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal, Required, TypedDict
from shared_params.metadata import Metadata
__all__ = [
    'VectorStoreUpdateParams',
    'ExpiresAfter']

def VectorStoreUpdateParams():
    '''VectorStoreUpdateParams'''
    name: 'Optional[str]' = 'VectorStoreUpdateParams'

VectorStoreUpdateParams = <NODE:27>(VectorStoreUpdateParams, 'VectorStoreUpdateParams', TypedDict, total = False)

def ExpiresAfter():
    '''ExpiresAfter'''
    days: 'Required[int]' = 'The expiration policy for a vector store.'

ExpiresAfter = <NODE:27>(ExpiresAfter, 'ExpiresAfter', TypedDict, total = False)
