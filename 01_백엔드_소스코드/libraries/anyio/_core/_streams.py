# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _streams.pyc (Python 3.11)

from __future__ import annotations
import math
from typing import TypeVar
from warnings import warn
from streams.memory import MemoryObjectReceiveStream, MemoryObjectSendStream, _MemoryObjectStreamState
T_Item = TypeVar('T_Item')

def create_memory_object_stream():
    '''create_memory_object_stream'''
    __doc__ = "\n    Create a memory object stream.\n\n    The stream's item type can be annotated like\n    :func:`create_memory_object_stream[T_Item]`.\n\n    :param max_buffer_size: number of items held in the buffer until ``send()`` starts\n        blocking\n    :param item_type: old way of marking the streams with the right generic type for\n        static typing (does nothing on AnyIO 4)\n\n        .. deprecated:: 4.0\n          Use ``create_memory_object_stream[YourItemType](...)`` instead.\n    :return: a tuple of (send stream, receive stream)\n\n    "
    
    def __new__(cls = None, max_buffer_size = None, item_type = None):
        if not max_buffer_size != math.inf and isinstance(max_buffer_size, int):
            raise ValueError('max_buffer_size must be either an integer or math.inf')
        if max_buffer_size < 0:
            raise ValueError('max_buffer_size cannot be negative')
    # WARNING: Decompyle incomplete


create_memory_object_stream = <NODE:27>(create_memory_object_stream, 'create_memory_object_stream', tuple[(MemoryObjectSendStream[T_Item], MemoryObjectReceiveStream[T_Item])])
