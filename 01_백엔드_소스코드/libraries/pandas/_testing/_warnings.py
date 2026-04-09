# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _warnings.pyc (Python 3.11)

from __future__ import annotations
from contextlib import AbstractContextManager, contextmanager, nullcontext
import inspect
import re
import sys
from typing import TYPE_CHECKING, Literal, Union, cast
import warnings
if TYPE_CHECKING:
    from collections.abc import Generator, Sequence
assert_produces_warning = (lambda expected_warning, filter_level = None, check_stacklevel = None, raise_on_extra_warnings = contextmanager, match = (Warning, 'always', True, True, None, True), must_find_all_warnings = ('expected_warning', 'type[Warning] | bool | tuple[type[Warning], ...] | None', 'filter_level', "Literal['error', 'ignore', 'always', 'default', 'module', 'once']", 'check_stacklevel', 'bool', 'raise_on_extra_warnings', 'bool', 'match', 'str | tuple[str | None, ...] | None', 'must_find_all_warnings', 'bool', 'return', 'Generator[list[warnings.WarningMessage]]'): pass# WARNING: Decompyle incomplete
)()

def maybe_produces_warning(warning = None, condition = None, **kwargs):
    '''
    Return a context manager that possibly checks a warning based on the condition
    '''
    pass
# WARNING: Decompyle incomplete


def _assert_caught_expected_warnings(*, caught_warnings, expected_warning, match, check_stacklevel):
    '''Assert that there was the expected warning among the caught warnings.'''
    saw_warning = False
    matched_message = False
    unmatched_messages = []
    warning_name = (lambda .0: pass# WARNING: Decompyle incomplete
)(expected_warning()) if isinstance(expected_warning, tuple) else expected_warning.__name__
# WARNING: Decompyle incomplete


def _assert_caught_no_extra_warnings(*, caught_warnings, expected_warning):
    '''Assert that no extra warnings apart from the expected ones are caught.'''
    extra_warnings = []
    for actual_warning in caught_warnings:
        if _is_unexpected_warning(actual_warning, expected_warning):
            if actual_warning.category == ResourceWarning:
                if 'unclosed <ssl.SSLSocket' in str(actual_warning.message):
                    continue
                if (lambda .0: pass# WARNING: Decompyle incomplete
)(sys.modules()):
                    continue
            if actual_warning.category == EncodingWarning:
                continue
            extra_warnings.append((actual_warning.category.__name__, actual_warning.message, actual_warning.filename, actual_warning.lineno))
        if extra_warnings:
            raise AssertionError(f'''Caused unexpected warning(s): {extra_warnings!r}''')
        return None


def _is_unexpected_warning(actual_warning = None, expected_warning = None):
    '''Check if the actual warning issued is unexpected.'''
    if not actual_warning and expected_warning:
        return True
    expected_warning = None(type[Warning], expected_warning)
    return bool(not issubclass(actual_warning.category, expected_warning))


def _assert_raised_with_correct_stacklevel(actual_warning = None):
    frame = inspect.currentframe()
# WARNING: Decompyle incomplete
