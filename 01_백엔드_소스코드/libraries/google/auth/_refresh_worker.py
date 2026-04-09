# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _refresh_worker.pyc (Python 3.11)

import copy
import logging
import threading

exceptions
logging.getLogger(__name__) = import google.auth.exceptions, auth

class RefreshThreadManager:
    '''
    Organizes exactly one background job that refresh a token.
    '''
    
    def __init__(self):
        '''Initializes the manager.'''
        self._worker = None
        self._lock = threading.Lock()

    
    def start_refresh(self, cred, request):
        '''Starts a refresh thread for the given credentials.
        The credentials are refreshed using the request parameter.
        request and cred MUST not be None

        Returns True if a background refresh was kicked off. False otherwise.

        Args:
            cred: A credentials object.
            request: A request object.
        Returns:
          bool
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def clear_error(self):
        '''
      Removes any errors that were stored from previous background refreshes.
      '''
        self._lock
        if self._worker:
            self._worker._error_info = None
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def __getstate__(self):
        '''Pickle helper that serializes the _lock attribute.'''
        state = self.__dict__.copy()
        state['_lock'] = None
        return state

    
    def __setstate__(self, state):
        '''Pickle helper that deserializes the _lock attribute.'''
        state['_lock'] = threading.Lock()
        self.__dict__.update(state)



class RefreshThread(threading.Thread):
    pass
# WARNING: Decompyle incomplete
