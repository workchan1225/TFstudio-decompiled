# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: storage.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING, Any
from selenium.webdriver.common.bidi.common import command_builder
if TYPE_CHECKING:
    from selenium.webdriver.remote.websocket_connection import WebSocketConnection

class SameSite:
    '''Represents the possible same site values for cookies.'''
    STRICT = 'strict'
    LAX = 'lax'
    NONE = 'none'
    DEFAULT = 'default'


class BytesValue:
    '''Represents a bytes value.'''
    TYPE_BASE64 = 'base64'
    TYPE_STRING = 'string'
    
    def __init__(self = None, type = None, value = None):
        self.type = type
        self.value = value

    
    def to_dict(self = None):
        '''Converts the BytesValue to a dictionary.

        Returns:
            A dictionary representation of the BytesValue.
        '''
        return {
            'type': self.type,
            'value': self.value }



class Cookie:
    '''Represents a cookie.'''
    
    def __init__(self, name, value, domain, path, size = None, http_only = None, secure = None, same_site = (None, None, None, None, None, None), expiry = ('name', 'str', 'value', 'BytesValue', 'domain', 'str', 'path', 'str | None', 'size', 'int | None', 'http_only', 'bool | None', 'secure', 'bool | None', 'same_site', 'str | None', 'expiry', 'int | None')):
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.size = size
        self.http_only = http_only
        self.secure = secure
        self.same_site = same_site
        self.expiry = expiry

    from_dict = (lambda cls = None, data = None: name = data.get('name')if not name:
raise ValueError('name is required and cannot be empty')domain = data.get('domain')if not domain:
raise ValueError('domain is required and cannot be empty')value = BytesValue(data.get('value', { }).get('type'), data.get('value', { }).get('value'))cls(name = str(name), value = value, domain = str(domain), path = data.get('path'), size = data.get('size'), http_only = data.get('httpOnly'), secure = data.get('secure'), same_site = data.get('sameSite'), expiry = data.get('expiry')))()


class CookieFilter:
    '''Represents a filter for cookies.'''
    
    def __init__(self, name, value, domain, path, size = None, http_only = None, secure = None, same_site = (None, None, None, None, None, None, None, None, None), expiry = ('name', 'str | None', 'value', 'BytesValue | None', 'domain', 'str | None', 'path', 'str | None', 'size', 'int | None', 'http_only', 'bool | None', 'secure', 'bool | None', 'same_site', 'str | None', 'expiry', 'int | None')):
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.size = size
        self.http_only = http_only
        self.secure = secure
        self.same_site = same_site
        self.expiry = expiry

    
    def to_dict(self = None):
        '''Converts the CookieFilter to a dictionary.

        Returns:
            A dictionary representation of the CookieFilter.
        '''
        result = { }
    # WARNING: Decompyle incomplete



class PartitionKey:
    '''Represents a storage partition key.'''
    
    def __init__(self = None, user_context = None, source_origin = None):
        self.user_context = user_context
        self.source_origin = source_origin

    from_dict = (lambda cls = None, data = None: cls(user_context = data.get('userContext'), source_origin = data.get('sourceOrigin')))()


class BrowsingContextPartitionDescriptor:
    '''Represents a browsing context partition descriptor.'''
    
    def __init__(self = None, context = None):
        self.type = 'context'
        self.context = context

    
    def to_dict(self = None):
        '''Converts the BrowsingContextPartitionDescriptor to a dictionary.

        Returns:
            Dict: A dictionary representation of the BrowsingContextPartitionDescriptor.
        '''
        return {
            'type': self.type,
            'context': self.context }



class StorageKeyPartitionDescriptor:
    '''Represents a storage key partition descriptor.'''
    
    def __init__(self = None, user_context = None, source_origin = None):
        self.type = 'storageKey'
        self.user_context = user_context
        self.source_origin = source_origin

    
    def to_dict(self = None):
        '''Converts the StorageKeyPartitionDescriptor to a dictionary.

        Returns:
            Dict: A dictionary representation of the StorageKeyPartitionDescriptor.
        '''
        result = {
            'type': self.type }
    # WARNING: Decompyle incomplete



class PartialCookie:
    '''Represents a partial cookie for setting.'''
    
    def __init__(self, name, value, domain, path = None, http_only = None, secure = None, same_site = (None, None, None, None, None), expiry = ('name', 'str', 'value', 'BytesValue', 'domain', 'str', 'path', 'str | None', 'http_only', 'bool | None', 'secure', 'bool | None', 'same_site', 'str | None', 'expiry', 'int | None')):
        self.name = name
        self.value = value
        self.domain = domain
        self.path = path
        self.http_only = http_only
        self.secure = secure
        self.same_site = same_site
        self.expiry = expiry

    
    def to_dict(self = None):
        '''Converts the PartialCookie to a dictionary.

        Returns:
        -------
            Dict: A dictionary representation of the PartialCookie.
        '''
        result = {
            'name': self.name,
            'value': self.value.to_dict(),
            'domain': self.domain }
    # WARNING: Decompyle incomplete



class GetCookiesResult:
    '''Represents the result of a getCookies command.'''
    
    def __init__(self = None, cookies = None, partition_key = None):
        self.cookies = cookies
        self.partition_key = partition_key

    from_dict = (lambda cls = None, data = None: cookies = data.get('cookies', [])()partition_key = PartitionKey.from_dict(data.get('partitionKey', { }))cls(cookies = cookies, partition_key = partition_key))()


class SetCookieResult:
    '''Represents the result of a setCookie command.'''
    
    def __init__(self = None, partition_key = None):
        self.partition_key = partition_key

    from_dict = (lambda cls = None, data = None: partition_key = PartitionKey.from_dict(data.get('partitionKey', { }))cls(partition_key = partition_key))()


class DeleteCookiesResult:
    '''Represents the result of a deleteCookies command.'''
    
    def __init__(self = None, partition_key = None):
        self.partition_key = partition_key

    from_dict = (lambda cls = None, data = None: partition_key = PartitionKey.from_dict(data.get('partitionKey', { }))cls(partition_key = partition_key))()


class Storage:
    '''BiDi implementation of the storage module.'''
    
    def __init__(self = None, conn = None):
        self.conn = conn

    
    def get_cookies(self = None, filter = None, partition = None):
        '''Gets cookies matching the specified filter.

        Args:
            filter: Optional filter to specify which cookies to retrieve.
            partition: Optional partition key to limit the scope of the operation.

        Returns:
            A GetCookiesResult containing the cookies and partition key.

        Example:
            result = await storage.get_cookies(
                filter=CookieFilter(name="sessionId"),
                partition=PartitionKey(...)
            )
        '''
        params = { }
    # WARNING: Decompyle incomplete

    
    def set_cookie(self = None, cookie = None, partition = None):
        '''Sets a cookie in the browser.

        Args:
            cookie: The cookie to set.
            partition: Optional partition descriptor.

        Returns:
            The result of the set cookie command.
        '''
        params = {
            'cookie': cookie.to_dict() }
    # WARNING: Decompyle incomplete

    
    def delete_cookies(self = None, filter = None, partition = None):
        '''Deletes cookies that match the given parameters.

        Args:
            filter: Optional filter to match cookies to delete.
            partition: Optional partition descriptor.

        Returns:
            The result of the delete cookies command.
        '''
        params = { }
    # WARNING: Decompyle incomplete
