# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: moderation_multi_modal_input_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from moderation_text_input_param import ModerationTextInputParam
from moderation_image_url_input_param import ModerationImageURLInputParam
__all__ = [
    'ModerationMultiModalInputParam']
ModerationMultiModalInputParam: 'TypeAlias' = Union[(ModerationImageURLInputParam, ModerationTextInputParam)]
