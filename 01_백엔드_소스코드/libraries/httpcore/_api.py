# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _api.pyc (Python 3.11)

from __future__ import annotations
import contextlib
import typing
from _models import URL, Extensions, HeaderTypes, Response
from _sync.connection_pool import ConnectionPool

def request(method = None, url = None, *, headers, content, extensions):
    '''
    Sends an HTTP request, returning the response.

    ```
    response = httpcore.request("GET", "https://www.example.com/")
    ```

    Arguments:
        method: The HTTP method for the request. Typically one of `"GET"`,
            `"OPTIONS"`, `"HEAD"`, `"POST"`, `"PUT"`, `"PATCH"`, or `"DELETE"`.
        url: The URL of the HTTP request. Either as an instance of `httpcore.URL`,
            or as str/bytes.
        headers: The HTTP request headers. Either as a dictionary of str/bytes,
            or as a list of two-tuples of str/bytes.
        content: The content of the request body. Either as bytes,
            or as a bytes iterator.
        extensions: A dictionary of optional extra information included on the request.
            Possible keys include `"timeout"`.

    Returns:
        An instance of `httpcore.Response`.
    '''
    pool = ConnectionPool()
    None(None, None)
    return 
    with None:
        if not None, pool.request(method = method, url = url, headers = headers, content = content, extensions = extensions):
            pass

stream = (lambda method = None, url = None, *, headers, content: pass# WARNING: Decompyle incomplete
)()
