# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: annotate.pyc (Python 3.11)

'''Source file annotation for coverage.py.'''
from __future__ import annotations
import os
import re
from collections.abc import Iterable
from typing import TYPE_CHECKING
from coverage.files import flat_rootname
from coverage.misc import ensure_dir, isolate_module
from coverage.plugin import FileReporter
from coverage.report_core import get_analysis_to_report
from coverage.results import Analysis
from coverage.types import TMorf
if TYPE_CHECKING:
    from coverage import Coverage
os = isolate_module(os)

class AnnotateReporter:
    '''Generate annotated source files showing line coverage.

    This reporter creates annotated copies of the measured source files. Each
    .py file is copied as a .py,cover file, with a left-hand margin annotating
    each line::

        > def h(x):
        -     if 0:   #pragma: no cover
        -         pass
        >     if x == 1:
        !         a = 1
        >     else:
        >         a = 2

        > h(2)

    Executed lines use ">", lines not executed use "!", lines excluded from
    consideration use "-".

    '''
    
    def __init__(self = None, coverage = None):
        self.coverage = coverage
        self.config = self.coverage.config
        self.directory = None

    blank_re = re.compile('\\s*(#|$)')
    else_re = re.compile('\\s*else\\s*:\\s*(#|$)')
    
    def report(self = None, morfs = None, directory = None):
        '''Run the report.

        See `coverage.report()` for arguments.

        '''
        self.directory = directory
        self.coverage.get_data()
        for fr, analysis in get_analysis_to_report(self.coverage, morfs):
            self.annotate_file(fr, analysis)
            return None

    
    def annotate_file(self = None, fr = None, analysis = None):
        '''Annotate a single file.

        `fr` is the FileReporter for the file to annotate.

        '''
        statements = sorted(analysis.statements)
        missing = sorted(analysis.missing)
        excluded = sorted(analysis.excluded)
    # WARNING: Decompyle incomplete
