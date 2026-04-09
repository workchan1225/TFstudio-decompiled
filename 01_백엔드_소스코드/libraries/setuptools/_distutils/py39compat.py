# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py39compat.pyc (Python 3.11)

import sys
import platform

def add_ext_suffix_39(vars):
    """
    Ensure vars contains 'EXT_SUFFIX'. pypa/distutils#130
    """
    import _imp
    ext_suffix = _imp.extension_suffixes()[0]
    vars.update(EXT_SUFFIX = ext_suffix, SO = ext_suffix)

if sys.version_info < (3, 10):
    needs_ext_suffix = platform.system() == 'Windows'
add_ext_suffix = add_ext_suffix_39 if needs_ext_suffix else (lambda vars: pass)
