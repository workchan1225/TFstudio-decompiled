# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _unbounded_queue.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Generic, TypeVar
import attrs
from  import _core
from _deprecate import deprecated
from _util import final
T = TypeVar('T')
if TYPE_CHECKING:
    from typing_extensions import Self
UnboundedQueueStatistics = <NODE:12>()

def UnboundedQueue():
    '''UnboundedQueue'''
    __doc__ = 'An unbounded queue suitable for certain unusual forms of inter-task\n    communication.\n\n    This class is designed for use as a queue in cases where the producer for\n    some reason cannot be subjected to back-pressure, i.e., :meth:`put_nowait`\n    has to always succeed. In order to prevent the queue backlog from actually\n    growing without bound, the consumer API is modified to dequeue items in\n    "batches". If a consumer task processes each batch without yielding, then\n    this helps achieve (but does not guarantee) an effective bound on the\n    queue\'s memory use, at the cost of potentially increasing system latencies\n    in general. You should generally prefer to use a memory channel\n    instead if you can.\n\n    Currently each batch completely empties the queue, but `this may change in\n    the future <https://github.com/python-trio/trio/issues/51>`__.\n\n    A :class:`UnboundedQueue` object can be used as an asynchronous iterator,\n    where each iteration returns a new batch of items. I.e., these two loops\n    are equivalent::\n\n       async for batch in queue:\n           ...\n\n       while True:\n           obj = await queue.get_batch()\n           ...\n\n    '
    __init__ = (lambda self = None: self._lot = _core.ParkingLot()self._data = []self._can_get = False)()
    
    def __repr__(self = None):
        return f'''<UnboundedQueue holding {len(self._data)} items>'''

    
    def qsize(self = None):
        '''Returns the number of items currently in the queue.'''
        return len(self._data)

    
    def empty(self = None):
        """Returns True if the queue is empty, False otherwise.

        There is some subtlety to interpreting this method's return value: see
        `issue #63 <https://github.com/python-trio/trio/issues/63>`__.

        """
        return not (self._data)

    put_nowait = (lambda self = None, obj = None: pass# WARNING: Decompyle incomplete
)()
    
    def _get_batch_protected(self = None):
        data = self._data.copy()
        self._data.clear()
        self._can_get = False
        return data

    
    def get_batch_nowait(self = None):
        '''Attempt to get the next batch from the queue, without blocking.

        Returns:
          list: A list of dequeued items, in order. On a successful call this
              list is always non-empty; if it would be empty we raise
              :exc:`~trio.WouldBlock` instead.

        Raises:
          ~trio.WouldBlock: if the queue is empty.

        '''
        if not self._can_get:
            raise _core.WouldBlock
        return self._get_batch_protected()

    
    async def get_batch(self = None):
        '''Get the next batch from the queue, blocking as necessary.

        Returns:
          list: A list of dequeued items, in order. This list is always
              non-empty.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def statistics(self = None):
        '''Return an :class:`UnboundedQueueStatistics` object containing debugging information.'''
        return UnboundedQueueStatistics(qsize = len(self._data), tasks_waiting = self._lot.statistics().tasks_waiting)

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete


UnboundedQueue = <NODE:27>(UnboundedQueue, 'UnboundedQueue', Generic[T])()
