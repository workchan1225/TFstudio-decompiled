# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: http11.pyc (Python 3.11)

from __future__ import annotations
import dataclasses
import os
import re
import sys
import warnings
from collections.abc import Generator
from typing import Callable
from datastructures import Headers
from exceptions import SecurityError
from version import version as websockets_version
__all__ = [
    'SERVER',
    'USER_AGENT',
    'Request',
    'Response']
# WARNING: Decompyle incomplete
