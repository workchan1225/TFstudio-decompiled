# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ImagePalette.pyc (Python 3.11)

from __future__ import annotations
import array
from collections.abc import Sequence
from typing import IO
from  import GimpGradientFile, GimpPaletteFile, ImageColor, PaletteFile
TYPE_CHECKING = False
if TYPE_CHECKING:
    from  import Image

class ImagePalette:
    '''
    Color palette for palette mapped images

    :param mode: The mode to use for the palette. See:
        :ref:`concept-modes`. Defaults to "RGB"
    :param palette: An optional palette. If given, it must be a bytearray,
        an array or a list of ints between 0-255. The list must consist of
        all channels for one color followed by the next color (e.g. RGBRGBRGB).
        Defaults to an empty palette.
    '''
    
    def __init__(self = None, mode = None, palette = None):
