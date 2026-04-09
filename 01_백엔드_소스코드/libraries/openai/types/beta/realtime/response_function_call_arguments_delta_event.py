# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response_function_call_arguments_delta_event.pyc (Python 3.11)

from typing_extensions import Literal
from _models import BaseModel
__all__ = [
    'ResponseFunctionCallArgumentsDeltaEvent']

class ResponseFunctionCallArgumentsDeltaEvent(BaseModel):
    type: Literal['response.function_call_arguments.delta'] = 'ResponseFunctionCallArgumentsDeltaEvent'
