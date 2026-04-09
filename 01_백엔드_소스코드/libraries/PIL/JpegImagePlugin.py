# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: JpegImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import array
import io
import math
import os
import struct
import subprocess
import sys
import tempfile
import warnings
from  import Image, ImageFile
from _binary import i16be as i16
from _binary import i32be as i32
from _binary import o8
from _binary import o16be as o16
from JpegPresets import presets
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import IO, Any
    from MpoImagePlugin import MpoImageFile

def Skip(self = None, marker = None):
    n = i16(self.fp.read(2)) - 2
    ImageFile._safe_read(self.fp, n)


def APP(self = None, marker = None):
    n = i16(self.fp.read(2)) - 2
    s = ImageFile._safe_read(self.fp, n)
    app = f'''APP{marker & 15}'''
    self.app[app] = s
    self.applist.append((app, s))
# WARNING: Decompyle incomplete


def COM(self = None, marker = None):
    n = i16(self.fp.read(2)) - 2
    s = ImageFile._safe_read(self.fp, n)
    self.info['comment'] = s
    self.app['COM'] = s
    self.applist.append(('COM', s))


def SOF(self = None, marker = None):
    n = i16(self.fp.read(2)) - 2
    s = ImageFile._safe_read(self.fp, n)
    self._size = (i16(s, 3), i16(s, 1))
# WARNING: Decompyle incomplete


def DQT(self = None, marker = None):
    pass
# WARNING: Decompyle incomplete

# WARNING: Decompyle incomplete
