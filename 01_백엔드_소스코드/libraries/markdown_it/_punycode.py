# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _punycode.pyc (Python 3.11)

import codecs
from collections.abc import Callable
import re
REGEX_SEPARATORS = re.compile('[\\x2E\\u3002\\uFF0E\\uFF61]')
REGEX_NON_ASCII = re.compile('[^\\0-\\x7E]')

def encode(uni = None):
    return codecs.encode(uni, encoding = 'punycode').decode()


def decode(ascii = None):
    return codecs.decode(ascii, encoding = 'punycode')


def map_domain(string = None, fn = None):
    pass
# WARNING: Decompyle incomplete


def to_unicode(obj = None):
    
    def mapping(obj = None):
        if obj.startswith('xn--'):
            return decode(obj[4:].lower())

    return map_domain(obj, mapping)


def to_ascii(obj = None):
    
    def mapping(obj = None):
        if REGEX_NON_ASCII.search(obj):
            return 'xn--' + encode(obj)

    return map_domain(obj, mapping)
