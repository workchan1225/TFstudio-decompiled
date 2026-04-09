# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: ironpython_console.pyc (Python 3.11)

import os
import re
import IronPythonConsole
import System
from pyreadline3.console.ansi import AnsiState
from pyreadline3.keysyms import make_keyinfo, make_KeyPress, make_KeyPress_from_keydescr, make_keysym
from pyreadline3.logger import log
from event import Event
import sys
import clr
clr.AddReferenceToFileAndPath(sys.executable)
color = System.ConsoleColor
# WARNING: Decompyle incomplete
