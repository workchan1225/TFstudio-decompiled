# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _cookie_helpers.pyc (Python 3.11)

'''
Internal cookie handling helpers.

This module contains internal utilities for cookie parsing and manipulation.
These are not part of the public API and may change without notice.
'''
import re
from http.cookies import Morsel
from typing import List, Optional, Sequence, Tuple, cast
from log import internal_logger
__all__ = ('parse_set_cookie_headers', 'parse_cookie_header', 'preserve_morsel_with_coded_value')
_COOKIE_NAME_RE = re.compile("^[!#$%&\\'()*+\\-./0-9:<=>?@A-Z\\[\\]^_`a-z{|}~]+$")
_COOKIE_KNOWN_ATTRS = frozenset(('path', 'domain', 'max-age', 'expires', 'secure', 'httponly', 'samesite', 'partitioned', 'version', 'comment'))
_COOKIE_BOOL_ATTRS = frozenset(('secure', 'httponly', 'partitioned'))
_COOKIE_PATTERN = re.compile('\n    \\s*                            # Optional whitespace at start of cookie\n    (?P<key>                       # Start of group \'key\'\n    # aiohttp has extended to include [] for compatibility with real-world cookies\n    [\\w\\d!#%&\'~_`><@,:/\\$\\*\\+\\-\\.\\^\\|\\)\\(\\?\\}\\{\\=\\[\\]]+?   # Any word of at least one letter\n    )                              # End of group \'key\'\n    (                              # Optional group: there may not be a value.\n    \\s*=\\s*                          # Equal Sign\n    (?P<val>                         # Start of group \'val\'\n    "(?:[^\\\\"]|\\\\.)*"                  # Any double-quoted string (properly closed)\n    |                                  # or\n    "[^";]*                            # Unmatched opening quote (differs from SimpleCookie - issue #7993)\n    |                                  # or\n    # Special case for "expires" attr - RFC 822, RFC 850, RFC 1036, RFC 1123\n    (\\w{3,6}day|\\w{3}),\\s              # Day of the week or abbreviated day (with comma)\n    [\\w\\d\\s-]{9,11}\\s[\\d:]{8}\\s        # Date and time in specific format\n    (GMT|[+-]\\d{4})                     # Timezone: GMT or RFC 2822 offset like -0000, +0100\n                                        # NOTE: RFC 2822 timezone support is an aiohttp extension\n                                        # for issue #4493 - SimpleCookie does NOT support this\n    |                                  # or\n    # ANSI C asctime() format: "Wed Jun  9 10:18:14 2021"\n    # NOTE: This is an aiohttp extension for issue #4327 - SimpleCookie does NOT support this format\n    \\w{3}\\s+\\w{3}\\s+[\\s\\d]\\d\\s+\\d{2}:\\d{2}:\\d{2}\\s+\\d{4}\n    |                                  # or\n    [\\w\\d!#%&\'~_`><@,:/\\$\\*\\+\\-\\.\\^\\|\\)\\(\\?\\}\\{\\=\\[\\]]*      # Any word or empty string\n    )                                # End of group \'val\'\n    )?                             # End of optional value group\n    \\s*                            # Any number of spaces.\n    (\\s+|;|$)                      # Ending either at space, semicolon, or EOS.\n    ', re.VERBOSE | re.ASCII)

def preserve_morsel_with_coded_value(cookie = None):
    """
    Preserve a Morsel's coded_value exactly as received from the server.

    This function ensures that cookie encoding is preserved exactly as sent by
    the server, which is critical for compatibility with old servers that have
    strict requirements about cookie formats.

    This addresses the issue described in https://github.com/aio-libs/aiohttp/pull/1453
    where Python's SimpleCookie would re-encode cookies, breaking authentication
    with certain servers.

    Args:
        cookie: A Morsel object from SimpleCookie

    Returns:
        A Morsel object with preserved coded_value

    """
    mrsl_val = cast('Morsel[str]', cookie.get(cookie.key, Morsel()))
    mrsl_val.__setstate__({
        'key': cookie.key,
        'value': cookie.value,
        'coded_value': cookie.coded_value })
    return mrsl_val

_unquote_sub = re.compile('\\\\(?:([0-3][0-7][0-7])|(.))').sub

def _unquote_replace(m = None):
    '''
    Replace function for _unquote_sub regex substitution.

    Handles escaped characters in cookie values:
    - Octal sequences are converted to their character representation
    - Other escaped characters are unescaped by removing the backslash
    '''
    if m[1]:
        return chr(int(m[1], 8))
    return None[2]


def _unquote(value = None):
    """
    Unquote a cookie value.

    Vendored from http.cookies._unquote to ensure compatibility.

    Note: The original implementation checked for None, but we've removed
    that check since all callers already ensure the value is not None.
    """
    if len(value) < 2:
        return value
    if None[0] != '"' or value[-1] != '"':
        return value
    value = None[1:-1]
    return _unquote_sub(_unquote_replace, value)


def parse_cookie_header(header = None):
    """
    Parse a Cookie header according to RFC 6265 Section 5.4.

    Cookie headers contain only name-value pairs separated by semicolons.
    There are no attributes in Cookie headers - even names that match
    attribute names (like 'path' or 'secure') should be treated as cookies.

    This parser uses the same regex-based approach as parse_set_cookie_headers
    to properly handle quoted values that may contain semicolons. When the
    regex fails to match a malformed cookie, it falls back to simple parsing
    to ensure subsequent cookies are not lost
    https://github.com/aio-libs/aiohttp/issues/11632

    Args:
        header: The Cookie header value to parse

    Returns:
        List of (name, Morsel) tuples for compatibility with SimpleCookie.update()
    """
    if not header:
        return []
    cookies = None
    i = 0
    n = len(header)
# WARNING: Decompyle incomplete


def parse_set_cookie_headers(headers = None):
    '''
    Parse cookie headers using a vendored version of SimpleCookie parsing.

    This implementation is based on SimpleCookie.__parse_string to ensure
    compatibility with how SimpleCookie parses cookies, including handling
    of malformed cookies with missing semicolons.

    This function is used for both Cookie and Set-Cookie headers in order to be
    forgiving. Ideally we would have followed RFC 6265 Section 5.2 (for Cookie
    headers) and RFC 6265 Section 4.2.1 (for Set-Cookie headers), but the
    real world data makes it impossible since we need to be a bit more forgiving.

    NOTE: This implementation differs from SimpleCookie in handling unmatched quotes.
    SimpleCookie will stop parsing when it encounters a cookie value with an unmatched
    quote (e.g., \'cookie="value\'), causing subsequent cookies to be silently dropped.
    This implementation handles unmatched quotes more gracefully to prevent cookie loss.
    See https://github.com/aio-libs/aiohttp/issues/7993
    '''
    parsed_cookies = []
# WARNING: Decompyle incomplete
