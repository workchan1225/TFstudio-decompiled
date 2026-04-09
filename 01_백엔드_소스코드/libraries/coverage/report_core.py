# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: report_core.pyc (Python 3.11)

'''Reporter foundation for coverage.py.'''
from __future__ import annotations
import sys
from collections.abc import Iterable
from typing import IO, TYPE_CHECKING, Callable, Protocol
from coverage.exceptions import NoDataError, NotPython
from coverage.files import GlobMatcher, prep_patterns
from coverage.misc import ensure_dir_for_file, file_be_gone
from coverage.plugin import FileReporter
from coverage.results import Analysis
from coverage.types import TMorf
if TYPE_CHECKING:
    from coverage import Coverage

class Reporter(Protocol):
    report_type: 'str' = 'What we expect of reporters.'
    
    def report(self = None, morfs = None, outfile = None):
        '''Generate a report of `morfs`, written to `outfile`.'''
        pass



def render_report(output_path = None, reporter = None, morfs = None, msgfn = ('output_path', 'str', 'reporter', 'Reporter', 'morfs', 'Iterable[TMorf] | None', 'msgfn', 'Callable[[str], None]', 'return', 'float')):
    '''Run a one-file report generator, managing the output file.

    This function ensures the output file is ready to be written to. Then writes
    the report to it. Then closes the file and cleans up.

    '''
    file_to_close = None
    delete_file = False
    if output_path == '-':
        outfile = sys.stdout
    else:
        ensure_dir_for_file(output_path)
        outfile = open(output_path, 'w', encoding = 'utf-8')
        file_to_close = outfile
        delete_file = True
# WARNING: Decompyle incomplete


def get_analysis_to_report(coverage = None, morfs = None):
    '''Get the files to report on.

    For each morf in `morfs`, if it should be reported on (based on the omit
    and include configuration options), yield a pair, the `FileReporter` and
    `Analysis` for the morf.

    '''
    pass
# WARNING: Decompyle incomplete
