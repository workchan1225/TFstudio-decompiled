# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: queues.pyc (Python 3.11)

import os
import sys
import errno
import weakref
import threading
from multiprocessing import util
from multiprocessing.queues import Full, Queue as mp_Queue, SimpleQueue as mp_SimpleQueue, _sentinel
from multiprocessing.context import assert_spawning
from reduction import dumps
__all__ = [
    'Queue',
    'SimpleQueue',
    'Full']

class Queue(mp_Queue):
    pass
# WARNING: Decompyle incomplete


class SimpleQueue(mp_SimpleQueue):
    pass
# WARNING: Decompyle incomplete
