# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _reloader.pyc (Python 3.11)

from __future__ import annotations
import fnmatch
import os
import subprocess
import sys
import threading
import time
import typing as t
from itertools import chain
from pathlib import PurePath
from _internal import _log
_ignore_always = tuple({
    sys.base_prefix,
    sys.base_exec_prefix})
# WARNING: Decompyle incomplete
