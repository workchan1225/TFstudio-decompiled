# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from _types import FileTypes
from file_purpose import FilePurpose
__all__ = [
    'FileCreateParams',
    'ExpiresAfter']

def FileCreateParams():
    '''FileCreateParams'''
    expires_after: 'ExpiresAfter' = 'FileCreateParams'

FileCreateParams = <NODE:27>(FileCreateParams, 'FileCreateParams', TypedDict, total = False)

def ExpiresAfter():
    '''ExpiresAfter'''
    seconds: 'Required[int]' = 'The expiration policy for a file.\n\n    By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.\n    '

ExpiresAfter = <NODE:27>(ExpiresAfter, 'ExpiresAfter', TypedDict, total = False)
