# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: helper_types.pyc (Python 3.11)

from __future__ import annotations
import google.api_core.timeout as google
import google.api_core.retry as google
import collections
import dataclasses
from typing import Union
from typing_extensions import TypedDict
__all__ = [
    'RequestOptions',
    'RequestOptionsType']

def RequestOptionsDict():
    '''RequestOptionsDict'''
    timeout: 'Union[int, float, google.api_core.timeout.TimeToDeadlineTimeout]' = 'RequestOptionsDict'

RequestOptionsDict = <NODE:27>(RequestOptionsDict, 'RequestOptionsDict', TypedDict, total = False)
RequestOptions = <NODE:12>()
RequestOptionsType = Union[(RequestOptions, RequestOptionsDict)]
