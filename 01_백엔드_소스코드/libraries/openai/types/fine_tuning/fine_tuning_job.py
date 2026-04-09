# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fine_tuning_job.pyc (Python 3.11)

from typing import List, Union, Optional
from typing_extensions import Literal
from _models import BaseModel
from dpo_method import DpoMethod
from shared.metadata import Metadata
from supervised_method import SupervisedMethod
from reinforcement_method import ReinforcementMethod
from fine_tuning_job_wandb_integration_object import FineTuningJobWandbIntegrationObject
__all__ = [
    'FineTuningJob',
    'Error',
    'Hyperparameters',
    'Method']

class Error(BaseModel):
    message: str = '\n    For fine-tuning jobs that have `failed`, this will contain more information on the cause of the failure.\n    '
    param: Optional[str] = None


class Hyperparameters(BaseModel):
    '''The hyperparameters used for the fine-tuning job.

    This value will only be returned when running `supervised` jobs.
    '''
    batch_size: Union[(Literal['auto'], int, None)] = None
    learning_rate_multiplier: Union[(Literal['auto'], float, None)] = None
    n_epochs: Union[(Literal['auto'], int, None)] = None


class Method(BaseModel):
    type: Literal[('supervised', 'dpo', 'reinforcement')] = 'The method used for fine-tuning.'
    dpo: Optional[DpoMethod] = None
    reinforcement: Optional[ReinforcementMethod] = None
    supervised: Optional[SupervisedMethod] = None


class FineTuningJob(BaseModel):
    created_at: int = '\n    The `fine_tuning.job` object represents a fine-tuning job that has been created through the API.\n    '
    error: Optional[Error] = None
    fine_tuned_model: Optional[str] = None
    status: Literal[('validating_files', 'queued', 'running', 'succeeded', 'failed', 'cancelled')] = None
    training_file: str = None
    validation_file: Optional[str] = None
    estimated_finish: Optional[int] = None
    integrations: Optional[List[FineTuningJobWandbIntegrationObject]] = None
    metadata: Optional[Metadata] = None
    method: Optional[Method] = None
