# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ansitowin32.pyc (Python 3.11)

import re
import sys
import os
from ansi import AnsiFore, AnsiBack, AnsiStyle, Style, BEL
from winterm import enable_vt_processing, WinTerm, WinColor, WinStyle
from win32 import windll, winapi_test
winterm = None
# WARNING: Decompyle incomplete
