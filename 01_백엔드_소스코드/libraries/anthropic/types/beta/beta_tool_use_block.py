# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_tool_use_block.pyc (Python 3.11)

from typing import Dict, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from beta_direct_caller import BetaDirectCaller
from beta_server_tool_caller import BetaServerToolCaller
__all__ = [
    'BetaToolUseBlock',
    'Caller']
Caller: TypeAlias = Annotated[(Union[(BetaDirectCaller, BetaServerToolCaller)], PropertyInfo(discriminator = 'type'))]

class BetaToolUseBlock(BaseModel):
    type: Literal['tool_use'] = 'BetaToolUseBlock'
    caller: Optional[Caller] = None
