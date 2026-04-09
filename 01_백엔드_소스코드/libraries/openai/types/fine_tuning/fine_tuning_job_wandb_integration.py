# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fine_tuning_job_wandb_integration.pyc (Python 3.11)

from typing import List, Optional
from _models import BaseModel
__all__ = [
    'FineTuningJobWandbIntegration']

class FineTuningJobWandbIntegration(BaseModel):
    project: str = 'The settings for your integration with Weights and Biases.\n\n    This payload specifies the project that\n    metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags\n    to your run, and set a default entity (team, username, etc) to be associated with your run.\n    '
    entity: Optional[str] = None
    name: Optional[str] = None
    tags: Optional[List[str]] = None
