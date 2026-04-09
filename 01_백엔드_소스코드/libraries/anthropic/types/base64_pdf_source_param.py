# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base64_pdf_source_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, Required, Annotated, TypedDict
from _types import Base64FileInput
from _utils import PropertyInfo
from _models import set_pydantic_config
__all__ = [
    'Base64PDFSourceParam']

def Base64PDFSourceParam():
    '''Base64PDFSourceParam'''
    type: "Required[Literal['base64']]" = 'Base64PDFSourceParam'

Base64PDFSourceParam = <NODE:27>(Base64PDFSourceParam, 'Base64PDFSourceParam', TypedDict, total = False)
set_pydantic_config(Base64PDFSourceParam, {
    'arbitrary_types_allowed': True })
