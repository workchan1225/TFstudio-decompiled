# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pagers.pyc (Python 3.11)

'''Pagers for the GenAI List APIs.'''
import copy
from typing import Any, AsyncIterator, Awaitable, Callable, Generic, Iterator, Literal, TypeVar, Union
from  import _common
from  import types
T = TypeVar('T')
PagedItem = Literal[('batch_jobs', 'models', 'tuning_jobs', 'files', 'cached_contents', 'file_search_stores', 'documents')]

def _BasePager():
    '''_BasePager'''
    __doc__ = 'Base pager class for iterating through paginated results.'
    
    def _init_page(self, name = None, request = None, response = None, config = ('name', PagedItem, 'request', Callable[(..., Any)], 'response', Any, 'config', Any, 'return', None)):
        self._name = name
        self._request = request
        if not getattr(response, self._name):
            self._page = []
            self._idx = 0
            self._sdk_http_response = getattr(response, 'sdk_http_response', None)
            if not config:
                request_config = { }
            elif isinstance(config, dict):
                request_config = copy.deepcopy(config)
            else:
                request_config = dict(config)
        request_config['page_token'] = getattr(response, 'next_page_token')
        self._config = request_config
        self._page_size = request_config.get('page_size', len(self._page))

    
    def __init__(self, name = None, request = None, response = None, config = ('name', PagedItem, 'request', Callable[(..., Any)], 'response', Any, 'config', Any)):
        self._init_page(name, request, response, config)

    page = (lambda self = None: self._page)()
    name = (lambda self = None: self._name)()
    page_size = (lambda self = None: self._page_size)()
    sdk_http_response = (lambda self = None: self._sdk_http_response)()
    config = (lambda self = None: self._config)()
    
    def __len__(self = None):
        '''Returns the total number of items in the current page.'''
        return len(self.page)

    
    def __getitem__(self = None, index = None):
        '''Returns the item at the given index.'''
        return self.page[index]

    
    def _init_next_page(self = None, response = None):
        '''Initializes the next page from the response.

    This is an internal method that should be called by subclasses after
    fetching the next page.

    Args:
      response: The response object from the API request.
    '''
        self._init_page(self.name, self._request, response, self.config)


_BasePager = <NODE:27>(_BasePager, '_BasePager', Generic[T])

def Pager():
    '''Pager'''
    __doc__ = 'Pager class for iterating through paginated results.'
    
    def __next__(self = None):
        '''Returns the next item.'''
        if self._idx >= len(self):
            
            try:
                self.next_page()
            except IndexError:
                raise StopIteration

            item = self.page[self._idx]
            return item

    
    def __iter__(self = None):
        '''Returns an iterator over the items.'''
        self._idx = 0
        return self

    
    def next_page(self = None):
        '''Fetches the next page of items. This makes a new API request.

    Usage:

    .. code-block:: python

      batch_jobs_pager = client.batches.list(config={\'page_size\': 5})
      print(f"current page: {batch_jobs_pager.page}")
      batch_jobs_pager.next_page()
      print(f"next page: {batch_jobs_pager.page}")
      # current page: [BatchJob(name=\'projects/.../batchPredictionJobs/1
      # next page: [BatchJob(name=\'projects/.../batchPredictionJobs/6
    '''
        if not self.config.get('page_token'):
            raise IndexError('No more pages to fetch.')
        response = self._request(config = self.config)
        self._init_next_page(response)
        return self.page


Pager = <NODE:27>(Pager, 'Pager', _BasePager[T])

def AsyncPager():
    '''AsyncPager'''
    pass
# WARNING: Decompyle incomplete

AsyncPager = <NODE:27>(AsyncPager, 'AsyncPager', _BasePager[T])
