# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: html.pyc (Python 3.11)

'''HTML reporting for coverage.py.'''
from __future__ import annotations
import collections
import dataclasses
import datetime
import functools
import json
import os
import re
import string
from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import TYPE_CHECKING, Any
import coverage
from coverage.data import CoverageData, add_data_to_hash
from coverage.exceptions import NoDataError
from coverage.files import flat_rootname
from coverage.misc import Hasher, ensure_dir, file_be_gone, format_local_datetime, human_sorted, isolate_module, plural, stdout_link
from coverage.report_core import get_analysis_to_report
from coverage.results import Analysis, AnalysisNarrower, Numbers
from coverage.templite import Templite
from coverage.types import TLineNo, TMorf
from coverage.version import __url__
if TYPE_CHECKING:
    from coverage import Coverage
    from coverage.plugins import FileReporter
os = isolate_module(os)

def data_filename(fname = None):
    '''Return the path to an "htmlfiles" data file of ours.'''
    static_dir = os.path.join(os.path.dirname(__file__), 'htmlfiles')
    static_filename = os.path.join(static_dir, fname)
    return static_filename


def read_data(fname = None):
    '''Return the contents of a data file of ours.'''
    data_file = open(data_filename(fname), encoding = 'utf-8')
    None(None, None)
    return 
    with None:
        if not None, data_file.read():
            pass


def write_html(fname = None, html = None):
    '''Write `html` to `fname`, properly encoded.'''
    html = re.sub('(\\A\\s+)|(\\s+$)', '', html, flags = re.MULTILINE) + '\n'
    fout = open(fname, 'wb')
    fout.write(html.encode('ascii', 'xmlcharrefreplace'))
    None(None, None)
    return None
    with None:
        if not None:
            pass

LineData = <NODE:12>()
FileData = <NODE:12>()
IndexItem = <NODE:12>()
IndexPage = <NODE:12>()

class HtmlDataGeneration:
    '''Generate structured data to be turned into HTML reports.'''
    EMPTY = '(empty)'
    
    def __init__(self = None, cov = None):
        self.coverage = cov
        self.config = self.coverage.config
        self.data = self.coverage.get_data()
        self.has_arcs = self.data.has_arcs()
        if self.config.show_contexts and self.data.measured_contexts() == {
            ''}:
            self.coverage._warn('No contexts were measured')
        self.data.set_query_contexts(self.config.report_contexts)

    
    def data_for_file(self = None, fr = None, analysis = None):
        """Produce the data needed for one file's report."""
        pass
    # WARNING: Decompyle incomplete



class FileToReport:
    """A file we're considering reporting."""
    
    def __init__(self = None, fr = None, analysis = None):
        self.fr = fr
        self.analysis = analysis
        self.rootname = flat_rootname(fr.relative_filename())
        self.html_filename = self.rootname + '.html'
        self.prev_html = ''
        self.next_html = ''


HTML_SAFE = string.ascii_letters + string.digits + "!#$%'()*+,-./:;=?@[]^_`{|}~"
encode_int = (lambda n = None: if n == 0:
HTML_SAFE[0]r = None# WARNING: Decompyle incomplete
)()

def copy_with_cache_bust(src = dataclass, dest_dir = dataclass):
