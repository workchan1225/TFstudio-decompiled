# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utils.pyc (Python 3.11)

'''
General helpers required for `tqdm.std`.
'''
import os
import re
import sys
from functools import partial, partialmethod, wraps
from inspect import signature
from unicodedata import east_asian_width
from warnings import warn
from weakref import proxy
(_range, _unich, _unicode, _basestring) = (range, chr, str, str)
CUR_OS = sys.platform
IS_WIN = (lambda .0: pass# WARNING: Decompyle incomplete
)(('win32', 'cygwin')())
IS_NIX = (lambda .0: pass# WARNING: Decompyle incomplete
)(('aix', 'linux', 'darwin', 'freebsd')())
RE_ANSI = re.compile('\\x1b\\[[;\\d]*[A-Za-z]')

try:
    if IS_WIN:
        import colorama
    else:
        raise ImportError
    
    try:
        colorama.init(strip = False)
    except TypeError:
        colorama.init()
    except ImportError:
        any
        colorama = None

    
    def envwrap(prefix, types, is_method = (None, False)):
        '''
    Override parameter defaults via `os.environ[prefix + param_name]`.
    Maps UPPER_CASE env vars map to lower_case param names.
    camelCase isn\'t supported (because Windows ignores case).

    Precedence (highest first):

    - call (`foo(a=3)`)
    - environ (`FOO_A=2`)
    - signature (`def foo(a=1)`)

    Parameters
    ----------
    prefix  : str
        Env var prefix, e.g. "FOO_"
    types  : dict, optional
        Fallback mappings `{\'param_name\': type, ...}` if types cannot be
        inferred from function signature.
        Consider using `types=collections.defaultdict(lambda: ast.literal_eval)`.
    is_method  : bool, optional
        Whether to use `functools.partialmethod`. If (default: False) use `functools.partial`.

    Examples
    --------
    ```
    $ cat foo.py
    from tqdm.utils import envwrap
    @envwrap("FOO_")
    def test(a=1, b=2, c=3):
        print(f"received: a={a}, b={b}, c={c}")

    $ FOO_A=42 FOO_C=1337 python -c \'import foo; foo.test(c=99)\'
    received: a=42, b=2, c=99
    ```
    '''
        pass
    # WARNING: Decompyle incomplete

    
    class FormatReplace(object):
        '''
    >>> a = FormatReplace(\'something\')
    >>> f"{a:5d}"
    \'something\'
    '''
        
        def __init__(self, replace = ('',)):
            self.replace = replace
            self.format_called = 0

        
        def __format__(self, _):
            return self.replace


    
    class Comparable(object):
        '''Assumes child has self._comparable attr/@property'''
        
        def __lt__(self, other):
            return self._comparable < other._comparable

        
        def __le__(self, other):
