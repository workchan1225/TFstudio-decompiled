# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_prompt_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Dict, Union, Optional
from typing_extensions import Required, TypeAlias, TypedDict
from response_input_file_param import ResponseInputFileParam
from response_input_text_param import ResponseInputTextParam
from response_input_image_param import ResponseInputImageParam
__all__ = [
    'ResponsePromptParam',
    'Variables']
Variables: 'TypeAlias' = Union[(str, ResponseInputTextParam, ResponseInputImageParam, ResponseInputFileParam)]

def ResponsePromptParam():
    '''ResponsePromptParam'''
    version: 'Optional[str]' = '\n    Reference to a prompt template and its variables.\n    [Learn more](https://platform.openai.com/docs/guides/text?api-mode=responses#reusable-prompts).\n    '

ResponsePromptParam = <NODE:27>(ResponsePromptParam, 'ResponsePromptParam', TypedDict, total = False)
