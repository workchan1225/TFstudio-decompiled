# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_input_content_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from response_input_file_param import ResponseInputFileParam
from response_input_text_param import ResponseInputTextParam
from response_input_image_param import ResponseInputImageParam
__all__ = [
    'ResponseInputContentParam']
ResponseInputContentParam: 'TypeAlias' = Union[(ResponseInputTextParam, ResponseInputImageParam, ResponseInputFileParam)]
