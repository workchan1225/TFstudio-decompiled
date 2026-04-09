# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_server_tool_use_block.pyc (Python 3.11)

from typing import Dict, Union
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from beta_direct_caller import BetaDirectCaller
from beta_server_tool_caller import BetaServerToolCaller
__all__ = [
    'BetaServerToolUseBlock',
    'Caller']
Caller: TypeAlias = Annotated[(Union[(BetaDirectCaller, BetaServerToolCaller)], PropertyInfo(discriminator = 'type'))]

class BetaServerToolUseBlock(BaseModel):
    type: Literal['server_tool_use'] = 'BetaServerToolUseBlock'
