# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _plugin_wrapping.pyc (Python 3.11)

import collections
import logging
import threading
from typing import Callable, Optional, Type
import grpc
from grpc import _common
from grpc._cython import cygrpc
from grpc._typing import MetadataType
_LOGGER = logging.getLogger(__name__)

def _AuthMetadataContext():
    '''_AuthMetadataContext'''
    pass

_AuthMetadataContext = <NODE:27>(_AuthMetadataContext, '_AuthMetadataContext', collections.namedtuple('AuthMetadataContext', ('service_url', 'method_name')), grpc.AuthMetadataContext)

class _CallbackState(object):
    
    def __init__(self):
        self.lock = threading.Lock()
        self.called = False
        self.exception = None



class _AuthMetadataPluginCallback(grpc.AuthMetadataPluginCallback):
    _callback: Callable = '_AuthMetadataPluginCallback'
    
    def __init__(self = None, state = None, callback = None):
        self._state = state
        self._callback = callback

    
    def __call__(self = None, metadata = None, error = None):
        self._state.lock
    # WARNING: Decompyle incomplete



class _Plugin(object):
    _metadata_plugin: grpc.AuthMetadataPlugin = '_Plugin'
    
    def __init__(self = None, metadata_plugin = None):
        self._metadata_plugin = metadata_plugin
        self._stored_ctx = None
        
        try:
            import contextvars
            self._stored_ctx = contextvars.copy_context()
            return None
        except ImportError:
            return None


    
    def __call__(self = None, service_url = None, method_name = None, callback = ('service_url', str, 'method_name', str, 'callback', Callable)):
        context = _AuthMetadataContext(_common.decode(service_url), _common.decode(method_name))
        callback_state = _CallbackState()
        
        try:
            self._metadata_plugin(context, _AuthMetadataPluginCallback(callback_state, callback))
            return None
        except Exception:
            exception = None
            _LOGGER.exception('AuthMetadataPluginCallback "%s" raised exception!', self._metadata_plugin)
            callback_state.lock
            callback_state.exception = exception
            if callback_state.called:
                None(None, None)
                exception = None
                del exception
                return None
            None(None, None)
        except:
            with None:
                if not None:
                    pass

        callback(None, cygrpc.StatusCode.internal, _common.encode(str(exception)))
        exception = None
        del exception
        return None
        exception = None
        del exception



def metadata_plugin_call_credentials(metadata_plugin = None, name = None):
    pass
# WARNING: Decompyle incomplete
