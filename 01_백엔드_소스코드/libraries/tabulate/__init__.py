# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__doc__ = 'Pretty-print tabular data.'
from collections import namedtuple
from collections.abc import Iterable, Sized
from html import escape as htmlescape
from itertools import chain, zip_longest as izip_longest
from functools import reduce, partial
import io
import re
import math
import textwrap
import dataclasses

try:
    import wcwidth
except ImportError:
    wcwidth = None


def _is_file(f):
    return isinstance(f, io.IOBase)

__all__ = [
    'tabulate',
    'tabulate_formats',
    'simple_separated_format']

try:
    from version import version as __version__
except ImportError:
    pass

MIN_PADDING = 2
PRESERVE_WHITESPACE = False
_DEFAULT_FLOATFMT = 'g'
_DEFAULT_INTFMT = ''
_DEFAULT_MISSINGVAL = ''
_DEFAULT_ALIGN = 'default'
WIDE_CHARS_MODE = wcwidth is not None
SEPARATING_LINE = '\x01'
Line = namedtuple('Line', [
    'begin',
    'hline',
    'sep',
    'end'])
DataRow = namedtuple('DataRow', [
    'begin',
    'sep',
    'end'])
TableFormat = namedtuple('TableFormat', [
    'lineabove',
    'linebelowheader',
    'linebetweenrows',
    'linebelow',
    'headerrow',
    'datarow',
    'padding',
    'with_header_hide'])

def _is_separating_line(row):
