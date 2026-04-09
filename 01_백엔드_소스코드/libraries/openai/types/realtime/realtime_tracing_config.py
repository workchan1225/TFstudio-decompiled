# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_tracing_config.pyc (Python 3.11)

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias
from _models import BaseModel
__all__ = [
    'RealtimeTracingConfig',
    'TracingConfiguration']

class TracingConfiguration(BaseModel):
    '''Granular configuration for tracing.'''
    group_id: Optional[str] = None
    metadata: Optional[object] = None
    workflow_name: Optional[str] = None

RealtimeTracingConfig: TypeAlias = Union[(Literal['auto'], TracingConfiguration, None)]
