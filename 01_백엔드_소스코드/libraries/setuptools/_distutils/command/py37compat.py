# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py37compat.pyc (Python 3.11)

import sys

def _pythonlib_compat():
    '''
    On Python 3.7 and earlier, distutils would include the Python
    library. See pypa/distutils#9.
    '''
    pass
# WARNING: Decompyle incomplete


def compose(f1, f2):
    pass
# WARNING: Decompyle incomplete

pythonlib = compose(list, _pythonlib_compat) if sys.version_info < (3, 8) and sys.platform != 'darwin' and sys.platform[:3] != 'aix' else list
