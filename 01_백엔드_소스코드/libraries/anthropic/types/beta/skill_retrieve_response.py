# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: skill_retrieve_response.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'SkillRetrieveResponse']

class SkillRetrieveResponse(BaseModel):
    created_at: str = 'SkillRetrieveResponse'
    display_title: Optional[str] = None
    updated_at: str = None
