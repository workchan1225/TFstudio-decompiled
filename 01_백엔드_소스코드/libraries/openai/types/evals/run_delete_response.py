# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: run_delete_response.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
__all__ = [
    'RunDeleteResponse']

class RunDeleteResponse(BaseModel):
    deleted: Optional[bool] = None
    object: Optional[str] = None
    run_id: Optional[str] = None
