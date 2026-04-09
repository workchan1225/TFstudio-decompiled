# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: job_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, TypedDict
from _types import SequenceNotStr
from dpo_method_param import DpoMethodParam
from shared_params.metadata import Metadata
from supervised_method_param import SupervisedMethodParam
from reinforcement_method_param import ReinforcementMethodParam
__all__ = [
    'JobCreateParams',
    'Hyperparameters',
    'Integration',
    'IntegrationWandb',
    'Method']

def JobCreateParams():
    '''JobCreateParams'''
    validation_file: 'Optional[str]' = 'JobCreateParams'

JobCreateParams = <NODE:27>(JobCreateParams, 'JobCreateParams', TypedDict, total = False)

def Hyperparameters():
    '''Hyperparameters'''
    n_epochs: "Union[Literal['auto'], int]" = '\n    The hyperparameters used for the fine-tuning job.\n    This value is now deprecated in favor of `method`, and should be passed in under the `method` parameter.\n    '

Hyperparameters = <NODE:27>(Hyperparameters, 'Hyperparameters', TypedDict, total = False)

def IntegrationWandb():
    '''IntegrationWandb'''
    tags: 'SequenceNotStr[str]' = 'The settings for your integration with Weights and Biases.\n\n    This payload specifies the project that\n    metrics will be sent to. Optionally, you can set an explicit display name for your run, add tags\n    to your run, and set a default entity (team, username, etc) to be associated with your run.\n    '

IntegrationWandb = <NODE:27>(IntegrationWandb, 'IntegrationWandb', TypedDict, total = False)

def Integration():
    '''Integration'''
    wandb: 'Required[IntegrationWandb]' = 'Integration'

Integration = <NODE:27>(Integration, 'Integration', TypedDict, total = False)

def Method():
    '''Method'''
    supervised: 'SupervisedMethodParam' = 'The method used for fine-tuning.'

Method = <NODE:27>(Method, 'Method', TypedDict, total = False)
