# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

from platform import system
from importlib.metadata import version, PackageNotFoundError
from  import clipboard, console, lineeditor, logger, modes, rlmain, unicode_helper
from rlmain import *
_S = system()
if _S.lower() != 'windows':
    raise RuntimeError('pyreadline3 is for Windows only, not {}.'.format(_S))
del system
del _S

try:
    __version__ = version('pyreadline3')
    return None
except PackageNotFoundError:
    return None
