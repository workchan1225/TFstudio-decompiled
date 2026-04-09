# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: token.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Callable, MutableMapping
import dataclasses as dc
from typing import Any, Literal
import warnings

def convert_attrs(value = None):
    '''Convert Token.attrs set as ``None`` or ``[[key, value], ...]`` to a dict.

    This improves compatibility with upstream markdown-it.
    '''
    if not value:
        return { }
    if None(value, list):
        return dict(value)

Token = <NODE:12>()
