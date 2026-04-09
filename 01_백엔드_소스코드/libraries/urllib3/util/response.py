# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: response.pyc (Python 3.11)

from __future__ import annotations
from http.client import client as httplib
from email.errors import MultipartInvariantViolationDefect, StartBoundaryNotFoundDefect
from exceptions import HeaderParsingError

def is_fp_closed(obj = None):
    '''
    Checks whether a given file-like object is closed.

    :param obj:
        The file-like object to check.
    '''
    
    try:
        return obj.isclosed()
    except AttributeError:
        pass

    
    try:
        return obj.closed
    except AttributeError:
        pass

    
    try:
        return obj.fp is None
    except AttributeError:
        pass

    raise ValueError('Unable to determine whether fp is closed.')


def assert_header_parsing(headers = None):
    '''
    Asserts whether all headers have been successfully parsed.
    Extracts encountered errors from the result of parsing headers.

    Only works on Python 3.

    :param http.client.HTTPMessage headers: Headers to verify.

    :raises urllib3.exceptions.HeaderParsingError:
        If parsing errors are found.
    '''
    if not isinstance(headers, httplib.HTTPMessage):
        raise TypeError(f'''expected httplib.Message, got {type(headers)}.''')
    unparsed_data = None
    if not headers.is_multipart():
        payload = headers.get_payload()
        if isinstance(payload, (bytes, str)):
            unparsed_data = payload
    defects = headers.defects()
    if defects or unparsed_data:
        raise HeaderParsingError(defects = defects, unparsed_data = unparsed_data)


def is_response_to_head(response = None):
    """
    Checks whether the request of a response has been a HEAD-request.

    :param http.client.HTTPResponse response:
        Response to check if the originating request
        used 'HEAD' as a method.
    """
    method_str = response._method
    return method_str.upper() == 'HEAD'
