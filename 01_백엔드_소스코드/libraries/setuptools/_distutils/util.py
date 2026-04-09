# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

"""distutils.util

Miscellaneous utility functions -- anything that doesn't fit into
one of the other *util.py modules.
"""
import importlib.util as importlib
import os
import re
import string
import subprocess
import sys
import sysconfig
import functools
from distutils.errors import DistutilsPlatformError, DistutilsByteCompileError
from distutils.dep_util import newer
from distutils.spawn import spawn
from distutils import log

def get_host_platform():
