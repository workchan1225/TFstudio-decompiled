# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: depends.pyc (Python 3.11)

import sys
import marshal
import contextlib
import dis
from setuptools.extern.packaging import version
from _imp import find_module, PY_COMPILED, PY_FROZEN, PY_SOURCE
from  import _imp
__all__ = [
    'Require',
    'find_module',
    'get_module_constant',
    'extract_constant']

class Require:
    '''A prerequisite to building or installing a distribution'''
    
    def __init__(self, name, requested_version, module, homepage, attribute, format = ('', None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def full_name(self):
        '''Return full package/distribution name, w/version'''
        pass
    # WARNING: Decompyle incomplete

    
    def version_ok(self, version):
