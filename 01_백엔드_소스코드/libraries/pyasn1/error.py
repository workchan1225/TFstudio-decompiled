# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error.pyc (Python 3.11)


class PyAsn1Error(Exception):
    '''Base pyasn1 exception

    `PyAsn1Error` is the base exception class (based on
    :class:`Exception`) that represents all possible ASN.1 related
    errors.

    Parameters
    ----------
    args:
        Opaque positional parameters

    Keyword Args
    ------------
    kwargs:
        Opaque keyword parameters

    '''
    
    def __init__(self, *args, **kwargs):
        self._args = args
        self._kwargs = kwargs

    context = (lambda self: self._kwargs.get('context', { }))()


class ValueConstraintError(PyAsn1Error):
    '''ASN.1 type constraints violation exception

    The `ValueConstraintError` exception indicates an ASN.1 value
    constraint violation.

    It might happen on value object instantiation (for scalar types) or on
    serialization (for constructed types).
    '''
    pass


class SubstrateUnderrunError(PyAsn1Error):
    '''ASN.1 data structure deserialization error

    The `SubstrateUnderrunError` exception indicates insufficient serialised
    data on input of a de-serialization codec.
    '''
    pass


class EndOfStreamError(SubstrateUnderrunError):
    '''ASN.1 data structure deserialization error

    The `EndOfStreamError` exception indicates the condition of the input
    stream has been closed.
    '''
    pass


class UnsupportedSubstrateError(PyAsn1Error):
    '''Unsupported substrate type to parse as ASN.1 data.'''
    pass


class PyAsn1UnicodeError(UnicodeError, PyAsn1Error):
    '''Unicode text processing error

    The `PyAsn1UnicodeError` exception is a base class for errors relating to
    unicode text de/serialization.

    Apart from inheriting from :class:`PyAsn1Error`, it also inherits from
    :class:`UnicodeError` to help the caller catching unicode-related errors.
    '''
    
    def __init__(self, message, unicode_error = (None,)):
        pass
    # WARNING: Decompyle incomplete



class PyAsn1UnicodeDecodeError(UnicodeDecodeError, PyAsn1UnicodeError):
    '''Unicode text decoding error

    The `PyAsn1UnicodeDecodeError` exception represents a failure to
    deserialize unicode text.

    Apart from inheriting from :class:`PyAsn1UnicodeError`, it also inherits
    from :class:`UnicodeDecodeError` to help the caller catching unicode-related
    errors.
    '''
    pass


class PyAsn1UnicodeEncodeError(UnicodeEncodeError, PyAsn1UnicodeError):
    '''Unicode text encoding error

    The `PyAsn1UnicodeEncodeError` exception represents a failure to
    serialize unicode text.

    Apart from inheriting from :class:`PyAsn1UnicodeError`, it also inherits
    from :class:`UnicodeEncodeError` to help the caller catching
    unicode-related errors.
    '''
    pass
