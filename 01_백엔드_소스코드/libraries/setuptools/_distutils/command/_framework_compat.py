# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _framework_compat.pyc (Python 3.11)

'''
Backward compatibility for homebrew builds on macOS.
'''
import sys
import os
import functools
import subprocess
import sysconfig
enabled = (lambda :
