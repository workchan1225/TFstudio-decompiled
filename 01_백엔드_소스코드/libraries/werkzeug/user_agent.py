# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: user_agent.pyc (Python 3.11)

from __future__ import annotations

class UserAgent:
    '''Represents a parsed user agent header value.

    The default implementation does no parsing, only the :attr:`string`
    attribute is set. A subclass may parse the string to set the
    common attributes or expose other information. Set
    :attr:`werkzeug.wrappers.Request.user_agent_class` to use a
    subclass.

    :param string: The header value to parse.

    .. versionadded:: 2.0
        This replaces the previous ``useragents`` module, but does not
        provide a built-in parser.
    '''
    platform: 'str | None' = None
    browser: 'str | None' = None
    version: 'str | None' = None
    language: 'str | None' = None
    
    def __init__(self = None, string = None):
        self.string = string

    
    def __repr__(self = None):
        return f'''<{type(self).__name__} {self.browser}/{self.version}>'''

    
    def __str__(self = None):
        return self.string

    
    def __bool__(self = None):
        return bool(self.browser)

    
    def to_header(self = None):
        '''Convert to a header value.'''
        return self.string
