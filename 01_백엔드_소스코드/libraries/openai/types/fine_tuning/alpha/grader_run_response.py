# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: grader_run_response.pyc (Python 3.11)

from typing import Dict, Optional
from pydantic import Field as FieldInfo
from _models import BaseModel
__all__ = [
    'GraderRunResponse',
    'Metadata',
    'MetadataErrors']

class MetadataErrors(BaseModel):
    invalid_variable_error: bool = 'MetadataErrors'
    api_model_grader_parse_error: bool = FieldInfo(alias = 'model_grader_parse_error')
    api_model_grader_refusal_error: bool = FieldInfo(alias = 'model_grader_refusal_error')
    api_model_grader_server_error: bool = FieldInfo(alias = 'model_grader_server_error')
    python_grader_runtime_error: bool = FieldInfo(alias = 'model_grader_server_error_details', default = None)
    python_grader_server_error: bool = None
    unresponsive_reward_error: bool = None


class Metadata(BaseModel):
    name: str = 'Metadata'
    scores: Dict[(str, object)] = None
    type: str = None


class GraderRunResponse(BaseModel):
    metadata: Metadata = 'GraderRunResponse'
    sub_rewards: Dict[(str, object)] = FieldInfo(alias = 'model_grader_token_usage_per_model')
