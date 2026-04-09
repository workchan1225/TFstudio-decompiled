# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_file_content_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from image_file_param import ImageFileParam
__all__ = [
    'ImageFileContentBlockParam']

def ImageFileContentBlockParam():
    '''ImageFileContentBlockParam'''
    type: "Required[Literal['image_file']]" = '\n    References an image [File](https://platform.openai.com/docs/api-reference/files) in the content of a message.\n    '

ImageFileContentBlockParam = <NODE:27>(ImageFileContentBlockParam, 'ImageFileContentBlockParam', TypedDict, total = False)
