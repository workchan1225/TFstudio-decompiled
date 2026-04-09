# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: realtime_tracing_config_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import Literal, TypeAlias, TypedDict
__all__ = [
    'RealtimeTracingConfigParam',
    'TracingConfiguration']

def TracingConfiguration():
    '''TracingConfiguration'''
    workflow_name: 'str' = 'Granular configuration for tracing.'

TracingConfiguration = <NODE:27>(TracingConfiguration, 'TracingConfiguration', TypedDict, total = False)
RealtimeTracingConfigParam: 'TypeAlias' = Union[(Literal['auto'], TracingConfiguration)]
