# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Iterable
from typing_extensions import Required, TypedDict
from message_create_params import MessageCreateParamsNonStreaming
__all__ = [
    'BatchCreateParams',
    'Request']

def BatchCreateParams():
    '''BatchCreateParams'''
    requests: 'Required[Iterable[Request]]' = 'BatchCreateParams'

BatchCreateParams = <NODE:27>(BatchCreateParams, 'BatchCreateParams', TypedDict, total = False)

def Request():
    '''Request'''
    params: 'Required[MessageCreateParamsNonStreaming]' = 'Request'

Request = <NODE:27>(Request, 'Request', TypedDict, total = False)
