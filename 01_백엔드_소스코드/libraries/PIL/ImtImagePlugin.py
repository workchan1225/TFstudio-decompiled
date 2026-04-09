# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImtImagePlugin.pyc (Python 3.11)

from __future__ import annotations
import re
from  import Image, ImageFile
field = re.compile(b'([a-z]*) ([^ \\r\\n]*)')

class ImtImageFile(ImageFile.ImageFile):
    format = 'IMT'
    format_description = 'IM Tools'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete


Image.register_open(ImtImageFile.format, ImtImageFile)
