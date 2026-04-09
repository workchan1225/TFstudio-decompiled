# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _common.pyc (Python 3.11)

__doc__ = 'Shared implementation.'
import logging
import time
from typing import Any, AnyStr, Callable, Optional, Union
import grpc
from grpc._cython import cygrpc
from grpc._typing import DeserializingFunction
from grpc._typing import SerializingFunction
_LOGGER = logging.getLogger(__name__)
CYGRPC_CONNECTIVITY_STATE_TO_CHANNEL_CONNECTIVITY = {
    cygrpc.ConnectivityState.shutdown: grpc.ChannelConnectivity.SHUTDOWN,
    cygrpc.ConnectivityState.transient_failure: grpc.ChannelConnectivity.TRANSIENT_FAILURE,
    cygrpc.ConnectivityState.ready: grpc.ChannelConnectivity.READY,
    cygrpc.ConnectivityState.connecting: grpc.ChannelConnectivity.CONNECTING,
    cygrpc.ConnectivityState.idle: grpc.ChannelConnectivity.IDLE }
# WARNING: Decompyle incomplete
