# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _base.pyc (Python 3.11)

from concurrent.futures import Future as _BaseFuture
from concurrent.futures._base import LOGGER

class Future(_BaseFuture):
    
    def _invoke_callbacks(self):
        for callback in self._done_callbacks:
            callback(self)
            except BaseException:
                LOGGER.exception(f'''exception calling callback for {self!r}''')
                continue
            return None
