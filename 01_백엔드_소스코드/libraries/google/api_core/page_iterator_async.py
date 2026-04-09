# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: page_iterator_async.pyc (Python 3.11)

"""AsyncIO iterators for paging through paged API methods.

These iterators simplify the process of paging through API responses
where the request takes a page token and the response is a list of results with
a token for the next page. See `list pagination`_ in the Google API Style Guide
for more details.

.. _list pagination:
    https://cloud.google.com/apis/design/design_patterns#list_pagination

API clients that have methods that follow the list pagination pattern can
return an :class:`.AsyncIterator`:

    >>> results_iterator = await client.list_resources()

Or you can walk your way through items and call off the search early if
you find what you're looking for (resulting in possibly fewer requests)::

    >>> async for resource in results_iterator:
    ...     print(resource.name)
    ...     if not resource.is_valid:
    ...         break

At any point, you may check the number of items consumed by referencing the
``num_results`` property of the iterator::

    >>> async for my_item in results_iterator:
    ...     if results_iterator.num_results >= 10:
    ...         break

When iterating, not every new item will send a request to the server.
To iterate based on each page of items (where a page corresponds to
a request)::

    >>> async for page in results_iterator.pages:
    ...     print('=' * 20)
    ...     print('    Page number: {:d}'.format(iterator.page_number))
    ...     print('  Items in page: {:d}'.format(page.num_items))
    ...     print('     First item: {!r}'.format(next(page)))
    ...     print('Items remaining: {:d}'.format(page.remaining))
    ...     print('Next page token: {}'.format(iterator.next_page_token))
    ====================
        Page number: 1
      Items in page: 1
         First item: <MyItemClass at 0x7f1d3cccf690>
    Items remaining: 0
    Next page token: eav1OzQB0OM8rLdGXOEsyQWSG
    ====================
        Page number: 2
      Items in page: 19
         First item: <MyItemClass at 0x7f1d3cccffd0>
    Items remaining: 18
    Next page token: None
"""
import abc
from google.api_core.page_iterator import Page

def _item_to_value_identity(iterator, item):
    '''An item to value transformer that returns the item un-changed.'''
    return item


class AsyncIterator(abc.ABC):
    '''A generic class for iterating through API list responses.

    Args:
        client(google.cloud.client.Client): The API client.
        item_to_value (Callable[google.api_core.page_iterator_async.AsyncIterator, Any]):
            Callable to convert an item from the type in the raw API response
            into the native object. Will be called with the iterator and a
            single item.
        page_token (str): A token identifying a page in a result set to start
            fetching results from.
        max_results (int): The maximum number of results to fetch.
    '''
    
    def __init__(self, client, item_to_value, page_token, max_results = (_item_to_value_identity, None, None)):
        self._started = False
        self._AsyncIterator__active_aiterator = None
        self.client = client
        self.item_to_value = item_to_value
        self.max_results = max_results
        self.page_number = 0
        self.next_page_token = page_token
        self.num_results = 0

    pages = (lambda self: if self._started:
raise ValueError('Iterator has already started', self)self._started = Trueself._page_aiter(increment = True))()
    
    def _items_aiter(self):
        '''Iterator for each item returned.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __aiter__(self):
        '''Iterator for each item returned.

        Returns:
            types.GeneratorType[Any]: A generator of items from the API.

        Raises:
            ValueError: If the iterator has already been started.
        '''
        if self._started:
            raise ValueError('Iterator has already started', self)
        self._started = True
        return self._items_aiter()

    
    async def __anext__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _page_aiter(self, increment):
        '''Generator of pages of API responses.

        Args:
            increment (bool): Flag indicating if the total number of results
                should be incremented on each page. This is useful since a page
                iterator will want to increment by results per page while an
                items iterator will want to increment per item.

        Yields:
            Page: each page of items from the API.
        '''
        pass
    # WARNING: Decompyle incomplete

    _next_page = (lambda self: pass# WARNING: Decompyle incomplete
)()


class AsyncGRPCIterator(AsyncIterator):
    pass
# WARNING: Decompyle incomplete
