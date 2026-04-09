# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: data.pyc (Python 3.11)

'''Coverage data for coverage.py.

This file had the 4.x JSON data support, which is now gone.  This file still
has storage-agnostic helpers, and is kept to avoid changing too many imports.
CoverageData is now defined in sqldata.py, and imported here to keep the
imports working.

'''
from __future__ import annotations
import functools
import glob
import hashlib
import os.path as os
from collections.abc import Iterable
from typing import Callable
from coverage.exceptions import CoverageException, NoDataError
from coverage.files import PathAliases
from coverage.misc import Hasher, file_be_gone, human_sorted, plural
from coverage.sqldata import CoverageData

def line_counts(data = None, fullpath = None):
    '''Return a dict summarizing the line coverage data.

    Keys are based on the file names, and values are the number of executed
    lines.  If `fullpath` is true, then the keys are the full pathnames of
    the files, otherwise they are the basenames of the files.

    Returns a dict mapping file names to counts of lines.

    '''
    summ = { }
    if fullpath:
        
        filename_fn = lambda f: f
    else:
        filename_fn = os.path.basename
# WARNING: Decompyle incomplete


def add_data_to_hash(data = None, filename = None, hasher = None):
    """Contribute `filename`'s data to the `hasher`.

    `hasher` is a `coverage.misc.Hasher` instance to be updated with
    the file's data.  It should only get the results data, not the run
    data.

    """
    if data.has_arcs():
        pass
    hasher.update(data.file_tracer(filename))


def combinable_files(data_file = None, data_paths = None):
    '''Make a list of data files to be combined.

    `data_file` is a path to a data file.  `data_paths` is a list of files or
    directories of files.

    Returns a list of absolute file paths.
    '''
    (data_dir, local) = os.path.split(os.path.abspath(data_file))
    if not data_paths:
        data_paths = [
            data_dir]
        files_to_combine = []
        for p in data_paths:
            if os.path.isfile(p):
                files_to_combine.append(os.path.abspath(p))
                continue
            if os.path.isdir(p):
                pattern = glob.escape(os.path.join(os.path.abspath(p), local)) + '.*'
                files_to_combine.extend(glob.glob(pattern))
                continue
            raise NoDataError(f'''Couldn\'t combine from non-existent path \'{p}\'''')
            files_to_combine = files_to_combine()
            return sorted(files_to_combine)


def combine_parallel_data(data, aliases = None, data_paths = None, strict = None, keep = (None, None, False, False, None), message = ('data', 'CoverageData', 'aliases', 'PathAliases | None', 'data_paths', 'Iterable[str] | None', 'strict', 'bool', 'keep', 'bool', 'message', 'Callable[[str], None] | None', 'return', 'None')):
    """Combine a number of data files together.

    `data` is a CoverageData.

    Treat `data.filename` as a file prefix, and combine the data from all
    of the data files starting with that prefix plus a dot.

    If `aliases` is provided, it's a `PathAliases` object that is used to
    re-map paths to match the local machine's.

    If `data_paths` is provided, it is a list of directories or files to
    combine.  Directories are searched for files that start with
    `data.filename` plus dot as a prefix, and those files are combined.

    If `data_paths` is not provided, then the directory portion of
    `data.filename` is used as the directory to search for data files.

    Unless `keep` is True every data file found and combined is then deleted
    from disk. If a file cannot be read, a warning will be issued, and the
    file will not be deleted.

    If `strict` is true, and no files are found to combine, an error is
    raised.

    `message` is a function to use for printing messages to the user.

    """
    files_to_combine = combinable_files(data.base_filename(), data_paths)
    if not strict and files_to_combine:
        raise NoDataError('No data to combine')
# WARNING: Decompyle incomplete


def debug_data_file(filename = None):
    """Implementation of 'coverage debug data'."""
    data = CoverageData(filename)
    filename = data.data_filename()
    print(f'''path: {filename}''')
    if not os.path.exists(filename):
        print("No data collected: file doesn't exist")
        return None
    None.read()
    print(f'''has_arcs: {data.has_arcs()!r}''')
    summary = line_counts(data, fullpath = True)
    filenames = human_sorted(summary.keys())
    nfiles = len(filenames)
    print(f'''{nfiles} file{plural(nfiles)}:''')
    for f in filenames:
        line = f'''{f}: {summary[f]} line{plural(summary[f])}'''
        plugin = data.file_tracer(f)
        if plugin:
            line += f''' [{plugin}]'''
        print(line)
        return None


def sorted_lines(data = None, filename = None):
