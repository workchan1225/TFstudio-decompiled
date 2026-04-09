# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: python.pyc (Python 3.11)

'''Python test discovery, setup and run of test functions.'''
from __future__ import annotations
import abc
from collections import Counter
from collections import defaultdict
from collections.abc import Callable
from collections.abc import Generator
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Mapping
from collections.abc import Sequence
import dataclasses
import enum
import fnmatch
from functools import partial
import inspect
import itertools
import os
from pathlib import Path
import re
import textwrap
import types
from typing import Any
from typing import cast
from typing import final
from typing import Literal
from typing import NoReturn
from typing import TYPE_CHECKING
import warnings
import _pytest
from _pytest import fixtures
from _pytest import nodes
from _pytest._code import filter_traceback
from _pytest._code import getfslineno
from _pytest._code.code import ExceptionInfo
from _pytest._code.code import TerminalRepr
from _pytest._code.code import Traceback
from _pytest._io.saferepr import saferepr
from _pytest.compat import ascii_escaped
from _pytest.compat import get_default_arg_names
from _pytest.compat import get_real_func
from _pytest.compat import getimfunc
from _pytest.compat import is_async_function
from _pytest.compat import LEGACY_PATH
from _pytest.compat import NOTSET
from _pytest.compat import safe_getattr
from _pytest.compat import safe_isclass
from _pytest.config import Config
from _pytest.config import hookimpl
from _pytest.config.argparsing import Parser
from _pytest.deprecated import check_ispytest
from _pytest.fixtures import FixtureDef
from _pytest.fixtures import FixtureRequest
from _pytest.fixtures import FuncFixtureInfo
from _pytest.fixtures import get_scope_node
from _pytest.main import Session
from _pytest.mark import ParameterSet
from _pytest.mark.structures import _HiddenParam
from _pytest.mark.structures import get_unpacked_marks
from _pytest.mark.structures import HIDDEN_PARAM
from _pytest.mark.structures import Mark
from _pytest.mark.structures import MarkDecorator
from _pytest.mark.structures import normalize_mark_list
from _pytest.outcomes import fail
from _pytest.outcomes import skip
from _pytest.pathlib import fnmatch_ex
from _pytest.pathlib import import_path
from _pytest.pathlib import ImportPathMismatchError
from _pytest.pathlib import scandir
from _pytest.scope import _ScopeName
from _pytest.scope import Scope
from _pytest.stash import StashKey
from _pytest.warning_types import PytestCollectionWarning
from _pytest.warning_types import PytestReturnNotNoneWarning
if TYPE_CHECKING:
    from typing_extensions import Self

def pytest_addoption(parser = None):
    parser.addini('python_files', type = 'args', default = [
        'test_*.py',
        '*_test.py'], help = 'Glob-style file patterns for Python test module discovery')
    parser.addini('python_classes', type = 'args', default = [
        'Test'], help = 'Prefixes or glob names for Python test class discovery')
    parser.addini('python_functions', type = 'args', default = [
        'test'], help = 'Prefixes or glob names for Python test function and method discovery')
    parser.addini('disable_test_id_escaping_and_forfeit_all_rights_to_community_support', type = 'bool', default = False, help = 'Disable string escape non-ASCII characters, might cause unwanted side effects(use at your own risk)')
    parser.addini('strict_parametrization_ids', type = 'bool', default = None, help = 'Emit an error if non-unique parameter set IDs are detected')


def pytest_generate_tests(metafunc = None):
    pass
# WARNING: Decompyle incomplete


def pytest_configure(config = None):
    config.addinivalue_line('markers', "parametrize(argnames, argvalues): call a test function multiple times passing in different arguments in turn. argvalues generally needs to be a list of values if argnames specifies only one name or a list of tuples of values if argnames specifies multiple names. Example: @parametrize('arg1', [1,2]) would lead to two calls of the decorated test function, one with arg1=1 and another with arg1=2.see https://docs.pytest.org/en/stable/how-to/parametrize.html for more info and examples.")
    config.addinivalue_line('markers', 'usefixtures(fixturename1, fixturename2, ...): mark tests as needing all of the specified fixtures. see https://docs.pytest.org/en/stable/explanation/fixtures.html#usefixtures ')


def async_fail(nodeid = None):
    msg = 'async def functions are not natively supported.\nYou need to install a suitable plugin for your async framework, for example:\n  - anyio\n  - pytest-asyncio\n  - pytest-tornasync\n  - pytest-trio\n  - pytest-twisted'
    fail(msg, pytrace = False)

pytest_pyfunc_call = (lambda pyfuncitem = None: pass# WARNING: Decompyle incomplete
)()

def pytest_collect_directory(path = None, parent = None):
    pkginit = path / '__init__.py'
    
    try:
        has_pkginit = pkginit.is_file()
    except PermissionError:
        return None

    if has_pkginit:
        return Package.from_parent(parent, path = path)


def pytest_collect_file(file_path = None, parent = None):
    if file_path.suffix == '.py':
        if not parent.session.isinitpath(file_path) and path_matches_patterns(file_path, parent.config.getini('python_files')):
            return None
        ihook = None.session.gethookproxy(file_path)
        module = ihook.pytest_pycollect_makemodule(module_path = file_path, parent = parent)
        return module


def path_matches_patterns(path = None, patterns = None):
    '''Return whether path matches any of the patterns in the list of globs given.'''
    pass
# WARNING: Decompyle incomplete


def pytest_pycollect_makemodule(module_path = None, parent = None):
    return Module.from_parent(parent, path = module_path)

pytest_pycollect_makeitem = (lambda collector = None, name = None, obj = hookimpl(trylast = True): pass# WARNING: Decompyle incomplete
)()

class PyobjMixin(nodes.Node):
    '''this mix-in inherits from Node to carry over the typing information

    as its intended to always mix in before a node
    its position in the mro is unaffected'''
    _ALLOW_MARKERS = True
    module = (lambda self: node = self.getparent(Module)# WARNING: Decompyle incomplete
)()
    cls = (lambda self: node = self.getparent(Class)# WARNING: Decompyle incomplete
)()
    instance = (lambda self: pass)()
    obj = (lambda self: obj = getattr(self, '_obj', None)# WARNING: Decompyle incomplete
)()
    obj = (lambda self, value: self._obj = value)()
    
    def _getobj(self):
        '''Get the underlying Python object. May be overwritten by subclasses.'''
        pass
    # WARNING: Decompyle incomplete

    
    def getmodpath(self = property, stopatmodule = property, includemodule = obj.setter):
