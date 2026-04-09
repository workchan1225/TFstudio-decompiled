# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: content_block_source_content_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from text_block_param import TextBlockParam
from image_block_param import ImageBlockParam
__all__ = [
    'ContentBlockSourceContentParam']
ContentBlockSourceContentParam: 'TypeAlias' = Union[(TextBlockParam, ImageBlockParam)]
