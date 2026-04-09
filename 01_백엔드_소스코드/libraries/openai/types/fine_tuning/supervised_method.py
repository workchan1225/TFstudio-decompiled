# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: supervised_method.pyc (Python 3.11)

from typing import Optional
from _models import BaseModel
from supervised_hyperparameters import SupervisedHyperparameters
__all__ = [
    'SupervisedMethod']

class SupervisedMethod(BaseModel):
    '''Configuration for the supervised fine-tuning method.'''
    hyperparameters: Optional[SupervisedHyperparameters] = None
