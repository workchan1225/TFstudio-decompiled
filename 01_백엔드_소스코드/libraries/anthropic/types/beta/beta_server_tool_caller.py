# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_server_tool_caller.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'BetaServerToolCaller']

class BetaServerToolCaller(BaseModel):
    type: Literal['code_execution_20250825'] = 'BetaServerToolCaller'
