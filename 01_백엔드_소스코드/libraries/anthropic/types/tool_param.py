# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from _models import set_pydantic_config
from cache_control_ephemeral_param import CacheControlEphemeralParam
__all__ = [
    'ToolParam',
    'InputSchema']

def InputSchemaTyped():
    '''InputSchemaTyped'''
    required: 'Optional[SequenceNotStr[str]]' = 'InputSchemaTyped'

InputSchemaTyped = <NODE:27>(InputSchemaTyped, 'InputSchemaTyped', TypedDict, total = False)
set_pydantic_config(InputSchemaTyped, {
    'extra': 'allow' })
InputSchema: 'TypeAlias' = Union[(InputSchemaTyped, Dict[(str, object)])]

def ToolParam():
    '''ToolParam'''
    type: "Optional[Literal['custom']]" = 'ToolParam'

ToolParam = <NODE:27>(ToolParam, 'ToolParam', TypedDict, total = False)
