# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: messages.pyc (Python 3.11)

from __future__ import annotations
import codecs
import queue
import threading
from typing import Any, Callable, Iterable, Iterator, Literal, overload
from exceptions import ConcurrencyError
from frames import OP_BINARY, OP_CONT, OP_TEXT, Frame
from typing import Data
from utils import Deadline
__all__ = [
    'Assembler']
UTF8Decoder = codecs.getincrementaldecoder('utf-8')

class Assembler:
    """
    Assemble messages from frames.

    :class:`Assembler` expects only data frames. The stream of frames must
    respect the protocol; if it doesn't, the behavior is undefined.

    Args:
        pause: Called when the buffer of frames goes above the high water mark;
            should pause reading from the network.
        resume: Called when the buffer of frames goes below the low water mark;
            should resume reading from the network.

    """
    
    def __init__(self = None, high = None, low = None, pause = (None, None, (lambda : pass), (lambda : pass)), resume = ('high', 'int | None', 'low', 'int | None', 'pause', 'Callable[[], Any]', 'resume', 'Callable[[], Any]', 'return', 'None')):
        self.mutex = threading.Lock()
        self.frames = queue.SimpleQueue()
    # WARNING: Decompyle incomplete

    
    def get_next_frame(self = None, timeout = None):
        pass
    # WARNING: Decompyle incomplete

    
    def reset_queue(self = None, frames = None):
        self.mutex
        queued = []
        queued.append(self.frames.get(block = False))
        continue
        except queue.Empty:
            pass
        for frame in frames:
            self.frames.put(frame)
            for frame in queued:
                self.frames.put(frame)
                None(None, None)
                return None
                with None:
                    if not None:
                        pass

    get = (lambda self = None, timeout = None, decode = overload: pass)()
    get = (lambda self = None, timeout = None, decode = overload: pass)()
    get = (lambda self = None, timeout = None, *, decode,
