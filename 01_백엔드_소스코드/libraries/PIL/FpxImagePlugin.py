# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: FpxImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import olefile
from  import Image, ImageFile
from _binary import i32le as i32
MODES = {
    (32766,): ('A', 'L'),
    (65536,): ('L', 'L'),
    (98304, 98302): ('RGBA', 'LA'),
    (131072, 131073, 131074): ('RGB', 'YCC;P'),
    (163840, 163841, 163842, 163838): ('RGBA', 'YCCA;P'),
    (196608, 196609, 196610): ('RGB', 'RGB'),
    (229376, 229377, 229378, 229374): ('RGBA', 'RGBA') }

def _accept(prefix = None):
    return prefix.startswith(olefile.MAGIC)


class FpxImageFile(ImageFile.ImageFile):
    pass
# WARNING: Decompyle incomplete

Image.register_open(FpxImageFile.format, FpxImageFile, _accept)
Image.register_extension(FpxImageFile.format, '.fpx')
