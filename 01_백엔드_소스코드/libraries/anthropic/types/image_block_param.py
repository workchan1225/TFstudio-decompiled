# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: image_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from url_image_source_param import URLImageSourceParam
from base64_image_source_param import Base64ImageSourceParam
from cache_control_ephemeral_param import CacheControlEphemeralParam
__all__ = [
    'ImageBlockParam',
    'Source']
Source: 'TypeAlias' = Union[(Base64ImageSourceParam, URLImageSourceParam)]

def ImageBlockParam():
    '''ImageBlockParam'''
    cache_control: 'Optional[CacheControlEphemeralParam]' = 'ImageBlockParam'

ImageBlockParam = <NODE:27>(ImageBlockParam, 'ImageBlockParam', TypedDict, total = False)
