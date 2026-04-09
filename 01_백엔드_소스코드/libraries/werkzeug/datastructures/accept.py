# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: accept.pyc (Python 3.11)

from __future__ import annotations
import codecs
from collections.abc import abc as cabc
import re
import typing as t
from structures import ImmutableList

def Accept():
    '''Accept'''
    pass
# WARNING: Decompyle incomplete

Accept = <NODE:27>(Accept, 'Accept', ImmutableList[tuple[(str, float)]])
_mime_split_re = re.compile('/|(?:\\s*;\\s*)')

def _normalize_mime(value = None):
    return _mime_split_re.split(value.lower())


class MIMEAccept(Accept):
    '''Like :class:`Accept` but with special methods and behavior for
    mimetypes.
    '''
    
    def _specificity(self = None, value = None):
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(_mime_split_re.split(value)())

    
    def _value_matches(self = None, value = None, item = None):
