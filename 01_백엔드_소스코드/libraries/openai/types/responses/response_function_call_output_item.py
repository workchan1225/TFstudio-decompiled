# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_call_output_item.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from response_input_file_content import ResponseInputFileContent
from response_input_text_content import ResponseInputTextContent
from response_input_image_content import ResponseInputImageContent
__all__ = [
    'ResponseFunctionCallOutputItem']
ResponseFunctionCallOutputItem: TypeAlias = Annotated[(Union[(ResponseInputTextContent, ResponseInputImageContent, ResponseInputFileContent)], PropertyInfo(discriminator = 'type'))]
