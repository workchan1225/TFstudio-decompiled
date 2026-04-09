# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: types.pyc (Python 3.11)

'''
Script Generation V2 types.
'''
from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional

class ScriptGenerationMode(Enum, str):
    STANDARD = 'standard'
    LONGFORM = 'longform'
    SHORTS = 'shorts'
    REFERENCE = 'reference'


def build_warning(code = None, message = None, *, field, suggestion, level):
    return {
        'level': level,
        'code': code,
        'message': message,
        'field': field,
        'suggestion': suggestion }

ScriptChapterV2 = <NODE:12>()
ScriptGenerationV2Request = <NODE:12>()
ScriptGenerationV2Response = <NODE:12>()
