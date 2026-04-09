# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: reports.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Iterable
from collections.abc import Iterator
from collections.abc import Mapping
from collections.abc import Sequence
import dataclasses
from io import StringIO
import os
from pprint import pprint
import sys
from typing import Any
from typing import cast
from typing import final
from typing import Literal
from typing import NoReturn
from typing import TYPE_CHECKING
from _pytest._code.code import ExceptionChainRepr
from _pytest._code.code import ExceptionInfo
from _pytest._code.code import ExceptionRepr
from _pytest._code.code import ReprEntry
from _pytest._code.code import ReprEntryNative
from _pytest._code.code import ReprExceptionInfo
from _pytest._code.code import ReprFileLocation
from _pytest._code.code import ReprFuncArgs
from _pytest._code.code import ReprLocals
from _pytest._code.code import ReprTraceback
from _pytest._code.code import TerminalRepr
from _pytest._io import TerminalWriter
from _pytest.config import Config
from _pytest.nodes import Collector
from _pytest.nodes import Item
from _pytest.outcomes import fail
from _pytest.outcomes import skip
if sys.version_info < (3, 11):
    from exceptiongroup import BaseExceptionGroup
if TYPE_CHECKING:
    from typing_extensions import Self
    from _pytest.runner import CallInfo

def getworkerinfoline(node):
    pass
# WARNING: Decompyle incomplete


class BaseReport:
    outcome: "Literal['passed', 'failed', 'skipped']" = 'BaseReport'
    
    def __init__(self = None, **kw):
        self.__dict__.update(kw)

    if TYPE_CHECKING:
        
        def __getattr__(self = None, key = None):
            pass

    
    def toterminal(self = None, out = None):
        if hasattr(self, 'node'):
            worker_info = getworkerinfoline(self.node)
            if worker_info:
                out.line(worker_info)
        longrepr = self.longrepr
    # WARNING: Decompyle incomplete

    
    def get_sections(self = None, prefix = None):
        pass
    # WARNING: Decompyle incomplete

    longreprtext = (lambda self = None: file = StringIO()tw = TerminalWriter(file)tw.hasmarkup = Falseself.toterminal(tw)exc = file.getvalue()exc.strip())()
    caplog = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.get_sections('Captured log')())
)()
    capstdout = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.get_sections('Captured stdout')())
)()
    capstderr = (lambda self = None: (lambda .0: pass# WARNING: Decompyle incomplete
)(self.get_sections('Captured stderr')())
)()
    passed = (lambda self = None: self.outcome == 'passed')()
    failed = (lambda self = None: self.outcome == 'failed')()
    skipped = (lambda self = None: self.outcome == 'skipped')()
    fspath = (lambda self = None: self.nodeid.split('::')[0])()
    count_towards_summary = (lambda self = None: True)()
    head_line = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
    
    def _get_verbose_word_with_markup(self = None, config = None, default_markup = None):
