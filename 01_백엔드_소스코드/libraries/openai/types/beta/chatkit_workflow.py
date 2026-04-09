# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: chatkit_workflow.pyc (Python 3.11)

from typing import Dict, Union, Optional
from _models import BaseModel
__all__ = [
    'ChatKitWorkflow',
    'Tracing']

class Tracing(BaseModel):
    enabled: bool = 'Tracing settings applied to the workflow.'


class ChatKitWorkflow(BaseModel):
    id: str = 'Workflow metadata and state returned for the session.'
    tracing: Tracing = None
    version: Optional[str] = None
