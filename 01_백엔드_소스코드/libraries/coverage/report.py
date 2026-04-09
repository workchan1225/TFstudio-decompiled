# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: report.pyc (Python 3.11)

'''Summary reporting'''
from __future__ import annotations
import sys
from collections.abc import Iterable
from typing import IO, TYPE_CHECKING, Any
from coverage.exceptions import ConfigError, NoDataError
from coverage.misc import human_sorted_items, plural
from coverage.plugin import FileReporter
from coverage.report_core import get_analysis_to_report
from coverage.results import Analysis, Numbers
from coverage.types import TMorf
if TYPE_CHECKING:
    from coverage import Coverage

class SummaryReporter:
    '''A reporter for writing the summary report.'''
    
    def __init__(self = None, coverage = None):
