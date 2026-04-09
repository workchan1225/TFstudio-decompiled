# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webhooks.pyc (Python 3.11)

from __future__ import annotations
import hmac
import json
import time
import base64
import hashlib
from typing import cast
from _types import HeadersLike
from _utils import get_required_header
from _models import construct_type
from _resource import SyncAPIResource, AsyncAPIResource
from _exceptions import InvalidWebhookSignatureError
from types.webhooks.unwrap_webhook_event import UnwrapWebhookEvent
__all__ = [
    'Webhooks',
    'AsyncWebhooks']

class Webhooks(SyncAPIResource):
    
    def unwrap(self = None, payload = None, headers = None, *, secret):
        '''Validates that the given payload was sent by OpenAI and parses the payload.'''
        pass
    # WARNING: Decompyle incomplete

    
    def verify_signature(self = None, payload = None, headers = None, *, secret, tolerance):
        '''Validates whether or not the webhook payload was sent by OpenAI.

        Args:
            payload: The webhook payload
            headers: The webhook headers
            secret: The webhook secret (optional, will use client secret if not provided)
            tolerance: Maximum age of the webhook in seconds (default: 300 = 5 minutes)
        '''
        pass
    # WARNING: Decompyle incomplete



class AsyncWebhooks(AsyncAPIResource):
    
    def unwrap(self = None, payload = None, headers = None, *, secret):
        '''Validates that the given payload was sent by OpenAI and parses the payload.'''
        pass
    # WARNING: Decompyle incomplete

    
    def verify_signature(self = None, payload = None, headers = None, *, secret, tolerance):
        '''Validates whether or not the webhook payload was sent by OpenAI.

        Args:
            payload: The webhook payload
            headers: The webhook headers
            secret: The webhook secret (optional, will use client secret if not provided)
            tolerance: Maximum age of the webhook in seconds (default: 300 = 5 minutes)
        '''
        pass
    # WARNING: Decompyle incomplete
