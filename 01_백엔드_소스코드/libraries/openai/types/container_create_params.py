# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: container_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
__all__ = [
    'ContainerCreateParams',
    'ExpiresAfter']

def ContainerCreateParams():
    '''ContainerCreateParams'''
    memory_limit: "Literal['1g', '4g', '16g', '64g']" = 'ContainerCreateParams'

ContainerCreateParams = <NODE:27>(ContainerCreateParams, 'ContainerCreateParams', TypedDict, total = False)

def ExpiresAfter():
    '''ExpiresAfter'''
    minutes: 'Required[int]' = "Container expiration time in seconds relative to the 'anchor' time."

ExpiresAfter = <NODE:27>(ExpiresAfter, 'ExpiresAfter', TypedDict, total = False)
