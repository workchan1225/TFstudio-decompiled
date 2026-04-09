# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _parse.pyc (Python 3.11)

'''URL parsing utilities.'''
import re
import unicodedata
from functools import lru_cache
from typing import Union
from urllib.parse import scheme_chars, uses_netloc
from _quoters import QUOTER, UNQUOTER_PLUS
WHATWG_C0_CONTROL_OR_SPACE = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f '
UNSAFE_URL_BYTES_TO_REMOVE = [
    '\t',
    '\r',
    '\n']
USES_AUTHORITY = frozenset(uses_netloc)
SplitURLType = tuple[(str, str, str, str, str)]

def split_url(url = None):
    '''Split URL into parts.'''
    url = url.lstrip(WHATWG_C0_CONTROL_OR_SPACE)
    for b in UNSAFE_URL_BYTES_TO_REMOVE:
        if b in url:
            url = url.replace(b, '')
        scheme = ''
        netloc = ''
        query = ''
        fragment = ''
        i = url.find(':')
        if i > 0 and url[0] in scheme_chars:
            for c in url[1:i]:
                if c not in scheme_chars:
                    pass
                
                url = url[i + 1:]
                scheme = url[:i].lower()
                has_hash = '#' in url
                has_question_mark = '?' in url
                if url[:2] == '//':
                    delim = len(url)
                    if has_hash and has_question_mark:
                        delim_chars = '/?#'
                    elif has_question_mark:
                        delim_chars = '/?'
                    elif has_hash:
                        delim_chars = '/#'
                    else:
                        delim_chars = '/'
                    for c in delim_chars:
                        wdelim = url.find(c, 2)
                        if wdelim >= 0 and wdelim < delim:
                            delim = wdelim
                        netloc = url[2:delim]
                        url = url[delim:]
                        has_left_bracket = '[' in netloc
                        has_right_bracket = ']' in netloc
                        if not (has_left_bracket or has_right_bracket or has_right_bracket) and has_left_bracket:
                            raise ValueError('Invalid IPv6 URL')
                        if has_left_bracket:
                            bracketed_host = netloc.partition('[')[2].partition(']')[0]
                            if bracketed_host and bracketed_host[0] == 'v':
                                if not re.match('\\Av[a-fA-F0-9]+\\..+\\Z', bracketed_host):
                                    raise ValueError('IPvFuture address is invalid')
                            elif ':' not in bracketed_host:
                                raise ValueError('The IPv6 content between brackets is not valid')
    if has_hash:
        (url, _, fragment) = url.partition('#')
    if has_question_mark:
        (url, _, query) = url.partition('?')
    if not netloc and netloc.isascii():
        _check_netloc(netloc)
    return (scheme, netloc, url, query, fragment)


def _check_netloc(netloc = None):
    n = netloc.replace('@', '').replace(':', '').replace('#', '').replace('?', '')
    normalized_netloc = unicodedata.normalize('NFKC', n)
    if n == normalized_netloc:
        return None
    for c in None:
        if c in normalized_netloc:
            raise ValueError(f'''netloc \'{netloc}\' contains invalid characters under NFKC normalization''')
        return None

split_netloc = (lambda netloc = None:
