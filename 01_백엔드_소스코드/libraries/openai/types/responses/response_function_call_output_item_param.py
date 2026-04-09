# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_call_output_item_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from response_input_file_content_param import ResponseInputFileContentParam
from response_input_text_content_param import ResponseInputTextContentParam
from response_input_image_content_param import ResponseInputImageContentParam
__all__ = [
    'ResponseFunctionCallOutputItemParam']
ResponseFunctionCallOutputItemParam: 'TypeAlias' = Union[(ResponseInputTextContentParam, ResponseInputImageContentParam, ResponseInputFileContentParam)]
