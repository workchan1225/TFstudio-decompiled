# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: debugging.pyc (Python 3.11)

'''Interactive debugging with PDB, the Python Debugger.'''
from __future__ import annotations
import argparse
from collections.abc import Callable
from collections.abc import Generator
import functools
import sys
import types
from typing import Any
import unittest
from _pytest import outcomes
from _pytest._code import ExceptionInfo
from _pytest.capture import CaptureManager
from _pytest.config import Config
from _pytest.config import ConftestImportFailure
from _pytest.config import hookimpl
from _pytest.config import PytestPluginManager
from _pytest.config.argparsing import Parser
from _pytest.config.exceptions import UsageError
from _pytest.nodes import Node
from _pytest.reports import BaseReport
from _pytest.runner import CallInfo

def _validate_usepdb_cls(value = None):
    '''Validate syntax of --pdbcls option.'''
    
    try:
        (modname, classname) = value.split(':')
    except ValueError:
        e = None
        raise argparse.ArgumentTypeError(f'''{value!r} is not in the format \'modname:classname\''''), e
        e = None
        del e

    return (modname, classname)


def pytest_addoption(parser = None):
    group = parser.getgroup('general')
    group.addoption('--pdb', dest = 'usepdb', action = 'store_true', help = 'Start the interactive Python debugger on errors or KeyboardInterrupt')
    group.addoption('--pdbcls', dest = 'usepdb_cls', metavar = 'modulename:classname', type = _validate_usepdb_cls, help = 'Specify a custom interactive Python debugger for use with --pdb.For example: --pdbcls=IPython.terminal.debugger:TerminalPdb')
    group.addoption('--trace', dest = 'trace', action = 'store_true', help = 'Immediately break when running each test')


def pytest_configure(config = None):
    pass
# WARNING: Decompyle incomplete


class pytestPDB:
    '''Pseudo PDB that defers to the real pdb.'''
    _pluginmanager: 'PytestPluginManager | None' = None
    _config: 'Config | None' = None
    _saved: 'list[tuple[Callable[..., None], PytestPluginManager | None, Config | None]]' = []
    _recursive_debug = 0
    _wrapped_pdb_cls: 'tuple[type[Any], type[Any]] | None' = None
    _is_capturing = (lambda cls = None, capman = None: if capman:
capman.is_capturing())()
    _import_pdb_cls = (lambda cls = None, capman = None: if not cls._config:
import pdbpdb.Pdbusepdb_cls = None._config.getvalue('usepdb_cls')if cls._wrapped_pdb_cls and cls._wrapped_pdb_cls[0] == usepdb_cls:
cls._wrapped_pdb_cls[1]if None:
(modname, classname) = usepdb_clstry:
__import__(modname)mod = sys.modules[modname]parts = classname.split('.')pdb_cls = getattr(mod, parts[0])for part in parts[1:]:
pdb_cls = getattr(pdb_cls, part)except Exception:
exc = Nonevalue = ':'.join((modname, classname))raise UsageError(f'''--pdbcls: could not import {value!r}: {exc}'''), excexc = Nonedel excimport pdbpdb_cls = pdb.Pdbwrapped_cls = cls._get_pdb_wrapper_class(pdb_cls, capman)cls._wrapped_pdb_cls = (usepdb_cls, wrapped_cls)wrapped_cls)()
    _get_pdb_wrapper_class = (lambda cls = None, pdb_cls = None, capman = classmethod: pass# WARNING: Decompyle incomplete
)()
    _init_pdb = (lambda cls, method: import _pytest.config as _pytest# WARNING: Decompyle incomplete
)()
    set_trace = (lambda cls = None: frame = sys._getframe().f_back# WARNING: Decompyle incomplete
)()


class PdbInvoke:
    
    def pytest_exception_interact(self = None, node = None, call = None, report = ('node', 'Node', 'call', 'CallInfo[Any]', 'report', 'BaseReport', 'return', 'None')):
        capman = node.config.pluginmanager.getplugin('capturemanager')
        if capman:
            capman.suspend_global_capture(in_ = True)
            (out, err) = capman.read_global_capture()
            sys.stdout.write(out)
            sys.stdout.write(err)
    # WARNING: Decompyle incomplete

    
    def pytest_internalerror(self = None, excinfo = None):
        exc_or_tb = _postmortem_exc_or_tb(excinfo)
        post_mortem(exc_or_tb)



class PdbTrace:
    pytest_pyfunc_call = (lambda self = None, pyfuncitem = None: pass# WARNING: Decompyle incomplete
)()


def wrap_pytest_function_for_tracing(pyfuncitem = None):
    '''Change the Python function object of the given Function item by a
    wrapper which actually enters pdb before calling the python function
    itself, effectively leaving the user in the pdb prompt in the first
    statement of the function.'''
    pass
# WARNING: Decompyle incomplete


def maybe_wrap_pytest_function_for_tracing(pyfuncitem = None):
    '''Wrap the given pytestfunct item for tracing support if --trace was given in
    the command line.'''
    if pyfuncitem.config.getvalue('trace'):
        wrap_pytest_function_for_tracing(pyfuncitem)
        return None


def _enter_pdb(node = None, excinfo = None, rep = None):
    tw = node.config.pluginmanager.getplugin('terminalreporter')._tw
    tw.line()
    showcapture = node.config.option.showcapture
    for sectionname, content in (('stdout', rep.capstdout), ('stderr', rep.capstderr), ('log', rep.caplog)):
        if showcapture in (sectionname, 'all') and content:
            tw.sep('>', 'captured ' + sectionname)
            if content[-1:] == '\n':
                content = content[:-1]
            tw.line(content)
        tw.sep('>', 'traceback')
        rep.toterminal(tw)
        tw.sep('>', 'entering PDB')
        tb_or_exc = _postmortem_exc_or_tb(excinfo)
        rep._pdbshown = True
        post_mortem(tb_or_exc)
        return rep


def _postmortem_exc_or_tb(excinfo = None):
    UnexpectedException = UnexpectedException
    import doctest
    get_exc = sys.version_info >= (3, 13)
    if isinstance(excinfo.value, UnexpectedException):
        underlying_exc = excinfo.value
        if get_exc:
            return underlying_exc.exc_info[1]
        return None.exc_info[2]
# WARNING: Decompyle incomplete


def post_mortem(tb_or_exc = None):
    p = pytestPDB._init_pdb('post_mortem')
    p.reset()
    p.interaction(None, tb_or_exc)
    if p.quitting:
        outcomes.exit('Quitting debugger')
        return None
