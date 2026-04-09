# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: config.pyc (Python 3.11)

'''Helpers for loading gapic configuration data.

The Google API generator creates supplementary configuration for each RPC
method to tell the client library how to deal with retries and timeouts.
'''
import collections
import grpc
from google.api_core import exceptions
from google.api_core import retry
from google.api_core import timeout
_MILLIS_PER_SECOND = 1000

def _exception_class_for_grpc_status_name(name):
    '''Returns the Google API exception class for a gRPC error code name.

    DEPRECATED: use ``exceptions.exception_class_for_grpc_status`` method
    directly instead.

    Args:
        name (str): The name of the gRPC status code, for example,
            ``UNAVAILABLE``.

    Returns:
        :func:`type`: The appropriate subclass of
            :class:`google.api_core.exceptions.GoogleAPICallError`.
    '''
    return exceptions.exception_class_for_grpc_status(getattr(grpc.StatusCode, name))


def _retry_from_retry_config(retry_params, retry_codes, retry_impl = (retry.Retry,)):
    '''Creates a Retry object given a gapic retry configuration.

    DEPRECATED: instantiate retry and timeout classes directly instead.

    Args:
        retry_params (dict): The retry parameter values, for example::

            {
                "initial_retry_delay_millis": 1000,
                "retry_delay_multiplier": 2.5,
                "max_retry_delay_millis": 120000,
                "initial_rpc_timeout_millis": 120000,
                "rpc_timeout_multiplier": 1.0,
                "max_rpc_timeout_millis": 120000,
                "total_timeout_millis": 600000
            }

        retry_codes (sequence[str]): The list of retryable gRPC error code
            names.

    Returns:
        google.api_core.retry.Retry: The default retry object for the method.
    '''
    exception_classes = retry_codes()
# WARNING: Decompyle incomplete


def _timeout_from_retry_config(retry_params):
    '''Creates a ExponentialTimeout object given a gapic retry configuration.

    DEPRECATED: instantiate retry and timeout classes directly instead.

    Args:
        retry_params (dict): The retry parameter values, for example::

            {
                "initial_retry_delay_millis": 1000,
                "retry_delay_multiplier": 2.5,
                "max_retry_delay_millis": 120000,
                "initial_rpc_timeout_millis": 120000,
                "rpc_timeout_multiplier": 1.0,
                "max_rpc_timeout_millis": 120000,
                "total_timeout_millis": 600000
            }

    Returns:
        google.api_core.retry.ExponentialTimeout: The default time object for
            the method.
    '''
    return timeout.ExponentialTimeout(initial = retry_params['initial_rpc_timeout_millis'] / _MILLIS_PER_SECOND, maximum = retry_params['max_rpc_timeout_millis'] / _MILLIS_PER_SECOND, multiplier = retry_params['rpc_timeout_multiplier'], deadline = retry_params['total_timeout_millis'] / _MILLIS_PER_SECOND)

MethodConfig = collections.namedtuple('MethodConfig', [
    'retry',
    'timeout'])

def parse_method_configs(interface_config, retry_impl = (retry.Retry,)):
    """Creates default retry and timeout objects for each method in a gapic
    interface config.

    DEPRECATED: instantiate retry and timeout classes directly instead.

    Args:
        interface_config (Mapping): The interface config section of the full
            gapic library config. For example, If the full configuration has
            an interface named ``google.example.v1.ExampleService`` you would
            pass in just that interface's configuration, for example
            ``gapic_config['interfaces']['google.example.v1.ExampleService']``.
        retry_impl (Callable): The constructor that creates a retry decorator
            that will be applied to the method based on method configs.

    Returns:
        Mapping[str, MethodConfig]: A mapping of RPC method names to their
            configuration.
    """
    retry_codes_map = interface_config.get('retry_codes', { }).items()()
    retry_params_map = interface_config.get('retry_params', { }).items()()
    method_configs = { }
# WARNING: Decompyle incomplete
