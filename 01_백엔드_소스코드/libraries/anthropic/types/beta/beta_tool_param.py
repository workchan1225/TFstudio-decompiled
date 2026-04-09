# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta_tool_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict
from _types import SequenceNotStr
from beta_cache_control_ephemeral_param import BetaCacheControlEphemeralParam
__all__ = [
    'BetaToolParam',
    'InputSchema']

def InputSchemaTyped():
    '''InputSchemaTyped'''
    required: 'Optional[SequenceNotStr[str]]' = 'InputSchemaTyped'

InputSchemaTyped = <NODE:27>(InputSchemaTyped, 'InputSchemaTyped', TypedDict, total = False)
InputSchema: 'TypeAlias' = Union[(InputSchemaTyped, Dict[(str, object)])]

def BetaToolParam():
    '''BetaToolParam'''
    type: "Optional[Literal['custom']]" = 'BetaToolParam'

BetaToolParam = <NODE:27>(BetaToolParam, 'BetaToolParam', TypedDict, total = False)
