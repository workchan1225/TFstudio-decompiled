# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _exceptions.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, cast
from typing_extensions import Literal
import httpx
from _utils import is_dict
from _models import construct_type
if TYPE_CHECKING:
    from types.chat import ChatCompletion
__all__ = [
    'BadRequestError',
    'AuthenticationError',
    'PermissionDeniedError',
    'NotFoundError',
    'ConflictError',
    'UnprocessableEntityError',
    'RateLimitError',
    'InternalServerError',
    'LengthFinishReasonError',
    'ContentFilterFinishReasonError',
    'InvalidWebhookSignatureError']

class OpenAIError(Exception):
    pass


class APIError(OpenAIError):
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


class UnprocessableEntityError(APIStatusError):
    status_code: 'Literal[422]' = 422


class RateLimitError(APIStatusError):
    status_code: 'Literal[429]' = 429


class InternalServerError(APIStatusError):
    pass


class LengthFinishReasonError(OpenAIError):
    pass
# WARNING: Decompyle incomplete


class ContentFilterFinishReasonError(OpenAIError):
    pass
# WARNING: Decompyle incomplete


class InvalidWebhookSignatureError(ValueError):
    '''Raised when a webhook signature is invalid, meaning the computed signature does not match the expected signature.'''
    pass
