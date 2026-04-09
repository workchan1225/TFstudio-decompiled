# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_image_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from beta_url_image_source_param import BetaURLImageSourceParam
from beta_file_image_source_param import BetaFileImageSourceParam
from beta_base64_image_source_param import BetaBase64ImageSourceParam
from beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
__all__ = [
    'BetaImageBlockParam',
    'Source']
Source: 'TypeAlias' = Union[(BetaBase64ImageSourceParam, BetaURLImageSourceParam, BetaFileImageSourceParam)]

def BetaImageBlockParam():
    '''BetaImageBlockParam'''
    cache_control: 'Optional[BetaCacheControlEphemeralParam]' = 'BetaImageBlockParam'

BetaImageBlockParam = <NODE:27>(BetaImageBlockParam, 'BetaImageBlockParam', TypedDict, total = False)
