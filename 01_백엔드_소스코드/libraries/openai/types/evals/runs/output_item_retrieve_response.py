# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: output_item_retrieve_response.pyc (Python 3.11)

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal
from pydantic import Field as FieldInfo
from _models import BaseModel
from eval_api_error import EvalAPIError
__all__ = [
    'OutputItemRetrieveResponse',
    'Result',
    'Sample',
    'SampleInput',
    'SampleOutput',
    'SampleUsage']

class Result(BaseModel):
    score: float = 'A single grader result for an evaluation run output item.'
    sample: Optional[Dict[(str, object)]] = None
    type: Optional[str] = None
    if TYPE_CHECKING:
        __pydantic_extra__: Dict[(str, object)] = FieldInfo(init = False)
        
        def __getattr__(self = None, attr = None):
            pass

        return None
    __pydantic_extra__: None[(str, object)]


class SampleInput(BaseModel):
    role: str = 'An input message.'


class SampleOutput(BaseModel):
    content: Optional[str] = None
    role: Optional[str] = None


class SampleUsage(BaseModel):
    total_tokens: int = 'Token usage details for the sample.'


class Sample(BaseModel):
    usage: SampleUsage = 'A sample containing the input and output of the evaluation run.'


class OutputItemRetrieveResponse(BaseModel):
    status: str = 'A schema representing an evaluation run output item.'
