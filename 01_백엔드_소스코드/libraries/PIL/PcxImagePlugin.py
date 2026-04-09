# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PcxImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import io
import logging
from typing import IO
from  import Image, ImageFile, ImagePalette
from _binary import i16le as i16
from _binary import o8
from _binary import o16le as o16
logger = logging.getLogger(__name__)

def _accept(prefix = None):
