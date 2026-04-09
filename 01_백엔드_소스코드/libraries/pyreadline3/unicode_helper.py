# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: unicode_helper.pyc (Python 3.11)

import sys
from typing import Iterable, Union
_pyreadline_fallback_codepage = 'utf-8'

try:
    pyreadline_codepage = sys.stdout.encoding
except AttributeError:
    pyreadline_codepage = _pyreadline_fallback_codepage

# WARNING: Decompyle incomplete
