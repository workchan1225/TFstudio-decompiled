# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exceptions.pyc (Python 3.11)

from __future__ import annotations
from typing_extensions import Literal
import httpx
__all__ = [
    'BadRequestError',
    'AuthenticationError',
    'PermissionDeniedError',
    'NotFoundError',
    'ConflictError',
    'UnprocessableEntityError',
    'RateLimitError',
    'InternalServerError']

class AnthropicError(Exception):
    pass


class APIError(AnthropicError):
    pass
# WARNING: Decompyle incomplete


class APIResponseValidationError(APIError):
    pass
# WARNING: Decompyle incomplete


class APIStatusError(APIError):
    pass
# WARNING: Decompyle incomplete


class APIConnectionError(APIError):
    pass
# WARNING: Decompyle incomplete


class APITimeoutError(APIConnectionError):
    pass
# WARNING: Decompyle incomplete


class BadRequestError(APIStatusError):
    status_code: 'Literal[400]' = 400


class AuthenticationError(APIStatusError):
    status_code: 'Literal[401]' = 401


class PermissionDeniedError(APIStatusError):
    status_code: 'Literal[403]' = 403


class NotFoundError(APIStatusError):
    status_code: 'Literal[404]' = 404


class ConflictError(APIStatusError):
    status_code: 'Literal[409]' = 409


class RequestTooLargeError(APIStatusError):
    status_code: 'Literal[413]' = 413


class UnprocessableEntityError(APIStatusError):
    status_code: 'Literal[422]' = 422


class RateLimitError(APIStatusError):
    status_code: 'Literal[429]' = 429


class ServiceUnavailableError(APIStatusError):
    status_code: 'Literal[503]' = 503


class OverloadedError(APIStatusError):
    status_code: 'Literal[529]' = 529


class DeadlineExceededError(APIStatusError):
    status_code: 'Literal[504]' = 504


class InternalServerError(APIStatusError):
    pass
