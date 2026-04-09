# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: XpmImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import re
from  import Image, ImageFile, ImagePalette
from _binary import o8
xpm_head = re.compile(b'"([0-9]*) ([0-9]*) ([0-9]*) ([0-9]*)')

def _accept(prefix = None):
    return prefix.startswith(b'/* XPM */')


class XpmImageFile(ImageFile.ImageFile):
    format = 'XPM'
    format_description = 'X11 Pixel Map'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def load_read(self = None, read_bytes = None):
        pass
    # WARNING: Decompyle incomplete



class XpmDecoder(ImageFile.PyDecoder):
    _pulls_fd = True
    
    def decode(self = None, buffer = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(XpmImageFile.format, XpmImageFile, _accept)
Image.register_decoder('xpm', XpmDecoder)
Image.register_extension(XpmImageFile.format, '.xpm')
Image.register_mime(XpmImageFile.format, 'image/xpm')
