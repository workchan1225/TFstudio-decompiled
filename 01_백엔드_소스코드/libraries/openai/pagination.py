# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pagination.pyc (Python 3.11)

from typing import Any, List, Generic, TypeVar, Optional, cast
from typing_extensions import Protocol, override, runtime_checkable
from _base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage
__all__ = [
    'SyncPage',
    'AsyncPage',
    'SyncCursorPage',
    'AsyncCursorPage',
    'SyncConversationCursorPage',
    'AsyncConversationCursorPage']
_T = TypeVar('_T')
CursorPageItem = <NODE:12>()

def SyncPage():
    '''SyncPage'''
    object: str = 'Note: no pagination actually occurs yet, this is for forwards-compatibility.'
    _get_page_items = (lambda self = None: data = self.dataif not data:
[])()
    next_page_info = (lambda self = None: pass)()

SyncPage = <NODE:27>(SyncPage, 'SyncPage', BaseSyncPage[_T], BasePage[_T], Generic[_T])

def AsyncPage():
    '''AsyncPage'''
    object: str = 'Note: no pagination actually occurs yet, this is for forwards-compatibility.'
    _get_page_items = (lambda self = None: data = self.dataif not data:
[])()
    next_page_info = (lambda self = None: pass)()

AsyncPage = <NODE:27>(AsyncPage, 'AsyncPage', BaseAsyncPage[_T], BasePage[_T], Generic[_T])

def SyncCursorPage():
    '''SyncCursorPage'''
    pass
# WARNING: Decompyle incomplete

SyncCursorPage = <NODE:27>(SyncCursorPage, 'SyncCursorPage', BaseSyncPage[_T], BasePage[_T], Generic[_T])

def AsyncCursorPage():
    '''AsyncCursorPage'''
    pass
# WARNING: Decompyle incomplete

AsyncCursorPage = <NODE:27>(AsyncCursorPage, 'AsyncCursorPage', BaseAsyncPage[_T], BasePage[_T], Generic[_T])

def SyncConversationCursorPage():
    '''SyncConversationCursorPage'''
    pass
# WARNING: Decompyle incomplete

SyncConversationCursorPage = <NODE:27>(SyncConversationCursorPage, 'SyncConversationCursorPage', BaseSyncPage[_T], BasePage[_T], Generic[_T])

def AsyncConversationCursorPage():
    '''AsyncConversationCursorPage'''
    pass
# WARNING: Decompyle incomplete

AsyncConversationCursorPage = <NODE:27>(AsyncConversationCursorPage, 'AsyncConversationCursorPage', BaseAsyncPage[_T], BasePage[_T], Generic[_T])
