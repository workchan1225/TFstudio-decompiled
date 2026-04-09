# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base_call.pyc (Python 3.11)

'''Abstract base classes for client-side Call objects.

Call objects represents the RPC itself, and offer methods to access / modify
its information. They also offer methods to manipulate the life-cycle of the
RPC, e.g. cancellation.
'''
from abc import ABCMeta
from abc import abstractmethod
from typing import Any, AsyncIterator, Generator, Generic, Optional, Union
import grpc
from _metadata import Metadata
from _typing import DoneCallbackType
from _typing import EOFType
from _typing import RequestType
from _typing import ResponseType
__all__ = ('RpcContext', 'Call', 'UnaryUnaryCall', 'UnaryStreamCall')

def RpcContext():
    '''RpcContext'''
    __doc__ = 'Provides RPC-related information and action.'
    cancelled = (lambda self = None: pass)()
    done = (lambda self = None: pass)()
    time_remaining = (lambda self = None: pass)()
    cancel = (lambda self = None: pass)()
    add_done_callback = (lambda self = None, callback = None: pass)()

RpcContext = <NODE:27>(RpcContext, 'RpcContext', metaclass = ABCMeta)

def Call():
    '''Call'''
    __doc__ = 'The abstract base class of an RPC on the client-side.'
    initial_metadata = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    trailing_metadata = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    code = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    details = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    wait_for_connection = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

Call = <NODE:27>(Call, 'Call', RpcContext, metaclass = ABCMeta)

def UnaryUnaryCall():
    '''UnaryUnaryCall'''
    __doc__ = 'The abstract base class of a unary-unary RPC on the client-side.'
    __await__ = (lambda self = None: pass)()

UnaryUnaryCall = <NODE:27>(UnaryUnaryCall, 'UnaryUnaryCall', Generic[(RequestType, ResponseType)], Call, metaclass = ABCMeta)

def UnaryStreamCall():
    '''UnaryStreamCall'''
    __aiter__ = (lambda self = None: pass)()
    read = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

UnaryStreamCall = <NODE:27>(UnaryStreamCall, 'UnaryStreamCall', Generic[(RequestType, ResponseType)], Call, metaclass = ABCMeta)

def StreamUnaryCall():
    '''StreamUnaryCall'''
    write = (lambda self = None, request = None: pass# WARNING: Decompyle incomplete
)()
    done_writing = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    __await__ = (lambda self = None: pass)()

StreamUnaryCall = <NODE:27>(StreamUnaryCall, 'StreamUnaryCall', Generic[(RequestType, ResponseType)], Call, metaclass = ABCMeta)

def StreamStreamCall():
    '''StreamStreamCall'''
    __aiter__ = (lambda self = None: pass)()
    read = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    write = (lambda self = None, request = None: pass# WARNING: Decompyle incomplete
)()
    done_writing = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

StreamStreamCall = <NODE:27>(StreamStreamCall, 'StreamStreamCall', Generic[(RequestType, ResponseType)], Call, metaclass = ABCMeta)
