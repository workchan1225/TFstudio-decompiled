# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_container.pyc (Python 3.11)

from typing import List, Optional
from datetime import datetime
from _models import BaseModel
from beta_skill import BetaSkill
__all__ = [
    'BetaContainer']

class BetaContainer(BaseModel):
    expires_at: datetime = 'BetaContainer'
    skills: Optional[List[BetaSkill]] = None
