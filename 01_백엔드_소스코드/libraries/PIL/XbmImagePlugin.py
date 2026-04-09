# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: XbmImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import re
from typing import IO
from  import Image, ImageFile
xbm_head = re.compile(b'\\s*#define[ \\t]+.*_width[ \\t]+(?P<width>[0-9]+)[\\r\\n]+#define[ \t]+.*_height[ \t]+(?P<height>[0-9]+)[\r\n]+(?P<hotspot>#define[ \t]+[^_]*_x_hot[ \t]+(?P<xhot>[0-9]+)[\r\n]+#define[ \t]+[^_]*_y_hot[ \t]+(?P<yhot>[0-9]+)[\r\n]+)?[\\000-\\377]*_bits\\[]')

def _accept(prefix = None):
    return prefix.lstrip().startswith(b'#define')


class XbmImageFile(ImageFile.ImageFile):
    format = 'XBM'
    format_description = 'X11 Bitmap'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete



def _save(im = None, fp = None, filename = None):
    if im.mode != '1':
        msg = f'''cannot write mode {im.mode} as XBM'''
        raise OSError(msg)
    fp.write(f'''#define im_width {im.size[0]}\n'''.encode('ascii'))
    fp.write(f'''#define im_height {im.size[1]}\n'''.encode('ascii'))
    hotspot = im.encoderinfo.get('hotspot')
    if hotspot:
        fp.write(f'''#define im_x_hot {hotspot[0]}\n'''.encode('ascii'))
        fp.write(f'''#define im_y_hot {hotspot[1]}\n'''.encode('ascii'))
    fp.write(b'static char im_bits[] = {\n')
    ImageFile._save(im, fp, [
        ImageFile._Tile('xbm', (0, 0) + im.size)])
    fp.write(b'};\n')

Image.register_open(XbmImageFile.format, XbmImageFile, _accept)
Image.register_save(XbmImageFile.format, _save)
Image.register_extension(XbmImageFile.format, '.xbm')
Image.register_mime(XbmImageFile.format, 'image/xbm')
