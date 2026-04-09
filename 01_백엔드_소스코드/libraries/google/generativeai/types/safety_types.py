# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: safety_types.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Mapping
import enum
import typing
from typing import Dict, Iterable, List, Union
from typing_extensions import TypedDict
from google.generativeai import protos
from google.generativeai import string_utils
__all__ = [
    'HarmCategory',
    'HarmProbability',
    'HarmBlockThreshold',
    'BlockedReason',
    'ContentFilterDict',
    'SafetyRatingDict',
    'SafetySettingDict',
    'SafetyFeedbackDict']
HarmProbability = protos.SafetyRating.HarmProbability
HarmBlockThreshold = protos.SafetySetting.HarmBlockThreshold
BlockedReason = protos.ContentFilter.BlockedReason
import proto

class HarmCategory(proto.Enum):
    '''
    Harm Categories supported by the gemini-family model
    '''
    HARM_CATEGORY_UNSPECIFIED = protos.HarmCategory.HARM_CATEGORY_UNSPECIFIED.value
    HARM_CATEGORY_HARASSMENT = protos.HarmCategory.HARM_CATEGORY_HARASSMENT.value
    HARM_CATEGORY_HATE_SPEECH = protos.HarmCategory.HARM_CATEGORY_HATE_SPEECH.value
    HARM_CATEGORY_SEXUALLY_EXPLICIT = protos.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT.value
    HARM_CATEGORY_DANGEROUS_CONTENT = protos.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT.value

HarmCategoryOptions = Union[(str, int, HarmCategory)]
# WARNING: Decompyle incomplete
