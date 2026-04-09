# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: MspImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import io
import struct
from typing import IO
from  import Image, ImageFile
from _binary import i16le as i16
from _binary import o16le as o16

def _accept(prefix = None):
    return prefix.startswith((b'DanM', b'LinS'))


class MspImageFile(ImageFile.ImageFile):
    format = 'MSP'
    format_description = 'Windows Paint'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete



class MspDecoder(ImageFile.PyDecoder):
    _pulls_fd = True
    
    def decode(self = None, buffer = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_decoder('MSP', MspDecoder)

def _save(im = None, fp = None, filename = None):
    if im.mode != '1':
        msg = f'''cannot write mode {im.mode} as MSP'''
        raise OSError(msg)
    header = [
        0] * 16
    header[0], header[1] = i16(b'Da'), i16(b'nM')
    (header[2], header[3]) = im.size
    (header[4], header[5]) = (1, 1)
    (header[6], header[7]) = (1, 1)
    (header[8], header[9]) = im.size
    checksum = 0
    for h in header:
        checksum = checksum ^ h
        header[12] = checksum
        for h in header:
            fp.write(o16(h))
            ImageFile._save(im, fp, [
                ImageFile._Tile('raw', (0, 0) + im.size, 32, '1')])
            return None

Image.register_open(MspImageFile.format, MspImageFile, _accept)
Image.register_save(MspImageFile.format, _save)
Image.register_extension(MspImageFile.format, '.msp')
