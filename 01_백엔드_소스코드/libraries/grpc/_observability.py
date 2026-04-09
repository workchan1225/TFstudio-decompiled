# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _observability.pyc (Python 3.11)

from __future__ import annotations
import abc
import contextlib
import logging
import threading
from typing import Any, Generator, Generic, List, Optional, Tuple, TypeVar, Union
from grpc._cython import cygrpc as _cygrpc
from grpc._typing import ChannelArgumentType
_LOGGER = logging.getLogger(__name__)
_channel = Any
ClientCallTracerCapsule = TypeVar('ClientCallTracerCapsule')
ServerCallTracerFactoryCapsule = TypeVar('ServerCallTracerFactoryCapsule')
_plugin_lock: 'threading.RLock' = threading.RLock()
_OBSERVABILITY_PLUGIN: "Optional['ObservabilityPlugin']" = None
_SERVICES_TO_EXCLUDE: 'List[bytes]' = [
    b'google.monitoring.v3.MetricService',
    b'google.devtools.cloudtrace.v2.TraceService']

class ServerCallTracerFactory:
    '''An encapsulation of a ServerCallTracerFactory.

    Instances of this class can be passed to a Channel as values for the
    grpc.experimental.server_call_tracer_factory option
    '''
    
    def __init__(self, address):
        self._address = address

    
    def __int__(self):
        return self._address



def ObservabilityPlugin():
    '''ObservabilityPlugin'''
    __doc__ = 'Abstract base class for observability plugin.\n\n    *This is a semi-private class that was intended for the exclusive use of\n     the gRPC team.*\n\n    The ClientCallTracerCapsule and ClientCallTracerCapsule created by this\n    plugin should be injected to gRPC core using observability_init at the\n    start of a program, before any channels/servers are built.\n\n    Any future methods added to this interface cannot have the\n    @abc.abstractmethod annotation.\n\n    Attributes:\n      _stats_enabled: A bool indicates whether tracing is enabled.\n      _tracing_enabled: A bool indicates whether stats(metrics) is enabled.\n      _registered_methods: A set which stores the registered method names in\n        bytes.\n    '
    _tracing_enabled: 'bool' = False
    _stats_enabled: 'bool' = False
    create_client_call_tracer = (lambda self = None, method_name = None, target = abc.abstractmethod: raise NotImplementedError())()
    save_trace_context = (lambda self = None, trace_id = None, span_id = abc.abstractmethod, is_sampled = ('trace_id', 'str', 'span_id', 'str', 'is_sampled', 'bool', 'return', 'None'): raise NotImplementedError())()
    create_server_call_tracer_factory = (lambda self = None, *, xds: raise NotImplementedError())()
    record_rpc_latency = (lambda self, method = None, target = None, rpc_latency = abc.abstractmethod, status_code = ('method', 'str', 'target', 'str', 'rpc_latency', 'float', 'status_code', 'Any', 'return', 'None'): raise NotImplementedError())()
    
    def set_tracing(self = None, enable = None):
        '''Enable or disable tracing.

        Args:
          enable: A bool indicates whether tracing should be enabled.
        '''
        self._tracing_enabled = enable

    
    def set_stats(self = None, enable = None):
        '''Enable or disable stats(metrics).

        Args:
          enable: A bool indicates whether stats should be enabled.
        '''
        self._stats_enabled = enable

    
    def save_registered_method(self = None, method_name = None):
        """Saves the method name to registered_method list.

        When exporting metrics, method name for unregistered methods will be replaced
        with 'other' by default.

        Args:
          method_name: The method name in bytes.
        """
        raise NotImplementedError()

    tracing_enabled = (lambda self = None: self._tracing_enabled)()
    stats_enabled = (lambda self = None: self._stats_enabled)()
    observability_enabled = (lambda self = None:
