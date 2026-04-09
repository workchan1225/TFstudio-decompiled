# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: errors.pyc (Python 3.11)

'''Error classes for the GenAI SDK.'''
from typing import Any, Callable, Optional, TYPE_CHECKING, Union
import httpx
import json
from  import _common
if TYPE_CHECKING:
    from replay_api_client import ReplayResponse
    import aiohttp

class APIError(Exception):
    pass
# WARNING: Decompyle incomplete


class ClientError(APIError):
    '''Client error raised by the GenAI API.'''
    pass


class ServerError(APIError):
    '''Server error raised by the GenAI API.'''
    pass


class UnknownFunctionCallArgumentError(ValueError):
    '''Raised when the function call argument cannot be converted to the parameter annotation.'''
    pass


class UnsupportedFunctionError(ValueError):
    '''Raised when the function is not supported.'''
    pass


class FunctionInvocationError(ValueError):
    '''Raised when the function cannot be invoked with the given arguments.'''
    pass


class UnknownApiResponseError(ValueError):
    '''Raised when the response from the API cannot be parsed as JSON.'''
    pass

ExperimentalWarning = _common.ExperimentalWarning
