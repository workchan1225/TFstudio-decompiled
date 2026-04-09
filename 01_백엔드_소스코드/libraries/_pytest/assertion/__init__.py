# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''Support for presenting detailed information in failing assertions.'''
from __future__ import annotations
from collections.abc import Generator
import sys
from typing import Any
from typing import Protocol
from typing import TYPE_CHECKING
from _pytest.assertion import rewrite
from _pytest.assertion import truncate
from _pytest.assertion import util
from _pytest.assertion.rewrite import assertstate_key
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.nodes import Item
if TYPE_CHECKING:
    from _pytest.main import Session

def pytest_addoption(parser = None):
    group = parser.getgroup('debugconfig')
    group.addoption('--assert', action = 'store', dest = 'assertmode', choices = ('rewrite', 'plain'), default = 'rewrite', metavar = 'MODE', help = "Control assertion debugging tools.\n'plain' performs no assertion debugging.\n'rewrite' (the default) rewrites assert statements in test modules on import to provide assert expression information.")
    parser.addini('enable_assertion_pass_hook', type = 'bool', default = False, help = 'Enables the pytest_assertion_pass hook. Make sure to delete any previously generated pyc cache files.')
    parser.addini('truncation_limit_lines', default = None, help = 'Set threshold of LINES after which truncation will take effect')
    parser.addini('truncation_limit_chars', default = None, help = 'Set threshold of CHARS after which truncation will take effect')
    Config._add_verbosity_ini(parser, Config.VERBOSITY_ASSERTIONS, help = 'Specify a verbosity level for assertions, overriding the main level. Higher levels will provide more detailed explanation when an assertion fails.')


def register_assert_rewrite(*names):
    '''Register one or more module names to be rewritten on import.

    This function will make sure that this module or all modules inside
    the package will get their assert statements rewritten.
    Thus you should make sure to call this before the module is
    actually imported, usually in your __init__.py if you are a plugin
    using a package.

    :param names: The module names to register.
    '''
    pass
# WARNING: Decompyle incomplete


class RewriteHook(Protocol):
    
    def mark_rewrite(self = None, *names):
        pass



class DummyRewriteHook:
    '''A no-op import hook for when rewriting is disabled.'''
    
    def mark_rewrite(self = None, *names):
        pass



class AssertionState:
    '''State for the assertion plugin.'''
    
    def __init__(self = None, config = None, mode = None):
        self.mode = mode
        self.trace = config.trace.root.get('assertion')
        self.hook = None



def install_importhook(config = None):
    '''Try to install the rewrite hook, raise SystemError if it fails.'''
    pass
# WARNING: Decompyle incomplete


def pytest_collection(session = None):
    assertstate = session.config.stash.get(assertstate_key, None)
# WARNING: Decompyle incomplete

pytest_runtest_protocol = (lambda item = None: pass# WARNING: Decompyle incomplete
)()

def pytest_sessionfinish(session = None):
    assertstate = session.config.stash.get(assertstate_key, None)
# WARNING: Decompyle incomplete


def pytest_assertrepr_compare(config = None, op = None, left = None, right = ('config', 'Config', 'op', 'str', 'left', 'Any', 'right', 'Any', 'return', 'list[str] | None')):
    return util.assertrepr_compare(config = config, op = op, left = left, right = right)
