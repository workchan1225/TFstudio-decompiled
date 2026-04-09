# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _receivebuffer.pyc (Python 3.11)

import re
import sys
from typing import List, Optional, Union
__all__ = [
    'ReceiveBuffer']
blank_line_regex = re.compile(b'\n\r?\n', re.MULTILINE)

class ReceiveBuffer:
    
    def __init__(self = None):
        self._data = bytearray()
        self._next_line_search = 0
        self._multiple_lines_search = 0

    
    def __iadd__(self = None, byteslike = None):
        return self

    
    def __bool__(self = None):
        return bool(len(self))

    
    def __len__(self = None):
        return len(self._data)

    
    def __bytes__(self = None):
        return bytes(self._data)

    
    def _extract(self = None, count = None):
        out = self._data[:count]
        del self._data[:count]
        self._next_line_search = 0
        self._multiple_lines_search = 0
        return out

    
    def maybe_extract_at_most(self = None, count = None):
        '''
        Extract a fixed number of bytes from the buffer.
        '''
        out = self._data[:count]
        if not out:
            return None
        return None._extract(count)

    
    def maybe_extract_next_line(self = None):
        '''
        Extract the first line, if it is completed in the buffer.
        '''
        search_start_index = max(0, self._next_line_search - 1)
        partial_idx = self._data.find(b'\r\n', search_start_index)
        if partial_idx == -1:
            self._next_line_search = len(self._data)
            return None
        idx = None + 2
        return self._extract(idx)

    
    def maybe_extract_lines(self = None):
        '''
        Extract everything up to the first blank line, and return a list of lines.
        '''
        if self._data[:1] == b'\n':
            self._extract(1)
            return []
        if None._data[:2] == b'\r\n':
            self._extract(2)
            return []
        match = None.search(self._data, self._multiple_lines_search)
    # WARNING: Decompyle incomplete

    
    def is_next_line_obviously_invalid_request_line(self = None):
        
        try:
            return self._data[0] < 33
        except IndexError:
            return False
