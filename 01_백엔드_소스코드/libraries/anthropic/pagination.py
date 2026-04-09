# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pagination.pyc (Python 3.11)

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override
from _base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage
__all__ = [
    'SyncPage',
    'AsyncPage',
    'SyncTokenPage',
    'AsyncTokenPage',
    'SyncPageCursor',
    'AsyncPageCursor']
_T = TypeVar('_T')

def SyncPage():
    '''SyncPage'''
    pass
# WARNING: Decompyle incomplete

SyncPage = <NODE:27>(SyncPage, 'SyncPage', BaseSyncPage[_T], BasePage[_T], Generic[_T])

def AsyncPage():
    '''AsyncPage'''
    pass
# WARNING: Decompyle incomplete

AsyncPage = <NODE:27>(AsyncPage, 'AsyncPage', BaseAsyncPage[_T], BasePage[_T], Generic[_T])

def SyncTokenPage():
    '''SyncTokenPage'''
    pass
# WARNING: Decompyle incomplete

SyncTokenPage = <NODE:27>(SyncTokenPage, 'SyncTokenPage', BaseSyncPage[_T], BasePage[_T], Generic[_T])

def AsyncTokenPage():
    '''AsyncTokenPage'''
    pass
# WARNING: Decompyle incomplete

AsyncTokenPage = <NODE:27>(AsyncTokenPage, 'AsyncTokenPage', BaseAsyncPage[_T], BasePage[_T], Generic[_T])

def SyncPageCursor():
    '''SyncPageCursor'''
    pass
# WARNING: Decompyle incomplete

SyncPageCursor = <NODE:27>(SyncPageCursor, 'SyncPageCursor', BaseSyncPage[_T], BasePage[_T], Generic[_T])

def AsyncPageCursor():
    '''AsyncPageCursor'''
    pass
# WARNING: Decompyle incomplete

AsyncPageCursor = <NODE:27>(AsyncPageCursor, 'AsyncPageCursor', BaseAsyncPage[_T], BasePage[_T], Generic[_T])
