# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: headers.pyc (Python 3.11)

from __future__ import annotations
import base64
import binascii
import ipaddress
import re
from collections.abc import Sequence
from typing import Callable, TypeVar, cast
from exceptions import InvalidHeaderFormat, InvalidHeaderValue
from typing import ConnectionOption, ExtensionHeader, ExtensionName, ExtensionParameter, Subprotocol, UpgradeProtocol
__all__ = [
    'build_host',
    'parse_connection',
    'parse_upgrade',
    'parse_extension',
    'build_extension',
    'parse_subprotocol',
    'build_subprotocol',
    'validate_subprotocols',
    'build_www_authenticate_basic',
    'parse_authorization_basic',
    'build_authorization_basic']
T = TypeVar('T')

def build_host(host = None, port = None, secure = None, *, always_include_port):
    '''
    Build a ``Host`` header.

    '''
    
    try:
        address = ipaddress.ip_address(host)
        if address.version == 6:
            host = f'''[{host}]'''
        else:
            except ValueError:
                pass
            if always_include_port or port != 443 if secure else 80:
                host = f'''{host}:{port}'''

    return host


def peek_ahead(header = None, pos = None):
    '''
    Return the next character from ``header`` at the given position.

    Return :obj:`None` at the end of ``header``.

    We never need to peek more than one character ahead.

    '''
    return None if pos == len(header) else header[pos]

_OWS_re = re.compile('[\\t ]*')

def parse_OWS(header = None, pos = None):
    """
    Parse optional whitespace from ``header`` at the given position.

    Return the new position.

    The whitespace itself isn't returned because it isn't significant.

    """
    match = _OWS_re.match(header, pos)
# WARNING: Decompyle incomplete

_token_re = re.compile("[-!#$%&\\'*+.^_`|~0-9a-zA-Z]+")

def parse_token(header = None, pos = None, header_name = None):
    '''
    Parse a token from ``header`` at the given position.

    Return the token value and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    match = _token_re.match(header, pos)
# WARNING: Decompyle incomplete

_quoted_string_re = re.compile('"(?:[\\x09\\x20-\\x21\\x23-\\x5b\\x5d-\\x7e]|\\\\[\\x09\\x20-\\x7e\\x80-\\xff])*"')
_unquote_re = re.compile('\\\\([\\x09\\x20-\\x7e\\x80-\\xff])')

def parse_quoted_string(header = None, pos = None, header_name = None):
    '''
    Parse a quoted string from ``header`` at the given position.

    Return the unquoted value and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    match = _quoted_string_re.match(header, pos)
# WARNING: Decompyle incomplete

_quotable_re = re.compile('[\\x09\\x20-\\x7e\\x80-\\xff]*')
_quote_re = re.compile('([\\x22\\x5c])')

def build_quoted_string(value = None):
    '''
    Format ``value`` as a quoted string.

    This is the reverse of :func:`parse_quoted_string`.

    '''
    match = _quotable_re.fullmatch(value)
# WARNING: Decompyle incomplete


def parse_list(parse_item = None, header = None, pos = None, header_name = ('parse_item', 'Callable[[str, int, str], tuple[T, int]]', 'header', 'str', 'pos', 'int', 'header_name', 'str', 'return', 'list[T]')):
    '''
    Parse a comma-separated list from ``header`` at the given position.

    This is appropriate for parsing values with the following grammar:

        1#item

    ``parse_item`` parses one item.

    ``header`` is assumed not to start or end with whitespace.

    (This function is designed for parsing an entire header value and
    :func:`~websockets.http.read_headers` strips whitespace from values.)

    Return a list of items.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    pass
# WARNING: Decompyle incomplete


def parse_connection_option(header = None, pos = None, header_name = None):
    '''
    Parse a Connection option from ``header`` at the given position.

    Return the protocol value and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    (item, pos) = parse_token(header, pos, header_name)
    return (cast(ConnectionOption, item), pos)


def parse_connection(header = None):
    '''
    Parse a ``Connection`` header.

    Return a list of HTTP connection options.

    Args
        header: value of the ``Connection`` header.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    return parse_list(parse_connection_option, header, 0, 'Connection')

_protocol_re = re.compile("[-!#$%&\\'*+.^_`|~0-9a-zA-Z]+(?:/[-!#$%&\\'*+.^_`|~0-9a-zA-Z]+)?")

def parse_upgrade_protocol(header = None, pos = None, header_name = None):
    '''
    Parse an Upgrade protocol from ``header`` at the given position.

    Return the protocol value and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    match = _protocol_re.match(header, pos)
# WARNING: Decompyle incomplete


def parse_upgrade(header = None):
    '''
    Parse an ``Upgrade`` header.

    Return a list of HTTP protocols.

    Args:
        header: Value of the ``Upgrade`` header.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    return parse_list(parse_upgrade_protocol, header, 0, 'Upgrade')


def parse_extension_item_param(header = None, pos = None, header_name = None):
    '''
    Parse a single extension parameter from ``header`` at the given position.

    Return a ``(name, value)`` pair and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    (name, pos) = parse_token(header, pos, header_name)
    pos = parse_OWS(header, pos)
    value = None
# WARNING: Decompyle incomplete


def parse_extension_item(header = None, pos = None, header_name = None):
    '''
    Parse an extension definition from ``header`` at the given position.

    Return an ``(extension name, parameters)`` pair, where ``parameters`` is a
    list of ``(name, value)`` pairs, and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    (name, pos) = parse_token(header, pos, header_name)
    pos = parse_OWS(header, pos)
    parameters = []
# WARNING: Decompyle incomplete


def parse_extension(header = None):
    """
    Parse a ``Sec-WebSocket-Extensions`` header.

    Return a list of WebSocket extensions and their parameters in this format::

        [
            (
                'extension name',
                [
                    ('parameter name', 'parameter value'),
                    ....
                ]
            ),
            ...
        ]

    Parameter values are :obj:`None` when no value is provided.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    """
    return parse_list(parse_extension_item, header, 0, 'Sec-WebSocket-Extensions')

parse_extension_list = parse_extension

def build_extension_item(name = None, parameters = None):
    '''
    Build an extension definition.

    This is the reverse of :func:`parse_extension_item`.

    '''
    return [
        cast(str, name)]((lambda .0: pass# WARNING: Decompyle incomplete
) + parameters())


def build_extension(extensions = None):
    '''
    Build a ``Sec-WebSocket-Extensions`` header.

    This is the reverse of :func:`parse_extension`.

    '''
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(extensions())

build_extension_list = build_extension

def parse_subprotocol_item(header = None, pos = None, header_name = None):
    '''
    Parse a subprotocol from ``header`` at the given position.

    Return the subprotocol value and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    (item, pos) = parse_token(header, pos, header_name)
    return (cast(Subprotocol, item), pos)


def parse_subprotocol(header = None):
    '''
    Parse a ``Sec-WebSocket-Protocol`` header.

    Return a list of WebSocket subprotocols.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    return parse_list(parse_subprotocol_item, header, 0, 'Sec-WebSocket-Protocol')

parse_subprotocol_list = parse_subprotocol

def build_subprotocol(subprotocols = None):
    '''
    Build a ``Sec-WebSocket-Protocol`` header.

    This is the reverse of :func:`parse_subprotocol`.

    '''
    return ', '.join(subprotocols)

build_subprotocol_list = build_subprotocol

def validate_subprotocols(subprotocols = None):
    '''
    Validate that ``subprotocols`` is suitable for :func:`build_subprotocol`.

    '''
    if not isinstance(subprotocols, Sequence):
        raise TypeError('subprotocols must be a list')
    if isinstance(subprotocols, str):
        raise TypeError('subprotocols must be a list, not a str')
    for subprotocol in subprotocols:
        if not _token_re.fullmatch(subprotocol):
            raise ValueError(f'''invalid subprotocol: {subprotocol}''')
        return None


def build_www_authenticate_basic(realm = None):
    '''
    Build a ``WWW-Authenticate`` header for HTTP Basic Auth.

    Args:
        realm: Identifier of the protection space.

    '''
    realm = build_quoted_string(realm)
    charset = build_quoted_string('UTF-8')
    return f'''Basic realm={realm}, charset={charset}'''

_token68_re = re.compile('[A-Za-z0-9-._~+/]+=*')

def parse_token68(header = None, pos = None, header_name = None):
    '''
    Parse a token68 from ``header`` at the given position.

    Return the token value and the new position.

    Raises:
        InvalidHeaderFormat: On invalid inputs.

    '''
    match = _token68_re.match(header, pos)
# WARNING: Decompyle incomplete


def parse_end(header = None, pos = None, header_name = None):
    '''
    Check that parsing reached the end of header.

    '''
    if pos < len(header):
        raise InvalidHeaderFormat(header_name, 'trailing data', header, pos)


def parse_authorization_basic(header = None):
    '''
    Parse an ``Authorization`` header for HTTP Basic Auth.

    Return a ``(username, password)`` tuple.

    Args:
        header: Value of the ``Authorization`` header.

    Raises:
        InvalidHeaderFormat: On invalid inputs.
        InvalidHeaderValue: On unsupported inputs.

    '''
    (scheme, pos) = parse_token(header, 0, 'Authorization')
    if scheme.lower() != 'basic':
        raise InvalidHeaderValue('Authorization', f'''unsupported scheme: {scheme}''')
    if peek_ahead(header, pos) != ' ':
        raise InvalidHeaderFormat('Authorization', 'expected space after scheme', header, pos)
    pos += 1
    (basic_credentials, pos) = parse_token68(header, pos, 'Authorization')
    parse_end(header, pos, 'Authorization')
    
    try:
        user_pass = base64.b64decode(basic_credentials.encode()).decode()
    except binascii.Error:
        raise InvalidHeaderValue('Authorization', 'expected base64-encoded credentials'), None

    
    try:
        (username, password) = user_pass.split(':', 1)
    except ValueError:
        raise InvalidHeaderValue('Authorization', 'expected username:password credentials'), None

    return (username, password)


def build_authorization_basic(username = None, password = None):
    '''
    Build an ``Authorization`` header for HTTP Basic Auth.

    This is the reverse of :func:`parse_authorization_basic`.

    '''
    pass
# WARNING: Decompyle incomplete
