# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''
oauthlib.utils
~~~~~~~~~~~~~~

This module contains utility methods used by various parts of the OAuth 2 spec.
'''
import datetime
import os
from urllib.parse import quote, urlparse
from oauthlib.common import urldecode

def list_to_scope(scope):
    '''Convert a list of scopes to a space separated string.'''
    pass
# WARNING: Decompyle incomplete


def scope_to_list(scope):
    '''Convert a space separated string to a list of scopes.'''
    if isinstance(scope, (tuple, list, set)):
        return scope()
# WARNING: Decompyle incomplete


def params_from_uri(uri):
    params = dict(urldecode(urlparse(uri).query))
    if 'scope' in params:
        params['scope'] = scope_to_list(params['scope'])
    return params


def host_from_uri(uri):
    '''Extract hostname and port from URI.

    Will use default port for HTTP and HTTPS if none is present in the URI.
    '''
    default_ports = {
        'HTTP': '80',
        'HTTPS': '443' }
    (sch, netloc, path, par, query, fra) = urlparse(uri)
    if ':' in netloc:
        (netloc, port) = netloc.split(':', 1)
    else:
        port = default_ports.get(sch.upper())
    return (netloc, port)


def escape(u):
    '''Escape a string in an OAuth-compatible fashion.

    TODO: verify whether this can in fact be used for OAuth 2

    '''
    if not isinstance(u, str):
        raise ValueError('Only unicode objects are escapable.')
    return quote(u.encode('utf-8'), safe = b'~')


def generate_age(issue_time):
    '''Generate a age parameter for MAC authentication draft 00.'''
    td = datetime.datetime.now() - issue_time
    age = (td.microseconds + (td.seconds + td.days * 24 * 3600) * 1000000) / 1000000
    return str(age)


def is_secure_transport(uri):
    '''Check if the uri is over ssl.'''
    if os.environ.get('OAUTHLIB_INSECURE_TRANSPORT'):
        return True
    return None.lower().startswith('https://')
