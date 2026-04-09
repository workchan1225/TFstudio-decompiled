# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: archive_util.pyc (Python 3.11)

'''distutils.archive_util

Utility functions for creating archive files (tarballs, zip files,
that sort of thing).'''
import os
from warnings import warn
import sys

try:
    import zipfile
except ImportError:
    zipfile = None

from distutils.errors import DistutilsExecError
from distutils.spawn import spawn
from distutils.dir_util import mkpath
from distutils import log

try:
    from pwd import getpwnam
except ImportError:
    getpwnam = None


try:
    from grp import getgrnam
except ImportError:
    getgrnam = None


def _get_gid(name):
    '''Returns a gid, given a group name.'''
    pass
# WARNING: Decompyle incomplete


def _get_uid(name):
    '''Returns an uid, given a user name.'''
    pass
# WARNING: Decompyle incomplete


def make_tarball(base_name, base_dir, compress, verbose, dry_run, owner, group = ('gzip', 0, 0, None, None)):
    '''Create a (possibly compressed) tar file from all the files under
    \'base_dir\'.

    \'compress\' must be "gzip" (the default), "bzip2", "xz", "compress", or
    None.  ("compress" will be deprecated in Python 3.2)

    \'owner\' and \'group\' can be used to define an owner and a group for the
    archive that is being built. If not provided, the current owner and group
    will be used.

    The output tar file will be named \'base_dir\' +  ".tar", possibly plus
    the appropriate compression extension (".gz", ".bz2", ".xz" or ".Z").

    Returns the output filename.
    '''
    pass
# WARNING: Decompyle incomplete


def make_zipfile(base_name, base_dir, verbose, dry_run = (0, 0)):
    '''Create a zip file from all the files under \'base_dir\'.

    The output zip file will be named \'base_name\' + ".zip".  Uses either the
    "zipfile" Python module (if available) or the InfoZIP "zip" utility
    (if installed and found on the default search path).  If neither tool is
    available, raises DistutilsExecError.  Returns the name of the output zip
    file.
    '''
    zip_filename = base_name + '.zip'
    mkpath(os.path.dirname(zip_filename), dry_run = dry_run)
# WARNING: Decompyle incomplete

ARCHIVE_FORMATS = {
    'gztar': (make_tarball, [
        ('compress', 'gzip')], "gzip'ed tar-file"),
    'bztar': (make_tarball, [
        ('compress', 'bzip2')], "bzip2'ed tar-file"),
    'xztar': (make_tarball, [
        ('compress', 'xz')], "xz'ed tar-file"),
    'ztar': (make_tarball, [
        ('compress', 'compress')], 'compressed tar file'),
    'tar': (make_tarball, [
        ('compress', None)], 'uncompressed tar file'),
    'zip': (make_zipfile, [], 'ZIP file') }

def check_archive_formats(formats):
    """Returns the first format from the 'format' list that is unknown.

    If all formats are known, returns None
    """
    for format in formats:
        if format not in ARCHIVE_FORMATS:
            
            return None, format
        return None


def make_archive(base_name, format, root_dir, base_dir, verbose, dry_run, owner, group = (None, None, 0, 0, None, None)):
    '''Create an archive file (eg. zip or tar).

    \'base_name\' is the name of the file to create, minus any format-specific
    extension; \'format\' is the archive format: one of "zip", "tar", "gztar",
    "bztar", "xztar", or "ztar".

    \'root_dir\' is a directory that will be the root directory of the
    archive; ie. we typically chdir into \'root_dir\' before creating the
    archive.  \'base_dir\' is the directory where we start archiving from;
    ie. \'base_dir\' will be the common prefix of all files and
    directories in the archive.  \'root_dir\' and \'base_dir\' both default
    to the current directory.  Returns the name of the archive file.

    \'owner\' and \'group\' are used when creating a tar archive. By default,
    uses the current owner and group.
    '''
    save_cwd = os.getcwd()
# WARNING: Decompyle incomplete
