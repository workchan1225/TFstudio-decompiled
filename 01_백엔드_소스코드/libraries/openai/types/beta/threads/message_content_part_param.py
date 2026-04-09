# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: message_content_part_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from text_content_block_param import TextContentBlockParam
from image_url_content_block_param import ImageURLContentBlockParam
from image_file_content_block_param import ImageFileContentBlockParam
__all__ = [
    'MessageContentPartParam']
MessageContentPartParam: 'TypeAlias' = Union[(ImageFileContentBlockParam, ImageURLContentBlockParam, TextContentBlockParam)]
