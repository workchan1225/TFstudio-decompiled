# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: brotli.pyc (Python 3.11)

'''Functions to compress and decompress data using the Brotli library.'''
import _brotli
version = _brotli.__version__
__version__ = _brotli.__version__
MODE_GENERIC = _brotli.MODE_GENERIC
MODE_TEXT = _brotli.MODE_TEXT
MODE_FONT = _brotli.MODE_FONT
Compressor = _brotli.Compressor
Decompressor = _brotli.Decompressor

def compress(string, mode, quality, lgwin, lgblock = (MODE_GENERIC, 11, 22, 0)):
    '''Compress a byte string.

    Args:
      string (bytes): The input data.
      mode (int, optional): The compression mode; value 0 should be used for
        generic input (MODE_GENERIC); value 1 might be beneficial for UTF-8 text
        input (MODE_TEXT); value 2 tunes encoder for WOFF 2.0 data (MODE_FONT).
        Defaults to 0.
      quality (int, optional): Controls the compression-speed vs compression-
        density tradeoff. The higher the quality, the slower the compression.
        Range is 0 to 11. Defaults to 11.
      lgwin (int, optional): Base 2 logarithm of the sliding window size. Range
        is 10 to 24. Defaults to 22.
      lgblock (int, optional): Base 2 logarithm of the maximum input block size.
        Range is 16 to 24. If set to 0, the value will be set based on the
        quality. Defaults to 0.

    Returns:
      The compressed byte string.

    Raises:
      brotli.error: If arguments are invalid, or compressor fails.
    '''
    compressor = Compressor(mode = mode, quality = quality, lgwin = lgwin, lgblock = lgblock)
    return compressor.process(string) + compressor.finish()

decompress = _brotli.decompress
error = _brotli.error
