# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eval_stored_completions_data_source_config.pyc (Python 3.11)

from typing import Dict, Optional
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from _models import BaseModel
from shared.metadata import Metadata
__all__ = [
    'EvalStoredCompletionsDataSourceConfig']

class EvalStoredCompletionsDataSourceConfig(BaseModel):
    '''Deprecated in favor of LogsDataSourceConfig.'''
    type: Literal['stored_completions'] = FieldInfo(alias = 'schema')
    metadata: Optional[Metadata] = None
