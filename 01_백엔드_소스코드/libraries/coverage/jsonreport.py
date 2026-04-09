# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: jsonreport.pyc (Python 3.11)

'''Json reporting for coverage.py'''
from __future__ import annotations
import datetime
import json
import sys
from collections.abc import Iterable
from typing import IO, TYPE_CHECKING, Any
from coverage import __version__
from coverage.report_core import get_analysis_to_report
from coverage.results import Analysis, AnalysisNarrower, Numbers
from coverage.types import TLineNo, TMorf
if TYPE_CHECKING:
    from coverage import Coverage
    from coverage.data import CoverageData
    from coverage.plugin import FileReporter
JsonObj = dict[(str, Any)]
FORMAT_VERSION = 3

class JsonReporter:
    '''A reporter for writing JSON coverage results.'''
    report_type = 'JSON report'
    
    def __init__(self = None, coverage = None):
        self.coverage = coverage
        self.config = self.coverage.config
        self.total = Numbers(self.config.precision)
        self.report_data = { }

    
    def make_summary(self = None, nums = None):
        '''Create a dict summarizing `nums`.'''
        return {
            'covered_lines': nums.n_executed,
            'num_statements': nums.n_statements,
            'percent_covered': nums.pc_covered,
            'percent_covered_display': nums.pc_covered_str,
            'missing_lines': nums.n_missing,
            'excluded_lines': nums.n_excluded,
            'percent_statements_covered': nums.pc_statements,
            'percent_statements_covered_display': nums.pc_statements_str }

    
    def make_branch_summary(self = None, nums = None):
        '''Create a dict summarizing the branch info in `nums`.'''
        return {
            'num_branches': nums.n_branches,
            'num_partial_branches': nums.n_partial_branches,
            'covered_branches': nums.n_executed_branches,
            'missing_branches': nums.n_missing_branches,
            'percent_branches_covered': nums.pc_branches,
            'percent_branches_covered_display': nums.pc_branches_str }

    
    def report(self = None, morfs = None, outfile = None):
