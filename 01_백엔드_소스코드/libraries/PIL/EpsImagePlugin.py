# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: EpsImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import io
import os
import re
import subprocess
import sys
import tempfile
from typing import IO
from  import Image, ImageFile
from _binary import i32le as i32
split = re.compile('^%%([^:]*):[ \\t]*(.*)[ \\t]*$')
field = re.compile('^%[%!\\w]([^:]*)[ \\t]*$')
gs_binary: 'str | bool | None' = None
gs_windows_binary = None

def has_ghostscript():
    pass
# WARNING: Decompyle incomplete


def Ghostscript(tile = None, size = None, fp = None, scale = (1, False), transparency = ('tile', 'list[ImageFile._Tile]', 'size', 'tuple[int, int]', 'fp', 'IO[bytes]', 'scale', 'int', 'transparency', 'bool', 'return', 'Image.core.ImagingCore')):
    '''Render an image using Ghostscript'''
    if not has_ghostscript():
        msg = 'Unable to locate Ghostscript on paths'
        raise OSError(msg)
# WARNING: Decompyle incomplete


def _accept(prefix = None):
