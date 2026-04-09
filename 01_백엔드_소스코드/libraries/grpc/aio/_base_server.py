# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base_server.pyc (Python 3.11)

'''Abstract base classes for server-side classes.'''
import abc
from typing import Generic, Iterable, Mapping, NoReturn, Optional, Sequence
import grpc
from _metadata import Metadata
from _typing import DoneCallbackType
from _typing import MetadataType
from _typing import RequestType
from _typing import ResponseType

class Server(abc.ABC):
    '''Serves RPCs.'''
    add_generic_rpc_handlers = (lambda self = None, generic_rpc_handlers = None: pass)()
    add_insecure_port = (lambda self = None, address = None: pass)()
    add_secure_port = (lambda self = None, address = None, server_credentials = abc.abstractmethod: pass)()
    start = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    stop = (lambda self = None, grace = None: pass# WARNING: Decompyle incomplete
)()
    wait_for_termination = (lambda self = None, timeout = None: pass# WARNING: Decompyle incomplete
)()
    
    def add_registered_method_handlers(self, service_name, method_handlers):
        '''Registers GenericRpcHandlers with this Server.

        This method is only safe to call before the server is started.

        Args:
          service_name: The service name.
          method_handlers: A dictionary that maps method names to corresponding
            RpcMethodHandler.
        '''
        pass



def ServicerContext():
    '''ServicerContext'''
    __doc__ = 'A context object passed to method implementations.'
    read = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    write = (lambda self = None, message = None: pass# WARNING: Decompyle incomplete
)()
    send_initial_metadata = (lambda self = None, initial_metadata = None: pass# WARNING: Decompyle incomplete
)()
    abort = (lambda self = None, code = None, details = abc.abstractmethod, trailing_metadata = ('', ()): pass# WARNING: Decompyle incomplete
)()
    set_trailing_metadata = (lambda self = None, trailing_metadata = None: pass)()
    invocation_metadata = (lambda self = None: pass)()
    set_code = (lambda self = None, code = None: pass)()
    set_details = (lambda self = None, details = None: pass)()
    set_compression = (lambda self = None, compression = None: pass)()
    disable_next_message_compression = (lambda self = None: pass)()
    peer = (lambda self = None: pass)()
    peer_identities = (lambda self = None: pass)()
    peer_identity_key = (lambda self = None: pass)()
    auth_context = (lambda self = None: pass)()
    
    def time_remaining(self = None):
        '''Describes the length of allowed time remaining for the RPC.

        Returns:
          A nonnegative float indicating the length of allowed time in seconds
          remaining for the RPC to complete before it is considered to have
          timed out, or None if no deadline was specified for the RPC.
        '''
        pass

    
    def trailing_metadata(self):
        '''Access value to be used as trailing metadata upon RPC completion.

        This is an EXPERIMENTAL API.

        Returns:
          The trailing :term:`metadata` for the RPC.
        '''
        raise NotImplementedError()

    
    def code(self):
        '''Accesses the value to be used as status code upon RPC completion.

        This is an EXPERIMENTAL API.

        Returns:
          The StatusCode value for the RPC.
        '''
        raise NotImplementedError()

    
    def details(self):
        '''Accesses the value to be used as detail string upon RPC completion.

        This is an EXPERIMENTAL API.

        Returns:
          The details string of the RPC.
        '''
        raise NotImplementedError()

    
    def add_done_callback(self = None, callback = None):
        '''Registers a callback to be called on RPC termination.

        This is an EXPERIMENTAL API.

        Args:
          callback: A callable object will be called with the servicer context
            object as its only argument.
        '''
        pass

    
    def cancelled(self = None):
        '''Return True if the RPC is cancelled.

        The RPC is cancelled when the cancellation was requested with cancel().

        This is an EXPERIMENTAL API.

        Returns:
          A bool indicates whether the RPC is cancelled or not.
        '''
        pass

    
    def done(self = None):
        '''Return True if the RPC is done.

        An RPC is done if the RPC is completed, cancelled or aborted.

        This is an EXPERIMENTAL API.

        Returns:
          A bool indicates if the RPC is done.
        '''
        pass


ServicerContext = <NODE:27>(ServicerContext, 'ServicerContext', Generic[(RequestType, ResponseType)], abc.ABC)
