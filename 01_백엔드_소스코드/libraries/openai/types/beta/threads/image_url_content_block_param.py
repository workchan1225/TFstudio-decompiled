# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_url_content_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal, Required, TypedDict
from image_url_param import ImageURLParam
__all__ = [
    'ImageURLContentBlockParam']

def ImageURLContentBlockParam():
    '''ImageURLContentBlockParam'''
    type: "Required[Literal['image_url']]" = 'References an image URL in the content of a message.'

ImageURLContentBlockParam = <NODE:27>(ImageURLContentBlockParam, 'ImageURLContentBlockParam', TypedDict, total = False)
