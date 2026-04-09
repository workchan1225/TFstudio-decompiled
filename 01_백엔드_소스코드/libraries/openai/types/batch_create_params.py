# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Optional
from typing_extensions import Literal, Required, TypedDict
from shared_params.metadata import Metadata
__all__ = [
    'BatchCreateParams',
    'OutputExpiresAfter']

def BatchCreateParams():
    '''BatchCreateParams'''
    output_expires_after: 'OutputExpiresAfter' = 'BatchCreateParams'

BatchCreateParams = <NODE:27>(BatchCreateParams, 'BatchCreateParams', TypedDict, total = False)

def OutputExpiresAfter():
    '''OutputExpiresAfter'''
    seconds: 'Required[int]' = '\n    The expiration policy for the output and/or error file that are generated for a batch.\n    '

OutputExpiresAfter = <NODE:27>(OutputExpiresAfter, 'OutputExpiresAfter', TypedDict, total = False)
