# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dpo_method.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from dpo_hyperparameters import DpoHyperparameters
__all__ = [
    'DpoMethod']

class DpoMethod(BaseModel):
    '''Configuration for the DPO fine-tuning method.'''
    hyperparameters: Optional[DpoHyperparameters] = None
