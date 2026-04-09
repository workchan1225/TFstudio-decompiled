# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''
oauthlib.utils
~~~~~~~~~~~~~~

This module contains utility methods used by various parts of the OAuth
spec.
'''
from urllib.request import request as urllib2
from oauthlib.common import quote, unquote
UNICODE_ASCII_CHARACTER_SET = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

def filter_params(target):
    '''Decorator which filters params to remove non-oauth_* parameters

    Assumes the decorated method takes a params dict or list of tuples as its
    first argument.
    '''
    pass
# WARNING: Decompyle incomplete


def filter_oauth_params(params):
    '''Removes all non oauth parameters from a dict or a list of params.'''
    
    def is_oauth(kv):
        return kv[0].startswith('oauth_')

    if isinstance(params, dict):
        return list(filter(is_oauth, list(params.items())))
    return None(filter(is_oauth, params))


def escape(u):
    '''Escape a unicode string in an OAuth-compatible fashion.

    Per `section 3.6`_ of the spec.

    .. _`section 3.6`: https://tools.ietf.org/html/rfc5849#section-3.6

    '''
    if not isinstance(u, str):
        raise ValueError('Only unicode objects are escapable. ' + 'Got {!r} of type {}.'.format(u, type(u)))
    return quote(u, safe = b'~')


def unescape(u):
    if not isinstance(u, str):
        raise ValueError('Only unicode objects are unescapable.')
    return unquote(u)


def parse_keqv_list(l):
    '''A unicode-safe version of urllib2.parse_keqv_list'''
    return urllib2.parse_keqv_list(l)


def parse_http_list(u):
    '''A unicode-safe version of urllib2.parse_http_list'''
    return urllib2.parse_http_list(u)


def parse_authorization_header(authorization_header):
    '''Parse an OAuth authorization header into a list of 2-tuples'''
    auth_scheme = 'OAuth '.lower()
    if authorization_header[:len(auth_scheme)].lower().startswith(auth_scheme):
        items = parse_http_list(authorization_header[len(auth_scheme):])
        
        try:
            return list(parse_keqv_list(items).items())
        except (IndexError, ValueError):
            pass

        raise ValueError('Malformed authorization header')
