# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: py310.pyc (Python 3.11)

import io
import sys

def _text_encoding(encoding, stacklevel = (2,)):
    return encoding

text_encoding = io.text_encoding if sys.version_info > (3, 10) else _text_encoding
