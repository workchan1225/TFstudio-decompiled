# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: supervised_hyperparameters_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypedDict
__all__ = [
    'SupervisedHyperparametersParam']

def SupervisedHyperparametersParam():
    '''SupervisedHyperparametersParam'''
    n_epochs: "Union[Literal['auto'], int]" = 'The hyperparameters used for the fine-tuning job.'

SupervisedHyperparametersParam = <NODE:27>(SupervisedHyperparametersParam, 'SupervisedHyperparametersParam', TypedDict, total = False)
