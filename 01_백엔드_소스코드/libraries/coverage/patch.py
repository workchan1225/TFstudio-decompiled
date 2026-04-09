# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: patch.pyc (Python 3.11)

'''Invasive patches for coverage.py.'''
from __future__ import annotations
import contextlib
import os
from typing import TYPE_CHECKING, Any, NoReturn
from coverage import env
from coverage.debug import DevNullDebug
from coverage.exceptions import ConfigError, CoverageException
if TYPE_CHECKING:
    from coverage import Coverage
    from coverage.config import CoverageConfig
    from coverage.types import TDebugCtl

def apply_patches(cov = None, config = None, debug = None):
    '''Apply invasive patches requested by `[run] patch=`.'''
    debug = debug if debug.should('patch') else DevNullDebug()
    for patch in sorted(set(config.patch)):
        if patch == '_exit':
            patch
            _patch__exit(cov, debug)
            continue
        if None == 'execv':
            _patch_execv(cov, config, debug)
            continue
        if None == 'fork':
            _patch_fork(debug)
            continue
        if None == 'subprocess':
            _patch_subprocess(config, debug)
            continue
        raise ConfigError(f'''Unknown patch {patch!r}''')
        return None


def _patch__exit(cov = None, debug = None):
    '''Patch os._exit.'''
    pass
# WARNING: Decompyle incomplete


def _patch_execv(cov = None, config = None, debug = None):
    '''Patch the execv family of functions.'''
    pass
# WARNING: Decompyle incomplete


def _patch_fork(debug = None):
    '''Ensure Coverage is properly reset after a fork.'''
    _after_fork_in_child = _after_fork_in_child
    import coverage.control
    if env.WINDOWS:
        raise CoverageException("patch=fork isn't supported yet on Windows.")
    debug.write('Patching fork')
    os.register_at_fork(after_in_child = _after_fork_in_child)


def _patch_subprocess(config = None, debug = None):
    '''Write .pth files and set environment vars to measure subprocesses.'''
    debug.write('Patching subprocess')
# WARNING: Decompyle incomplete
