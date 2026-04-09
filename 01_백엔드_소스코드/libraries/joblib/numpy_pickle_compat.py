# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: numpy_pickle_compat.pyc (Python 3.11)

'''Numpy pickle compatibility functions.'''
import inspect
import os
import pickle
import zlib
from io import BytesIO
from numpy_pickle_utils import _ZFILE_PREFIX, Unpickler, _ensure_native_byte_order, _reconstruct

def hex_str(an_int):
    '''Convert an int to an hexadecimal string.'''
    return '{:#x}'.format(an_int)


def asbytes(s):
    if isinstance(s, bytes):
        return s
    return None.encode('latin1')

_MAX_LEN = len(hex_str(0x10000000000000000))
_CHUNK_SIZE = 65536

def read_zfile(file_handle):
    '''Read the z-file and return the content as a string.

    Z-files are raw data compressed with zlib used internally by joblib
    for persistence. Backward compatibility is not guaranteed. Do not
    use for external purposes.
    '''
    file_handle.seek(0)
    header_length = len(_ZFILE_PREFIX) + _MAX_LEN
    length = file_handle.read(header_length)
    length = length[len(_ZFILE_PREFIX):]
    length = int(length, 16)
    next_byte = file_handle.read(1)
    if next_byte != b' ':
        file_handle.seek(header_length)
    data = zlib.decompress(file_handle.read(), 15, length)
# WARNING: Decompyle incomplete


def write_zfile(file_handle, data, compress = (1,)):
    '''Write the data in the given file as a Z-file.

    Z-files are raw data compressed with zlib used internally by joblib
    for persistence. Backward compatibility is not guaranteed. Do not
    use for external purposes.
    '''
    file_handle.write(_ZFILE_PREFIX)
    length = hex_str(len(data))
    file_handle.write(asbytes(length.ljust(_MAX_LEN)))
    file_handle.write(zlib.compress(asbytes(data), compress))


class NDArrayWrapper(object):
    '''An object to be persisted instead of numpy arrays.

    The only thing this object does, is to carry the filename in which
    the array has been persisted, and the array subclass.
    '''
    
    def __init__(self, filename, subclass, allow_mmap = (True,)):
        '''Constructor. Store the useful information for later.'''
        self.filename = filename
        self.subclass = subclass
        self.allow_mmap = allow_mmap

    
    def read(self, unpickler):
        '''Reconstruct the array.'''
        filename = os.path.join(unpickler._dirname, self.filename)
        allow_mmap = getattr(self, 'allow_mmap', True)
        kwargs = { }
        if allow_mmap:
            kwargs['mmap_mode'] = unpickler.mmap_mode
        if 'allow_pickle' in inspect.signature(unpickler.np.load).parameters:
            kwargs['allow_pickle'] = True
    # WARNING: Decompyle incomplete



class ZNDArrayWrapper(NDArrayWrapper):
    '''An object to be persisted instead of numpy arrays.

    This object store the Zfile filename in which
    the data array has been persisted, and the meta information to
    retrieve it.
    The reason that we store the raw buffer data of the array and
    the meta information, rather than array representation routine
    (tobytes) is that it enables us to use completely the strided
    model to avoid memory copies (a and a.T store as fast). In
    addition saving the heavy information separately can avoid
    creating large temporary buffers when unpickling data with
    large arrays.
    '''
    
    def __init__(self, filename, init_args, state):
        '''Constructor. Store the useful information for later.'''
        self.filename = filename
        self.state = state
        self.init_args = init_args

    
    def read(self, unpickler):
        '''Reconstruct the array from the meta-information and the z-file.'''
        filename = os.path.join(unpickler._dirname, self.filename)
    # WARNING: Decompyle incomplete



class ZipNumpyUnpickler(Unpickler):
    '''A subclass of the Unpickler to unpickle our numpy pickles.'''
    dispatch = Unpickler.dispatch.copy()
    
    def __init__(self, filename, file_handle, mmap_mode = (None,)):
        '''Constructor.'''
        self._filename = os.path.basename(filename)
        self._dirname = os.path.dirname(filename)
        self.mmap_mode = mmap_mode
        self.file_handle = self._open_pickle(file_handle)
        Unpickler.__init__(self, self.file_handle)
        
        try:
            import numpy as np
        except ImportError:
            np = None

        self.np = np

    
    def _open_pickle(self, file_handle):
        return BytesIO(read_zfile(file_handle))

    
    def load_build(self):
        '''Set the state of a newly created object.

        We capture it to replace our place-holder objects,
        NDArrayWrapper, by the array we are interested in. We
        replace them directly in the stack of pickler.
        '''
        Unpickler.load_build(self)
    # WARNING: Decompyle incomplete

    dispatch[pickle.BUILD[0]] = load_build


def load_compatibility(filename):
    '''Reconstruct a Python object from a file persisted with joblib.dump.

    This function ensures the compatibility with joblib old persistence format
    (<= 0.9.3).

    Parameters
    ----------
    filename: string
        The name of the file from which to load the object

    Returns
    -------
    result: any Python object
        The object stored in the file.

    See Also
    --------
    joblib.dump : function to save an object

    Notes
    -----

    This function can load numpy array files saved separately during the
    dump.
    '''
    file_handle = open(filename, 'rb')
    unpickler = ZipNumpyUnpickler(filename, file_handle = file_handle)
    obj = unpickler.load()
