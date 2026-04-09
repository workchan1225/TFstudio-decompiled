# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: verifier.pyc (Python 3.11)

import sys
import os
import binascii
import shutil
import io
from  import __version_verifier_modules__
from  import ffiplatform
from error import VerificationError
if sys.version_info >= (3, 3):
    import importlib.machinery as importlib
    
    def _extension_suffixes():
        return importlib.machinery.EXTENSION_SUFFIXES[:]

else:
    import imp
    
    def _extension_suffixes():
        return imp.get_suffixes()()


class Verifier(object):
    
    def __init__(self, ffi, preamble, tmpdir, modulename, ext_package, tag, force_generic_engine, source_extension, flags, relative_to = (None, None, None, '', False, '.c', None, None), **kwds):
