# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: create_eval_jsonl_run_data_source.pyc (Python 3.11)

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias
from _utils import PropertyInfo
from _models import BaseModel
__all__ = [
    'CreateEvalJSONLRunDataSource',
    'Source',
    'SourceFileContent',
    'SourceFileContentContent',
    'SourceFileID']

class SourceFileContentContent(BaseModel):
    item: Dict[(str, object)] = 'SourceFileContentContent'
    sample: Optional[Dict[(str, object)]] = None


class SourceFileContent(BaseModel):
    type: Literal['file_content'] = 'SourceFileContent'


class SourceFileID(BaseModel):
    type: Literal['file_id'] = 'SourceFileID'

Source: TypeAlias = Annotated[(Union[(SourceFileContent, SourceFileID)], PropertyInfo(discriminator = 'type'))]

class CreateEvalJSONLRunDataSource(BaseModel):
    type: Literal['jsonl'] = '\n    A JsonlRunDataSource object with that specifies a JSONL file that matches the eval\n    '
