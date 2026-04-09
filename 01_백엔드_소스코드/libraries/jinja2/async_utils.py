# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: async_utils.pyc (Python 3.11)

import inspect
import typing as t
from functools import WRAPPER_ASSIGNMENTS
from functools import wraps
from utils import _PassArg
from utils import pass_eval_context
if t.TYPE_CHECKING:
    import typing_extensions as te
V = t.TypeVar('V')

def async_variant(normal_func):
    pass
# WARNING: Decompyle incomplete

_common_primitives = {
    int,
    float,
    bool,
    str,
    list,
    dict,
    tuple,
    type(None)}

async def auto_await(value = None):
    pass
# WARNING: Decompyle incomplete


def _IteratorToAsyncIterator():
    '''_IteratorToAsyncIterator'''
    
    def __init__(self = None, iterator = None):
        self._iterator = iterator

    
    def __aiter__(self = None):
        return self

    
    async def __anext__(self = None):
        pass
    # WARNING: Decompyle incomplete


_IteratorToAsyncIterator = <NODE:27>(_IteratorToAsyncIterator, '_IteratorToAsyncIterator', t.Generic[V])

def auto_aiter(iterable = None):
    if hasattr(iterable, '__aiter__'):
        return iterable.__aiter__()
    return None(iter(iterable))


async def auto_to_list(value = None):
    pass
# WARNING: Decompyle incomplete
