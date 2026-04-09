# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: streams.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Generator

class StreamReader:
    """
    Generator-based stream reader.

    This class doesn't support concurrent calls to :meth:`read_line`,
    :meth:`read_exact`, or :meth:`read_to_eof`. Make sure calls are
    serialized.

    """
    
    def __init__(self = None):
        self.buffer = bytearray()
        self.eof = False

    
    def read_line(self = None, m = None):
        '''
        Read a LF-terminated line from the stream.

        This is a generator-based coroutine.

        The return value includes the LF character.

        Args:
            m: Maximum number bytes to read; this is a security limit.

        Raises:
            EOFError: If the stream ends without a LF.
            RuntimeError: If the stream ends in more than ``m`` bytes.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def read_exact(self = None, n = None):
        '''
        Read a given number of bytes from the stream.

        This is a generator-based coroutine.

        Args:
            n: How many bytes to read.

        Raises:
            EOFError: If the stream ends in less than ``n`` bytes.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def read_to_eof(self = None, m = None):
        '''
        Read all bytes from the stream.

        This is a generator-based coroutine.

        Args:
            m: Maximum number bytes to read; this is a security limit.

        Raises:
            RuntimeError: If the stream ends in more than ``m`` bytes.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def at_eof(self = None):
        '''
        Tell whether the stream has ended and all data was read.

        This is a generator-based coroutine.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def feed_data(self = None, data = None):
        '''
        Write data to the stream.

        :meth:`feed_data` cannot be called after :meth:`feed_eof`.

        Args:
            data: Data to write.

        Raises:
            EOFError: If the stream has ended.

        '''
        if self.eof:
            raise EOFError('stream ended')

    
    def feed_eof(self = None):
        '''
        End the stream.

        :meth:`feed_eof` cannot be called more than once.

        Raises:
            EOFError: If the stream has ended.

        '''
        if self.eof:
            raise EOFError('stream ended')
        self.eof = True

    
    def discard(self = None):
        """
        Discard all buffered data, but don't end the stream.

        """
        del self.buffer[:]
