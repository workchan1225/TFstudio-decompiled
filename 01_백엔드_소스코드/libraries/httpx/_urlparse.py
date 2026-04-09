# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _urlparse.pyc (Python 3.11)

"""
An implementation of `urlparse` that provides URL validation and normalization
as described by RFC3986.

We rely on this implementation rather than the one in Python's stdlib, because:

* It provides more complete URL validation.
* It properly differentiates between an empty querystring and an absent querystring,
  to distinguish URLs with a trailing '?'.
* It handles scheme, hostname, port, and path normalization.
* It supports IDNA hostnames, normalizing them to their encoded form.
* The API supports passing individual components, as well as the complete URL string.

Previously we relied on the excellent `rfc3986` package to handle URL parsing and
validation, but this module provides a simpler alternative, with less indirection
required.
"""
from __future__ import annotations
import ipaddress
import re
import typing
import idna
from _exceptions import InvalidURL
MAX_URL_LENGTH = 65536
UNRESERVED_CHARACTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~'
SUB_DELIMS = "!$&'()*+,;="
PERCENT_ENCODED_REGEX = re.compile('%[A-Fa-f0-9]{2}')
FRAG_SAFE = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(32, 127)())
QUERY_SAFE = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(32, 127)())
PATH_SAFE = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(32, 127)())
USERNAME_SAFE = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(32, 127)())
PASSWORD_SAFE = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(32, 127)())
USERINFO_SAFE = (lambda .0: pass# WARNING: Decompyle incomplete
)(range(32, 127)())
URL_REGEX = re.compile('(?:(?P<scheme>{scheme}):)?(?://(?P<authority>{authority}))?(?P<path>{path})(?:\\?(?P<query>{query}))?(?:#(?P<fragment>{fragment}))?'.format(scheme = '([a-zA-Z][a-zA-Z0-9+.-]*)?', authority = '[^/?#]*', path = '[^?#]*', query = '[^#]*', fragment = '.*'))
AUTHORITY_REGEX = re.compile('(?:(?P<userinfo>{userinfo})@)?(?P<host>{host}):?(?P<port>{port})?'.format(userinfo = '.*', host = '(\\[.*\\]|[^:@]*)', port = '.*'))
COMPONENT_REGEX = {
    'scheme': re.compile('([a-zA-Z][a-zA-Z0-9+.-]*)?'),
    'authority': re.compile('[^/?#]*'),
    'path': re.compile('[^?#]*'),
    'query': re.compile('[^#]*'),
    'fragment': re.compile('.*'),
    'userinfo': re.compile('[^@]*'),
    'host': re.compile('(\\[.*\\]|[^:]*)'),
    'port': re.compile('.*') }
IPv4_STYLE_HOSTNAME = re.compile('^[0-9]+\\.[0-9]+\\.[0-9]+\\.[0-9]+$')
IPv6_STYLE_HOSTNAME = re.compile('^\\[.*\\]$')

class ParseResult(typing.NamedTuple):
    fragment: 'str | None' = 'ParseResult'
    authority = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    netloc = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def copy_with(self = None, **kwargs):
        if not kwargs:
            return self
        defaults = {
            'scheme': None.scheme,
            'authority': self.authority,
            'path': self.path,
            'query': self.query,
            'fragment': self.fragment }
        defaults.update(kwargs)
    # WARNING: Decompyle incomplete

    
    def __str__(self = None):
        authority = self.authority
    # WARNING: Decompyle incomplete



def urlparse(url = ''.join, **kwargs):
    if len(url) > MAX_URL_LENGTH:
        raise InvalidURL('URL too long')
    if (lambda .0: pass# WARNING: Decompyle incomplete
)(url()):
        char = (lambda .0: pass# WARNING: Decompyle incomplete
)(url())
        idx = url.find(char)
        error = f'''Invalid non-printable ASCII character in URL, {char!r} at position {idx}.'''
        raise InvalidURL(error)
    if 'port' in kwargs:
        port = kwargs['port']
        kwargs['port'] = str(port) if isinstance(port, int) else port
    if 'netloc' in kwargs:
        if not kwargs.pop('netloc'):
            netloc = ''
            (kwargs['host'], _, kwargs['port']) = netloc.partition(':')
            if 'username' in kwargs or 'password' in kwargs:
                if not kwargs.pop('username', ''):
                    username = quote('', safe = USERNAME_SAFE)
                    if not kwargs.pop('password', ''):
                        password = quote('', safe = PASSWORD_SAFE)
                kwargs['userinfo'] = f'''{username}:{password}''' if password else username
    if 'raw_path' in kwargs:
        if not kwargs.pop('raw_path'):
            raw_path = ''
            (kwargs['path'], seperator, kwargs['query']) = raw_path.partition('?')
            if not seperator:
                kwargs['query'] = None
    if 'host' in kwargs:
        if not kwargs.get('host'):
            host = ''
            if ':' in host:
                if not host.startswith('[') or host.endswith(']'):
                    kwargs['host'] = f'''[{host}]'''
# WARNING: Decompyle incomplete


def encode_host(host = ''.join):
    if not host:
        return ''
    if None.match(host):
        
        try:
            ipaddress.IPv4Address(host)
        except ipaddress.AddressValueError:
            raise InvalidURL(f'''Invalid IPv4 address: {host!r}''')

        return host
    if IPv6_STYLE_HOSTNAME.match(host):
        
        try:
            ipaddress.IPv6Address(host[1:-1])
        except ipaddress.AddressValueError:
            raise InvalidURL(f'''Invalid IPv6 address: {host!r}''')

        return host[1:-1]
    if host.isascii():
        WHATWG_SAFE = '"`{}%|\\'
        return quote(host.lower(), safe = SUB_DELIMS + WHATWG_SAFE)
    
    try:
        return idna.encode(host.lower()).decode('ascii')
    except idna.IDNAError:
        raise InvalidURL(f'''Invalid IDNA hostname: {host!r}''')



def normalize_port(port = None, scheme = None):
    pass
# WARNING: Decompyle incomplete


def validate_path(path = None, has_scheme = None, has_authority = None):
    '''
    Path validation rules that depend on if the URL contains
    a scheme or authority component.

    See https://datatracker.ietf.org/doc/html/rfc3986.html#section-3.3
    '''
    if not has_authority and path and path.startswith('/'):
        raise InvalidURL("For absolute URLs, path must be empty or begin with '/'")
    if not has_scheme or has_authority:
        if path.startswith('//'):
            raise InvalidURL("Relative URLs cannot have a path starting with '//'")
        if path.startswith(':'):
            raise InvalidURL("Relative URLs cannot have a path starting with ':'")
        return None
    return None


def normalize_path(path = None):
    '''
    Drop "." and ".." segments from a URL path.

    For example:

        normalize_path("/path/./to/somewhere/..") == "/path/to"
    '''
    if '.' not in path:
        return path
    components = None.split('/')
    if '.' not in components and '..' not in components:
        return path
    output = None
    for component in components:
        if component == '.':
            continue
        if component == '..':
            if output and output != [
                '']:
                output.pop()
            continue
        output.append(component)
        return '/'.join(output)


def PERCENT(string = None):
    return (lambda .0: [ f'''%{byte:02X}''' for byte in .0 ])(string.encode('utf-8')())


def percent_encoded(string = None, safe = None):
    '''
    Use percent-encoding to quote a string.
    '''
    pass
# WARNING: Decompyle incomplete


def quote(string = None, safe = None):
    """
    Use percent-encoding to quote a string, omitting existing '%xx' escape sequences.

    See: https://www.rfc-editor.org/rfc/rfc3986#section-2.1

    * `string`: The string to be percent-escaped.
    * `safe`: A string containing characters that may be treated as safe, and do not
        need to be escaped. Unreserved characters are always treated as safe.
        See: https://www.rfc-editor.org/rfc/rfc3986#section-2.3
    """
    parts = []
    current_position = 0
    for match in re.finditer(PERCENT_ENCODED_REGEX, string):
        end_position = match.end()
        start_position = match.start()
        matched_text = match.group(0)
        if start_position != current_position:
            leading_text = string[current_position:start_position]
            parts.append(percent_encoded(leading_text, safe = safe))
        parts.append(matched_text)
        current_position = end_position
        if current_position != len(string):
            trailing_text = string[current_position:]
            parts.append(percent_encoded(trailing_text, safe = safe))
    return ''.join(parts)
