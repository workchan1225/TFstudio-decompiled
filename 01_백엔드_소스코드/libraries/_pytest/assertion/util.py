# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: util.pyc (Python 3.11)

'''Utilities for assertion debugging.'''
from __future__ import annotations
import collections.abc as collections
from collections.abc import Callable
from collections.abc import Iterable
from collections.abc import Mapping
from collections.abc import Sequence
from collections.abc import Set as AbstractSet
import pprint
from typing import Any
from typing import Literal
from typing import Protocol
from unicodedata import normalize
from _pytest import outcomes
import _pytest._code as _pytest
from _pytest._io.pprint import PrettyPrinter
from _pytest._io.saferepr import saferepr
from _pytest._io.saferepr import saferepr_unlimited
from _pytest.compat import running_on_ci
from _pytest.config import Config
_reprcompare: 'Callable[[str, object, object], str | None] | None' = None
_assertion_pass: 'Callable[[int, str, str], None] | None' = None
_config: 'Config | None' = None

class _HighlightFunc(Protocol):
    
    def __call__(self = None, source = None, lexer = None):
        '''Apply highlighting to the given source.'''
        pass



def dummy_highlighter(source = None, lexer = None):
    '''Dummy highlighter that returns the text unprocessed.

    Needed for _notin_text, as the diff gets post-processed to only show the "+" part.
    '''
    return source


def format_explanation(explanation = None):
    '''Format an explanation.

    Normally all embedded newlines are escaped, however there are
    three exceptions: \\n{, \\n} and \\n~.  The first two are intended
    cover nested explanations, see function and attribute explanations
    for examples (.visit_Call(), visit_Attribute()).  The last one is
    for when one explanation needs to span multiple lines, e.g. when
    displaying diffs.
    '''
    lines = _split_explanation(explanation)
    result = _format_lines(lines)
    return '\n'.join(result)


def _split_explanation(explanation = None):
    """Return a list of individual lines in the explanation.

    This will return a list of lines split on '\\n{', '\\n}' and '\\n~'.
    Any other newlines will be escaped and appear in the line as the
    literal '\\n' characters.
    """
    if not explanation:
        raw_lines = ''.split('\n')
        lines = [
            raw_lines[0]]
        for values in raw_lines[1:]:
            if values and values[0] in ('{', '}', '~', '>'):
                lines.append(values)
                continue
            return lines


def _format_lines(lines = None):
    """Format the individual lines.

    This will replace the '{', '}' and '~' characters of our mini formatting
    language with the proper 'where ...', 'and ...' and ' + ...' text, taking
    care of indentation along the way.

    Return a list of formatted lines.
    """
    result = list(lines[:1])
    stack = [
        0]
    stackcnt = [
        0]
# WARNING: Decompyle incomplete


def issequence(x = None):
