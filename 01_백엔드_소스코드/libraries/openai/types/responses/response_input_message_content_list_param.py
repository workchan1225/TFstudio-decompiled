# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_message_content_list_param.pyc (Python 3.11)

from __future__ import annotations
from typing import List, Union
from typing_extensions import TypeAlias
from response_input_file_param import ResponseInputFileParam
from response_input_text_param import ResponseInputTextParam
from response_input_image_param import ResponseInputImageParam
__all__ = [
    'ResponseInputMessageContentListParam',
    'ResponseInputContentParam']
ResponseInputContentParam: 'TypeAlias' = Union[(ResponseInputTextParam, ResponseInputImageParam, ResponseInputFileParam)]
ResponseInputMessageContentListParam: 'TypeAlias' = List[ResponseInputContentParam]
