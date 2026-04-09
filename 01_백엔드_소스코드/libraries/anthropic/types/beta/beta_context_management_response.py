# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_context_management_response.pyc (Python 3.11)

from typing import List, Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
from beta_clear_thinking_20251015_edit_response import BetaClearThinking20251015EditResponse
from beta_clear_tool_uses_20250919_edit_response import BetaClearToolUses20250919EditResponse
__all__ = [
    'BetaContextManagementResponse',
    'AppliedEdit']
AppliedEdit: TypeAlias = Annotated[(Union[(BetaClearToolUses20250919EditResponse, BetaClearThinking20251015EditResponse)], PropertyInfo(discriminator = 'type'))]

class BetaContextManagementResponse(BaseModel):
    applied_edits: List[AppliedEdit] = 'BetaContextManagementResponse'
