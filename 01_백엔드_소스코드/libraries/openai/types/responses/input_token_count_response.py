# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: input_token_count_response.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'InputTokenCountResponse']

class InputTokenCountResponse(BaseModel):
    object: Literal['response.input_tokens'] = 'InputTokenCountResponse'
