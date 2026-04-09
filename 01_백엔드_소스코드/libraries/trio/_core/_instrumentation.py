# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _instrumentation.pyc (Python 3.11)

from __future__ import annotations
import logging
import types
from collections import UserDict
from typing import TYPE_CHECKING, TypeVar
from _abc import Instrument
INSTRUMENT_LOGGER = logging.getLogger('trio.abc.Instrument')
if TYPE_CHECKING:
    from collections.abc import Sequence
    T = TypeVar('T')

def _public(fn = None):
    return fn


def Instruments():
    '''Instruments'''
    pass
# WARNING: Decompyle incomplete

Instruments = <NODE:27>(Instruments, 'Instruments', UserDict[(str, dict[(Instrument, None)])])
