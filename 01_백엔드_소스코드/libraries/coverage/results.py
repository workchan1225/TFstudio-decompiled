# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: results.pyc (Python 3.11)

'''Results of coverage measurement.'''
from __future__ import annotations
import collections
import dataclasses
from collections.abc import Iterable
from typing import TYPE_CHECKING
from coverage.exceptions import ConfigError
from coverage.misc import nice_pair
from coverage.types import TArc, TLineNo
if TYPE_CHECKING:
    from coverage.data import CoverageData
    from coverage.plugin import FileReporter

def analysis_from_file_reporter(data = None, precision = None, file_reporter = None, filename = ('data', 'CoverageData', 'precision', 'int', 'file_reporter', 'FileReporter', 'filename', 'str', 'return', 'Analysis')):
    '''Create an Analysis from a FileReporter.'''
    has_arcs = data.has_arcs()
    statements = file_reporter.lines()
    excluded = file_reporter.excluded_lines()
    if not data.lines(filename):
        executed = file_reporter.translate_lines([])
        if has_arcs:
            arc_possibilities_set = file_reporter.arcs()
            if not data.arcs(filename):
                arcs = []
                arcs = file_reporter.translate_arcs(arcs)
                dests = collections.defaultdict(set)
                for fromno, tono in arc_possibilities_set:
                    dests[fromno].add(tono)
                    single_dests = dests.items()()
                    new_arcs = set()
                    for fromno, tono in arcs:
                        if fromno != tono:
                            new_arcs.add((fromno, tono))
                            continue
                        if fromno in single_dests:
                            new_arcs.add((fromno, single_dests[fromno]))
                        arcs_executed_set = file_reporter.translate_arcs(new_arcs)
                        exit_counts = file_reporter.exit_counts()
                        no_branch = file_reporter.no_branch_lines()
                    arc_possibilities_set = set()
                    arcs_executed_set = set()
                    exit_counts = { }
                    no_branch = set()
                    return Analysis(precision = precision, filename = filename, has_arcs = has_arcs, statements = statements, excluded = excluded, executed = executed, arc_possibilities_set = arc_possibilities_set, arcs_executed_set = arcs_executed_set, exit_counts = exit_counts, no_branch = no_branch)

Analysis = <NODE:12>()
TRegionLines = frozenset[TLineNo]

class AnalysisNarrower:
    '''
    For reducing an `Analysis` to a subset of its lines.

    Originally this was a simpler method on Analysis, but that led to quadratic
    behavior.  This class does the bulk of the work up-front to provide the
    same results in linear time.

    Create an AnalysisNarrower from an Analysis, bulk-add region lines to it
    with `add_regions`, then individually request new narrowed Analysis objects
    for each region with `narrow`.  Doing most of the work in limited calls to
    `add_regions` lets us avoid poor performance.
    '''
    
    def __init__(self = None, analysis = None):
        self.analysis = analysis
        self.region2arc_possibilities = collections.defaultdict(set)
        self.region2arc_executed = collections.defaultdict(set)
        self.region2exit_counts = collections.defaultdict(dict)

    
    def add_regions(self = None, liness = None):
        '''
        Pre-process a number of sets of line numbers.  Later calls to `narrow`
        with one of these sets will provide a narrowed Analysis.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def narrow(self = None, lines = None):
        '''Create a narrowed Analysis.

        The current analysis is copied to make a new one that only considers
        the lines in `lines`.
        '''
        statements = self.analysis.statements & lines
        excluded = self.analysis.excluded & lines
        executed = self.analysis.executed & lines
        if self.analysis.has_arcs:
            fzlines = frozenset(lines)
            arc_possibilities_set = self.region2arc_possibilities[fzlines]
            arcs_executed_set = self.region2arc_executed[fzlines]
            exit_counts = self.region2exit_counts[fzlines]
            no_branch = self.analysis.no_branch & lines
        else:
            arc_possibilities_set = set()
            arcs_executed_set = set()
            exit_counts = { }
            no_branch = set()
        return Analysis(precision = self.analysis.precision, filename = self.analysis.filename, has_arcs = self.analysis.has_arcs, statements = statements, excluded = excluded, executed = executed, arc_possibilities_set = arc_possibilities_set, arcs_executed_set = arcs_executed_set, exit_counts = exit_counts, no_branch = no_branch)


Numbers = <NODE:12>()

def display_covered(pc = dataclasses.dataclass, precision = None):
