# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: wait.pyc (Python 3.11)

from __future__ import annotations
import select
import socket
from functools import partial
__all__ = [
    'wait_for_read',
    'wait_for_write']

def select_wait_for_socket(sock = None, read = None, write = None, timeout = (False, False, None)):
