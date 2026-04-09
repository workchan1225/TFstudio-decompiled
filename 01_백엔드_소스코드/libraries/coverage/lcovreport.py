# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: lcovreport.pyc (Python 3.11)

'''LCOV reporting for coverage.py.'''
from __future__ import annotations
import base64
import hashlib
import sys
from collections.abc import Iterable
from typing import IO, TYPE_CHECKING
from coverage.plugin import FileReporter
from coverage.report_core import get_analysis_to_report
from coverage.results import Analysis, AnalysisNarrower, Numbers
from coverage.types import TMorf
if TYPE_CHECKING:
    from coverage import Coverage

def line_hash(line = None):
    '''Produce a hash of a source line for use in the LCOV file.'''
    hashed = hashlib.md5(line.encode('utf-8'), usedforsecurity = False).digest()
    return base64.b64encode(hashed).decode('ascii').rstrip('=')


def lcov_lines(analysis = None, lines = None, source_lines = None, outfile = ('analysis', 'Analysis', 'lines', 'list[int]', 'source_lines', 'list[str]', 'outfile', 'IO[str]', 'return', 'None')):
    '''Emit line coverage records for an analyzed file.'''
    hash_suffix = ''
    for line in lines:
        if source_lines:
            hash_suffix = ',' + line_hash(source_lines[line - 1])
        hit = int(line not in analysis.missing)
        outfile.write(f'''DA:{line},{hit}{hash_suffix}\n''')
        if analysis.numbers.n_statements > 0:
            outfile.write(f'''LF:{analysis.numbers.n_statements}\n''')
            outfile.write(f'''LH:{analysis.numbers.n_executed}\n''')
            return None
        return None


def lcov_functions(fr = None, file_analysis = None, outfile = None):
    '''Emit function coverage records for an analyzed file.'''
    functions = fr.code_regions()()
    if not functions:
        return None
    narrower = (lambda .0: pass# WARNING: Decompyle incomplete
)(file_analysis)
    (lambda .0: pass# WARNING: Decompyle incomplete
)(functions())
    functions.sort()
    functions_hit = 0
    for first_line, last_line, region in functions:
        analysis = narrower.narrow(region.lines)
        hit = int(analysis.numbers.n_executed > 0)
        functions_hit += hit
        outfile.write(f'''FN:{first_line},{last_line},{region.name}\n''')
        outfile.write(f'''FNDA:{hit},{region.name}\n''')
        outfile.write(f'''FNF:{len(functions)}\n''')
        outfile.write(f'''FNH:{functions_hit}\n''')
        return None


def lcov_arcs(fr = None, analysis = None, lines = None, outfile = ('fr', 'FileReporter', 'analysis', 'Analysis', 'lines', 'list[int]', 'outfile', 'IO[str]', 'return', 'None')):
    '''Emit branch coverage records for an analyzed file.'''
    branch_stats = analysis.branch_stats()
    executed_arcs = analysis.executed_branch_arcs()
    missing_arcs = analysis.missing_branch_arcs()
# WARNING: Decompyle incomplete


class LcovReporter:
    '''A reporter for writing LCOV coverage reports.'''
    report_type = 'LCOV report'
    
    def __init__(self = None, coverage = None):
        self.coverage = coverage
        self.config = coverage.config
        self.total = Numbers(self.coverage.config.precision)

    
    def report(self = None, morfs = None, outfile = None):
