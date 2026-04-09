# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: eval_custom_data_source_config.pyc (Python 3.11)

from typing import Dict
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from _models import BaseModel
__all__ = [
    'EvalCustomDataSourceConfig']

class EvalCustomDataSourceConfig(BaseModel):
    '''
    A CustomDataSourceConfig which specifies the schema of your `item` and optionally `sample` namespaces.
    The response schema defines the shape of the data that will be:
    - Used to define your testing criteria and
    - What data is required when creating a run
    '''
    type: Literal['custom'] = FieldInfo(alias = 'schema')
