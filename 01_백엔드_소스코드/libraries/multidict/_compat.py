# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _compat.pyc (Python 3.11)

import os
import platform
NO_EXTENSIONS = bool(os.environ.get('MULTIDICT_NO_EXTENSIONS'))
PYPY = platform.python_implementation() == 'PyPy'
if not NO_EXTENSIONS:
    USE_EXTENSIONS = not PYPY
    if USE_EXTENSIONS:
        
        try:
            from  import _multidict
            return None
        except ImportError:
            USE_EXTENSIONS = False
            return None
            return None
