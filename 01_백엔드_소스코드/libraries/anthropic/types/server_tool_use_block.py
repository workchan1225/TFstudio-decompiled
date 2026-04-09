# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: server_tool_use_block.pyc (Python 3.11)

from typing import Dict
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ServerToolUseBlock']

class ServerToolUseBlock(BaseModel):
    type: Literal['server_tool_use'] = 'ServerToolUseBlock'
