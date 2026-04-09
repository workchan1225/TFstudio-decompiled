# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_text_config.pyc (Python 3.11)

from typing import Union
from typing_extensions import Annotated, TypeAlias
from _utils import PropertyInfo
from shared.response_format_text import ResponseFormatText
from shared.response_format_json_object import ResponseFormatJSONObject
from response_format_text_json_schema_config import ResponseFormatTextJSONSchemaConfig
__all__ = [
    'ResponseFormatTextConfig']
ResponseFormatTextConfig: TypeAlias = Annotated[(Union[(ResponseFormatText, ResponseFormatTextJSONSchemaConfig, ResponseFormatJSONObject)], PropertyInfo(discriminator = 'type'))]
