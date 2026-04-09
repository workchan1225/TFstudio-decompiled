# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: log.pyc (Python 3.11)

from pyreadline3.unicode_helper import ensure_str
from logger import LOGGER

def log(record = None):
    s = ensure_str(record)
    LOGGER.debug(s)
