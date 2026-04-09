# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PpmImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import math
from typing import IO
from  import Image, ImageFile
from _binary import i16be as i16
from _binary import o8
from _binary import o32le as o32
b_whitespace = b' \t\n\x0b\x0c\r'
MODES = {
    b'P1': '1',
    b'P2': 'L',
    b'P3': 'RGB',
    b'P4': '1',
    b'P5': 'L',
    b'P6': 'RGB',
    b'P0CMYK': 'CMYK',
    b'Pf': 'F',
    b'PyP': 'P',
    b'PyRGBA': 'RGBA',
    b'PyCMYK': 'CMYK' }

def _accept(prefix = None):
