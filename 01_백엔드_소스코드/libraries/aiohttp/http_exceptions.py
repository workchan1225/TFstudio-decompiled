# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http_exceptions.pyc (Python 3.11)

'''Low-level http related exceptions.'''
from textwrap import indent
from typing import Optional, Union
from typedefs import _CIMultiDict
__all__ = ('HttpProcessingError',)

class HttpProcessingError(Exception):
    '''HTTP error.

    Shortcut for raising HTTP errors with custom code, message and headers.

    code: HTTP Error code.
    message: (optional) Error message.
    headers: (optional) Headers to be sent in response, a list of pairs
    '''
    code = 0
    message = ''
    headers = None
    
    def __init__(self = None, *, code, message, headers):
        pass
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        msg = indent(self.message, '  ')
        return f'''{self.code}, message:\n{msg}'''

    
    def __repr__(self = None):
        return f'''<{self.__class__.__name__}: {self.code}, message={self.message!r}>'''



class BadHttpMessage(HttpProcessingError):
    pass
# WARNING: Decompyle incomplete


class HttpBadRequest(BadHttpMessage):
    code = 400
    message = 'Bad Request'


class PayloadEncodingError(BadHttpMessage):
    '''Base class for payload errors'''
    pass


class ContentEncodingError(PayloadEncodingError):
    '''Content encoding error.'''
    pass


class TransferEncodingError(PayloadEncodingError):
    '''transfer encoding error.'''
    pass


class ContentLengthError(PayloadEncodingError):
    '''Not enough data to satisfy content length header.'''
    pass


class LineTooLong(BadHttpMessage):
    pass
# WARNING: Decompyle incomplete


class InvalidHeader(BadHttpMessage):
    pass
# WARNING: Decompyle incomplete


class BadStatusLine(BadHttpMessage):
    pass
# WARNING: Decompyle incomplete


class BadHttpMethod(BadStatusLine):
    pass
# WARNING: Decompyle incomplete


class InvalidURLError(BadHttpMessage):
    pass
