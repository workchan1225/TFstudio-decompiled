# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: moderation_create_params.pyc (Python 3.11)

from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import Required, TypedDict
from _types import SequenceNotStr
from moderation_model import ModerationModel
from moderation_multi_modal_input_param import ModerationMultiModalInputParam
__all__ = [
    'ModerationCreateParams']

def ModerationCreateParams():
    '''ModerationCreateParams'''
    model: 'Union[str, ModerationModel]' = 'ModerationCreateParams'

ModerationCreateParams = <NODE:27>(ModerationCreateParams, 'ModerationCreateParams', TypedDict, total = False)
