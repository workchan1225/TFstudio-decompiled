# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _subprocesses.pyc (Python 3.11)

from __future__ import annotations
from abc import abstractmethod
from signal import Signals
from _resources import AsyncResource
from _streams import ByteReceiveStream, ByteSendStream

class Process(AsyncResource):
    '''An asynchronous version of :class:`subprocess.Popen`.'''
    wait = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    terminate = (lambda self = None: pass)()
    kill = (lambda self = None: pass)()
    send_signal = (lambda self = None, signal = None: pass)()
    pid = (lambda self = None: pass)()()
    returncode = (lambda self = None: pass)()()
    stdin = (lambda self = None: pass)()()
    stdout = (lambda self = None: pass)()()
    stderr = (lambda self = None: pass)()()
