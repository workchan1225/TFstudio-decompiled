# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_mcphttp_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RealtimeMcphttpError']

class RealtimeMcphttpError(BaseModel):
    type: Literal['http_error'] = 'RealtimeMcphttpError'
