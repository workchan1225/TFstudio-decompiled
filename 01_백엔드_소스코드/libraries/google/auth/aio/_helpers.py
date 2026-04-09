# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _helpers.pyc (Python 3.11)

'''Helper functions for commonly used utilities.'''
import logging
from typing import Any
from google.auth import _helpers

async def _parse_response_async(response = None):
    '''
    Parses an async response, attempting to decode JSON.

    Args:
        response: The response object to parse. This can be any type, but
            it is expected to have a `json()` method if it contains JSON.

    Returns:
        The parsed response. If the response contains valid JSON, the
        decoded JSON object (e.g., a dictionary) is returned.
        If the response does not have a `json()` method or if the JSON
        decoding fails, None is returned.
    '''
    pass
# WARNING: Decompyle incomplete


async def response_log_async(logger = None, response = None):
    '''
    Logs an Async HTTP response at the DEBUG level if logging is enabled.

    Args:
        logger: The logging.Logger instance to use.
        response: The HTTP response object to log.
    '''
    pass
# WARNING: Decompyle incomplete
