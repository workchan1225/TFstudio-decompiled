# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: McIdasImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import struct
from  import Image, ImageFile

def _accept(prefix = None):
    return prefix.startswith(b'\x00\x00\x00\x00\x00\x00\x00\x04')


class McIdasImageFile(ImageFile.ImageFile):
    format = 'MCIDAS'
    format_description = 'McIdas area file'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(McIdasImageFile.format, McIdasImageFile, _accept)
