# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rate_limit_error.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'RateLimitError']

class RateLimitError(BaseModel):
    type: Literal['rate_limit_error'] = 'RateLimitError'
