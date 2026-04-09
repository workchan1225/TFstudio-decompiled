# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: heapq.pyc (Python 3.11)

import heapq as hq
from numba.core import types
from numba.core.errors import TypingError
from numba.core.extending import overload, register_jitable
_siftdown = (lambda heap, startpos, pos: newitem = heap[pos]if pos > startpos:
parentpos = pos - 1 >> 1parent = heap[parentpos]if newitem < parent:
heap[pos] = parentpos = parentposcontinueheap[pos] = newitem)()
_siftup = (lambda heap, pos: endpos = len(heap)startpos = posnewitem = heap[pos]childpos = 2 * pos + 1# WARNING: Decompyle incomplete
)()
_siftdown_max = (lambda heap, startpos, pos: newitem = heap[pos]if pos > startpos:
parentpos = pos - 1 >> 1parent = heap[parentpos]if parent < newitem:
heap[pos] = parentpos = parentposcontinueheap[pos] = newitem)()
_siftup_max = (lambda heap, pos: endpos = len(heap)startpos = posnewitem = heap[pos]childpos = 2 * pos + 1# WARNING: Decompyle incomplete
)()
reversed_range = (lambda x: range(x - 1, -1, -1))()
_heapify_max = (lambda x: n = len(x)for i in reversed_range(n // 2):
_siftup_max(x, i)None)()
_heapreplace_max = (lambda heap, item: returnitem = heap[0]heap[0] = item_siftup_max(heap, 0)returnitem)()

def assert_heap_type(heap):
    if not isinstance(heap, (types.List, types.ListType)):
        raise TypingError('heap argument must be a list')
    dt = heap.dtype
    if isinstance(dt, types.Complex):
        msg = "'<' not supported between instances of 'complex' and 'complex'"
        raise TypingError(msg)


def assert_item_type_consistent_with_heap_type(heap, item):
    if not heap.dtype == item:
        raise TypingError('heap type must be the same as item type')

hq_heapify = (lambda x: assert_heap_type(x)
def hq_heapify_impl(x):
n = len(x)for i in reversed_range(n // 2):
_siftup(x, i)Nonehq_heapify_impl)()
hq_heappop = (lambda heap: assert_heap_type(heap)
def hq_heappop_impl(heap):
lastelt = heap.pop()if heap:
returnitem = heap[0]heap[0] = lastelt_siftup(heap, 0)returnitemhq_heappop_impl)()
heappush = (lambda heap, item: assert_heap_type(heap)assert_item_type_consistent_with_heap_type(heap, item)
def hq_heappush_impl(heap, item):
heap.append(item)_siftdown(heap, 0, len(heap) - 1)hq_heappush_impl)()
heapreplace = (lambda heap, item: assert_heap_type(heap)assert_item_type_consistent_with_heap_type(heap, item)
def hq_heapreplace(heap, item):
returnitem = heap[0]heap[0] = item_siftup(heap, 0)returnitemhq_heapreplace)()
heappushpop = (lambda heap, item: assert_heap_type(heap)assert_item_type_consistent_with_heap_type(heap, item)
def hq_heappushpop_impl(heap, item):
if heap and heap[0] < item:
item, heap[0] = heap[0], item_siftup(heap, 0)itemhq_heappushpop_impl)()

def check_input_types(n, iterable):
    if not isinstance(n, (types.Integer, types.Boolean)):
        raise TypingError("First argument 'n' must be an integer")
    if not isinstance(iterable, (types.Sequence, types.Array, types.ListType)):
        raise TypingError("Second argument 'iterable' must be iterable")

nsmallest = (lambda n, iterable: check_input_types(n, iterable)
def hq_nsmallest_impl(n, iterable):
pass# WARNING: Decompyle incomplete
hq_nsmallest_impl)()
nlargest = (lambda n, iterable: check_input_types(n, iterable)
def hq_nlargest_impl(n, iterable):
pass# WARNING: Decompyle incomplete
hq_nlargest_impl)()
