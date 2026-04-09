# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_json_schema.pyc (Python 3.11)

from typing import Dict, Optional
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from _models import BaseModel
__all__ = [
    'ResponseFormatJSONSchema',
    'JSONSchema']

class JSONSchema(BaseModel):
    name: str = 'Structured Outputs configuration options, including a JSON Schema.'
    description: Optional[str] = None
    schema_: Optional[Dict[(str, object)]] = FieldInfo(alias = 'schema', default = None)
    strict: Optional[bool] = None


class ResponseFormatJSONSchema(BaseModel):
    type: Literal['json_schema'] = 'JSON Schema response format.\n\n    Used to generate structured JSON responses.\n    Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).\n    '
