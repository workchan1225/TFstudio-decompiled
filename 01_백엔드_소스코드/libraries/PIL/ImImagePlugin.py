# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import os
import re
from typing import IO, Any
from  import Image, ImageFile, ImagePalette
from _util import DeferredError
COMMENT = 'Comment'
DATE = 'Date'
EQUIPMENT = 'Digitalization equipment'
FRAMES = 'File size (no of images)'
LUT = 'Lut'
NAME = 'Name'
SCALE = 'Scale (x,y)'
SIZE = 'Image size (x*y)'
MODE = 'Image type'
TAGS = {
    MODE: 0,
    SIZE: 0,
    SCALE: 0,
    NAME: 0,
    LUT: 0,
    FRAMES: 0,
    EQUIPMENT: 0,
    DATE: 0,
    COMMENT: 0 }
# WARNING: Decompyle incomplete
