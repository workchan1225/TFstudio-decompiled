# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

import os
import typing
from typing import NamedTuple, Union, Callable, Any, Generator, Tuple, List, TextIO, Set, Sequence
from abc import ABC, abstractmethod
from enum import Enum
import string
import copy
import warnings
import re
import sys
from collections.abc import Iterable
import traceback
import types
from operator import itemgetter
from functools import wraps
from threading import RLock
from pathlib import Path
from util import _FifoCache, _UnboundedCache, __config_flags, _collapse_string_to_ranges, _escape_regex_range_chars, _bslash, _flatten, LRUMemo as _LRUMemo, UnboundedMemo as _UnboundedMemo
from exceptions import *
from actions import *
from results import ParseResults, _ParseResultsWithOffset
from unicode import pyparsing_unicode
_MAX_INT = sys.maxsize
str_type: Tuple[(type, ...)] = (str, bytes)

class __compat__(__config_flags):
    '''
    A cross-version compatibility configuration for pyparsing features that will be
    released in a future version. By setting values in this configuration to True,
    those features can be enabled in prior versions for compatibility development
    and testing.

    - ``collect_all_And_tokens`` - flag to enable fix for Issue #63 that fixes erroneous grouping
      of results names when an :class:`And` expression is nested within an :class:`Or` or :class:`MatchFirst`;
      maintained for compatibility, but setting to ``False`` no longer restores pre-2.3.1
      behavior
    '''
    _type_desc = 'compatibility'
    collect_all_And_tokens = True
    _all_names = locals()()
    _fixed_names = '\n        collect_all_And_tokens\n        '.split()


class __diag__(__config_flags):
    _type_desc = 'diagnostic'
    warn_multiple_tokens_in_named_alternation = False
    warn_ungrouped_named_tokens_in_collection = False
    warn_name_set_on_empty_Forward = False
    warn_on_parse_using_empty_Forward = False
    warn_on_assignment_to_Forward = False
    warn_on_multiple_string_args_to_oneof = False
    warn_on_match_first_with_lshift_operator = False
    enable_debug_on_named_expressions = False
    _all_names = locals()()
    _warning_names = _all_names()
    _debug_names = _all_names()
    enable_all_warnings = (lambda cls = (lambda .0: pass# WARNING: Decompyle incomplete
): for name in cls._warning_names:
cls.enable(name)None)()


class Diagnostics(Enum):
    """
    Diagnostic configuration (all default to disabled)
    - ``warn_multiple_tokens_in_named_alternation`` - flag to enable warnings when a results
      name is defined on a :class:`MatchFirst` or :class:`Or` expression with one or more :class:`And` subexpressions
    - ``warn_ungrouped_named_tokens_in_collection`` - flag to enable warnings when a results
      name is defined on a containing expression with ungrouped subexpressions that also
      have results names
    - ``warn_name_set_on_empty_Forward`` - flag to enable warnings when a :class:`Forward` is defined
      with a results name, but has no contents defined
    - ``warn_on_parse_using_empty_Forward`` - flag to enable warnings when a :class:`Forward` is
      defined in a grammar but has never had an expression attached to it
    - ``warn_on_assignment_to_Forward`` - flag to enable warnings when a :class:`Forward` is defined
      but is overwritten by assigning using ``'='`` instead of ``'<<='`` or ``'<<'``
    - ``warn_on_multiple_string_args_to_oneof`` - flag to enable warnings when :class:`one_of` is
      incorrectly called with multiple str arguments
    - ``enable_debug_on_named_expressions`` - flag to auto-enable debug on all subsequent
      calls to :class:`ParserElement.set_name`

    Diagnostics are enabled/disabled by calling :class:`enable_diag` and :class:`disable_diag`.
    All warnings can be enabled by calling :class:`enable_all_warnings`.
    """
    warn_multiple_tokens_in_named_alternation = 0
    warn_ungrouped_named_tokens_in_collection = 1
    warn_name_set_on_empty_Forward = 2
    warn_on_parse_using_empty_Forward = 3
    warn_on_assignment_to_Forward = 4
    warn_on_multiple_string_args_to_oneof = 5
    warn_on_match_first_with_lshift_operator = 6
    enable_debug_on_named_expressions = 7


def enable_diag(diag_enum = None):
    '''
    Enable a global pyparsing diagnostic flag (see :class:`Diagnostics`).
    '''
    __diag__.enable(diag_enum.name)


def disable_diag(diag_enum = None):
    '''
    Disable a global pyparsing diagnostic flag (see :class:`Diagnostics`).
    '''
    __diag__.disable(diag_enum.name)


def enable_all_warnings():
    '''
    Enable all global pyparsing diagnostic warnings (see :class:`Diagnostics`).
    '''
    __diag__.enable_all_warnings()

del __config_flags

def _should_enable_warnings(cmd_line_warn_options = None, warn_env_var = None):
    enable = bool(warn_env_var)
    for warn_opt in cmd_line_warn_options:
        (w_action, w_message, w_category, w_module, w_line) = (warn_opt + '::::').split(':')[:5]
        if not w_action.lower().startswith('i'):
            if w_message and w_category or w_module or w_module == 'pyparsing':
                enable = True
                continue
        if w_action.lower().startswith('i') and w_module in ('pyparsing', ''):
            enable = False
        return enable

if _should_enable_warnings(sys.warnoptions, os.environ.get('PYPARSINGENABLEALLWARNINGS')):
    enable_all_warnings()
_single_arg_builtins = {
    sum,
    len,
    sorted,
    reversed,
    list,
    tuple,
    set,
    any,
    all,
    min,
    max}
_generatorType = types.GeneratorType
ParseAction = Union[(Callable[([], Any)], Callable[([
    ParseResults], Any)], Callable[([
    int,
    ParseResults], Any)], Callable[([
    str,
    int,
    ParseResults], Any)])]
ParseCondition = Union[(Callable[([], bool)], Callable[([
    ParseResults], bool)], Callable[([
    int,
    ParseResults], bool)], Callable[([
    str,
    int,
    ParseResults], bool)])]
ParseFailAction = Callable[([
    str,
    int,
    'ParserElement',
    Exception], None)]
DebugStartAction = Callable[([
    str,
    int,
    'ParserElement',
    bool], None)]
DebugSuccessAction = Callable[([
    str,
    int,
    int,
    'ParserElement',
    ParseResults,
    bool], None)]
DebugExceptionAction = Callable[([
    str,
    int,
    'ParserElement',
    Exception,
    bool], None)]
alphas = string.ascii_uppercase + string.ascii_lowercase
identchars = pyparsing_unicode.Latin1.identchars
identbodychars = pyparsing_unicode.Latin1.identbodychars
nums = '0123456789'
hexnums = nums + 'ABCDEFabcdef'
alphanums = alphas + nums
printables = (lambda .0: pass# WARNING: Decompyle incomplete
)(string.printable())
_trim_arity_call_line: traceback.StackSummary = None

def _trim_arity(func, max_limit = (3,)):
    '''decorator to trim function calls to match the arity of the target'''
    pass
# WARNING: Decompyle incomplete


def condition_as_parse_action(fn = None, message = None, fatal = ''.join):
    '''
    Function to convert a simple predicate function that returns ``True`` or ``False``
    into a parse action. Can be used in places when a parse action is required
    and :class:`ParserElement.add_condition` cannot be used (such as when adding a condition
    to an operator level in :class:`infix_notation`).

    Optional keyword arguments:

    - ``message`` - define a custom message to be used in the raised exception
    - ``fatal`` - if True, will raise :class:`ParseFatalException` to stop parsing immediately;
      otherwise will raise :class:`ParseException`

    '''
    pass
# WARNING: Decompyle incomplete


def _default_start_debug_action(instring = None, loc = None, expr = None, cache_hit = (False,)):
    cache_hit_str = '*' if cache_hit else ''
    print('{}Match {} at loc {}({},{})\n  {}\n  {}^'.format(cache_hit_str, expr, loc, lineno(loc, instring), col(loc, instring), line(loc, instring), ' ' * (col(loc, instring) - 1)))


def _default_success_debug_action(instring, startloc = None, endloc = None, expr = None, toks = (False,), cache_hit = ('instring', str, 'startloc', int, 'endloc', int, 'expr', 'ParserElement', 'toks', ParseResults, 'cache_hit', bool)):
    cache_hit_str = '*' if cache_hit else ''
    print('{}Matched {} -> {}'.format(cache_hit_str, expr, toks.as_list()))


def _default_exception_debug_action(instring = None, loc = None, expr = None, exc = (False,), cache_hit = ('instring', str, 'loc', int, 'expr', 'ParserElement', 'exc', Exception, 'cache_hit', bool)):
    cache_hit_str = '*' if cache_hit else ''
    print('{}Match {} failed, {} raised: {}'.format(cache_hit_str, expr, type(exc).__name__, exc))


def null_debug_action(*args):
    """'Do-nothing' debug action, to suppress debugging output during parsing."""
    pass


class ParserElement(ABC):
    '''Abstract base level parser element class.'''
    DEFAULT_WHITE_CHARS: str = ' \n\t\r'
    verbose_stacktrace: bool = False
    _literalStringClass: typing.Optional[type] = None
    set_default_whitespace_chars = (lambda chars = None: ParserElement.DEFAULT_WHITE_CHARS = charsfor expr in _builtin_exprs:
if expr.copyDefaultWhiteChars:
expr.whiteChars = set(chars)None)()
    inline_literals_using = (lambda cls = None: ParserElement._literalStringClass = cls)()
    
    class DebugActions(NamedTuple):
        debug_fail: typing.Optional[DebugExceptionAction] = 'ParserElement.DebugActions'

    
    def __init__(self = None, savelist = None):
        self.parseAction = list()
        self.failAction = None
        self.customName = None
        self._defaultName = None
        self.resultsName = None
        self.saveAsList = savelist
        self.skipWhitespace = True
        self.whiteChars = set(ParserElement.DEFAULT_WHITE_CHARS)
        self.copyDefaultWhiteChars = True
        self.mayReturnEmpty = False
        self.keepTabs = False
        self.ignoreExprs = list()
        self.debug = False
        self.streamlined = False
        self.mayIndexError = True
        self.errmsg = ''
        self.modalResults = True
        self.debugActions = self.DebugActions(None, None, None)
        self.callPreparse = True
        self.callDuringTry = False
        self.suppress_warnings_ = []

    
    def suppress_warning(self = None, warning_type = None):
        '''
        Suppress warnings emitted for a particular diagnostic on this expression.

        Example::

            base = pp.Forward()
            base.suppress_warning(Diagnostics.warn_on_parse_using_empty_Forward)

            # statement would normally raise a warning, but is now suppressed
            print(base.parseString("x"))

        '''
        self.suppress_warnings_.append(warning_type)
        return self

    
    def copy(self = None):
        '''
        Make a copy of this :class:`ParserElement`.  Useful for defining
        different parse actions for the same parsing pattern, using copies of
        the original parse element.

        Example::

            integer = Word(nums).set_parse_action(lambda toks: int(toks[0]))
            integerK = integer.copy().add_parse_action(lambda toks: toks[0] * 1024) + Suppress("K")
            integerM = integer.copy().add_parse_action(lambda toks: toks[0] * 1024 * 1024) + Suppress("M")

            print((integerK | integerM | integer)[1, ...].parse_string("5K 100 640K 256M"))

        prints::

            [5120, 100, 655360, 268435456]

        Equivalent form of ``expr.copy()`` is just ``expr()``::

            integerM = integer().add_parse_action(lambda toks: toks[0] * 1024 * 1024) + Suppress("M")
        '''
        cpy = copy.copy(self)
        cpy.parseAction = self.parseAction[:]
        cpy.ignoreExprs = self.ignoreExprs[:]
        if self.copyDefaultWhiteChars:
            cpy.whiteChars = set(ParserElement.DEFAULT_WHITE_CHARS)
        return cpy

    
    def set_results_name(self = None, name = None, list_all_matches = None, *, listAllMatches):
