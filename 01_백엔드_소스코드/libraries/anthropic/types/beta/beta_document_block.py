# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_document_block.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from beta_citation_config import BetaCitationConfig
from beta_base64_pdf_source import BetaBase64PDFSource
from beta_plain_text_source import BetaPlainTextSource
__all__ = [
    'BetaDocumentBlock',
    'Source']
Source: TypeAlias = Annotated[(Union[(BetaBase64PDFSource, BetaPlainTextSource)], PropertyInfo(discriminator = 'type'))]

class BetaDocumentBlock(BaseModel):
    source: Source = None
    type: Literal['document'] = None
