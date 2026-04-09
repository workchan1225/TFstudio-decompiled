# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: compression.pyc (Python 3.11)

'''Helper functions for a standard streaming compression API'''
from zipfile import ZipFile
import fsspec.utils as fsspec
from fsspec.spec import AbstractBufferedFile

def noop_file(file, mode, **kwargs):
    return file

compr = {
    None: noop_file }

def register_compression(name, callback, extensions, force = (False,)):
    '''Register an "inferable" file compression type.

    Registers transparent file compression type for use with fsspec.open.
    Compression can be specified by name in open, or "infer"-ed for any files
    ending with the given extensions.

    Args:
        name: (str) The compression type name. Eg. "gzip".
        callback: A callable of form (infile, mode, **kwargs) -> file-like.
            Accepts an input file-like object, the target mode and kwargs.
            Returns a wrapped file-like object.
        extensions: (str, Iterable[str]) A file extension, or list of file
            extensions for which to infer this compression scheme. Eg. "gz".
        force: (bool) Force re-registration of compression type or extensions.

    Raises:
        ValueError: If name or extensions already registered, and not force.

    '''
    if isinstance(extensions, str):
        extensions = [
            extensions]
    if not name in compr and force:
        raise ValueError(f'''Duplicate compression registration: {name}''')
    for ext in extensions:
        if not ext in fsspec.utils.compressions and force:
            raise ValueError(f'''Duplicate compression file extension: {ext} ({name})''')
        compr[name] = callback
        for ext in extensions:
            fsspec.utils.compressions[ext] = name
            return None


def unzip(infile, mode, filename = ('rb', None), **kwargs):
    pass
# WARNING: Decompyle incomplete

register_compression('zip', unzip, 'zip')

try:
    from bz2 import BZ2File
    register_compression('bz2', BZ2File, 'bz2')
except ImportError:
    pass


try:
    from isal import igzip
    
    def isal(infile, mode = ('rb',), **kwargs):
        pass
    # WARNING: Decompyle incomplete

    register_compression('gzip', isal, 'gz')
except ImportError:
    from gzip import GzipFile
    register_compression('gzip', (lambda f: pass# WARNING: Decompyle incomplete
), 'gz')


try:
    from lzma import LZMAFile
    register_compression('lzma', LZMAFile, 'lzma')
    register_compression('xz', LZMAFile, 'xz')
except ImportError:
    pass


try:
    import lzmaffi
    register_compression('lzma', lzmaffi.LZMAFile, 'lzma', force = True)
    register_compression('xz', lzmaffi.LZMAFile, 'xz', force = True)
except ImportError:
    pass


class SnappyFile(AbstractBufferedFile):
    pass
# WARNING: Decompyle incomplete


try:
    import snappy
    snappy.compress(b'')
    register_compression('snappy', SnappyFile, [])
except (ImportError, NameError, AttributeError):
    pass


try:
    import lz4.frame as lz4
    register_compression('lz4', lz4.frame.open, 'lz4')
except ImportError:
    pass


try:
    from compression.zstd import ZstdFile
    register_compression('zstd', ZstdFile, 'zst')
except ImportError:
    import zstandard as zstd
    
    def zstandard_file(infile, mode = ('rb',)):
        if 'r' in mode:
            cctx = zstd.ZstdDecompressor()
            return cctx.stream_reader(infile)
        cctx = None.ZstdCompressor(level = 10)
        return cctx.stream_writer(infile)

    register_compression('zstd', zstandard_file, 'zst')
except ImportError:
    pass


def available_compressions():
    '''Return a list of the implemented compressions.'''
    return list(compr)
