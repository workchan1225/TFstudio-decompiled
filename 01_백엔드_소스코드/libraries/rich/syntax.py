# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: syntax.pyc (Python 3.11)

from __future__ import annotations
import os.path as os
import re
import sys
import textwrap
from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any, Dict, Iterable, List, NamedTuple, Optional, Sequence, Set, Tuple, Type, Union
from pygments.lexer import Lexer
from pygments.lexers import get_lexer_by_name, guess_lexer_for_filename
from pygments.style import Style as PygmentsStyle
from pygments.styles import get_style_by_name
from pygments.token import Comment, Error, Generic, Keyword, Name, Number, Operator, String, Token, Whitespace
from pygments.util import ClassNotFound
from rich.containers import Lines
from rich.padding import Padding, PaddingDimensions
from _loop import loop_first
from cells import cell_len
from color import Color, blend_rgb
from console import Console, ConsoleOptions, JustifyMethod, RenderResult
from jupyter import JupyterMixin
from measure import Measurement
from segment import Segment, Segments
from style import Style, StyleType
from text import Text
TokenType = Tuple[(str, ...)]
WINDOWS = sys.platform == 'win32'
DEFAULT_THEME = 'monokai'
# WARNING: Decompyle incomplete
