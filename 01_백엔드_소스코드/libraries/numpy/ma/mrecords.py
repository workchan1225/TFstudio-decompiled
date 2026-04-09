# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: mrecords.pyc (Python 3.11)

''':mod:`numpy.ma..mrecords`

Defines the equivalent of :class:`numpy.recarrays` for masked arrays,
where fields can be accessed as attributes.
Note that :class:`numpy.ma.MaskedArray` already supports structured datatypes
and the masking of individual fields.

.. moduleauthor:: Pierre Gerard-Marchant

'''
from numpy.ma import MAError, MaskedArray, masked, nomask, masked_array, getdata, getmaskarray, filled
from numpy.ma import ma
import warnings
import numpy as np
from numpy import bool_, dtype, ndarray, recarray, array as narray
from numpy.core.records import fromarrays as recfromarrays, fromrecords as recfromrecords
_byteorderconv = np.core.records._byteorderconv
_check_fill_value = ma.core._check_fill_value
__all__ = [
    'MaskedRecords',
    'mrecarray',
    'fromarrays',
    'fromrecords',
    'fromtextfile',
    'addfield']
reserved_fields = [
    '_data',
    '_mask',
    '_fieldmask',
    'dtype']

def _checknames(descr, names = (None,)):
    """
    Checks that field names ``descr`` are not reserved keywords.

    If this is the case, a default 'f%i' is substituted.  If the argument
    `names` is not None, updates the field names to valid names.

    """
    ndescr = len(descr)
    default_names = range(ndescr)()
# WARNING: Decompyle incomplete


def _get_fieldmask(self):
    mdescr = self.dtype.names()
    fdmask = np.empty(self.shape, dtype = mdescr)
    fdmask.flat = tuple([
        False] * len(mdescr))
    return fdmask


class MaskedRecords(MaskedArray):
    '''

    Attributes
    ----------
    _data : recarray
        Underlying data, as a record array.
    _mask : boolean array
        Mask of the records. A record is masked when all its fields are
        masked.
    _fieldmask : boolean recarray
        Record array of booleans, setting the mask of each individual field
        of each record.
    _fill_value : record
        Filling values for each field.

    '''
    
    def __new__(cls, shape, dtype, buf, offset, strides, formats, names, titles, byteorder, aligned, mask, hard_mask, fill_value, keep_mask, copy = (None, None, 0, None, None, None, None, None, False, nomask, False, None, True, False), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def __array_finalize__(self, obj):
        pass
    # WARNING: Decompyle incomplete

    _data = (lambda self: ndarray.view(self, recarray))()
    _fieldmask = (lambda self: self._mask)()
    
    def __len__(self):
        '''
        Returns the length

        '''
        if self.ndim:
            return len(self._data)
        return None(self.dtype)

    
    def __getattribute__(self, attr):
        
        try:
            return object.__getattribute__(self, attr)
        except AttributeError:
            pass

        fielddict = ndarray.__getattribute__(self, 'dtype').fields
        
        try:
            res = fielddict[attr][:2]
        except (TypeError, KeyError):
            e = None
            raise AttributeError(f'''record array has no attribute {attr}'''), e
            e = None
            del e

        _localdict = ndarray.__getattribute__(self, '__dict__')
        _data = ndarray.view(self, _localdict['_baseclass'])
    # WARNING: Decompyle incomplete

    
    def __setattr__(self, attr, val):
        '''
        Sets the attribute attr to the value val.

        '''
        if attr in ('mask', 'fieldmask'):
            self.__setmask__(val)
            return None
        _localdict = None.__getattribute__(self, '__dict__')
        newattr = attr not in _localdict
        
        try:
            ret = object.__setattr__(self, attr, val)
            if not ndarray.__getattribute__(self, 'dtype').fields:
                fielddict = { }
                if attr not in fielddict:
                    return ret
                if None:
                    
                    try:
                        object.__delattr__(self, attr)
                    except Exception:
                        return 
                    except Exception:
                        None, ret


        
        try:
            res = fielddict[attr][:2]
        except (TypeError, KeyError):
            e = { }
            raise AttributeError(f'''record array has no attribute {attr}'''), e
            e = None
            del e

    # WARNING: Decompyle incomplete

    
    def __getitem__(self, indx):
        '''
        Returns all the fields sharing the same fieldname base.

        The fieldname base is either `_data` or `_mask`.

        '''
        _localdict = self.__dict__
        _mask = ndarray.__getattribute__(self, '_mask')
        _data = ndarray.view(self, _localdict['_baseclass'])
    # WARNING: Decompyle incomplete

    
    def __setitem__(self, indx, value):
        '''
        Sets the given record to value.

        '''
        MaskedArray.__setitem__(self, indx, value)
        if isinstance(indx, str):
            self._mask[indx] = ma.getmaskarray(value)
            return None

    
    def __str__(self):
        '''
        Calculates the string representation.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        '''
        Calculates the repr representation.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def view(self, dtype, type = (None, None)):
        '''
        Returns a view of the mrecarray.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def harden_mask(self):
        '''
        Forces the mask to hard.

        '''
        self._hardmask = True

    
    def soften_mask(self):
        '''
        Forces the mask to soft

        '''
        self._hardmask = False

    
    def copy(self):
        '''
        Returns a copy of the masked record.

        '''
        copied = self._data.copy().view(type(self))
        copied._mask = self._mask.copy()
        return copied

    
    def tolist(self, fill_value = (None,)):
        '''
        Return the data portion of the array as a list.

        Data items are converted to the nearest compatible Python type.
        Masked values are converted to fill_value. If fill_value is None,
        the corresponding entries in the output list will be ``None``.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __getstate__(self):
        '''Return the internal state of the masked array.

        This is for pickling.

        '''
        state = (1, self.shape, self.dtype, self.flags.fnc, self._data.tobytes(), self._mask.tobytes(), self._fill_value)
        return state

    
    def __setstate__(self, state):
        '''
        Restore the internal state of the masked array.

        This is for pickling.  ``state`` is typically the output of the
        ``__getstate__`` output, and is a 5-tuple:

        - class name
        - a tuple giving the shape of the data
        - a typecode for the data
        - a binary string for the data
        - a binary string for the mask.

        '''
        (ver, shp, typ, isf, raw, msk, flv) = state
        ndarray.__setstate__(self, (shp, typ, isf, raw))
        mdtype = (lambda .0: [ (k, bool_) for k, _ in .0 ])(self.dtype.descr())
        self.__dict__['_mask'].__setstate__((shp, mdtype, isf, msk))
        self.fill_value = flv

    
    def __reduce__(self):
        '''
        Return a 3-tuple for pickling a MaskedArray.

        '''
        return (_mrreconstruct, (self.__class__, self._baseclass, (0,), 'b'), self.__getstate__())



def _mrreconstruct(subtype, baseclass, baseshape, basetype):
    '''
    Build a new MaskedArray from the information stored in a pickle.

    '''
    _data = ndarray.__new__(baseclass, baseshape, basetype).view(subtype)
    _mask = ndarray.__new__(ndarray, baseshape, 'b1')
    return subtype.__new__(subtype, _data, mask = _mask, dtype = basetype)

mrecarray = MaskedRecords

def fromarrays(arraylist, dtype, shape, formats, names, titles, aligned, byteorder, fill_value = (None, None, None, None, None, False, None, None)):
    '''
    Creates a mrecarray from a (flat) list of masked arrays.

    Parameters
    ----------
    arraylist : sequence
        A list of (masked) arrays. Each element of the sequence is first converted
        to a masked array if needed. If a 2D array is passed as argument, it is
        processed line by line
    dtype : {None, dtype}, optional
        Data type descriptor.
    shape : {None, integer}, optional
        Number of records. If None, shape is defined from the shape of the
        first array in the list.
    formats : {None, sequence}, optional
        Sequence of formats for each individual field. If None, the formats will
        be autodetected by inspecting the fields and selecting the highest dtype
        possible.
    names : {None, sequence}, optional
        Sequence of the names of each field.
    fill_value : {None, sequence}, optional
        Sequence of data to be used as filling values.

    Notes
    -----
    Lists of tuples should be preferred over lists of lists for faster processing.

    '''
    datalist = arraylist()
    masklist = arraylist()
    _array = recfromarrays(datalist, dtype = dtype, shape = shape, formats = formats, names = names, titles = titles, aligned = aligned, byteorder = byteorder).view(mrecarray)
# WARNING: Decompyle incomplete


def fromrecords(reclist, dtype, shape, formats, names, titles, aligned, byteorder, fill_value, mask = (None, None, None, None, None, False, None, None, nomask)):
    '''
    Creates a MaskedRecords from a list of records.

    Parameters
    ----------
    reclist : sequence
        A list of records. Each element of the sequence is first converted
        to a masked array if needed. If a 2D array is passed as argument, it is
        processed line by line
    dtype : {None, dtype}, optional
        Data type descriptor.
    shape : {None,int}, optional
        Number of records. If None, ``shape`` is defined from the shape of the
        first array in the list.
    formats : {None, sequence}, optional
        Sequence of formats for each individual field. If None, the formats will
        be autodetected by inspecting the fields and selecting the highest dtype
        possible.
    names : {None, sequence}, optional
        Sequence of the names of each field.
    fill_value : {None, sequence}, optional
        Sequence of data to be used as filling values.
    mask : {nomask, sequence}, optional.
        External mask to apply on the data.

    Notes
    -----
    Lists of tuples should be preferred over lists of lists for faster processing.

    '''
    _mask = getattr(reclist, '_mask', None)
# WARNING: Decompyle incomplete


def _guessvartypes(arr):
    '''
    Tries to guess the dtypes of the str_ ndarray `arr`.

    Guesses by testing element-wise conversion. Returns a list of dtypes.
    The array is first converted to ndarray. If the array is 2D, the test
    is performed on the first line. An exception is raised if the file is
    3D or more.

    '''
    vartypes = []
    arr = np.asarray(arr)
    if arr.ndim == 2:
        arr = arr[0]
    elif arr.ndim > 2:
        raise ValueError('The array should be 2D at most!')
    for f in arr:
        int(f)
        vartypes.append(np.dtype(int))
        except (ValueError, TypeError):
            float(f)
            vartypes.append(np.dtype(float))
        except (ValueError, TypeError):
            complex(f)
            vartypes.append(np.dtype(complex))
        except (ValueError, TypeError):
            vartypes.append(arr.dtype)
    continue
    return vartypes


def openfile(fname):
    '''
    Opens the file handle of file `fname`.

    '''
    if hasattr(fname, 'readline'):
        return fname
    
    try:
        f = open(fname)
    except FileNotFoundError:
        e = None
        raise FileNotFoundError(f'''No such file: \'{fname}\''''), e
        e = None
        del e

    if f.readline()[:2] != '\\x':
        f.seek(0, 0)
        return f
    None.close()
    raise NotImplementedError('Wow, binary file')


def fromtextfile(fname, delimiter, commentchar, missingchar = None, varnames = (None, '#', '', None, None), vartypes = {
    'delimitor': np._NoValue }, *, delimitor):
    """
    Creates a mrecarray from data stored in the file `filename`.

    Parameters
    ----------
    fname : {file name/handle}
        Handle of an opened file.
    delimiter : {None, string}, optional
        Alphanumeric character used to separate columns in the file.
        If None, any (group of) white spacestring(s) will be used.
    commentchar : {'#', string}, optional
        Alphanumeric character used to mark the start of a comment.
    missingchar : {'', string}, optional
        String indicating missing data, and used to create the masks.
    varnames : {None, sequence}, optional
        Sequence of the variable names. If None, a list will be created from
        the first non empty line of the file.
    vartypes : {None, sequence}, optional
        Sequence of the variables dtypes. If None, it will be estimated from
        the first non-commented line.


    Ultra simple: the varnames are in the header, one line"""
    pass
# WARNING: Decompyle incomplete


def addfield(mrecord, newfield, newfieldname = (None,)):
    """Adds a new field to the masked record array

    Uses `newfield` as data and `newfieldname` as name. If `newfieldname`
    is None, the new field name is set to 'fi', where `i` is the number of
    existing fields.

    """
    pass
# WARNING: Decompyle incomplete
