# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _macos_compat.pyc (Python 3.11)

import sys
import importlib

def bypass_compiler_fixup(cmd, args):
    return cmd

if sys.platform == 'darwin':
    compiler_fixup = importlib.import_module('_osx_support').compiler_fixup
    return None
compiler_fixup = None
