# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pagers_base.pyc (Python 3.11)

from typing import Any, Callable, Sequence, Tuple
from google.longrunning import operations_pb2

class ListOperationsPagerBase:
    '''A pager for iterating through ``list_operations`` requests.

    This class thinly wraps an initial
    :class:`google.longrunning.operations_pb2.ListOperationsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``operations`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListOperations`` requests and continue to iterate
    through the ``operations`` field on the
    corresponding responses.

    All the usual :class:`google.longrunning.operations_pb2.ListOperationsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    '''
    
    def __init__(self = None, method = None, request = None, response = None, *, metadata):
        '''Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.longrunning.operations_pb2.ListOperationsRequest):
                The initial request object.
            response (google.longrunning.operations_pb2.ListOperationsResponse):
                The initial response object.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        '''
        self._method = method
        self._request = request
        self._response = response
        self._metadata = metadata

    
    def __getattr__(self = None, name = None):
        return getattr(self._response, name)

    
    def __repr__(self = None):
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
