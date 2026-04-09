# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_text_config_param.pyc (Python 3.11)

from __future__ import annotations
from typing import Union
from typing_extensions import TypeAlias
from shared_params.response_format_text import ResponseFormatText
from shared_params.response_format_json_object import ResponseFormatJSONObject
from response_format_text_json_schema_config_param import ResponseFormatTextJSONSchemaConfigParam
__all__ = [
    'ResponseFormatTextConfigParam']
ResponseFormatTextConfigParam: 'TypeAlias' = Union[(ResponseFormatText, ResponseFormatTextJSONSchemaConfigParam, ResponseFormatJSONObject)]
