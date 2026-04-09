# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: request.pyc (Python 3.11)

'''An extensible library for opening URLs using a variety of protocols

The simplest way to use this module is to call the urlopen function,
which accepts a string containing a URL or a Request object (described
below).  It opens the URL and returns the results as file-like
object; the returned object has some extra methods described below.

The OpenerDirector manages a collection of Handler objects that do
all the actual work.  Each Handler implements a particular protocol or
option.  The OpenerDirector is a composite object that invokes the
Handlers needed to open the requested URL.  For example, the
HTTPHandler performs HTTP GET and POST requests and deals with
non-error returns.  The HTTPRedirectHandler automatically deals with
HTTP 301, 302, 303, 307, and 308 redirect errors, and the
HTTPDigestAuthHandler deals with digest authentication.

urlopen(url, data=None) -- Basic usage is the same as original
urllib.  pass the url and optionally data to post to an HTTP URL, and
get a file-like object back.  One difference is that you can also pass
a Request instance instead of URL.  Raises a URLError (subclass of
OSError); for HTTP errors, raises an HTTPError, which can also be
treated as a valid response.

build_opener -- Function that creates a new OpenerDirector instance.
Will install the default handlers.  Accepts one or more Handlers as
arguments, either instances or Handler classes that it will
instantiate.  If one of the argument is a subclass of the default
handler, the argument will be installed instead of the default.

install_opener -- Installs a new opener as the default opener.

objects of interest:

OpenerDirector -- Sets up the User Agent as the Python-urllib client and manages
the Handler classes, while dealing with requests and responses.

Request -- An object that encapsulates the state of a request.  The
state can be as simple as the URL.  It can also include extra HTTP
headers, e.g. a User-Agent.

BaseHandler --

internals:
BaseHandler and parent
_call_chain conventions

Example usage:

import urllib.request

# set up authentication info
authinfo = urllib.request.HTTPBasicAuthHandler()
authinfo.add_password(realm=\'PDQ Application\',
                      uri=\'https://mahler:8092/site-updates.py\',
                      user=\'klem\',
                      passwd=\'geheim$parole\')

proxy_support = urllib.request.ProxyHandler({"http" : "http://ahad-haam:3128"})

# build a new opener that adds authentication and caching FTP handlers
opener = urllib.request.build_opener(proxy_support, authinfo,
                                     urllib.request.CacheFTPHandler)

# install it
urllib.request.install_opener(opener)

f = urllib.request.urlopen(\'https://www.python.org/\')
'''
import base64
import bisect
import email
import hashlib
import http.client as http
import io
import os
import posixpath
import re
import socket
import string
import sys
import time
import tempfile
import contextlib
import warnings
from urllib.error import URLError, HTTPError, ContentTooShortError
from urllib.parse import urlparse, urlsplit, urljoin, unwrap, quote, unquote, _splittype, _splithost, _splitport, _splituser, _splitpasswd, _splitattr, _splitquery, _splitvalue, _splittag, _to_bytes, unquote_to_bytes, urlunparse
from urllib.response import addinfourl, addclosehook

try:
    import ssl
    _have_ssl = True
except ImportError:
    _have_ssl = False

__all__ = [
    'Request',
    'OpenerDirector',
    'BaseHandler',
    'HTTPDefaultErrorHandler',
    'HTTPRedirectHandler',
    'HTTPCookieProcessor',
    'ProxyHandler',
    'HTTPPasswordMgr',
    'HTTPPasswordMgrWithDefaultRealm',
    'HTTPPasswordMgrWithPriorAuth',
    'AbstractBasicAuthHandler',
    'HTTPBasicAuthHandler',
    'ProxyBasicAuthHandler',
    'AbstractDigestAuthHandler',
    'HTTPDigestAuthHandler',
    'ProxyDigestAuthHandler',
    'HTTPHandler',
    'FileHandler',
    'FTPHandler',
    'CacheFTPHandler',
    'DataHandler',
    'UnknownHandler',
    'HTTPErrorProcessor',
    'urlopen',
    'install_opener',
    'build_opener',
    'pathname2url',
    'url2pathname',
    'getproxies',
    'urlretrieve',
    'urlcleanup',
    'URLopener',
    'FancyURLopener']
__version__ = '%d.%d' % sys.version_info[:2]
_opener = None

def urlopen(url = None, data = (None, socket._GLOBAL_DEFAULT_TIMEOUT), timeout = {
    'cafile': None,
    'capath': None,
    'cadefault': False,
    'context': None }, *, cafile, capath, cadefault, context):
    '''Open the URL url, which can be either a string or a Request object.

    *data* must be an object specifying additional data to be sent to
    the server, or None if no such data is needed.  See Request for
    details.

    urllib.request module uses HTTP/1.1 and includes a "Connection:close"
    header in its HTTP requests.

    The optional *timeout* parameter specifies a timeout in seconds for
    blocking operations like the connection attempt (if not specified, the
    global default timeout setting will be used). This only works for HTTP,
    HTTPS and FTP connections.

    If *context* is specified, it must be a ssl.SSLContext instance describing
    the various SSL options. See HTTPSConnection for more details.

    The optional *cafile* and *capath* parameters specify a set of trusted CA
    certificates for HTTPS requests. cafile should point to a single file
    containing a bundle of CA certificates, whereas capath should point to a
    directory of hashed certificate files. More information can be found in
    ssl.SSLContext.load_verify_locations().

    The *cadefault* parameter is ignored.


    This function always returns an object which can work as a
    context manager and has the properties url, headers, and status.
    See urllib.response.addinfourl for more detail on these properties.

    For HTTP and HTTPS URLs, this function returns a http.client.HTTPResponse
    object slightly modified. In addition to the three new methods above, the
    msg attribute contains the same information as the reason attribute ---
    the reason phrase returned by the server --- instead of the response
    headers as it is specified in the documentation for HTTPResponse.

    For FTP, file, and data URLs and requests explicitly handled by legacy
    URLopener and FancyURLopener classes, this function returns a
    urllib.response.addinfourl object.

    Note that None may be returned if no handler handles the request (though
    the default installed global OpenerDirector uses UnknownHandler to ensure
    this never happens).

    In addition, if proxy settings are detected (for example, when a *_proxy
    environment variable like http_proxy is set), ProxyHandler is default
    installed and makes sure the requests are handled through the proxy.

    '''
    pass
# WARNING: Decompyle incomplete


def install_opener(opener):
    global _opener
    _opener = opener

_url_tempfiles = []

def urlretrieve(url, filename, reporthook, data = (None, None, None)):
