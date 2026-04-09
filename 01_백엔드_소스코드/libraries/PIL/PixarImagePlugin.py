# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PixarImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from  import Image, ImageFile
from _binary import i16le as i16

def _accept(prefix = None):
    return prefix.startswith(b'\x80\xe8\x00\x00')


class PixarImageFile(ImageFile.ImageFile):
    format = 'PIXAR'
    format_description = 'PIXAR raster image'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(PixarImageFile.format, PixarImageFile, _accept)
Image.register_extension(PixarImageFile.format, '.pxr')
