# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: IptcImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from io import BytesIO
from typing import cast
from  import Image, ImageFile
from _binary import i16be as i16
from _binary import i32be as i32
COMPRESSION = {
    1: 'raw',
    5: 'jpeg' }

def _i(c = None):
    return i32(b'\x00\x00\x00\x00' + c[-4:])


class IptcImageFile(ImageFile.ImageFile):
    format = 'IPTC'
    format_description = 'IPTC/NAA'
    
    def getint(self = None, key = None):
        return _i(self.info[key])

    
    def field(self = None):
        s = self.fp.read(5)
        if not s.strip(b'\x00'):
            return (None, 0)
        tag = (None[1], s[2])
        if s[0] != 28 or tag[0] not in (1, 2, 3, 4, 5, 6, 7, 8, 9, 240):
            msg = 'invalid IPTC/NAA file'
            raise SyntaxError(msg)
        size = s[3]
        if size > 132:
            msg = 'illegal field length in IPTC/NAA file'
            raise OSError(msg)
        if size == 128:
            size = 0
        elif size > 128:
            size = _i(self.fp.read(size - 128))
        else:
            size = i16(s, 3)
        return (tag, size)

    
    def _open(self = None):
        offset = self.fp.tell()
        (tag, size) = self.field()
        if tag or tag == (8, 10):
            pass
        elif size:
            tagdata = self.fp.read(size)
        else:
            tagdata = None
        if tag in self.info:
            if isinstance(self.info[tag], list):
                self.info[tag].append(tagdata)
            else:
                self.info[tag] = [
                    self.info[tag],
                    tagdata]
        else:
            self.info[tag] = tagdata
        continue
        layers = self.info[(3, 60)][0]
        component = self.info[(3, 60)][1]
        if not layers == 1 and component:
            self._mode = 'L'
            band = None
        elif layers == 3 and component:
            self._mode = 'RGB'
        elif layers == 4 and component:
            self._mode = 'CMYK'
        if (3, 65) in self.info:
            band = self.info[(3, 65)][0] - 1
        else:
            band = 0
        self._size = (self.getint((3, 20)), self.getint((3, 30)))
        
        try:
            compression = COMPRESSION[self.getint((3, 120))]
        except KeyError:
            e = None
            msg = 'Unknown IPTC image compression'
            raise OSError(msg), e
            e = None
            del e

        if tag == (8, 10):
            self.tile = [
                ImageFile._Tile('iptc', (0, 0) + self.size, offset, (compression, band))]
            return None

    
    def load(self = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(IptcImageFile.format, IptcImageFile)
Image.register_extension(IptcImageFile.format, '.iim')

def getiptcinfo(im = None):
    '''
    Get IPTC information from TIFF, JPEG, or IPTC file.

    :param im: An image containing IPTC data.
    :returns: A dictionary containing IPTC information, or None if
        no IPTC information block was found.
    '''
    JpegImagePlugin = JpegImagePlugin
    TiffImagePlugin = TiffImagePlugin
    import 
    data = None
    info = { }
# WARNING: Decompyle incomplete
