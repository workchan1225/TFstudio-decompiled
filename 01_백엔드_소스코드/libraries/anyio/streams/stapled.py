# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: stapled.pyc (Python 3.11)

from __future__ import annotations
__all__ = ('MultiListener', 'StapledByteStream', 'StapledObjectStream')
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass
from typing import Any, Generic, TypeVar
from abc import ByteReceiveStream, ByteSendStream, ByteStream, Listener, ObjectReceiveStream, ObjectSendStream, ObjectStream, TaskGroup
T_Item = TypeVar('T_Item')
T_Stream = TypeVar('T_Stream')
StapledByteStream = <NODE:12>()

def StapledObjectStream():
    '''StapledObjectStream'''
    receive_stream: 'ObjectReceiveStream[T_Item]' = '\n    Combines two object streams into a single, bidirectional object stream.\n\n    Extra attributes will be provided from both streams, with the receive stream\n    providing the values in case of a conflict.\n\n    :param ObjectSendStream send_stream: the sending object stream\n    :param ObjectReceiveStream receive_stream: the receiving object stream\n    '
    
    async def receive(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send(self = None, item = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def send_eof(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    extra_attributes = (lambda self = None: pass# WARNING: Decompyle incomplete
)()

StapledObjectStream = <NODE:27>(StapledObjectStream, 'StapledObjectStream', Generic[T_Item], ObjectStream[T_Item])()

def MultiListener():
    '''MultiListener'''
    listeners: 'Sequence[Listener[T_Stream]]' = '\n    Combines multiple listeners into one, serving connections from all of them at once.\n\n    Any MultiListeners in the given collection of listeners will have their listeners\n    moved into this one.\n\n    Extra attributes are provided from each listener, with each successive listener\n    overriding any conflicting attributes from the previous one.\n\n    :param listeners: listeners to serve\n    :type listeners: Sequence[Listener[T_Stream]]\n    '
    
    def __post_init__(self = None):
        listeners = []
        for listener in self.listeners:
            if isinstance(listener, MultiListener):
                listeners.extend(listener.listeners)
                del listener.listeners[:]
                continue
            listeners.append(listener)
            self.listeners = listeners
            return None

    
    async def serve(self = None, handler = None, task_group = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete

    extra_attributes = (lambda self = None: attributes = { }for listener in self.listeners:
attributes.update(listener.extra_attributes)attributes)()

MultiListener = <NODE:27>(MultiListener, 'MultiListener', Generic[T_Stream], Listener[T_Stream])()
