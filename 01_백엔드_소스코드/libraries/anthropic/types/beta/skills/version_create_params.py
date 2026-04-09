# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: version_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Optional
from typing_extensions import Annotated, TypedDict
from _types import FileTypes, SequenceNotStr
from _utils import PropertyInfo
from anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'VersionCreateParams']

def VersionCreateParams():
    '''VersionCreateParams'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'VersionCreateParams'

VersionCreateParams = <NODE:27>(VersionCreateParams, 'VersionCreateParams', TypedDict, total = False)
