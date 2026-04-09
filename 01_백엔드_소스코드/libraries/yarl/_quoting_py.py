# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _quoting_py.pyc (Python 3.11)

import codecs
import re
from string import ascii_letters, ascii_lowercase, digits
from typing import Union, overload
BASCII_LOWERCASE = ascii_lowercase.encode('ascii')
BPCT_ALLOWED = range(256)()
GEN_DELIMS = ':/?#[]@'
SUB_DELIMS_WITHOUT_QS = "!$'()*,"
SUB_DELIMS = SUB_DELIMS_WITHOUT_QS + '+&=;'
RESERVED = GEN_DELIMS + SUB_DELIMS
UNRESERVED = ascii_letters + digits + '-._~'
ALLOWED = UNRESERVED + SUB_DELIMS_WITHOUT_QS
_IS_HEX = re.compile(b'[A-Z0-9][A-Z0-9]')
_IS_HEX_STR = re.compile('[A-Fa-f0-9][A-Fa-f0-9]')
utf8_decoder = codecs.getincrementaldecoder('utf-8')

class _Quoter:
    
    def __init__(self = None, *, safe, protected, qs, requote):
        self._safe = safe
        self._protected = protected
        self._qs = qs
        self._requote = requote

    __call__ = (lambda self = None, val = None: pass)()
    __call__ = (lambda self = None, val = None: pass)()
    
    def __call__(self = None, val = None):
        pass
    # WARNING: Decompyle incomplete



class _Unquoter:
    
    def __init__(self = None, *, ignore, unsafe, qs, plus):
        self._ignore = ignore
        self._unsafe = unsafe
        self._qs = qs
        self._plus = plus
        self._quoter = _Quoter()
        self._qs_quoter = _Quoter(qs = True)

    __call__ = (lambda self = None, val = None: pass)()
    __call__ = (lambda self = None, val = None: pass)()
    
    def __call__(self = None, val = None):
        pass
    # WARNING: Decompyle incomplete
