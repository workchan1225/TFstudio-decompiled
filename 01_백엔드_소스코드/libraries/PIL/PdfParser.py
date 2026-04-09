# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: PdfParser.pyc (Python 3.11)

from __future__ import annotations
import calendar
import codecs
import collections
import mmap
import os
import re
import time
import zlib
from typing import Any, NamedTuple
TYPE_CHECKING = False
if TYPE_CHECKING:
    from typing import IO
    _DictBase = collections.UserDict[(str | bytes, Any)]
else:
    _DictBase = collections.UserDict

def encode_text(s = None):
    return codecs.BOM_UTF16_BE + s.encode('utf_16_be')

# WARNING: Decompyle incomplete
