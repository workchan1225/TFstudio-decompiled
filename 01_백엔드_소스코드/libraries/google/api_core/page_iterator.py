# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: page_iterator.pyc (Python 3.11)

"""Iterators for paging through paged API methods.

These iterators simplify the process of paging through API responses
where the request takes a page token and the response is a list of results with
a token for the next page. See `list pagination`_ in the Google API Style Guide
for more details.

.. _list pagination:
    https://cloud.google.com/apis/design/design_patterns#list_pagination

API clients that have methods that follow the list pagination pattern can
return an :class:`.Iterator`. You can use this iterator to get **all** of
the results across all pages::

    >>> results_iterator = client.list_resources()
    >>> list(results_iterator)  # Convert to a list (consumes all values).

Or you can walk your way through items and call off the search early if
you find what you're looking for (resulting in possibly fewer requests)::

    >>> for resource in results_iterator:
    ...     print(resource.name)
    ...     if not resource.is_valid:
    ...         break

At any point, you may check the number of items consumed by referencing the
``num_results`` property of the iterator::

    >>> for my_item in results_iterator:
    ...     if results_iterator.num_results >= 10:
    ...         break

When iterating, not every new item will send a request to the server.
To iterate based on each page of items (where a page corresponds to
a request)::

    >>> for page in results_iterator.pages:
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

Then, for each page you can get all the resources on that page by iterating
through it or using :func:`list`::

    >>> list(page)
    [
        <MyItemClass at 0x7fd64a098ad0>,
        <MyItemClass at 0x7fd64a098ed0>,
        <MyItemClass at 0x7fd64a098e90>,
    ]
"""
import abc

class Page(object):
    '''Single page of results in an iterator.

    Args:
        parent (google.api_core.page_iterator.Iterator): The iterator that owns
            the current page.
        items (Sequence[Any]): An iterable (that also defines __len__) of items
            from a raw API response.
        item_to_value (Callable[google.api_core.page_iterator.Iterator, Any]):
            Callable to convert an item from the type in the raw API response
            into the native object. Will be called with the iterator and a
            single item.
        raw_page Optional[google.protobuf.message.Message]:
            The raw page response.
    '''
    
    def __init__(self, parent, items, item_to_value, raw_page = (None,)):
        self._parent = parent
        self._num_items = len(items)
        self._remaining = self._num_items
        self._item_iter = iter(items)
        self._item_to_value = item_to_value
        self._raw_page = raw_page

    raw_page = (lambda self: self._raw_page)()
    num_items = (lambda self: self._num_items)()
    remaining = (lambda self: self._remaining)()
    
    def __iter__(self):
        '''The :class:`Page` is an iterator of items.'''
        return self

    
    def __next__(self):
        '''Get the next value in the page.'''
        item = next(self._item_iter)
        result = self._item_to_value(self._parent, item)
        return result



def _item_to_value_identity(iterator, item):
    '''An item to value transformer that returns the item un-changed.'''
    return item


def Iterator():
    '''Iterator'''
    __doc__ = 'A generic class for iterating through API list responses.\n\n    Args:\n        client(google.cloud.client.Client): The API client.\n        item_to_value (Callable[google.api_core.page_iterator.Iterator, Any]):\n            Callable to convert an item from the type in the raw API response\n            into the native object. Will be called with the iterator and a\n            single item.\n        page_token (str): A token identifying a page in a result set to start\n            fetching results from.\n        max_results (int): The maximum number of results to fetch.\n    '
    
    def __init__(self, client, item_to_value, page_token, max_results = (_item_to_value_identity, None, None)):
        self._started = False
        self._Iterator__active_iterator = None
        self.client = client
        self.item_to_value = item_to_value
        self.max_results = max_results
        self.page_number = 0
        self.next_page_token = page_token
        self.num_results = 0

    pages = (lambda self: if self._started:
raise ValueError('Iterator has already started', self)self._started = Trueself._page_iter(increment = True))()
    
    def _items_iter(self):
        '''Iterator for each item returned.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __iter__(self):
        '''Iterator for each item returned.

        Returns:
            types.GeneratorType[Any]: A generator of items from the API.

        Raises:
            ValueError: If the iterator has already been started.
        '''
        if self._started:
            raise ValueError('Iterator has already started', self)
        self._started = True
        return self._items_iter()

    
    def __next__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def _page_iter(self, increment):
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

    _next_page = (lambda self: raise NotImplementedError)()

Iterator = <NODE:27>(Iterator, 'Iterator', object, metaclass = abc.ABCMeta)

def _do_nothing_page_start(iterator, page, response):
    '''Helper to provide custom behavior after a :class:`Page` is started.

    This is a do-nothing stand-in as the default value.

    Args:
        iterator (Iterator): An iterator that holds some request info.
        page (Page): The page that was just created.
        response (Any): The API response for a page.
    '''
    pass


class HTTPIterator(Iterator):
    pass
# WARNING: Decompyle incomplete


class _GAXIterator(Iterator):
    pass
# WARNING: Decompyle incomplete


class GRPCIterator(Iterator):
    pass
# WARNING: Decompyle incomplete
