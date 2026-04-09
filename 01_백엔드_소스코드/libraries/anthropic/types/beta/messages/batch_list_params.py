# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: batch_list_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List
from typing_extensions import Annotated, TypedDict
from _utils import PropertyInfo
from anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'BatchListParams']

def BatchListParams():
    '''BatchListParams'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'BatchListParams'

BatchListParams = <NODE:27>(BatchListParams, 'BatchListParams', TypedDict, total = False)
