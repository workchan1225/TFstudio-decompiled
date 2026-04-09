# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: xmlreport.pyc (Python 3.11)

'''XML reporting for coverage.py'''
from __future__ import annotations
import os
import os.path as os
import sys
import time
import xml.dom.minidom as xml
from collections.abc import Iterable
from dataclasses import dataclass
from typing import IO, TYPE_CHECKING, Any
from coverage import __version__, files
from coverage.misc import human_sorted, human_sorted_items, isolate_module
from coverage.plugin import FileReporter
from coverage.report_core import get_analysis_to_report
from coverage.results import Analysis
from coverage.types import TMorf
from coverage.version import __url__
if TYPE_CHECKING:
    from coverage import Coverage
os = isolate_module(os)
DTD_URL = 'https://raw.githubusercontent.com/cobertura/web/master/htdocs/xml/coverage-04.dtd'

def rate(hit = None, num = None):
    '''Return the fraction of `hit`/`num`, as a string.'''
    if num == 0:
        return '1'
    return f'''{None / num:.4g}'''

PackageData = <NODE:12>()

def appendChild(parent = None, child = None):
    '''Append a child to a parent, in a way mypy will shut up about.'''
    parent.appendChild(child)


class XmlReporter:
    '''A reporter for writing Cobertura-style XML coverage results.'''
    report_type = 'XML report'
    
    def __init__(self = None, coverage = None):
        self.coverage = coverage
        self.config = self.coverage.config
        self.source_paths = set()
        if self.config.source:
            for src in self.config.source:
                if os.path.exists(src):
                    if self.config.relative_files:
                        src = src.rstrip('\\/')
                    else:
                        src = files.canonical_filename(src)
                    self.source_paths.add(src)
                self.packages = { }
                self
                return None

    
    def report(self = None, morfs = None, outfile = None):
        '''Generate a Cobertura-compatible XML report for `morfs`.

        `morfs` is a list of modules or file names.

        `outfile` is a file object to write the XML to.

        '''
        if not outfile:
            pass
        outfile = sys.stdout
        has_arcs = self.coverage.get_data().has_arcs()
        impl = xml.dom.minidom.getDOMImplementation()
    # WARNING: Decompyle incomplete

    
    def xml_file(self = None, fr = None, analysis = None, has_arcs = ('fr', 'FileReporter', 'analysis', 'Analysis', 'has_arcs', 'bool', 'return', 'None')):
        '''Add to the XML report for a single file.'''
        if self.config.skip_empty and analysis.numbers.n_statements == 0:
            return None
        filename = None.filename.replace('\\', '/')
        for source_path in self.source_paths:
            if not self.config.relative_files:
                source_path = files.canonical_filename(source_path)
            if filename.startswith(source_path.replace('\\', '/') + '/'):
                rel_name = filename[len(source_path) + 1:]
            
            rel_name = fr.relative_filename().replace('\\', '/')
            self.source_paths.add(fr.filename[:-len(rel_name)].rstrip('\\/'))
            if not os.path.dirname(rel_name):
                dirname = '.'
                dirname = '/'.join(dirname.split('/')[:self.config.xml_package_depth])
                package_name = dirname.replace('/', '.')
                package = self.packages.setdefault(package_name, PackageData({ }, 0, 0, 0, 0))
                xclass = self.xml_out.createElement('class')
                appendChild(xclass, self.xml_out.createElement('methods'))
                xlines = self.xml_out.createElement('lines')
                appendChild(xclass, xlines)
                xclass.setAttribute('name', os.path.relpath(rel_name, dirname))
                xclass.setAttribute('filename', rel_name.replace('\\', '/'))
                xclass.setAttribute('complexity', '0')
                branch_stats = analysis.branch_stats()
                missing_branch_arcs = analysis.missing_branch_arcs()
                for line in sorted(analysis.statements):
                    xline = self.xml_out.createElement('line')
                    xline.setAttribute('number', str(line))
                    xline.setAttribute('hits', str(int(line not in analysis.missing)))
                    if has_arcs:
                        if line in branch_stats:
                            (total, taken) = branch_stats[line]
                            xline.setAttribute('branch', 'true')
                            xline.setAttribute('condition-coverage', f'''{100 * taken // total}% ({taken}/{total})''')
                        if line in missing_branch_arcs:
                            annlines = missing_branch_arcs[line]()
                            xline.setAttribute('missing-branches', ','.join(annlines))
                    appendChild(xlines, xline)
                    class_lines = len(analysis.statements)
                    class_hits = class_lines - len(analysis.missing)
        xclass.setAttribute('line-rate', rate(class_hits, class_lines))
        xclass.setAttribute('branch-rate', branch_rate)
        package.elements[rel_name] = xclass



def serialize_xml(dom = None):
    '''Serialize a minidom node to XML.'''
    return dom.toprettyxml()
