# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numpy_pickle.pyc (Python 3.11)

'''Utilities for fast persistence of big data, with optional compression.'''
import io
import os
import pickle
import warnings
from pathlib import Path
from backports import make_memmap
from compressor import _COMPRESSORS, LZ4_NOT_INSTALLED_ERROR, BinaryZlibFile, BZ2CompressorWrapper, GzipCompressorWrapper, LZ4CompressorWrapper, LZMACompressorWrapper, XZCompressorWrapper, ZlibCompressorWrapper, lz4, register_compressor
from numpy_pickle_compat import NDArrayWrapper, ZNDArrayWrapper, load_compatibility
from numpy_pickle_utils import BUFFER_SIZE, Pickler, Unpickler, _ensure_native_byte_order, _read_bytes, _reconstruct, _validate_fileobject_and_memmap, _write_fileobject
register_compressor('zlib', ZlibCompressorWrapper())
register_compressor('gzip', GzipCompressorWrapper())
register_compressor('bz2', BZ2CompressorWrapper())
register_compressor('lzma', LZMACompressorWrapper())
register_compressor('xz', XZCompressorWrapper())
register_compressor('lz4', LZ4CompressorWrapper())
NUMPY_ARRAY_ALIGNMENT_BYTES = 16

class NumpyArrayWrapper(object):
    """An object to be persisted instead of numpy arrays.

    This object is used to hack into the pickle machinery and read numpy
    array data from our custom persistence format.
    More precisely, this object is used for:
    * carrying the information of the persisted array: subclass, shape, order,
    dtype. Those ndarray metadata are used to correctly reconstruct the array
    with low level numpy functions.
    * determining if memmap is allowed on the array.
    * reading the array bytes from a file.
    * reading the array using memorymap from a file.
    * writing the array bytes to a file.

    Attributes
    ----------
    subclass: numpy.ndarray subclass
        Determine the subclass of the wrapped array.
    shape: numpy.ndarray shape
        Determine the shape of the wrapped array.
    order: {'C', 'F'}
        Determine the order of wrapped array data. 'C' is for C order, 'F' is
        for fortran order.
    dtype: numpy.ndarray dtype
        Determine the data type of the wrapped array.
    allow_mmap: bool
        Determine if memory mapping is allowed on the wrapped array.
        Default: False.
    """
    
    def __init__(self, subclass, shape, order, dtype, allow_mmap, numpy_array_alignment_bytes = (False, NUMPY_ARRAY_ALIGNMENT_BYTES)):
        '''Constructor. Store the useful information for later.'''
        self.subclass = subclass
        self.shape = shape
        self.order = order
        self.dtype = dtype
        self.allow_mmap = allow_mmap
        self.numpy_array_alignment_bytes = numpy_array_alignment_bytes

    
    def safe_get_numpy_array_alignment_bytes(self):
        return getattr(self, 'numpy_array_alignment_bytes', None)

    
    def write_array(self, array, pickler):
        '''Write array bytes to pickler file handle.

        This function is an adaptation of the numpy write_array function
        available in version 1.10.1 in numpy/lib/format.py.
        '''
        buffersize = max(16777216 // array.itemsize, 1)
        if array.dtype.hasobject:
            pickle.dump(array, pickler.file_handle, protocol = 5)
            return None
        numpy_array_alignment_bytes = None.safe_get_numpy_array_alignment_bytes()
    # WARNING: Decompyle incomplete

    
    def read_array(self, unpickler, ensure_native_byte_order):
        '''Read array from unpickler file handle.

        This function is an adaptation of the numpy read_array function
        available in version 1.10.1 in numpy/lib/format.py.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def read_mmap(self, unpickler):
        '''Read an array using numpy memmap.'''
        current_pos = unpickler.file_handle.tell()
        offset = current_pos
        numpy_array_alignment_bytes = self.safe_get_numpy_array_alignment_bytes()
    # WARNING: Decompyle incomplete

    
    def read(self, unpickler, ensure_native_byte_order):
        '''Read the array corresponding to this wrapper.

        Use the unpickler to get all information to correctly read the array.

        Parameters
        ----------
        unpickler: NumpyUnpickler
        ensure_native_byte_order: bool
            If true, coerce the array to use the native endianness of the
            host system.

        Returns
        -------
        array: numpy.ndarray

        '''
        pass
    # WARNING: Decompyle incomplete



class NumpyPickler(Pickler):
    '''A pickler to persist big data efficiently.

    The main features of this object are:
    * persistence of numpy arrays in a single file.
    * optional compression with a special care on avoiding memory copies.

    Attributes
    ----------
    fp: file
        File object handle used for serializing the input object.
    protocol: int, optional
        Pickle protocol used. Default is pickle.DEFAULT_PROTOCOL.
    '''
    dispatch = Pickler.dispatch.copy()
    
    def __init__(self, fp, protocol = (None,)):
        self.file_handle = fp
        self.buffered = isinstance(self.file_handle, BinaryZlibFile)
    # WARNING: Decompyle incomplete

    
    def _create_array_wrapper(self, array):
        '''Create and returns a numpy array wrapper from a numpy array.'''
        order = 'F' if not array.flags.f_contiguous and array.flags.c_contiguous else 'C'
    # WARNING: Decompyle incomplete

    
    def save(self, obj):
        '''Subclass the Pickler `save` method.

        This is a total abuse of the Pickler class in order to use the numpy
        persistence function `save` instead of the default pickle
        implementation. The numpy array is replaced by a custom wrapper in the
        pickle persistence stack and the serialized array is written right
        after in the file. Warning: the file produced does not follow the
        pickle format. As such it can not be read with `pickle.load`.
        '''
        pass
    # WARNING: Decompyle incomplete



class NumpyUnpickler(Unpickler):
    '''A subclass of the Unpickler to unpickle our numpy pickles.

    Attributes
    ----------
    mmap_mode: str
        The memorymap mode to use for reading numpy arrays.
    file_handle: file_like
        File object to unpickle from.
    ensure_native_byte_order: bool
        If True, coerce the array to use the native endianness of the
        host system.
    filename: str
        Name of the file to unpickle from. It should correspond to file_handle.
        This parameter is required when using mmap_mode.
    np: module
        Reference to numpy module if numpy is installed else None.

    '''
    dispatch = Unpickler.dispatch.copy()
    
    def __init__(self, filename, file_handle, ensure_native_byte_order, mmap_mode = (None,)):
        self._dirname = os.path.dirname(filename)
        self.mmap_mode = mmap_mode
        self.file_handle = file_handle
        self.filename = filename
        self.compat_mode = False
        self.ensure_native_byte_order = ensure_native_byte_order
        Unpickler.__init__(self, self.file_handle)
        
        try:
            import numpy as np
        except ImportError:
            np = None

        self.np = np

    
    def load_build(self):
        '''Called to set the state of a newly created object.

        We capture it to replace our place-holder objects, NDArrayWrapper or
        NumpyArrayWrapper, by the array we are interested in. We
        replace them directly in the stack of pickler.
        NDArrayWrapper is used for backward compatibility with joblib <= 0.9.
        '''
        Unpickler.load_build(self)
    # WARNING: Decompyle incomplete

    dispatch[pickle.BUILD[0]] = load_build


def dump(value, filename, compress, protocol = (0, None)):
    """Persist an arbitrary Python object into one file.

    Read more in the :ref:`User Guide <persistence>`.

    Parameters
    ----------
    value: any Python object
        The object to store to disk.
    filename: str, pathlib.Path, or file object.
        The file object or path of the file in which it is to be stored.
        The compression method corresponding to one of the supported filename
        extensions ('.z', '.gz', '.bz2', '.xz' or '.lzma') will be used
        automatically.
    compress: int from 0 to 9 or bool or 2-tuple, optional
        Optional compression level for the data. 0 or False is no compression.
        Higher value means more compression, but also slower read and
        write times. Using a value of 3 is often a good compromise.
        See the notes for more details.
        If compress is True, the compression level used is 3.
        If compress is a 2-tuple, the first element must correspond to a string
        between supported compressors (e.g 'zlib', 'gzip', 'bz2', 'lzma'
        'xz'), the second element must be an integer from 0 to 9, corresponding
        to the compression level.
    protocol: int, optional
        Pickle protocol, see pickle.dump documentation for more details.

    Returns
    -------
    filenames: list of strings
        The list of file names in which the data is stored. If
        compress is false, each array is stored in a different file.

    See Also
    --------
    joblib.load : corresponding loader

    Notes
    -----
    Memmapping on load cannot be used for compressed files. Thus
    using compression can significantly slow down loading. In
    addition, compressed files take up extra memory during
    dump and load.

    """
    pass
# WARNING: Decompyle incomplete


def _unpickle(fobj, ensure_native_byte_order, filename, mmap_mode = ('', None)):
    '''Internal unpickling function.'''
    unpickler = NumpyUnpickler(filename, fobj, ensure_native_byte_order, mmap_mode = mmap_mode)
    obj = None
    
    try:
        obj = unpickler.load()

    return obj


def load_temporary_memmap(filename, mmap_mode, unlink_on_gc_collect):
