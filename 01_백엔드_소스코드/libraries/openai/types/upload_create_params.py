# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: upload_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from file_purpose import FilePurpose
__all__ = [
    'UploadCreateParams',
    'ExpiresAfter']

def UploadCreateParams():
    '''UploadCreateParams'''
    expires_after: 'ExpiresAfter' = 'UploadCreateParams'

UploadCreateParams = <NODE:27>(UploadCreateParams, 'UploadCreateParams', TypedDict, total = False)

def ExpiresAfter():
    '''ExpiresAfter'''
    seconds: 'Required[int]' = 'The expiration policy for a file.\n\n    By default, files with `purpose=batch` expire after 30 days and all other files are persisted until they are manually deleted.\n    '

ExpiresAfter = <NODE:27>(ExpiresAfter, 'ExpiresAfter', TypedDict, total = False)
