# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: XVThumbImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from  import Image, ImageFile, ImagePalette
from _binary import o8
_MAGIC = b'P7 332'
PALETTE = b''
for r in range(8):
    for g in range(8):
        for b in range(4):
            PALETTE = PALETTE + o8(r * 255 // 7) + o8(g * 255 // 7) + o8(b * 255 // 3)
            
            def _accept(prefix = None):
                return prefix.startswith(_MAGIC)

            
            class XVThumbImageFile(ImageFile.ImageFile):
                format = 'XVThumb'
                format_description = 'XV thumbnail image'
                
                def _open(self = None):
                    pass
                # WARNING: Decompyle incomplete


            Image.register_open(XVThumbImageFile.format, XVThumbImageFile, _accept)
            return None
