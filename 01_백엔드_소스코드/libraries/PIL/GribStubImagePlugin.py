# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: GribStubImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import IO
from  import Image, ImageFile
_handler = None

def register_handler(handler = None):
    '''
    Install application-specific GRIB image handler.

    :param handler: Handler object.
    '''
    global _handler
    _handler = handler


def _accept(prefix = None):
