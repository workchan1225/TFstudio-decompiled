# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: BufrStubImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import IO
from  import Image, ImageFile
_handler = None

def register_handler(handler = None):
    '''
    Install application-specific BUFR image handler.

    :param handler: Handler object.
    '''
    global _handler
    _handler = handler


def _accept(prefix = None):
    return prefix.startswith((b'BUFR', b'ZCZC'))


class BufrStubImageFile(ImageFile.StubImageFile):
    format = 'BUFR'
    format_description = 'BUFR'
    
    def _open(self = None):
        if not _accept(self.fp.read(4)):
            msg = 'Not a BUFR file'
            raise SyntaxError(msg)
        self.fp.seek(-4, os.SEEK_CUR)
        self._mode = 'F'
        self._size = (1, 1)
        loader = self._load()
        if loader:
            loader.open(self)
            return None

    
    def _load(self = None):
        return _handler



def _save(im = None, fp = None, filename = None):
    pass
# WARNING: Decompyle incomplete

Image.register_open(BufrStubImageFile.format, BufrStubImageFile, _accept)
Image.register_save(BufrStubImageFile.format, _save)
Image.register_extension(BufrStubImageFile.format, '.bufr')
