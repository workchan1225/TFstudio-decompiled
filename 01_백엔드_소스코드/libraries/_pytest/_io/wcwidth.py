# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wcwidth.pyc (Python 3.11)

from __future__ import annotations
from functools import lru_cache
import unicodedata
wcwidth = (lambda c = None: o = ord(c)if  <= 32, o or 32, o < 127:
pass1if not o == 0:
if not  <= 8203, o or 8203, o <= 8207:
passif not  <= 8232, o or 8232, o <= 8238:
passif  <= 8288, o or 8288, o <= 8291:
passelse:
0if category == 'Cc':
-1if None.category(c) in ('Me', 'Mn'):
0if None.east_asian_width(c) in ('F', 'W'):
2)()

def wcswidth(s = None):
    '''Determine how many columns are needed to display a string in a terminal.

    Returns -1 if the string contains non-printable characters.
    '''
    width = 0
    for c in unicodedata.normalize('NFC', s):
        wc = wcwidth(c)
        if wc < 0:
            return -1
        None += wc
        return width
