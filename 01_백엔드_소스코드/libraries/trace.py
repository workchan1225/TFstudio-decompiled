# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: trace.pyc (Python 3.11)

'''program/module to trace Python program or function execution

Sample use, command line:
  trace.py -c -f counts --ignore-dir \'$prefix\' spam.py eggs
  trace.py -t --ignore-dir \'$prefix\' spam.py eggs
  trace.py --trackcalls spam.py eggs

Sample use, programmatically
  import sys

  # create a Trace object, telling it what to ignore, and whether to
  # do tracing or line-counting or both.
  tracer = trace.Trace(ignoredirs=[sys.base_prefix, sys.base_exec_prefix,],
                       trace=0, count=1)
  # run the new command using the given tracer
  tracer.run(\'main()\')
  # make a report, placing output in /tmp
  r = tracer.results()
  r.write_results(show_missing=True, coverdir="/tmp")
'''
__all__ = [
    'Trace',
    'CoverageResults']
import io
import linecache
import os
import sys
import sysconfig
import token
import tokenize
import inspect
import gc
import dis
import pickle
from time import monotonic as _time
import threading
PRAGMA_NOCOVER = '#pragma NO COVER'

class _Ignore:
    
    def __init__(self, modules, dirs = (None, None)):
        self._mods = set() if not modules else set(modules)
        self._dirs = (lambda .0: [ os.path.normpath(d) for d in .0 ]) if not dirs else dirs()
        self._ignore = {
            '<string>': 1 }

    
    def names(self, filename, modulename):
        if modulename in self._ignore:
            return self._ignore[modulename]
        if None in self._mods:
            self._ignore[modulename] = 1
            return 1
    # WARNING: Decompyle incomplete



def _modname(path):
    '''Return a plausible module name for the path.'''
    base = os.path.basename(path)
    (filename, ext) = os.path.splitext(base)
    return filename


def _fullmodname(path):
    '''Return a plausible module name for the path.'''
    comparepath = os.path.normcase(path)
    longest = ''
    for dir in sys.path:
        dir = os.path.normcase(dir)
        if comparepath.startswith(dir) and comparepath[len(dir)] == os.sep and len(dir) > len(longest):
            longest = dir
        if longest:
            base = path[len(longest) + 1:]
        else:
            base = path
    (drive, base) = os.path.splitdrive(base)
    base = base.replace(os.sep, '.')
    if os.altsep:
        base = base.replace(os.altsep, '.')
    (filename, ext) = os.path.splitext(base)
    return filename.lstrip('.')


class CoverageResults:
    
    def __init__(self, counts, calledfuncs, infile, callers, outfile = (None, None, None, None, None)):
        self.counts = counts
    # WARNING: Decompyle incomplete

    
    def is_ignored_filename(self, filename):
