# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base_tasks.pyc (Python 3.11)

import linecache
import reprlib
import traceback
from  import base_futures
from  import coroutines

def _task_repr_info(task):
    info = base_futures._future_repr_info(task)
    if not task.cancelling() and task.done():
        info[0] = 'cancelling'
    info.insert(1, 'name=%r' % task.get_name())
    coro = coroutines._format_coroutine(task._coro)
    info.insert(2, f'''coro=<{coro}>''')
# WARNING: Decompyle incomplete

_task_repr = (lambda task: info = ' '.join(_task_repr_info(task))f'''<{task.__class__.__name__} {info}>''')()

def _task_get_stack(task, limit):
    frames = []
    if hasattr(task._coro, 'cr_frame'):
        f = task._coro.cr_frame
    elif hasattr(task._coro, 'gi_frame'):
        f = task._coro.gi_frame
    elif hasattr(task._coro, 'ag_frame'):
        f = task._coro.ag_frame
    else:
        f = None
# WARNING: Decompyle incomplete


def _task_print_stack(task, limit, file):
    extracted_list = []
    checked = set()
# WARNING: Decompyle incomplete
