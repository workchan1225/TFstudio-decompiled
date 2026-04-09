# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: MicImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import olefile
from  import Image, TiffImagePlugin

def _accept(prefix = None):
    return prefix.startswith(olefile.MAGIC)


class MicImageFile(TiffImagePlugin.TiffImageFile):
    pass
# WARNING: Decompyle incomplete

Image.register_open(MicImageFile.format, MicImageFile, _accept)
Image.register_extension(MicImageFile.format, '.mic')
