# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dpo_hyperparameters_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypedDict
__all__ = [
    'DpoHyperparametersParam']

def DpoHyperparametersParam():
    '''DpoHyperparametersParam'''
    n_epochs: "Union[Literal['auto'], int]" = 'The hyperparameters used for the DPO fine-tuning job.'

DpoHyperparametersParam = <NODE:27>(DpoHyperparametersParam, 'DpoHyperparametersParam', TypedDict, total = False)
