# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: file_proxy.pyc (Python 3.11)

import io
from typing import IO, TYPE_CHECKING, Any, List
from ansi import AnsiDecoder
from text import Text
if TYPE_CHECKING:
    from console import Console

class FileProxy(io.TextIOBase):
    '''Wraps a file (e.g. sys.stdout) and redirects writes to a console.'''
    
    def __init__(self = None, console = None, file = None):
        self._FileProxy__console = console
        self._FileProxy__file = file
        self._FileProxy__buffer = []
        self._FileProxy__ansi_decoder = AnsiDecoder()

    rich_proxied_file = (lambda self = None: self._FileProxy__file)()
    
    def __getattr__(self = None, name = None):
        return getattr(self._FileProxy__file, name)

    
    def write(self = None, text = None):
        pass
    # WARNING: Decompyle incomplete

    
    def flush(self = None):
        output = ''.join(self._FileProxy__buffer)
        if output:
            self._FileProxy__console.print(output)
        del self._FileProxy__buffer[:]

    
    def fileno(self = None):
        return self._FileProxy__file.fileno()
