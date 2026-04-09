# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PcdImagePlugin.pyc (Python 3.11)

from __future__ import annotations
from  import Image, ImageFile

class PcdImageFile(ImageFile.ImageFile):
    format = 'PCD'
    format_description = 'Kodak PhotoCD'
    
    def _open(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def load_prepare(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def load_end(self = None):
        if self.tile_post_rotate:
            self.im = self.rotate(self.tile_post_rotate, expand = True).im
            return None


Image.register_open(PcdImageFile.format, PcdImageFile)
Image.register_extension(PcdImageFile.format, '.pcd')
