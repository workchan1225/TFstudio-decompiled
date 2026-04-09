# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''
requests.utils
~~~~~~~~~~~~~~

This module provides utility functions that are used within Requests
that are also useful for external consumption.
'''
import codecs
import contextlib
import io
import os
import re
import socket
import struct
import sys
import tempfile
import warnings
import zipfile
from collections import OrderedDict
from urllib3.util import make_headers, parse_url
from  import certs
from __version__ import __version__
from _internal_utils import _HEADER_VALIDATORS_BYTE, _HEADER_VALIDATORS_STR, HEADER_VALIDATORS, to_native_string
from compat import Mapping, basestring, bytes, getproxies, getproxies_environment, integer_types
from compat import parse_http_list as _parse_list_header
from compat import proxy_bypass, proxy_bypass_environment, quote, str, unquote, urlparse, urlunparse
from cookies import cookiejar_from_dict
from exceptions import FileModeWarning, InvalidHeader, InvalidURL, UnrewindableBodyError
from structures import CaseInsensitiveDict
NETRC_FILES = ('.netrc', '_netrc')
DEFAULT_CA_BUNDLE_PATH = certs.where()
DEFAULT_PORTS = {
    'http': 80,
    'https': 443 }
DEFAULT_ACCEPT_ENCODING = ', '.join(re.split(',\\s*', make_headers(accept_encoding = True)['accept-encoding']))
if sys.platform == 'win32':
    
    def proxy_bypass_registry(host):
        
        try:
            import winreg
        except ImportError:
            return False

        
        try:
            internetSettings = winreg.OpenKey(winreg.HKEY_CURRENT_USER, 'Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings')
            proxyEnable = int(winreg.QueryValueEx(internetSettings, 'ProxyEnable')[0])
            proxyOverride = winreg.QueryValueEx(internetSettings, 'ProxyOverride')[0]
        except (OSError, ValueError):
            return False

        if not proxyEnable or proxyOverride:
            return False
        proxyOverride = None.split(';')
        for test in proxyOverride:
            if test == '<local>' and '.' not in host:
                return True
            test = None.replace('.', '\\.')
            test = test.replace('*', '.*')
            test = test.replace('?', '.')
            if re.match(test, host, re.I):
                return True
            return False

    
    def proxy_bypass(host):
        '''Return True, if the host should be bypassed.

        Checks proxy settings gathered from the environment, if specified,
        or the registry.
        '''
        if getproxies_environment():
            return proxy_bypass_environment(host)
        return None(host)


def dict_to_sequence(d):
    '''Returns an internal sequence dictionary update.'''
    if hasattr(d, 'items'):
        d = d.items()
    return d


def super_len(o):
    total_length = None
    current_position = 0
    if hasattr(o, '__len__'):
        total_length = len(o)
    elif hasattr(o, 'len'):
        total_length = o.len
# WARNING: Decompyle incomplete


def get_netrc_auth(url, raise_errors = (False,)):
    '''Returns the Requests tuple auth for a given url from netrc.'''
    netrc_file = os.environ.get('NETRC')
# WARNING: Decompyle incomplete


def guess_filename(obj):
    '''Tries to guess the filename of the given object.'''
    name = getattr(obj, 'name', None)
    if name or isinstance(name, basestring) or name[0] != '<' or name[-1] != '>':
        return os.path.basename(name)
    return None
    return None
    return None


def extract_zipped_paths(path):
    '''Replace nonexistent paths that look like they refer to a member of a zip
    archive with the location of an extracted copy of the target, or else
    just return the provided path unchanged.
    '''
    if os.path.exists(path):
        return path
    (archive, member) = None.path.split(path)
# WARNING: Decompyle incomplete

atomic_open = (lambda filename: pass# WARNING: Decompyle incomplete
)()

def from_key_val_list(value):
    """Take an object and test to see if it can be represented as a
    dictionary. Unless it can not be represented as such, return an
    OrderedDict, e.g.,

    ::

        >>> from_key_val_list([('key', 'val')])
        OrderedDict([('key', 'val')])
        >>> from_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples
        >>> from_key_val_list({'key': 'val'})
        OrderedDict([('key', 'val')])

    :rtype: OrderedDict
    """
    pass
# WARNING: Decompyle incomplete


def to_key_val_list(value):
    """Take an object and test to see if it can be represented as a
    dictionary. If it can be, return a list of tuples, e.g.,

    ::

        >>> to_key_val_list([('key', 'val')])
        [('key', 'val')]
        >>> to_key_val_list({'key': 'val'})
        [('key', 'val')]
        >>> to_key_val_list('string')
        Traceback (most recent call last):
        ...
        ValueError: cannot encode objects that are not 2-tuples

    :rtype: list
    """
    pass
# WARNING: Decompyle incomplete


def parse_list_header(value):
    '''Parse lists as described by RFC 2068 Section 2.

    In particular, parse comma-separated lists where the elements of
    the list may include quoted-strings.  A quoted-string could
    contain a comma.  A non-quoted string could have quotes in the
    middle.  Quotes are removed automatically after parsing.

    It basically works like :func:`parse_set_header` just that items
    may appear multiple times and case sensitivity is preserved.

    The return value is a standard :class:`list`:

    >>> parse_list_header(\'token, "quoted value"\')
    [\'token\', \'quoted value\']

    To create a header from the :class:`list` again, use the
    :func:`dump_header` function.

    :param value: a string with a list header.
    :return: :class:`list`
    :rtype: list
    '''
    result = []
    for item in _parse_list_header(value):
        if  == item[:1], item[-1:] or item[:1], item[-1:] == '"':
            pass
        
    result.append(item)
    continue
    return result


def parse_dict_header(value):
    '''Parse lists of key, value pairs as described by RFC 2068 Section 2 and
    convert them into a python dict:

    >>> d = parse_dict_header(\'foo="is a fish", bar="as well"\')
    >>> type(d) is dict
    True
    >>> sorted(d.items())
    [(\'bar\', \'as well\'), (\'foo\', \'is a fish\')]

    If there is no value for a key it will be `None`:

    >>> parse_dict_header(\'key_without_value\')
    {\'key_without_value\': None}

    To create a header from the :class:`dict` again, use the
    :func:`dump_header` function.

    :param value: a string with a dict header.
    :return: :class:`dict`
    :rtype: dict
    '''
    result = { }
    for item in _parse_list_header(value):
        if '=' not in item:
            result[item] = None
            continue
        (name, value) = item.split('=', 1)
        if  == value[:1], value[-1:] or value[:1], value[-1:] == '"':
            pass
        
    value = unquote_header_value(value[1:-1])
    continue
    return result


def unquote_header_value(value, is_filename = (False,)):
    '''Unquotes a header value.  (Reversal of :func:`quote_header_value`).
    This does not use the real unquoting but what browsers are actually
    using for quoting.

    :param value: the header value to unquote.
    :rtype: str
    '''
    if value:
        if  == value[0], value[-1] or value[0], value[-1] == '"':
            pass
        
    elif is_filename or value[:2] != '\\\\':
        return value.replace('\\\\', '\\').replace('\\"', '"')
    return value


def dict_from_cookiejar(cj):
    '''Returns a key/value dictionary from a CookieJar.

    :param cj: CookieJar object to extract cookies from.
    :rtype: dict
    '''
    cookie_dict = { }
    for cookie in cj:
        cookie_dict[cookie.name] = cookie.value
        return cookie_dict


def add_dict_to_cookiejar(cj, cookie_dict):
    '''Returns a CookieJar from a key/value dictionary.

    :param cj: CookieJar to insert cookies into.
    :param cookie_dict: Dict of key/values to insert into CookieJar.
    :rtype: CookieJar
    '''
    return cookiejar_from_dict(cookie_dict, cj)


def get_encodings_from_content(content):
    '''Returns encodings from given content string.

    :param content: bytestring to extract encodings from.
    '''
    warnings.warn('In requests 3.0, get_encodings_from_content will be removed. For more information, please see the discussion on issue #2266. (This warning should only appear once.)', DeprecationWarning)
    charset_re = re.compile('<meta.*?charset=["\\\']*(.+?)["\\\'>]', flags = re.I)
    pragma_re = re.compile('<meta.*?content=["\\\']*;?charset=(.+?)["\\\'>]', flags = re.I)
    xml_re = re.compile('^<\\?xml.*?encoding=["\\\']*(.+?)["\\\'>]')
    return charset_re.findall(content) + pragma_re.findall(content) + xml_re.findall(content)


def _parse_content_type_header(header):
    '''Returns content type and parameters from given header

    :param header: string
    :return: tuple containing content type and dictionary of
         parameters
    '''
    tokens = header.split(';')
    params = tokens[1:]
    content_type = tokens[0].strip()
    params_dict = { }
    items_to_strip = '"\' '
    for param in params:
        param = param.strip()
        if param:
            value = True
            key = param
            index_of_equals = param.find('=')
            if index_of_equals != -1:
                key = param[:index_of_equals].strip(items_to_strip)
                value = param[index_of_equals + 1:].strip(items_to_strip)
            params_dict[key.lower()] = value
        return (content_type, params_dict)


def get_encoding_from_headers(headers):
    '''Returns encodings from given HTTP Header Dict.

    :param headers: dictionary to extract encoding from.
    :rtype: str
    '''
    content_type = headers.get('content-type')
    if not content_type:
        return None
    (content_type, params) = None(content_type)
    if 'charset' in params:
        return params['charset'].strip('\'"')
    if None in content_type:
        return 'ISO-8859-1'
    if None in content_type:
        return 'utf-8'


def stream_decode_response_unicode(iterator, r):
    '''Stream decodes an iterator.'''
    pass
# WARNING: Decompyle incomplete


def iter_slices(string, slice_length):
    '''Iterate over slices of a string.'''
    pass
# WARNING: Decompyle incomplete


def get_unicode_from_response(r):
    '''Returns the requested content back in unicode.

    :param r: Response object to get unicode content from.

    Tried:

    1. charset from content-type
    2. fall back and replace all unicode characters

    :rtype: str
    '''
    warnings.warn('In requests 3.0, get_unicode_from_response will be removed. For more information, please see the discussion on issue #2266. (This warning should only appear once.)', DeprecationWarning)
    tried_encodings = []
    encoding = get_encoding_from_headers(r.headers)
    if encoding:
        
        try:
            return str(r.content, encoding)
        except UnicodeError:
            tried_encodings.append(encoding)

        
        try:
            return str(r.content, encoding, errors = 'replace')
        except TypeError:
            return 


UNRESERVED_SET = frozenset('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-._~')

def unquote_unreserved(uri):
    '''Un-escape any percent-escape sequences in a URI that are unreserved
    characters. This leaves all reserved, illegal and non-ASCII bytes encoded.

    :rtype: str
    '''
    parts = uri.split('%')
    for i in range(1, len(parts)):
        h = parts[i][0:2]
        if c in UNRESERVED_SET:
            parts[i] = c + parts[i][2:]
            continue
        parts[i] = f'''%{parts[i]}'''
        parts[i] = f'''%{parts[i]}'''
        return ''.join(parts)


def requote_uri(uri):
    '''Re-quote the given URI.

    This function passes the given URI through an unquote/quote cycle to
    ensure that it is fully and consistently quoted.

    :rtype: str
    '''
    safe_with_percent = "!#$%&'()*+,/:;=?@[]~"
    safe_without_percent = "!#$&'()*+,/:;=?@[]~"
    
    try:
        return quote(unquote_unreserved(uri), safe = safe_with_percent)
    except InvalidURL:
        return 



def address_in_network(ip, net):
    '''This function allows you to check if an IP belongs to a network subnet

    Example: returns True if ip = 192.168.1.1 and net = 192.168.1.0/24
             returns False if ip = 192.168.1.1 and net = 192.168.100.0/24

    :rtype: bool
    '''
    ipaddr = struct.unpack('=L', socket.inet_aton(ip))[0]
    (netaddr, bits) = net.split('/')
    netmask = struct.unpack('=L', socket.inet_aton(dotted_netmask(int(bits))))[0]
    network = struct.unpack('=L', socket.inet_aton(netaddr))[0] & netmask
    return ipaddr & netmask == network & netmask


def dotted_netmask(mask):
    '''Converts mask from /xx format to xxx.xxx.xxx.xxx

    Example: if mask is 24 function returns 255.255.255.0

    :rtype: str
    '''
    bits = 0xFFFFFFFF ^ (1 << 32 - mask) - 1
    return socket.inet_ntoa(struct.pack('>I', bits))


def is_ipv4_address(string_ip):
    '''
    :rtype: bool
    '''
    
    try:
        socket.inet_aton(string_ip)
    except OSError:
        return False

    return True


def is_valid_cidr(string_network):
    '''
    Very simple check of the cidr format in no_proxy variable.

    :rtype: bool
    '''
    if string_network.count('/') == 1:
        
        try:
            mask = int(string_network.split('/')[1])
        except ValueError:
            return False

        if mask < 1 or mask > 32:
            return False
        
        try:
            socket.inet_aton(string_network.split('/')[0])
        except OSError:
            return False
            return False

        return True

set_environ = (lambda env_name, value: pass# WARNING: Decompyle incomplete
)()

def should_bypass_proxies(url, no_proxy):
    '''
    Returns whether we should bypass proxies or not.

    :rtype: bool
    '''
    
    def get_proxy(key):
        if not os.environ.get(key):
            pass
        return os.environ.get(key.upper())

    no_proxy_arg = no_proxy
# WARNING: Decompyle incomplete


def get_environ_proxies(url, no_proxy = (None,)):
    '''
    Return a dict of environment proxies.

    :rtype: dict
    '''
    if should_bypass_proxies(url, no_proxy = no_proxy):
        return { }
    return None()


def select_proxy(url, proxies):
    '''Select a proxy for the url, if applicable.

    :param url: The url being for the request
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    '''
    pass
# WARNING: Decompyle incomplete


def resolve_proxies(request, proxies, trust_env = (True,)):
    '''This method takes proxy information from a request and configuration
    input to resolve a mapping of target proxies. This will consider settings
    such a NO_PROXY to strip proxy configurations.

    :param request: Request or PreparedRequest
    :param proxies: A dictionary of schemes or schemes and hosts to proxy URLs
    :param trust_env: Boolean declaring whether to trust environment configs

    :rtype: dict
    '''
    pass
# WARNING: Decompyle incomplete


def default_user_agent(name = ('python-requests',)):
    '''
    Return a string representing the default user agent.

    :rtype: str
    '''
    return f'''{name}/{__version__}'''


def default_headers():
    '''
    :rtype: requests.structures.CaseInsensitiveDict
    '''
    return CaseInsensitiveDict({
        'User-Agent': default_user_agent(),
        'Accept-Encoding': DEFAULT_ACCEPT_ENCODING,
        'Accept': '*/*',
        'Connection': 'keep-alive' })


def parse_header_links(value):
    '''Return a list of parsed link headers proxies.

    i.e. Link: <http:/.../front.jpeg>; rel=front; type="image/jpeg",<http://.../back.jpeg>; rel=back;type="image/jpeg"

    :rtype: list
    '''
    links = []
    replace_chars = ' \'"'
    value = value.strip(replace_chars)
    if not value:
        return links
    for val in None.split(', *<', value):
        (url, params) = val.split(';', 1)
    except ValueError:
        params = ''
        url = val
    link = {
        'url': url.strip('<> \'"') }
    for param in params.split(';'):
        (key, value) = param.split('=')
    except ValueError:
        pass
    except:
        link[key.strip(replace_chars)] = value.strip(replace_chars)
        continue
    links.append(link)
    continue
    return links

_null = '\x00'.encode('ascii')
_null2 = _null * 2
_null3 = _null * 3

def guess_json_utf(data):
