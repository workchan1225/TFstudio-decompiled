# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: dep_util.pyc (Python 3.11)

'''distutils.dep_util

Utility functions for simple, timestamp-based dependency of files
and groups of files; also, function based entirely on such
timestamp dependency analysis.'''
import os
from distutils.errors import DistutilsFileError

def newer(source, target):
    """Return true if 'source' exists and is more recently modified than
    'target', or if 'source' exists and 'target' doesn't.  Return false if
    both exist and 'target' is the same age or younger than 'source'.
    Raise DistutilsFileError if 'source' does not exist.
    """
    if not os.path.exists(source):
        raise DistutilsFileError("file '%s' does not exist" % os.path.abspath(source))
    if not os.path.exists(target):
        return 1
    ST_MTIME = ST_MTIME
    import stat
    mtime1 = os.stat(source)[ST_MTIME]
    mtime2 = os.stat(target)[ST_MTIME]
    return mtime1 > mtime2


def newer_pairwise(sources, targets):
    """Walk two filename lists in parallel, testing if each source is newer
    than its corresponding target.  Return a pair of lists (sources,
    targets) where source is newer than target, according to the semantics
    of 'newer()'.
    """
    if len(sources) != len(targets):
        raise ValueError("'sources' and 'targets' must be same length")
    n_sources = []
    n_targets = []
    for i in range(len(sources)):
        if newer(sources[i], targets[i]):
            n_sources.append(sources[i])
            n_targets.append(targets[i])
        return (n_sources, n_targets)


def newer_group(sources, target, missing = ('error',)):
