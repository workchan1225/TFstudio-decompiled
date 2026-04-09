# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: MpegImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from  import Image, ImageFile
from _binary import i8
from _typing import SupportsRead

class BitStream:
    
    def __init__(self = None, fp = None):
        self.fp = fp
        self.bits = 0
        self.bitbuffer = 0

    
    def next(self = None):
        return i8(self.fp.read(1))

    
    def peek(self = None, bits = None):
        pass
    # WARNING: Decompyle incomplete

    
    def skip(self = None, bits = None):
        pass
    # WARNING: Decompyle incomplete

    
    def read(self = None, bits = None):
        v = self.peek(bits)
        self.bits = self.bits - bits
        return v



def _accept(prefix = None):
    return prefix.startswith(b'\x00\x00\x01\xb3')


class MpegImageFile(ImageFile.ImageFile):
    format = 'MPEG'
    format_description = 'MPEG'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(MpegImageFile.format, MpegImageFile, _accept)
Image.register_extensions(MpegImageFile.format, [
    '.mpg',
    '.mpeg'])
Image.register_mime(MpegImageFile.format, 'video/mpeg')
