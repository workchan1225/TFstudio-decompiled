# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from pyreadline3.py3k_compat import is_ironpython
from  import winconstants
if is_ironpython:
    
    try:
        from ironpython_keysyms import *
        return None
    except ImportError:
        x = None
        raise ImportError('Could not import keysym for local ironpython version'), x
        x = None
        del x
        
        try:
            from keysyms import *
            return None
        except ImportError:
            x = None
            raise ImportError('Could not import keysym for local python version'), x
            x = None
            del x
