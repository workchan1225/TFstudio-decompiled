# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_container_upload_block.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaContainerUploadBlock']

class BetaContainerUploadBlock(BaseModel):
    type: Literal['container_upload'] = 'BetaContainerUploadBlock'
