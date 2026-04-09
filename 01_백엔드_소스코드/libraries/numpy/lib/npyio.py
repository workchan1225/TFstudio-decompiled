# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: npyio.pyc (Python 3.11)

import os
import re
import functools
import itertools
import warnings
import weakref
import contextlib
import operator
from operator import itemgetter, index as opindex, methodcaller
from collections.abc import Mapping
import numpy as np
from  import format
from _datasource import DataSource
from numpy.core import overrides
from numpy.core.multiarray import packbits, unpackbits
from numpy.core._multiarray_umath import _load_from_filelike
from numpy.core.overrides import set_array_function_like_doc, set_module
from _iotools import LineSplitter, NameValidator, StringConverter, ConverterError, ConverterLockError, ConversionWarning, _is_string_like, has_nested_fields, flatten_dtype, easy_dtype, _decode_line
from numpy.compat import asbytes, asstr, asunicode, os_fspath, os_PathLike, pickle
__all__ = [
    'savetxt',
    'loadtxt',
    'genfromtxt',
    'recfromtxt',
    'recfromcsv',
    'load',
    'save',
    'savez',
    'savez_compressed',
    'packbits',
    'unpackbits',
    'fromregex',
    'DataSource']
array_function_dispatch = functools.partial(overrides.array_function_dispatch, module = 'numpy')

class BagObj:
    '''
    BagObj(obj)

    Convert attribute look-ups to getitems on the object passed in.

    Parameters
    ----------
    obj : class instance
        Object on which attribute look-up is performed.

    Examples
    --------
    >>> from numpy.lib.npyio import BagObj as BO
    >>> class BagDemo:
    ...     def __getitem__(self, key): # An instance of BagObj(BagDemo)
    ...                                 # will call this method when any
    ...                                 # attribute look-up is required
    ...         result = "Doesn\'t matter what you want, "
    ...         return result + "you\'re gonna get this"
    ...
    >>> demo_obj = BagDemo()
    >>> bagobj = BO(demo_obj)
    >>> bagobj.hello_there
    "Doesn\'t matter what you want, you\'re gonna get this"
    >>> bagobj.I_can_be_anything
    "Doesn\'t matter what you want, you\'re gonna get this"

    '''
    
    def __init__(self, obj):
        self._obj = weakref.proxy(obj)

    
    def __getattribute__(self, key):
        
        try:
            return object.__getattribute__(self, '_obj')[key]
        except KeyError:
            raise AttributeError(key), None


    
    def __dir__(self):
        '''
        Enables dir(bagobj) to list the files in an NpzFile.

        This also enables tab-completion in an interpreter or IPython.
        '''
        return list(object.__getattribute__(self, '_obj').keys())



def zipfile_factory(file, *args, **kwargs):
    '''
    Create a ZipFile.

    Allows for Zip64, and the `file` argument can accept file, str, or
    pathlib.Path objects. `args` and `kwargs` are passed to the zipfile.ZipFile
    constructor.
    '''
    if not hasattr(file, 'read'):
        file = os_fspath(file)
    import zipfile
    kwargs['allowZip64'] = True
# WARNING: Decompyle incomplete


class NpzFile(Mapping):
    """
    NpzFile(fid)

    A dictionary-like object with lazy-loading of files in the zipped
    archive provided on construction.

    `NpzFile` is used to load files in the NumPy ``.npz`` data archive
    format. It assumes that files in the archive have a ``.npy`` extension,
    other files are ignored.

    The arrays and file strings are lazily loaded on either
    getitem access using ``obj['key']`` or attribute lookup using
    ``obj.f.key``. A list of all files (without ``.npy`` extensions) can
    be obtained with ``obj.files`` and the ZipFile object itself using
    ``obj.zip``.

    Attributes
    ----------
    files : list of str
        List of all files in the archive with a ``.npy`` extension.
    zip : ZipFile instance
        The ZipFile object initialized with the zipped archive.
    f : BagObj instance
        An object on which attribute can be performed as an alternative
        to getitem access on the `NpzFile` instance itself.
    allow_pickle : bool, optional
        Allow loading pickled data. Default: False

        .. versionchanged:: 1.16.3
            Made default False in response to CVE-2019-6446.

    pickle_kwargs : dict, optional
        Additional keyword arguments to pass on to pickle.load.
        These are only useful when loading object arrays saved on
        Python 2 when using Python 3.
    max_header_size : int, optional
        Maximum allowed size of the header.  Large headers may not be safe
        to load securely and thus require explicitly passing a larger value.
        See :py:func:`ast.literal_eval()` for details.
        This option is ignored when `allow_pickle` is passed.  In that case
        the file is by definition trusted and the limit is unnecessary.

    Parameters
    ----------
    fid : file or str
        The zipped archive to open. This is either a file-like object
        or a string containing the path to the archive.
    own_fid : bool, optional
        Whether NpzFile should close the file handle.
        Requires that `fid` is a file-like object.

    Examples
    --------
    >>> from tempfile import TemporaryFile
    >>> outfile = TemporaryFile()
    >>> x = np.arange(10)
    >>> y = np.sin(x)
    >>> np.savez(outfile, x=x, y=y)
    >>> _ = outfile.seek(0)

    >>> npz = np.load(outfile)
    >>> isinstance(npz, np.lib.npyio.NpzFile)
    True
    >>> npz
    NpzFile 'object' with keys x, y
    >>> sorted(npz.files)
    ['x', 'y']
    >>> npz['x']  # getitem access
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    >>> npz.f.x  # attribute lookup
    array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    """
    zip = None
    fid = None
    _MAX_REPR_ARRAY_COUNT = 5
    
    def __init__(self, fid, own_fid = None, allow_pickle = (False, False, None), pickle_kwargs = {
        'max_header_size': format._MAX_HEADER_SIZE }, *, max_header_size):
        _zip = zipfile_factory(fid)
        self._files = _zip.namelist()
        self.files = []
        self.allow_pickle = allow_pickle
        self.max_header_size = max_header_size
        self.pickle_kwargs = pickle_kwargs
        for x in self._files:
            if x.endswith('.npy'):
                self.files.append(x[:-4])
                continue
            self.files.append(x)
            self.zip = _zip
            self.f = BagObj(self)
            if own_fid:
                self.fid = fid
                return None
            return None

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    
    def close(self):
        '''
        Close the file.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __del__(self):
        self.close()

    
    def __iter__(self):
        return iter(self.files)

    
    def __len__(self):
        return len(self.files)

    
    def __getitem__(self, key):
        member = False
        if key in self._files:
            member = True
        elif key in self.files:
            member = True
            key += '.npy'
        if member:
            bytes = self.zip.open(key)
            magic = bytes.read(len(format.MAGIC_PREFIX))
            bytes.close()
            if magic == format.MAGIC_PREFIX:
                bytes = self.zip.open(key)
                return format.read_array(bytes, allow_pickle = self.allow_pickle, pickle_kwargs = self.pickle_kwargs, max_header_size = self.max_header_size)
            return None.zip.read(key)
        raise None(f'''{key} is not a file in the archive''')

    
    def __contains__(self, key):
