# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: GimpPaletteFile.pyc (Python 3.11)

from __future__ import annotations
import re
from io import BytesIO
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import IO

class GimpPaletteFile:
    """File handler for GIMP's palette format."""
    rawmode = 'RGB'
    
    def _read(self = None, fp = None, limit = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __init__(self = None, fp = None):
        self._read(fp)

    frombytes = (lambda cls = None, data = None: self = cls.__new__(cls)self._read(BytesIO(data), False)self)()
    
    def getpalette(self = None):
        return (self.palette, self.rawmode)
