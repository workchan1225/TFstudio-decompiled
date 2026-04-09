# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_json_object.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFormatJSONObject']

class ResponseFormatJSONObject(BaseModel):
    type: Literal['json_object'] = 'JSON object response format.\n\n    An older method of generating JSON responses.\n    Using `json_schema` is recommended for models that support it. Note that the\n    model will not generate JSON without a system or user message instructing it\n    to do so.\n    '
