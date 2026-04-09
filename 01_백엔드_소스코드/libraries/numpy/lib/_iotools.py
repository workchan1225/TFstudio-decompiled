# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _iotools.pyc (Python 3.11)

'''A collection of functions designed to help I/O with ascii files.

'''
__docformat__ = 'restructuredtext en'
import numpy as np

numeric
from numpy.compat import asbytes, asunicode
asunicode = asunicode
import numpy.core.numeric, core

def _decode_line(line, encoding = (None,)):
    """Decode bytes from binary input streams.

    Defaults to decoding from 'latin1'. That differs from the behavior of
    np.compat.asunicode that decodes from 'ascii'.

    Parameters
    ----------
    line : str or bytes
         Line to be decoded.
    encoding : str
         Encoding used to decode `line`.

    Returns
    -------
    decoded_line : str

    """
    pass
# WARNING: Decompyle incomplete


def _is_string_like(obj):
    '''
    Check whether obj behaves like a string.
    '''
    
    try:
        obj + ''
    except (TypeError, ValueError):
        return False

    return True


def _is_bytes_like(obj):
    '''
    Check whether obj behaves like a bytes object.
    '''
    
    try:
        obj + b''
    except (TypeError, ValueError):
        return False

    return True


def has_nested_fields(ndtype):
    """
    Returns whether one or several fields of a dtype are nested.

    Parameters
    ----------
    ndtype : dtype
        Data-type of a structured array.

    Raises
    ------
    AttributeError
        If `ndtype` does not have a `names` attribute.

    Examples
    --------
    >>> dt = np.dtype([('name', 'S4'), ('x', float), ('y', float)])
    >>> np.lib._iotools.has_nested_fields(dt)
    False

    """
    pass
# WARNING: Decompyle incomplete


def flatten_dtype(ndtype, flatten_base = (False,)):
    """
    Unpack a structured data-type by collapsing nested fields and/or fields
    with a shape.

    Note that the field names are lost.

    Parameters
    ----------
    ndtype : dtype
        The datatype to collapse
    flatten_base : bool, optional
       If True, transform a field with a shape into several fields. Default is
       False.

    Examples
    --------
    >>> dt = np.dtype([('name', 'S4'), ('x', float), ('y', float),
    ...                ('block', int, (2, 3))])
    >>> np.lib._iotools.flatten_dtype(dt)
    [dtype('S4'), dtype('float64'), dtype('float64'), dtype('int64')]
    >>> np.lib._iotools.flatten_dtype(dt, flatten_base=True)
    [dtype('S4'),
     dtype('float64'),
     dtype('float64'),
     dtype('int64'),
     dtype('int64'),
     dtype('int64'),
     dtype('int64'),
     dtype('int64'),
     dtype('int64')]

    """
    names = ndtype.names
# WARNING: Decompyle incomplete


class LineSplitter:
    """
    Object to split a string at a given delimiter or at given places.

    Parameters
    ----------
    delimiter : str, int, or sequence of ints, optional
        If a string, character used to delimit consecutive fields.
        If an integer or a sequence of integers, width(s) of each field.
    comments : str, optional
        Character used to mark the beginning of a comment. Default is '#'.
    autostrip : bool, optional
        Whether to strip each individual field. Default is True.

    """
    
    def autostrip(self, method):
        '''
        Wrapper to strip each member of the output of `method`.

        Parameters
        ----------
        method : function
            Function that takes a single argument and returns a sequence of
            strings.

        Returns
        -------
        wrapped : function
            The result of wrapping `method`. `wrapped` takes a single input
            argument and returns a list of strings that are stripped of
            white-space.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __init__(self, delimiter, comments, autostrip, encoding = (None, '#', True, None)):
        delimiter = _decode_line(delimiter)
        comments = _decode_line(comments)
        self.comments = comments
    # WARNING: Decompyle incomplete

    
    def _delimited_splitter(self, line):
        '''Chop off comments, strip, and split at delimiter. '''
        pass
    # WARNING: Decompyle incomplete

    
    def _fixedwidth_splitter(self, line):
        pass
    # WARNING: Decompyle incomplete

    
    def _variablewidth_splitter(self, line):
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, line):
        return self._handyman(_decode_line(line, self.encoding))



class NameValidator:
    '''
    Object to validate a list of strings to use as field names.

    The strings are stripped of any non alphanumeric character, and spaces
    are replaced by \'_\'. During instantiation, the user can define a list
    of names to exclude, as well as a list of invalid characters. Names in
    the exclusion list are appended a \'_\' character.

    Once an instance has been created, it can be called with a list of
    names, and a list of valid names will be created.  The `__call__`
    method accepts an optional keyword "default" that sets the default name
    in case of ambiguity. By default this is \'f\', so that names will
    default to `f0`, `f1`, etc.

    Parameters
    ----------
    excludelist : sequence, optional
        A list of names to exclude. This list is appended to the default
        list [\'return\', \'file\', \'print\']. Excluded names are appended an
        underscore: for example, `file` becomes `file_` if supplied.
    deletechars : str, optional
        A string combining invalid characters that must be deleted from the
        names.
    case_sensitive : {True, False, \'upper\', \'lower\'}, optional
        * If True, field names are case-sensitive.
        * If False or \'upper\', field names are converted to upper case.
        * If \'lower\', field names are converted to lower case.

        The default value is True.
    replace_space : \'_\', optional
        Character(s) used in replacement of white spaces.

    Notes
    -----
    Calling an instance of `NameValidator` is the same as calling its
    method `validate`.

    Examples
    --------
    >>> validator = np.lib._iotools.NameValidator()
    >>> validator([\'file\', \'field2\', \'with space\', \'CaSe\'])
    (\'file_\', \'field2\', \'with_space\', \'CaSe\')

    >>> validator = np.lib._iotools.NameValidator(excludelist=[\'excl\'],
    ...                                           deletechars=\'q\',
    ...                                           case_sensitive=False)
    >>> validator([\'excl\', \'field2\', \'no_q\', \'with space\', \'CaSe\'])
    (\'EXCL\', \'FIELD2\', \'NO_Q\', \'WITH_SPACE\', \'CASE\')

    '''
    defaultexcludelist = [
        'return',
        'file',
        'print']
    defaultdeletechars = set("~!@#$%^&*()-=+~\\|]}[{';: /?.>,<")
    
    def __init__(self, excludelist, deletechars, case_sensitive, replace_space = (None, None, None, '_')):
        pass
    # WARNING: Decompyle incomplete

    
    def validate(self, names, defaultfmt, nbfields = ('f%i', None)):
        '''
        Validate a list of strings as field names for a structured array.

        Parameters
        ----------
        names : sequence of str
            Strings to be validated.
        defaultfmt : str, optional
            Default format string, used if validating a given string
            reduces its length to zero.
        nbfields : integer, optional
            Final number of validated names, used to expand or shrink the
            initial list of names.

        Returns
        -------
        validatednames : list of str
            The list of validated field names.

        Notes
        -----
        A `NameValidator` instance can be called directly, which is the
        same as calling `validate`. For examples, see `NameValidator`.

        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __call__(self, names, defaultfmt, nbfields = ('f%i', None)):
        return self.validate(names, defaultfmt = defaultfmt, nbfields = nbfields)



def str2bool(value):
    """
    Tries to transform a string supposed to represent a boolean to a boolean.

    Parameters
    ----------
    value : str
        The string that is transformed to a boolean.

    Returns
    -------
    boolval : bool
        The boolean representation of `value`.

    Raises
    ------
    ValueError
        If the string is not 'True' or 'False' (case independent)

    Examples
    --------
    >>> np.lib._iotools.str2bool('TRUE')
    True
    >>> np.lib._iotools.str2bool('false')
    False

    """
    value = value.upper()
    if value == 'TRUE':
        return True
    if None == 'FALSE':
        return False
    raise None('Invalid boolean')


class ConverterError(Exception):
    '''
    Exception raised when an error occurs in a converter for string values.

    '''
    pass


class ConverterLockError(ConverterError):
    '''
    Exception raised when an attempt is made to upgrade a locked converter.

    '''
    pass


class ConversionWarning(UserWarning):
    '''
    Warning issued when a string converter has a problem.

    Notes
    -----
    In `genfromtxt` a `ConversionWarning` is issued if raising exceptions
    is explicitly suppressed with the "invalid_raise" keyword.

    '''
    pass


class StringConverter:
    '''
    Factory class for function transforming a string into another object
    (int, float).

    After initialization, an instance can be called to transform a string
    into another object. If the string is recognized as representing a
    missing value, a default value is returned.

    Attributes
    ----------
    func : function
        Function used for the conversion.
    default : any
        Default value to return when the input corresponds to a missing
        value.
    type : type
        Type of the output.
    _status : int
        Integer representing the order of the conversion.
    _mapper : sequence of tuples
        Sequence of tuples (dtype, function, default value) to evaluate in
        order.
    _locked : bool
        Holds `locked` parameter.

    Parameters
    ----------
    dtype_or_func : {None, dtype, function}, optional
        If a `dtype`, specifies the input data type, used to define a basic
        function and a default value for missing data. For example, when
        `dtype` is float, the `func` attribute is set to `float` and the
        default value to `np.nan`.  If a function, this function is used to
        convert a string to another object. In this case, it is recommended
        to give an associated default value as input.
    default : any, optional
        Value to return by default, that is, when the string to be
        converted is flagged as missing. If not given, `StringConverter`
        tries to supply a reasonable default value.
    missing_values : {None, sequence of str}, optional
        ``None`` or sequence of strings indicating a missing value. If ``None``
        then missing values are indicated by empty entries. The default is
        ``None``.
    locked : bool, optional
        Whether the StringConverter should be locked to prevent automatic
        upgrade or not. Default is False.

    '''
    _mapper = [
        (nx.bool_, str2bool, False),
        (nx.int_, int, -1)]
    if nx.dtype(nx.int_).itemsize < nx.dtype(nx.int64).itemsize:
        _mapper.append((nx.int64, int, -1))
    _mapper.extend([
        (nx.float64, float, nx.nan),
        (nx.complex128, complex, nx.nan + (0+0j)),
        (nx.longdouble, nx.longdouble, nx.nan),
        (nx.integer, int, -1),
        (nx.floating, float, nx.nan),
        (nx.complexfloating, complex, nx.nan + (0+0j)),
        (nx.str_, asunicode, '???'),
        (nx.bytes_, asbytes, '???')])
    _getdtype = (lambda cls, val: np.array(val).dtype)()
    _getsubdtype = (lambda cls, val: np.array(val).dtype.type)()
    _dtypeortype = (lambda cls, dtype: if dtype.type == np.datetime64:
dtypeNone.type)()
    upgrade_mapper = (lambda cls, func, default = (None,): if hasattr(func, '__call__'):
cls._mapper.insert(-1, (cls._getsubdtype(default), func, default))None# WARNING: Decompyle incomplete
)()
    _find_map_entry = (lambda cls, dtype: for deftype, func, default_def in enumerate(cls._mapper):
if dtype.type == deftype:
None, (i, (deftype, func, default_def))for deftype, func, default_def in enumerate(cls._mapper):
if np.issubdtype(dtype.type, deftype):
None, (i, (deftype, func, default_def))raise LookupError)()
    
    def __init__(self, dtype_or_func, default, missing_values, locked = (None, None, None, False)):
        self._locked = bool(locked)
    # WARNING: Decompyle incomplete

    
    def _loose_call(self, value):
        
        try:
            return self.func(value)
        except ValueError:
            return 


    
    def _strict_call(self, value):
        
        try:
            new_value = self.func(value)
            if self.func is int:
                
                try:
                    np.array(value, dtype = self.type)
                    
                    try:
                        pass
                    except OverflowError:
                        raise ValueError

                    
                    try:
                        return new_value
                    except ValueError:
                        if value.strip() in self.missing_values:
                            if not self._status:
                                self._checked = False
                            return 
                        raise None("Cannot convert string '%s'" % value)




    
    def __call__(self, value):
        return self._callingfunction(value)

    
    def _do_upgrade(self):
        if self._locked:
            errmsg = 'Converter is locked and cannot be upgraded'
            raise ConverterLockError(errmsg)
        _statusmax = len(self._mapper)
        _status = self._status
        if _status == _statusmax:
            errmsg = 'Could not find a valid conversion function'
            raise ConverterError(errmsg)
        if _status < _statusmax - 1:
            _status += 1
        (self.type, self.func, default) = self._mapper[_status]
        self._status = _status
    # WARNING: Decompyle incomplete

    
    def upgrade(self, value):
        '''
        Find the best converter for a given string, and return the result.

        The supplied string `value` is converted by testing different
        converters in order. First the `func` method of the
        `StringConverter` instance is tried, if this fails other available
        converters are tried.  The order in which these other converters
        are tried is determined by the `_status` attribute of the instance.

        Parameters
        ----------
        value : str
            The string to convert.

        Returns
        -------
        out : any
            The result of converting `value` with the appropriate converter.

        '''
        self._checked = True
        
        try:
            return self._strict_call(value)
        except ValueError:
            self._do_upgrade()
            return 


    
    def iterupgrade(self, value):
        self._checked = True
        if not hasattr(value, '__iter__'):
            value = (value,)
        _strict_call = self._strict_call
        
        try:
            for _m in value:
                _strict_call(_m)
                return None
                except ValueError:
                    self._do_upgrade()
                    self.iterupgrade(value)
                    return None


    
    def update(self, func, default, testing_value, missing_values, locked = (None, None, '', False)):
        """
        Set StringConverter attributes directly.

        Parameters
        ----------
        func : function
            Conversion function.
        default : any, optional
            Value to return by default, that is, when the string to be
            converted is flagged as missing. If not given,
            `StringConverter` tries to supply a reasonable default value.
        testing_value : str, optional
            A string representing a standard input value of the converter.
            This string is used to help defining a reasonable default
            value.
        missing_values : {sequence of str, None}, optional
            Sequence of strings indicating a missing value. If ``None``, then
            the existing `missing_values` are cleared. The default is `''`.
        locked : bool, optional
            Whether the StringConverter should be locked to prevent
            automatic upgrade or not. Default is False.

        Notes
        -----
        `update` takes the same parameters as the constructor of
        `StringConverter`, except that `func` does not accept a `dtype`
        whereas `dtype_or_func` in the constructor does.

        """
        self.func = func
        self._locked = locked
    # WARNING: Decompyle incomplete



def easy_dtype(ndtype, names, defaultfmt = (None, 'f%i'), **validationargs):
    '''
    Convenience function to create a `np.dtype` object.

    The function processes the input `dtype` and matches it with the given
    names.

    Parameters
    ----------
    ndtype : var
        Definition of the dtype. Can be any string or dictionary recognized
        by the `np.dtype` function, or a sequence of types.
    names : str or sequence, optional
        Sequence of strings to use as field names for a structured dtype.
        For convenience, `names` can be a string of a comma-separated list
        of names.
    defaultfmt : str, optional
        Format string used to define missing names, such as ``"f%i"``
        (default) or ``"fields_%02i"``.
    validationargs : optional
        A series of optional arguments used to initialize a
        `NameValidator`.

    Examples
    --------
    >>> np.lib._iotools.easy_dtype(float)
    dtype(\'float64\')
    >>> np.lib._iotools.easy_dtype("i4, f8")
    dtype([(\'f0\', \'<i4\'), (\'f1\', \'<f8\')])
    >>> np.lib._iotools.easy_dtype("i4, f8", defaultfmt="field_%03i")
    dtype([(\'field_000\', \'<i4\'), (\'field_001\', \'<f8\')])

    >>> np.lib._iotools.easy_dtype((int, float, float), names="a,b,c")
    dtype([(\'a\', \'<i8\'), (\'b\', \'<f8\'), (\'c\', \'<f8\')])
    >>> np.lib._iotools.easy_dtype(float, names="a,b,c")
    dtype([(\'a\', \'<f8\'), (\'b\', \'<f8\'), (\'c\', \'<f8\')])

    '''
    pass
# WARNING: Decompyle incomplete
