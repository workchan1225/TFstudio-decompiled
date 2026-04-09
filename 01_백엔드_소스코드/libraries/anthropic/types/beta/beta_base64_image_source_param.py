# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_base64_image_source_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict
from _types import Base64FileInput
from _utils import PropertyInfo
from _models import set_pydantic_config
__all__ = [
    'BetaBase64ImageSourceParam']

def BetaBase64ImageSourceParam():
    '''BetaBase64ImageSourceParam'''
    type: "Required[Literal['base64']]" = 'BetaBase64ImageSourceParam'

BetaBase64ImageSourceParam = <NODE:27>(BetaBase64ImageSourceParam, 'BetaBase64ImageSourceParam', TypedDict, total = False)
set_pydantic_config(BetaBase64ImageSourceParam, {
    'arbitrary_types_allowed': True })
