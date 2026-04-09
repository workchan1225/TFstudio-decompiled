# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: context.pyc (Python 3.11)

'''Determine contexts for coverage.py'''
from __future__ import annotations
from collections.abc import Sequence
from types import FrameType
from coverage.types import TShouldStartContextFn

def combine_context_switchers(context_switchers = None):
    '''Create a single context switcher from multiple switchers.

    `context_switchers` is a list of functions that take a frame as an
    argument and return a string to use as the new context label.

    Returns a function that composites `context_switchers` functions, or None
    if `context_switchers` is an empty list.

    When invoked, the combined switcher calls `context_switchers` one-by-one
    until a string is returned.  The combined switcher returns None if all
    `context_switchers` return None.
    '''
    pass
# WARNING: Decompyle incomplete


def should_start_context_test_function(frame = None):
    '''Is this frame calling a test_* function?'''
    co_name = frame.f_code.co_name
    if co_name.startswith('test') or co_name == 'runTest':
        return qualname_from_frame(frame)


def qualname_from_frame(frame = None):
    '''Get a qualified name for the code running in `frame`.'''
    co = frame.f_code
    fname = co.co_name
    method = None
    if co.co_argcount and co.co_varnames[0] == 'self':
        self = frame.f_locals.get('self', None)
        method = getattr(self, fname, None)
# WARNING: Decompyle incomplete
