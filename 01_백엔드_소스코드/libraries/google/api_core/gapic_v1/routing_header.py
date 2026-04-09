# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: routing_header.pyc (Python 3.11)

'''Helpers for constructing routing headers.

These headers are used by Google infrastructure to determine how to route
requests, especially for services that are regional.

Generally, these headers are specified as gRPC metadata.
'''
import functools
from enum import Enum
from urllib.parse import urlencode
ROUTING_METADATA_KEY = 'x-goog-request-params'
ROUTING_PARAM_CACHE_SIZE = 32

def to_routing_header(params, qualified_enums = (True,)):
    '''Returns a routing header string for the given request parameters.

    Args:
        params (Mapping[str, str | bytes | Enum]): A dictionary containing the request
            parameters used for routing.
        qualified_enums (bool): Whether to represent enum values
            as their type-qualified symbol names instead of as their
            unqualified symbol names.

    Returns:
        str: The routing header string.
    '''
    tuples = params.items() if isinstance(params, dict) else params
    if not qualified_enums:
        tuples = tuples()
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(tuples())


def to_grpc_metadata(params, qualified_enums = (True,)):
    '''Returns the gRPC metadata containing the routing headers for the given
    request parameters.

    Args:
        params (Mapping[str, str | bytes | Enum]): A dictionary containing the request
            parameters used for routing.
        qualified_enums (bool): Whether to represent enum values
            as their type-qualified symbol names instead of as their
            unqualified symbol names.

    Returns:
        Tuple(str, str): The gRPC metadata containing the routing header key
            and value.
    '''
    return (ROUTING_METADATA_KEY, to_routing_header(params, qualified_enums))

_urlencode_param = (lambda key, value: urlencode({
key: value }, safe = '/'))()
