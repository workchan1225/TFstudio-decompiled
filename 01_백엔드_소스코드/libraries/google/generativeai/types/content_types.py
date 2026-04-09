# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: content_types.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterable, Mapping, Sequence
import io
import inspect
import mimetypes
import pathlib
import typing
from typing import Any, Callable, Union
from typing_extensions import TypedDict
import pydantic
from google.generativeai.types import file_types
from google.generativeai import protos
if typing.TYPE_CHECKING:
    import PIL.Image as PIL
    import PIL.ImageFile as PIL
    import IPython.display as IPython
    IMAGE_TYPES = (PIL.Image.Image, IPython.display.Image)
else:
    IMAGE_TYPES = ()
    
    try:
        import PIL.Image as PIL
        import PIL.ImageFile as PIL
        IMAGE_TYPES = IMAGE_TYPES + (PIL.Image.Image,)
    except ImportError:
        PIL = None

    
    try:
        import IPython.display as IPython
        IMAGE_TYPES = IMAGE_TYPES + (IPython.display.Image,)
    except ImportError:
        IPython = None

    __all__ = [
        'BlobDict',
        'BlobType',
        'PartDict',
        'PartType',
        'ContentDict',
        'ContentType',
        'StrictContentType',
        'ContentsType',
        'FunctionDeclaration',
        'CallableFunctionDeclaration',
        'FunctionDeclarationType',
        'Tool',
        'ToolDict',
        'ToolsType',
        'FunctionLibrary',
        'FunctionLibraryType']
    Mode = protos.DynamicRetrievalConfig.Mode
    ModeOptions = Union[(int, str, Mode)]
    _MODE: 'dict[ModeOptions, Mode]' = {
        'dynamic': Mode.MODE_DYNAMIC,
        'mode_dynamic': Mode.MODE_DYNAMIC,
        1: Mode.MODE_DYNAMIC,
        Mode.MODE_DYNAMIC: Mode.MODE_DYNAMIC,
        'unspecified': Mode.MODE_UNSPECIFIED,
        'mode_unspecified': Mode.MODE_UNSPECIFIED,
        0: Mode.MODE_UNSPECIFIED,
        Mode.MODE_UNSPECIFIED: Mode.MODE_UNSPECIFIED }
    
    def to_mode(x = None):
        if isinstance(x, str):
            x = x.lower()
        return _MODE[x]

    
    def _pil_to_blob(image = None):
