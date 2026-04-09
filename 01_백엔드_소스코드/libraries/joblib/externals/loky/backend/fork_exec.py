# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fork_exec.pyc (Python 3.11)

import sys
import os
import subprocess

def fork_exec(cmd, keep_fds, env = (None,)):
    import _posixsubprocess
    cmd = cmd()
# WARNING: Decompyle incomplete
