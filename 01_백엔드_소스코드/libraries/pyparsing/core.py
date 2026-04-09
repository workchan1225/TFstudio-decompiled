# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

from __future__ import annotations
import collections.abc as collections
from collections import deque
import os
import typing
from typing import Any, Callable, Generator, NamedTuple, Sequence, TextIO, Union, cast
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
from util import _FifoCache, _UnboundedCache, __config_flags, _collapse_string_to_ranges, _escape_regex_range_chars, _flatten, LRUMemo as _LRUMemo, UnboundedMemo as _UnboundedMemo, replaced_by_pep8
from exceptions import *
from actions import *
from results import ParseResults, _ParseResultsWithOffset
from unicode import pyparsing_unicode
_MAX_INT = sys.maxsize
str_type: 'tuple[type, ...]' = (str, bytes)
from functools import cached_property

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
ParseImplReturnType = tuple[(int, Any)]
PostParseReturnType = Union[(ParseResults, Sequence[ParseResults])]
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
alphas: 'str' = string.ascii_uppercase + string.ascii_lowercase
identchars: 'str' = pyparsing_unicode.Latin1.identchars
identbodychars: 'str' = pyparsing_unicode.Latin1.identbodychars
nums: 'str' = '0123456789'
hexnums: 'str' = nums + 'ABCDEFabcdef'
alphanums: 'str' = alphas + nums
printables: 'str' = (lambda .0: pass# WARNING: Decompyle incomplete
)(string.printable())

class _ParseActionIndexError(Exception):
    """
    Internal wrapper around IndexError so that IndexErrors raised inside
    parse actions aren't misinterpreted as IndexErrors raised inside
    ParserElement parseImpl methods.
    """
    
    def __init__(self = None, msg = None, exc = None):
        self.msg = msg
        self.exc = exc


_trim_arity_call_line: 'traceback.StackSummary' = None
pa_call_line_synth = ()

def _trim_arity(func, max_limit = (3,)):
    '''decorator to trim function calls to match the arity of the target'''
    pass
# WARNING: Decompyle incomplete


def condition_as_parse_action(fn = None, message = ''.join, fatal = None):
    '''
    Function to convert a simple predicate function that returns ``True`` or ``False``
    into a parse action. Can be used in places when a parse action is required
    and :meth:`ParserElement.add_condition` cannot be used (such as when adding a condition
    to an operator level in :class:`infix_notation`).

    Optional keyword arguments:

    :param message: define a custom message to be used in the raised exception
    :param fatal: if ``True``, will raise :class:`ParseFatalException`
                  to stop parsing immediately;
                  otherwise will raise :class:`ParseException`

    '''
    pass
# WARNING: Decompyle incomplete


def _default_start_debug_action(instring = None, loc = None, expr = None, cache_hit = (False,)):
    cache_hit_str = '*' if cache_hit else ''
    print(f'''{cache_hit_str}Match {expr} at loc {loc}({lineno(loc, instring)},{col(loc, instring)})\n  {line(loc, instring)}\n  {'^':
