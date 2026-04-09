# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reinforcement_hyperparameters.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ReinforcementHyperparameters']

class ReinforcementHyperparameters(BaseModel):
    '''The hyperparameters used for the reinforcement fine-tuning job.'''
    batch_size: Union[(Literal['auto'], int, None)] = None
    compute_multiplier: Union[(Literal['auto'], float, None)] = None
    eval_interval: Union[(Literal['auto'], int, None)] = None
    eval_samples: Union[(Literal['auto'], int, None)] = None
    learning_rate_multiplier: Union[(Literal['auto'], float, None)] = None
    n_epochs: Union[(Literal['auto'], int, None)] = None
    reasoning_effort: Optional[Literal[('default', 'low', 'medium', 'high')]] = None
