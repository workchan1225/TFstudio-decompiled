# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reusable_executor.pyc (Python 3.11)

import time
import warnings
import threading
import multiprocessing as mp
from process_executor import ProcessPoolExecutor, EXTRA_QUEUED_CALLS
from backend.context import cpu_count
from backend import get_context
__all__ = [
    'get_reusable_executor']
_executor_lock = threading.RLock()
_next_executor_id = 0
_executor = None
_executor_kwargs = None

def _get_next_executor_id():
    '''Ensure that each successive executor instance has a unique, monotonic id.

    The purpose of this monotonic id is to help debug and test automated
    instance creation.
    '''
    global _next_executor_id
    _executor_lock
    executor_id = _next_executor_id
    _next_executor_id += 1
    None(None, None)
    return 
    with None:
        if not None, executor_id:
            pass


def get_reusable_executor(max_workers, context, timeout, kill_workers, reuse, job_reducers, result_reducers, initializer, initargs, env = (None, None, 10, False, 'auto', None, None, None, (), None)):
    '''Return the current ReusableExectutor instance.

    Start a new instance if it has not been started already or if the previous
    instance was left in a broken state.

    If the previous instance does not have the requested number of workers, the
    executor is dynamically resized to adjust the number of workers prior to
    returning.

    Reusing a singleton instance spares the overhead of starting new worker
    processes and importing common python packages each time.

    ``max_workers`` controls the maximum number of tasks that can be running in
    parallel in worker processes. By default this is set to the number of
    CPUs on the host.

    Setting ``timeout`` (in seconds) makes idle workers automatically shutdown
    so as to release system resources. New workers are respawn upon submission
    of new tasks so that ``max_workers`` are available to accept the newly
    submitted tasks. Setting ``timeout`` to around 100 times the time required
    to spawn new processes and import packages in them (on the order of 100ms)
    ensures that the overhead of spawning workers is negligible.

    Setting ``kill_workers=True`` makes it possible to forcibly interrupt
    previously spawned jobs to get a new instance of the reusable executor
    with new constructor argument values.

    The ``job_reducers`` and ``result_reducers`` are used to customize the
    pickling of tasks and results send to the executor.

    When provided, the ``initializer`` is run first in newly spawned
    processes with argument ``initargs``.

    The environment variable in the child process are a copy of the values in
    the main process. One can provide a dict ``{ENV: VAL}`` where ``ENV`` and
    ``VAL`` are string literals to overwrite the environment variable ``ENV``
    in the child processes to value ``VAL``. The environment variables are set
    in the children before any module is loaded. This only works with the
    ``loky`` context.
    '''
    (_executor, _) = _ReusablePoolExecutor.get_reusable_executor(max_workers = max_workers, context = context, timeout = timeout, kill_workers = kill_workers, reuse = reuse, job_reducers = job_reducers, result_reducers = result_reducers, initializer = initializer, initargs = initargs, env = env)
    return _executor


class _ReusablePoolExecutor(ProcessPoolExecutor):
    pass
# WARNING: Decompyle incomplete
