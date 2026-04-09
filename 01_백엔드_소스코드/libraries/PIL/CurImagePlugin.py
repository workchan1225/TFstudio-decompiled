# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: CurImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from  import BmpImagePlugin, Image
from _binary import i16le as i16
from _binary import i32le as i32

def _accept(prefix = None):
    return prefix.startswith(b'\x00\x00\x02\x00')


class CurImageFile(BmpImagePlugin.BmpImageFile):
    format = 'CUR'
    format_description = 'Windows Cursor'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(CurImageFile.format, CurImageFile, _accept)
Image.register_extension(CurImageFile.format, '.cur')
