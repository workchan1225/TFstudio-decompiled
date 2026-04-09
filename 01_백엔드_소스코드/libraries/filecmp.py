# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: filecmp.pyc (Python 3.11)

'''Utilities for comparing files and directories.

Classes:
    dircmp

Functions:
    cmp(f1, f2, shallow=True) -> int
    cmpfiles(a, b, common) -> ([], [], [])
    clear_cache()

'''
import os
import stat
from itertools import filterfalse
from types import GenericAlias
__all__ = [
    'clear_cache',
    'cmp',
    'dircmp',
    'cmpfiles',
    'DEFAULT_IGNORES']
_cache = { }
BUFSIZE = 8192
DEFAULT_IGNORES = [
    'RCS',
    'CVS',
    'tags',
    '.git',
    '.hg',
    '.bzr',
    '_darcs',
    '__pycache__']

def clear_cache():
    '''Clear the filecmp cache.'''
    _cache.clear()


def cmp(f1, f2, shallow = (True,)):
    '''Compare two files.

    Arguments:

    f1 -- First file name

    f2 -- Second file name

    shallow -- treat files as identical if their stat signatures (type, size,
               mtime) are identical. Otherwise, files are considered different
               if their sizes or contents differ.  [default: True]

    Return value:

    True if the files are the same, False otherwise.

    This function uses a cache for past comparisons and the results,
    with cache entries invalidated if their stat information
    changes.  The cache may be cleared by calling clear_cache().

    '''
    s1 = _sig(os.stat(f1))
    s2 = _sig(os.stat(f2))
    if s1[0] != stat.S_IFREG or s2[0] != stat.S_IFREG:
        return False
    if None and s1 == s2:
        return True
    if None[1] != s2[1]:
        return False
    outcome = None.get((f1, f2, s1, s2))
# WARNING: Decompyle incomplete


def _sig(st):
    return (stat.S_IFMT(st.st_mode), st.st_size, st.st_mtime)


def _do_cmp(f1, f2):
    bufsize = BUFSIZE
    fp1 = open(f1, 'rb')
    fp2 = open(f2, 'rb')
    b1 = fp1.read(bufsize)
    b2 = fp2.read(bufsize)
    if b1 != b2:
        None(None, None)
        None(None, None)
        return False
    if not None:
        None(None, None)
        None(None, None)
        return True
    with None:
        if not None:
            pass
    None(None, None)
    return None
    with None:
        if not None:
            pass


class dircmp:
    '''A class that manages the comparison of 2 directories.

    dircmp(a, b, ignore=None, hide=None)
      A and B are directories.
      IGNORE is a list of names to ignore,
        defaults to DEFAULT_IGNORES.
      HIDE is a list of names to hide,
        defaults to [os.curdir, os.pardir].

    High level usage:
      x = dircmp(dir1, dir2)
      x.report() -> prints a report on the differences between dir1 and dir2
       or
      x.report_partial_closure() -> prints report on differences between dir1
            and dir2, and reports on common immediate subdirectories.
      x.report_full_closure() -> like report_partial_closure,
            but fully recursive.

    Attributes:
     left_list, right_list: The files in dir1 and dir2,
        filtered by hide and ignore.
     common: a list of names in both dir1 and dir2.
     left_only, right_only: names only in dir1, dir2.
     common_dirs: subdirectories in both dir1 and dir2.
     common_files: files in both dir1 and dir2.
     common_funny: names in both dir1 and dir2 where the type differs between
        dir1 and dir2, or the name is not stat-able.
     same_files: list of identical files.
     diff_files: list of filenames which differ.
     funny_files: list of files which could not be compared.
     subdirs: a dictionary of dircmp instances (or MyDirCmp instances if this
       object is of type MyDirCmp, a subclass of dircmp), keyed by names
       in common_dirs.
     '''
    
    def __init__(self, a, b, ignore, hide = (None, None)):
        self.left = a
        self.right = b
    # WARNING: Decompyle incomplete

    
    def phase0(self):
        self.left_list = _filter(os.listdir(self.left), self.hide + self.ignore)
        self.right_list = _filter(os.listdir(self.right), self.hide + self.ignore)
        self.left_list.sort()
        self.right_list.sort()

    
    def phase1(self):
        a = dict(zip(map(os.path.normcase, self.left_list), self.left_list))
        b = dict(zip(map(os.path.normcase, self.right_list), self.right_list))
        self.common = list(map(a.__getitem__, filter(b.__contains__, a)))
        self.left_only = list(map(a.__getitem__, filterfalse(b.__contains__, a)))
        self.right_only = list(map(b.__getitem__, filterfalse(a.__contains__, b)))

    
    def phase2(self):
        self.common_dirs = []
        self.common_files = []
        self.common_funny = []
        for x in self.common:
            a_path = os.path.join(self.left, x)
            b_path = os.path.join(self.right, x)
            ok = 1
            a_stat = os.stat(a_path)
        except OSError:
            ok = 0
        b_stat = os.stat(b_path)

    
    def phase3(self):
        xx = cmpfiles(self.left, self.right, self.common_files)
        (self.same_files, self.diff_files, self.funny_files) = xx

    
    def phase4(self):
        self.subdirs = { }
        for x in self.common_dirs:
            a_x = os.path.join(self.left, x)
            b_x = os.path.join(self.right, x)
            self.subdirs[x] = self.__class__(a_x, b_x, self.ignore, self.hide)
            return None

    
    def phase4_closure(self):
        self.phase4()
        for sd in self.subdirs.values():
            sd.phase4_closure()
            return None

    
    def report(self):
        print('diff', self.left, self.right)
        if self.left_only:
            self.left_only.sort()
            print('Only in', self.left, ':', self.left_only)
        if self.right_only:
            self.right_only.sort()
            print('Only in', self.right, ':', self.right_only)
        if self.same_files:
            self.same_files.sort()
            print('Identical files :', self.same_files)
        if self.diff_files:
            self.diff_files.sort()
            print('Differing files :', self.diff_files)
        if self.funny_files:
            self.funny_files.sort()
            print('Trouble with common files :', self.funny_files)
        if self.common_dirs:
            self.common_dirs.sort()
            print('Common subdirectories :', self.common_dirs)
        if self.common_funny:
            self.common_funny.sort()
            print('Common funny cases :', self.common_funny)
            return None

    
    def report_partial_closure(self):
        self.report()
        for sd in self.subdirs.values():
            print()
            sd.report()
            return None

    
    def report_full_closure(self):
        self.report()
        for sd in self.subdirs.values():
            print()
            sd.report_full_closure()
            return None

    methodmap = dict(subdirs = phase4, same_files = phase3, diff_files = phase3, funny_files = phase3, common_dirs = phase2, common_files = phase2, common_funny = phase2, common = phase1, left_only = phase1, right_only = phase1, left_list = phase0, right_list = phase0)
    
    def __getattr__(self, attr):
        if attr not in self.methodmap:
            raise AttributeError(attr)
        self.methodmap[attr](self)
        return getattr(self, attr)

    __class_getitem__ = classmethod(GenericAlias)


def cmpfiles(a, b, common, shallow = (True,)):
    """Compare common files in two directories.

    a, b -- directory names
    common -- list of file names found in both directories
    shallow -- if true, do comparison based solely on stat() information

    Returns a tuple of three lists:
      files that compare equal
      files that are different
      filenames that aren't regular files.

    """
    res = ([], [], [])
    for x in common:
        ax = os.path.join(a, x)
        bx = os.path.join(b, x)
        res[_cmp(ax, bx, shallow)].append(x)
        return res


def _cmp(a, b, sh, abs, cmp = (abs, cmp)):
    
    try:
        return not abs(cmp(a, b, sh))
    except OSError:
        return 2



def _filter(flist, skip):
    return list(filterfalse(skip.__contains__, flist))


def demo():
    import sys
    import getopt
    (options, args) = getopt.getopt(sys.argv[1:], 'r')
    if len(args) != 2:
        raise getopt.GetoptError('need exactly two args', None)
    dd = dircmp(args[0], args[1])
    if ('-r', '') in options:
        dd.report_full_closure()
        return None
    None.report()

if __name__ == '__main__':
    demo()
    return None
