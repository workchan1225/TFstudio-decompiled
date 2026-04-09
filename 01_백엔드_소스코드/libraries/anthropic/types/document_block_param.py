# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: document_block_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from url_pdf_source_param import URLPDFSourceParam
from citations_config_param import CitationsConfigParam
from base64_pdf_source_param import Base64PDFSourceParam
from plain_text_source_param import PlainTextSourceParam
from content_block_source_param import ContentBlockSourceParam
from cache_control_ephemeral_param import CacheControlEphemeralParam
__all__ = [
    'DocumentBlockParam',
    'Source']
Source: 'TypeAlias' = Union[(Base64PDFSourceParam, PlainTextSourceParam, ContentBlockSourceParam, URLPDFSourceParam)]

def DocumentBlockParam():
    '''DocumentBlockParam'''
    title: 'Optional[str]' = 'DocumentBlockParam'

DocumentBlockParam = <NODE:27>(DocumentBlockParam, 'DocumentBlockParam', TypedDict, total = False)
