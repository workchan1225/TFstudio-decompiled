# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: call_accept_params.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union, Optional
from typing_extensions import Literal, Required, TypedDict
from realtime_truncation_param import RealtimeTruncationParam
from realtime_audio_config_param import RealtimeAudioConfigParam
from realtime_tools_config_param import RealtimeToolsConfigParam
from realtime_tracing_config_param import RealtimeTracingConfigParam
from responses.response_prompt_param import ResponsePromptParam
from realtime_tool_choice_config_param import RealtimeToolChoiceConfigParam
__all__ = [
    'CallAcceptParams']

def CallAcceptParams():
    '''CallAcceptParams'''
    truncation: 'RealtimeTruncationParam' = 'CallAcceptParams'

CallAcceptParams = <NODE:27>(CallAcceptParams, 'CallAcceptParams', TypedDict, total = False)
