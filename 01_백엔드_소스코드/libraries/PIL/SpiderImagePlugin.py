# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: SpiderImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import os
import struct
import sys
from typing import IO, Any, cast
from  import Image, ImageFile
from _util import DeferredError
TYPE_CHECKING = False

def isInt(f = None):
    
    try:
        i = int(f)
        if f - i == 0:
            return 1
        return None
    except (ValueError, OverflowError):
        return 0


iforms = [
    1,
    3,
    -11,
    -12,
    -21,
    -22]

def isSpiderHeader(t = None):
    h = (99,) + t
    for i in (1, 2, 5, 12, 13, 22, 23):
        if not isInt(h[i]):
            return 0
        iform = int(h[5])
        if iform not in iforms:
            return 0
        labrec = None(h[13])
        labbyt = int(h[22])
        lenbyt = int(h[23])
        if labbyt != labrec * lenbyt:
            return 0
        return None


def isSpiderImage(filename = None):
    fp = open(filename, 'rb')
    f = fp.read(92)
    None(None, None)


class SpiderImageFile(ImageFile.ImageFile):
    format = 'SPIDER'
    format_description = 'Spider 2D image'
    _close_exclusive_fp_after_loading = False
    
    def _open(self = None):
        n = 108
        f = self.fp.read(n)
        
        try:
            self.bigendian = 1
            t = struct.unpack('>27f', f)
            hdrlen = isSpiderHeader(t)
            if hdrlen == 0:
                self.bigendian = 0
                t = struct.unpack('<27f', f)
                hdrlen = isSpiderHeader(t)
            if hdrlen == 0:
                msg = 'not a valid Spider file'
                raise SyntaxError(msg)
        except struct.error:
            e = None
            msg = 'not a valid Spider file'
            raise SyntaxError(msg), e
            e = None
            del e

        h = (99,) + t
        iform = int(h[5])
        if iform != 1:
            msg = 'not a Spider 2D image'
            raise SyntaxError(msg)
        self._size = (int(h[12]), int(h[2]))
        self.istack = int(h[24])
        self.imgnumber = int(h[27])
        if self.istack == 0 and self.imgnumber == 0:
            offset = hdrlen
            self._nimages = 1
        elif self.istack > 0 and self.imgnumber == 0:
            self.imgbytes = int(h[12]) * int(h[2]) * 4
            self.hdrlen = hdrlen
            self._nimages = int(h[26])
            offset = hdrlen * 2
            self.imgnumber = 1
        elif self.istack == 0 and self.imgnumber > 0:
            offset = hdrlen + self.stkoffset
            self.istack = 2
        else:
            msg = 'inconsistent stack header values'
            raise SyntaxError(msg)
        if self.bigendian:
            self.rawmode = 'F;32BF'
        else:
            self.rawmode = 'F;32F'
        self._mode = 'F'
        self.tile = [
            ImageFile._Tile('raw', (0, 0) + self.size, offset, self.rawmode)]
        self._fp = self.fp

    n_frames = (lambda self = None: self._nimages)()
    is_animated = (lambda self = None: self._nimages > 1)()
    
    def tell(self = None):
        if self.imgnumber < 1:
            return 0
        return None.imgnumber - 1

    
    def seek(self = None, frame = None):
        if self.istack == 0:
            msg = 'attempt to seek in a non-stack file'
            raise EOFError(msg)
        if not self._seek_check(frame):
            return None
        if None(self._fp, DeferredError):
            raise self._fp.ex
        self.stkoffset = self.hdrlen + frame * (self.hdrlen + self.imgbytes)
        self.fp = self._fp
        self.fp.seek(self.stkoffset)
        self._open()

    
    def convert2byte(self = None, depth = None):
        pass
    # WARNING: Decompyle incomplete

    if TYPE_CHECKING:
        from  import ImageTk
    
    def tkPhotoImage(self = None):
        ImageTk = ImageTk
        import 
        return ImageTk.PhotoImage(self.convert2byte(), palette = 256)



def loadImageSeries(filelist = None):
    '''create a list of :py:class:`~PIL.Image.Image` objects for use in a montage'''
    pass
# WARNING: Decompyle incomplete


def makeSpiderHeader(im = None):
    (nsam, nrow) = im.size
    lenbyt = nsam * 4
    labrec = int(1024 / lenbyt)
    if 1024 % lenbyt != 0:
        labrec += 1
    labbyt = labrec * lenbyt
    nvalues = int(labbyt / 4)
    if nvalues < 23:
        return []
    hdr = [
        None] * nvalues
    hdr[1] = 1
    hdr[2] = float(nrow)
    hdr[3] = float(nrow)
    hdr[5] = 1
    hdr[12] = float(nsam)
    hdr[13] = float(labrec)
    hdr[22] = float(labbyt)
    hdr[23] = float(lenbyt)
    hdr = hdr[1:]
    hdr.append(0)
    return hdr()


def _save(im = None, fp = None, filename = None):
    if im.mode != 'F':
        im = im.convert('F')
    hdr = makeSpiderHeader(im)
    if len(hdr) < 256:
        msg = 'Error creating Spider header'
        raise OSError(msg)
    fp.writelines(hdr)
    rawmode = 'F;32NF'
    ImageFile._save(im, fp, [
        ImageFile._Tile('raw', (0, 0) + im.size, 0, rawmode)])


def _save_spider(im = None, fp = None, filename = None):
    filename_ext = os.path.splitext(filename)[1]
    ext = filename_ext.decode() if isinstance(filename_ext, bytes) else filename_ext
    Image.register_extension(SpiderImageFile.format, ext)
    _save(im, fp, filename)

Image.register_open(SpiderImageFile.format, SpiderImageFile)
Image.register_save(SpiderImageFile.format, _save_spider)
if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Syntax: python3 SpiderImagePlugin.py [infile] [outfile]')
        sys.exit()
    filename = sys.argv[1]
    if not isSpiderImage(filename):
        print('input image must be in Spider format')
        sys.exit()
    im = Image.open(filename)
    print(f'''image: {im}''')
    print(f'''format: {im.format}''')
    print(f'''size: {im.size}''')
    print(f'''mode: {im.mode}''')
    print('max, min: ', end = ' ')
    print(im.getextrema())
    if len(sys.argv) > 2:
        outfile = sys.argv[2]
        im = im.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
        print(f'''saving a flipped version of {os.path.basename(filename)} as {outfile} ''')
        im.save(outfile, SpiderImageFile.format)
    None(None, None)
    return None
with None:
    if not None:
        pass
return None
