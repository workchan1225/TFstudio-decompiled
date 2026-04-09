# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pagers.pyc (Python 3.11)

from typing import Any, AsyncIterator, Awaitable, Callable, Iterator, Optional, Sequence, Tuple, Union
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.api_core import retry_async as retries_async

try:
    OptionalRetry = Union[(retries.Retry, gapic_v1.method._MethodDefault, None)]
    OptionalAsyncRetry = Union[(retries_async.AsyncRetry, gapic_v1.method._MethodDefault, None)]
except AttributeError:
    OptionalRetry = Union[(retries.Retry, object, None)]
    OptionalAsyncRetry = Union[(retries_async.AsyncRetry, object, None)]

from google.ai.generativelanguage_v1beta.types import retriever, retriever_service

class ListCorporaPager:
    '''A pager for iterating through ``list_corpora`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    '''
    
    def __init__(self = None, method = None, request = None, response = None, *, retry, timeout, metadata):
        '''Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListCorporaRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListCorporaResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        self._method = method
        self._request = retriever_service.ListCorporaRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    
    def __getattr__(self = None, name = None):
        return getattr(self._response, name)

    pages = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)



class ListCorporaAsyncPager:
    '''A pager for iterating through ``list_corpora`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``corpora`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListCorpora`` requests and continue to iterate
    through the ``corpora`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListCorporaResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    '''
    
    def __init__(self = None, method = None, request = None, response = None, *, retry, timeout, metadata):
        '''Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListCorporaRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListCorporaResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        self._method = method
        self._request = retriever_service.ListCorporaRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    
    def __getattr__(self = None, name = None):
        return getattr(self._response, name)

    pages = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)



class ListDocumentsPager:
    '''A pager for iterating through ``list_documents`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``documents`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListDocuments`` requests and continue to iterate
    through the ``documents`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    '''
    
    def __init__(self = None, method = None, request = None, response = None, *, retry, timeout, metadata):
        '''Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListDocumentsRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListDocumentsResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        self._method = method
        self._request = retriever_service.ListDocumentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    
    def __getattr__(self = None, name = None):
        return getattr(self._response, name)

    pages = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)



class ListDocumentsAsyncPager:
    '''A pager for iterating through ``list_documents`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``documents`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListDocuments`` requests and continue to iterate
    through the ``documents`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListDocumentsResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    '''
    
    def __init__(self = None, method = None, request = None, response = None, *, retry, timeout, metadata):
        '''Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListDocumentsRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListDocumentsResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        self._method = method
        self._request = retriever_service.ListDocumentsRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    
    def __getattr__(self = None, name = None):
        return getattr(self._response, name)

    pages = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)



class ListChunksPager:
    '''A pager for iterating through ``list_chunks`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse` object, and
    provides an ``__iter__`` method to iterate through its
    ``chunks`` field.

    If there are more pages, the ``__iter__`` method will make additional
    ``ListChunks`` requests and continue to iterate
    through the ``chunks`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    '''
    
    def __init__(self = None, method = None, request = None, response = None, *, retry, timeout, metadata):
        '''Instantiate the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListChunksRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListChunksResponse):
                The initial response object.
            retry (google.api_core.retry.Retry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        self._method = method
        self._request = retriever_service.ListChunksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    
    def __getattr__(self = None, name = None):
        return getattr(self._response, name)

    pages = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)



class ListChunksAsyncPager:
    '''A pager for iterating through ``list_chunks`` requests.

    This class thinly wraps an initial
    :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse` object, and
    provides an ``__aiter__`` method to iterate through its
    ``chunks`` field.

    If there are more pages, the ``__aiter__`` method will make additional
    ``ListChunks`` requests and continue to iterate
    through the ``chunks`` field on the
    corresponding responses.

    All the usual :class:`google.ai.generativelanguage_v1beta.types.ListChunksResponse`
    attributes are available on the pager. If multiple requests are made, only
    the most recent response is retained, and thus used for attribute lookup.
    '''
    
    def __init__(self = None, method = None, request = None, response = None, *, retry, timeout, metadata):
        '''Instantiates the pager.

        Args:
            method (Callable): The method that was originally called, and
                which instantiated this pager.
            request (google.ai.generativelanguage_v1beta.types.ListChunksRequest):
                The initial request object.
            response (google.ai.generativelanguage_v1beta.types.ListChunksResponse):
                The initial response object.
            retry (google.api_core.retry.AsyncRetry): Designation of what errors,
                if any, should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, Union[str, bytes]]]): Key/value pairs which should be
                sent along with the request as metadata. Normally, each value must be of type `str`,
                but for metadata keys ending with the suffix `-bin`, the corresponding values must
                be of type `bytes`.
        '''
        self._method = method
        self._request = retriever_service.ListChunksRequest(request)
        self._response = response
        self._retry = retry
        self._timeout = timeout
        self._metadata = metadata

    
    def __getattr__(self = None, name = None):
        return getattr(self._response, name)

    pages = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self = None):
        return '{0}<{1!r}>'.format(self.__class__.__name__, self._response)
