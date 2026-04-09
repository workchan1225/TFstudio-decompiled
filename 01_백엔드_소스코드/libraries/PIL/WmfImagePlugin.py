# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: WmfImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from typing import IO
from  import Image, ImageFile
from _binary import i16le as word
from _binary import si16le as short
from _binary import si32le as _long
_handler = None

def register_handler(handler = None):
    '''
    Install application-specific WMF image handler.

    :param handler: Handler object.
    '''
    global _handler
    _handler = handler

if hasattr(Image.core, 'drawwmf'):
    
    class WmfHandler(ImageFile.StubHandler):
        
        def open(self = None, im = None):
            im._mode = 'RGB'
            self.bbox = im.info['wmf_bbox']

        
        def load(self = None, im = None):
            im.fp.seek(0)
            return Image.frombytes('RGB', im.size, Image.core.drawwmf(im.fp.read(), im.size, self.bbox), 'raw', 'BGR', im.size[0] * 3 + 3 & -4, -1)


    register_handler(WmfHandler())

def _accept(prefix = None):
    return prefix.startswith((b'\xd7\xcd\xc6\x9a\x00\x00', b'\x01\x00\x00\x00'))


class WmfStubImageFile(ImageFile.StubImageFile):
    pass
# WARNING: Decompyle incomplete


def _save(im = None, fp = None, filename = None):
    pass
# WARNING: Decompyle incomplete

Image.register_open(WmfStubImageFile.format, WmfStubImageFile, _accept)
Image.register_save(WmfStubImageFile.format, _save)
Image.register_extensions(WmfStubImageFile.format, [
    '.wmf',
    '.emf'])
