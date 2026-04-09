# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_format_text_json_schema_config.pyc (Python 3.11)

from typing import Dict, Optional
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from _models import BaseModel
__all__ = [
    'ResponseFormatTextJSONSchemaConfig']

class ResponseFormatTextJSONSchemaConfig(BaseModel):
    name: str = 'JSON Schema response format.\n\n    Used to generate structured JSON responses.\n    Learn more about [Structured Outputs](https://platform.openai.com/docs/guides/structured-outputs).\n    '
    type: Literal['json_schema'] = FieldInfo(alias = 'schema')
    description: Optional[str] = None
    strict: Optional[bool] = None
