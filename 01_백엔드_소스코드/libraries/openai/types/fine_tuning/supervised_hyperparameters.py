# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: supervised_hyperparameters.pyc (Python 3.11)

from typing import Union
from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'SupervisedHyperparameters']

class SupervisedHyperparameters(BaseModel):
    '''The hyperparameters used for the fine-tuning job.'''
    batch_size: Union[(Literal['auto'], int, None)] = None
    learning_rate_multiplier: Union[(Literal['auto'], float, None)] = None
    n_epochs: Union[(Literal['auto'], int, None)] = None
