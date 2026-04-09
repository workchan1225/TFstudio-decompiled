# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _callers.pyc (Python 3.11)

'''
Call loop machinery
'''
from __future__ import annotations
from collections.abc import Generator
from collections.abc import Mapping
from collections.abc import Sequence
from typing import cast
from typing import NoReturn
import warnings
from _hooks import HookImpl
from _result import HookCallError
from _result import Result
from _warnings import PluggyTeardownRaisedWarning
Teardown = Generator[(None, object, object)]

def run_old_style_hookwrapper(hook_impl = None, hook_name = None, args = None):
    '''
    backward compatibility wrapper to run a old style hookwrapper as a wrapper
    '''
    pass
# WARNING: Decompyle incomplete


def _raise_wrapfail(wrap_controller = None, msg = None):
    co = wrap_controller.gi_code
    raise RuntimeError(f'''wrap_controller at {co.co_name!r} {co.co_filename}:{co.co_firstlineno} {msg}''')


def _warn_teardown_exception(hook_name = None, hook_impl = None, e = None):
    msg = 'A plugin raised an exception during an old-style hookwrapper teardown.\n'
    msg += f'''Plugin: {hook_impl.plugin_name}, Hook: {hook_name}\n'''
    msg += f'''{type(e).__name__}: {e}\n'''
    msg += 'For more information see https://pluggy.readthedocs.io/en/stable/api_reference.html#pluggy.PluggyTeardownRaisedWarning'
    warnings.warn(PluggyTeardownRaisedWarning(msg), stacklevel = 6)


def _multicall(hook_name = None, hook_impls = None, caller_kwargs = None, firstresult = ('hook_name', 'str', 'hook_impls', 'Sequence[HookImpl]', 'caller_kwargs', 'Mapping[str, object]', 'firstresult', 'bool', 'return', 'object | list[object]')):
    '''Execute a call into multiple python functions/methods and return the
    result(s).

    ``caller_kwargs`` comes from HookCaller.__call__().
    '''
    pass
# WARNING: Decompyle incomplete
