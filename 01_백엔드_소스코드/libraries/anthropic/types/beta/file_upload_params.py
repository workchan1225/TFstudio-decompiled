# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_upload_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List
from typing_extensions import Required, Annotated, TypedDict
from _types import FileTypes
from _utils import PropertyInfo
from anthropic_beta_param import AnthropicBetaParam
__all__ = [
    'FileUploadParams']

def FileUploadParams():
    '''FileUploadParams'''
    betas: "Annotated[List[AnthropicBetaParam], PropertyInfo(alias='anthropic-beta')]" = 'FileUploadParams'

FileUploadParams = <NODE:27>(FileUploadParams, 'FileUploadParams', TypedDict, total = False)
