# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: columns.pyc (Python 3.11)

from collections import defaultdict
from itertools import chain
from operator import itemgetter
from typing import Dict, Iterable, List, Optional, Tuple
from align import Align, AlignMethod
from console import Console, ConsoleOptions, RenderableType, RenderResult
from constrain import Constrain
from measure import Measurement
from padding import Padding, PaddingDimensions
from table import Table
from text import TextType
from jupyter import JupyterMixin

class Columns(JupyterMixin):
    '''Display renderables in neat columns.

    Args:
        renderables (Iterable[RenderableType]): Any number of Rich renderables (including str).
        width (int, optional): The desired width of the columns, or None to auto detect. Defaults to None.
        padding (PaddingDimensions, optional): Optional padding around cells. Defaults to (0, 1).
        expand (bool, optional): Expand columns to full width. Defaults to False.
        equal (bool, optional): Arrange in to equal sized columns. Defaults to False.
        column_first (bool, optional): Align items from top to bottom (rather than left to right). Defaults to False.
        right_to_left (bool, optional): Start column from right hand side. Defaults to False.
        align (str, optional): Align value ("left", "right", or "center") or None for default. Defaults to None.
        title (TextType, optional): Optional title for Columns.
    '''
    
    def __init__(self = None, renderables = None, padding = None, *, width, expand, equal, column_first, right_to_left, align, title):
