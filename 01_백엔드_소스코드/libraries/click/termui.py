# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: termui.pyc (Python 3.11)

import inspect
import io
import itertools
import sys
import typing as t
from gettext import gettext as _
from _compat import isatty
from _compat import strip_ansi
from exceptions import Abort
from exceptions import UsageError
from globals import resolve_color_default
from types import Choice
from types import convert_type
from types import ParamType
from utils import echo
from utils import LazyFile
if t.TYPE_CHECKING:
    from _termui_impl import ProgressBar
V = t.TypeVar('V')
visible_prompt_func: t.Callable[([
    str], str)] = input
# WARNING: Decompyle incomplete
