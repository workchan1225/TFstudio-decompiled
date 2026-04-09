# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: url.pyc (Python 3.11)

from __future__ import annotations
import re
import typing
from exceptions import LocationParseError
from util import to_str
_NORMALIZABLE_SCHEMES = ('http', 'https', None)
_PERCENT_RE = re.compile('%[a-fA-F0-9]{2}')
_SCHEME_RE = re.compile('^(?:[a-zA-Z][a-zA-Z0-9+-]*:|/)')
_URI_RE = re.compile('^(?:([a-zA-Z][a-zA-Z0-9+.-]*):)?(?://([^\\\\/?#]*))?([^?#]*)(?:\\?([^#]*))?(?:#(.*))?$', re.UNICODE | re.DOTALL)
_IPV4_PAT = '(?:[0-9]{1,3}\\.){3}[0-9]{1,3}'
_HEX_PAT = '[0-9A-Fa-f]{1,4}'
_LS32_PAT = '(?:{hex}:{hex}|{ipv4})'.format(hex = _HEX_PAT, ipv4 = _IPV4_PAT)
_subs = {
    'hex': _HEX_PAT,
    'ls32': _LS32_PAT }
_variations = [
    '(?:%(hex)s:){6}%(ls32)s',
    '::(?:%(hex)s:){5}%(ls32)s',
    '(?:%(hex)s)?::(?:%(hex)s:){4}%(ls32)s',
    '(?:(?:%(hex)s:)?%(hex)s)?::(?:%(hex)s:){3}%(ls32)s',
    '(?:(?:%(hex)s:){0,2}%(hex)s)?::(?:%(hex)s:){2}%(ls32)s',
    '(?:(?:%(hex)s:){0,3}%(hex)s)?::%(hex)s:%(ls32)s',
    '(?:(?:%(hex)s:){0,4}%(hex)s)?::%(ls32)s',
    '(?:(?:%(hex)s:){0,5}%(hex)s)?::%(hex)s',
    '(?:(?:%(hex)s:){0,6}%(hex)s)?::']
_UNRESERVED_PAT = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._\\-~'
_IPV6_PAT = '|'.join + (lambda .0: [ x % _subs for x in .0 ])(_variations()) + ')'
_ZONE_ID_PAT = '(?:%25|%)(?:[' + _UNRESERVED_PAT + ']|%[a-fA-F0-9]{2})+'
_IPV6_ADDRZ_PAT = '\\[' + _IPV6_PAT + '(?:' + _ZONE_ID_PAT + ')?\\]'
_REG_NAME_PAT = '(?:[^\\[\\]%:/?#]|%[a-fA-F0-9]{2})*'
_TARGET_RE = re.compile('^(/[^?#]*)(?:\\?([^#]*))?(?:#.*)?$')
_IPV4_RE = re.compile('^' + _IPV4_PAT + '$')
_IPV6_RE = re.compile('^' + _IPV6_PAT + '$')
_IPV6_ADDRZ_RE = re.compile('^' + _IPV6_ADDRZ_PAT + '$')
_BRACELESS_IPV6_ADDRZ_RE = re.compile('^' + _IPV6_ADDRZ_PAT[2:-2] + '$')
_ZONE_ID_RE = re.compile('(' + _ZONE_ID_PAT + ')\\]$')
_HOST_PORT_PAT = f'''^({_REG_NAME_PAT!s}|{_IPV4_PAT!s}|{_IPV6_ADDRZ_PAT!s})(?::0*?(|0|[1-9][0-9]{{0,4}}))?$'''
_HOST_PORT_RE = re.compile(_HOST_PORT_PAT, re.UNICODE | re.DOTALL)
_UNRESERVED_CHARS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789._-~')
_SUB_DELIM_CHARS = set("!$&'()*+,;=")
_USERINFO_CHARS = _UNRESERVED_CHARS | _SUB_DELIM_CHARS | {
    ':'}
_PATH_CHARS = _USERINFO_CHARS | {
    '@',
    '/'}
_QUERY_CHARS = _PATH_CHARS | {
    '?'}
_FRAGMENT_CHARS = _PATH_CHARS | {
    '?'}

def Url():
    '''Url'''
    pass
# WARNING: Decompyle incomplete

Url = <NODE:27>(Url, 'Url', typing.NamedTuple('Url', [
    ('scheme', typing.Optional[str]),
    ('auth', typing.Optional[str]),
    ('host', typing.Optional[str]),
    ('port', typing.Optional[int]),
    ('path', typing.Optional[str]),
    ('query', typing.Optional[str]),
    ('fragment', typing.Optional[str])]))
_encode_invalid_chars = (lambda component = None, allowed_chars = '(?:': pass)()
_encode_invalid_chars = (lambda component = None, allowed_chars = None: pass)()

def _encode_invalid_chars(component = None, allowed_chars = None):
    '''Percent-encodes a URI component without reapplying
    onto an already percent-encoded component.
    '''
    pass
# WARNING: Decompyle incomplete


def _remove_path_dot_segments(path = None):
    segments = path.split('/')
    output = []
    for segment in segments:
        if segment == '.':
            continue
        if segment != '..':
            output.append(segment)
            continue
        if output:
            output.pop()
        if path.startswith('/'):
            if output or output[0]:
                output.insert(0, '')
    if path.endswith(('/.', '/..')):
        output.append('')
    return '/'.join(output)

_normalize_host = (lambda host = None, scheme = None: pass)()
_normalize_host = (lambda host = None, scheme = None: pass)()

def _normalize_host(host = None, scheme = None):
