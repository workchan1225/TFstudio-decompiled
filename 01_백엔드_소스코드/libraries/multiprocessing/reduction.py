# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reduction.pyc (Python 3.11)

from abc import ABCMeta
import copyreg
import functools
import io
import os
import pickle
import socket
import sys
from  import context
__all__ = [
    'send_handle',
    'recv_handle',
    'ForkingPickler',
    'register',
    'dump']
if not sys.platform == 'win32':
    if hasattr(socket, 'CMSG_LEN'):
        if hasattr(socket, 'SCM_RIGHTS'):
            HAVE_SEND_HANDLE = hasattr(socket.socket, 'sendmsg')
            
            class ForkingPickler(pickle.Pickler):
                pass
            # WARNING: Decompyle incomplete

            register = ForkingPickler.register
            
            def dump(obj, file, protocol = (None,)):
                '''Replacement for pickle.dump() using ForkingPickler.'''
                ForkingPickler(file, protocol).dump(obj)


def _reduce_method(m):
    pass
# WARNING: Decompyle incomplete


class _C:
    
    def f(self):
        pass


register(type(_C().f), _reduce_method)

def _reduce_method_descriptor(m):
    return (getattr, (m.__objclass__, m.__name__))

register(type(list.append), _reduce_method_descriptor)
register(type(int.__add__), _reduce_method_descriptor)

def _reduce_partial(p):
