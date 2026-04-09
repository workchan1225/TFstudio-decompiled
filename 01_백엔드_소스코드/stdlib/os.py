# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: os.pyc (Python 3.11)

"""OS routines for NT or Posix depending on what system we're on.

This exports:
  - all functions from posix or nt, e.g. unlink, stat, etc.
  - os.path is either posixpath or ntpath
  - os.name is either 'posix' or 'nt'
  - os.curdir is a string representing the current directory (always '.')
  - os.pardir is a string representing the parent directory (always '..')
  - os.sep is the (or a most common) pathname separator ('/' or '\\\\')
  - os.extsep is the extension separator (always '.')
  - os.altsep is the alternate pathname separator (None or '/')
  - os.pathsep is the component separator used in $PATH etc
  - os.linesep is the line separator in text files ('\\r' or '\\n' or '\\r\\n')
  - os.defpath is the default search path for executables
  - os.devnull is the file path of the null device ('/dev/null', etc.)

Programs that import and use 'os' stand a better chance of being
portable between different platforms.  Of course, they must then
only use functions that are defined by all platforms (e.g., unlink
and opendir), and leave all pathname manipulation to os.path
(e.g., split and join).
"""
import abc
import sys
import stat as st
from _collections_abc import _check_methods
GenericAlias = type(list[int])
_names = sys.builtin_module_names
__all__ = [
    'altsep',
    'curdir',
    'pardir',
    'sep',
    'pathsep',
    'linesep',
    'defpath',
    'name',
    'path',
    'devnull',
    'SEEK_SET',
    'SEEK_CUR',
    'SEEK_END',
    'fsencode',
    'fsdecode',
    'get_exec_path',
    'fdopen',
    'extsep']

def _exists(name):
    return name in globals()


def _get_exports_list(module):
    
    try:
        return list(module.__all__)
    except AttributeError:
        return 


if 'posix' in _names:
    name = 'posix'
    linesep = '\n'
    from posix import *
    
    try:
        from posix import _exit
        __all__.append('_exit')
    except ImportError:
        pass

    import posixpath as path
    
    try:
        from posix import _have_functions
    except ImportError:
        pass

    import posix
    __all__.extend(_get_exports_list(posix))
    del posix
elif 'nt' in _names:
    name = 'nt'
    linesep = '\r\n'
    from nt import *
    
    try:
        from nt import _exit
        __all__.append('_exit')
    except ImportError:
        pass

    import ntpath as path
    import nt
    __all__.extend(_get_exports_list(nt))
    del nt
    
    try:
        from nt import _have_functions
    except ImportError:
        pass
    except:
        raise ImportError('no os specific module found')

    sys.modules['os.path'] = path
    from os.path import curdir, pardir, sep, pathsep, defpath, extsep, altsep, devnull
    del _names
    if _exists('_have_functions'):
        _globals = globals()
        
        def _add(str, fn):
            if fn in _globals or str in _have_functions:
                _set.add(_globals[fn])
                return None
            return None

        _set = set()
        _add('HAVE_FACCESSAT', 'access')
        _add('HAVE_FCHMODAT', 'chmod')
        _add('HAVE_FCHOWNAT', 'chown')
        _add('HAVE_FSTATAT', 'stat')
        _add('HAVE_FUTIMESAT', 'utime')
        _add('HAVE_LINKAT', 'link')
        _add('HAVE_MKDIRAT', 'mkdir')
        _add('HAVE_MKFIFOAT', 'mkfifo')
        _add('HAVE_MKNODAT', 'mknod')
        _add('HAVE_OPENAT', 'open')
        _add('HAVE_READLINKAT', 'readlink')
        _add('HAVE_RENAMEAT', 'rename')
        _add('HAVE_SYMLINKAT', 'symlink')
        _add('HAVE_UNLINKAT', 'unlink')
        _add('HAVE_UNLINKAT', 'rmdir')
        _add('HAVE_UTIMENSAT', 'utime')
        supports_dir_fd = _set
        _set = set()
        _add('HAVE_FACCESSAT', 'access')
        supports_effective_ids = _set
        _set = set()
        _add('HAVE_FCHDIR', 'chdir')
        _add('HAVE_FCHMOD', 'chmod')
        _add('HAVE_FCHOWN', 'chown')
        _add('HAVE_FDOPENDIR', 'listdir')
        _add('HAVE_FDOPENDIR', 'scandir')
        _add('HAVE_FEXECVE', 'execve')
        _set.add(stat)
        _add('HAVE_FTRUNCATE', 'truncate')
        _add('HAVE_FUTIMENS', 'utime')
        _add('HAVE_FUTIMES', 'utime')
        _add('HAVE_FPATHCONF', 'pathconf')
        if _exists('statvfs') and _exists('fstatvfs'):
            _add('HAVE_FSTATVFS', 'statvfs')
        supports_fd = _set
        _set = set()
        _add('HAVE_FACCESSAT', 'access')
        _add('HAVE_FCHOWNAT', 'chown')
        _add('HAVE_FSTATAT', 'stat')
        _add('HAVE_LCHFLAGS', 'chflags')
        _add('HAVE_LCHMOD', 'chmod')
        if _exists('lchown'):
            _add('HAVE_LCHOWN', 'chown')
        _add('HAVE_LINKAT', 'link')
        _add('HAVE_LUTIMES', 'utime')
        _add('HAVE_LSTAT', 'stat')
        _add('HAVE_FSTATAT', 'stat')
        _add('HAVE_UTIMENSAT', 'utime')
        _add('MS_WINDOWS', 'stat')
        supports_follow_symlinks = _set
        del _set
        del _have_functions
        del _globals
        del _add
SEEK_SET = 0
SEEK_CUR = 1
SEEK_END = 2

def makedirs(name, mode, exist_ok = (511, False)):
    '''makedirs(name [, mode=0o777][, exist_ok=False])

    Super-mkdir; create a leaf directory and all intermediate ones.  Works like
    mkdir, except that any intermediate path segment (not just the rightmost)
    will be created if it does not exist. If the target directory already
    exists, raise an OSError if exist_ok is False. Otherwise no exception is
    raised.  This is recursive.

    '''
    (head, tail) = path.split(name)
    if not tail:
        (head, tail) = path.split(head)
    if not head and tail and path.exists(head):
        
        try:
            makedirs(head, exist_ok = exist_ok)
        except FileExistsError:
            pass

        cdir = curdir
        if isinstance(tail, bytes):
            cdir = bytes(curdir, 'ASCII')
        if tail == cdir:
            return None
        
        try:
            mkdir(name, mode)
            return None
        except OSError:
            if not exist_ok or path.isdir(name):
                raise 
            return None



def removedirs(name):
    '''removedirs(name)

    Super-rmdir; remove a leaf directory and all empty intermediate
    ones.  Works like rmdir except that, if the leaf directory is
    successfully removed, directories corresponding to rightmost path
    segments will be pruned away until either the whole path is
    consumed or an error occurs.  Errors during this latter phase are
    ignored -- they generally mean that a directory was not empty.

    '''
    rmdir(name)
    (head, tail) = path.split(name)
    if not tail:
        (head, tail) = path.split(head)
# WARNING: Decompyle incomplete


def renames(old, new):
    '''renames(old, new)

    Super-rename; create directories as necessary and delete any left
    empty.  Works like rename, except creation of any intermediate
    directories needed to make the new pathname good is attempted
    first.  After the rename, directories corresponding to rightmost
    path segments of the old name will be pruned until either the
    whole path is consumed or a nonempty directory is found.

    Note: this function can fail with the new directory structure made
    if you lack permissions needed to unlink the leaf directory or
    file.

    '''
    (head, tail) = path.split(new)
    if not head and tail and path.exists(head):
        makedirs(head)
    rename(old, new)
    (head, tail) = path.split(old)
    if head or tail:
        
        try:
            removedirs(head)
            return None
        except OSError:
            return None
            return None
            return None


__all__.extend([
    'makedirs',
    'removedirs',
    'renames'])

def walk(top, topdown, onerror, followlinks = (True, None, False)):
    '''Directory tree generator.

    For each directory in the directory tree rooted at top (including top
    itself, but excluding \'.\' and \'..\'), yields a 3-tuple

        dirpath, dirnames, filenames

    dirpath is a string, the path to the directory.  dirnames is a list of
    the names of the subdirectories in dirpath (including symlinks to directories,
    and excluding \'.\' and \'..\').
    filenames is a list of the names of the non-directory files in dirpath.
    Note that the names in the lists are just names, with no path components.
    To get a full path (which begins with top) to a file or directory in
    dirpath, do os.path.join(dirpath, name).

    If optional arg \'topdown\' is true or not specified, the triple for a
    directory is generated before the triples for any of its subdirectories
    (directories are generated top down).  If topdown is false, the triple
    for a directory is generated after the triples for all of its
    subdirectories (directories are generated bottom up).

    When topdown is true, the caller can modify the dirnames list in-place
    (e.g., via del or slice assignment), and walk will only recurse into the
    subdirectories whose names remain in dirnames; this can be used to prune the
    search, or to impose a specific order of visiting.  Modifying dirnames when
    topdown is false has no effect on the behavior of os.walk(), since the
    directories in dirnames have already been generated by the time dirnames
    itself is generated. No matter the value of topdown, the list of
    subdirectories is retrieved before the tuples for the directory and its
    subdirectories are generated.

    By default errors from the os.scandir() call are ignored.  If
    optional arg \'onerror\' is specified, it should be a function; it
    will be called with one argument, an OSError instance.  It can
    report the error to continue with the walk, or raise the exception
    to abort the walk.  Note that the filename is available as the
    filename attribute of the exception object.

    By default, os.walk does not follow symbolic links to subdirectories on
    systems that support them.  In order to get this functionality, set the
    optional argument \'followlinks\' to true.

    Caution:  if you pass a relative pathname for top, don\'t change the
    current working directory between resumptions of walk.  walk never
    changes the current directory, and assumes that the client doesn\'t
    either.

    Example:

    import os
    from os.path import join, getsize
    for root, dirs, files in os.walk(\'python/Lib/email\'):
        print(root, "consumes ")
        print(sum(getsize(join(root, name)) for name in files), end=" ")
        print("bytes in", len(files), "non-directory files")
        if \'CVS\' in dirs:
            dirs.remove(\'CVS\')  # don\'t visit CVS directories

    '''
    sys.audit('os.walk', top, topdown, onerror, followlinks)
    return _walk(fspath(top), topdown, onerror, followlinks)


def _walk(top, topdown, onerror, followlinks):
    pass
# WARNING: Decompyle incomplete

__all__.append('walk')
if {
    open,
    stat} <= supports_dir_fd and {
    scandir,
    stat} <= supports_fd:
    
    def fwalk(top = None, topdown = ('.', True, None), onerror = {
        'follow_symlinks': False,
        'dir_fd': None }, *, follow_symlinks, dir_fd):
        '''Directory tree generator.

        This behaves exactly like walk(), except that it yields a 4-tuple

            dirpath, dirnames, filenames, dirfd

        `dirpath`, `dirnames` and `filenames` are identical to walk() output,
        and `dirfd` is a file descriptor referring to the directory `dirpath`.

        The advantage of fwalk() over walk() is that it\'s safe against symlink
        races (when follow_symlinks is False).

        If dir_fd is not None, it should be a file descriptor open to a directory,
          and top should be relative; top will then be relative to that directory.
          (dir_fd is always supported for fwalk.)

        Caution:
        Since fwalk() yields file descriptors, those are only valid until the
        next iteration step, so you should dup() them if you want to keep them
        for a longer period.

        Example:

        import os
        for root, dirs, files, rootfd in os.fwalk(\'python/Lib/email\'):
            print(root, "consumes", end="")
            print(sum(os.stat(name, dir_fd=rootfd).st_size for name in files),
                  end="")
            print("bytes in", len(files), "non-directory files")
            if \'CVS\' in dirs:
                dirs.remove(\'CVS\')  # don\'t visit CVS directories
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _fwalk(topfd, toppath, isbytes, topdown, onerror, follow_symlinks):
        pass
    # WARNING: Decompyle incomplete

    __all__.append('fwalk')

def execl(file, *args):
    '''execl(file, *args)

    Execute the executable file with argument list args, replacing the
    current process. '''
    execv(file, args)


def execle(file, *args):
    '''execle(file, *args, env)

    Execute the executable file with argument list args and
    environment env, replacing the current process. '''
    env = args[-1]
    execve(file, args[:-1], env)


def execlp(file, *args):
    '''execlp(file, *args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process. '''
    execvp(file, args)


def execlpe(file, *args):
    '''execlpe(file, *args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the current
    process. '''
    env = args[-1]
    execvpe(file, args[:-1], env)


def execvp(file, args):
    '''execvp(file, args)

    Execute the executable file (which is searched for along $PATH)
    with argument list args, replacing the current process.
    args may be a list or tuple of strings. '''
    _execvpe(file, args)


def execvpe(file, args, env):
    '''execvpe(file, args, env)

    Execute the executable file (which is searched for along $PATH)
    with argument list args and environment env, replacing the
    current process.
    args may be a list or tuple of strings. '''
    _execvpe(file, args, env)

__all__.extend([
    'execl',
    'execle',
    'execlp',
    'execlpe',
    'execvp',
    'execvpe'])

def _execvpe(file, args, env = (None,)):
    pass
# WARNING: Decompyle incomplete


def get_exec_path(env = (None,)):
    '''Returns the sequence of directories that will be searched for the
    named executable (similar to a shell) when launching a process.

    *env* must be an environment variable dict or None.  If *env* is None,
    os.environ will be used.
    '''
    import warnings
# WARNING: Decompyle incomplete

from _collections_abc import MutableMapping, Mapping

class _Environ(MutableMapping):
    
    def __init__(self, data, encodekey, decodekey, encodevalue, decodevalue):
        self.encodekey = encodekey
        self.decodekey = decodekey
        self.encodevalue = encodevalue
        self.decodevalue = decodevalue
        self._data = data

    
    def __getitem__(self, key):
        
        try:
            value = self._data[self.encodekey(key)]
        except KeyError:
            raise KeyError(key), None

        return self.decodevalue(value)

    
    def __setitem__(self, key, value):
        key = self.encodekey(key)
        value = self.encodevalue(value)
        putenv(key, value)
        self._data[key] = value

    
    def __delitem__(self, key):
        encodedkey = self.encodekey(key)
        unsetenv(encodedkey)
        
        try:
            del self._data[encodedkey]
            return None
        except KeyError:
            raise KeyError(key), None


    
    def __iter__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __len__(self):
        return len(self._data)

    
    def __repr__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def copy(self):
        return dict(self)

    
    def setdefault(self, key, value):
        if key not in self:
            self[key] = value
        return self[key]

    
    def __ior__(self, other):
        self.update(other)
        return self

    
    def __or__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        new = None(self)
        new.update(other)
        return new

    
    def __ror__(self, other):
        if not isinstance(other, Mapping):
            return NotImplemented
        new = None(other)
        new.update(self)
        return new



def _createenviron():
    pass
# WARNING: Decompyle incomplete

environ = _createenviron()
del _createenviron

def getenv(key, default = (None,)):
    """Get an environment variable, return None if it doesn't exist.
    The optional second argument can specify an alternate default.
    key, default and the result are str."""
    return environ.get(key, default)

supports_bytes_environ = name != 'nt'
__all__.extend(('getenv', 'supports_bytes_environ'))
if supports_bytes_environ:
    
    def _check_bytes(value):
        if not isinstance(value, bytes):
            raise TypeError('bytes expected, not %s' % type(value).__name__)
        return value

    environb = _Environ(environ._data, _check_bytes, bytes, _check_bytes, bytes)
    del _check_bytes
    
    def getenvb(key, default = (None,)):
        """Get an environment variable, return None if it doesn't exist.
        The optional second argument can specify an alternate default.
        key, default and the result are bytes."""
        return environb.get(key, default)

    __all__.extend(('environb', 'getenvb'))

def _fscodec():
    pass
# WARNING: Decompyle incomplete

(fsencode, fsdecode) = _fscodec()
del _fscodec
if _exists('fork') and _exists('spawnv') and _exists('execv'):
    P_WAIT = 0
    P_NOWAIT = 1
    P_NOWAITO = 1
    __all__.extend([
        'P_WAIT',
        'P_NOWAIT',
        'P_NOWAITO'])
    
    def _spawnvef(mode, file, args, env, func):
        if not isinstance(args, (tuple, list)):
            raise TypeError('argv must be a tuple or a list')
        if not args or args[0]:
            raise ValueError('argv first element cannot be empty')
        pid = fork()
    # WARNING: Decompyle incomplete

    
    def spawnv(mode, file, args):
        """spawnv(mode, file, args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, None, execv)

    
    def spawnve(mode, file, args, env):
        """spawnve(mode, file, args, env) -> integer

Execute file with arguments from args in a subprocess with the
specified environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, env, execve)

    
    def spawnvp(mode, file, args):
        """spawnvp(mode, file, args) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, None, execvp)

    
    def spawnvpe(mode, file, args, env):
        """spawnvpe(mode, file, args, env) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return _spawnvef(mode, file, args, env, execvpe)

    __all__.extend([
        'spawnv',
        'spawnve',
        'spawnvp',
        'spawnvpe'])
if _exists('spawnv'):
    
    def spawnl(mode, file, *args):
        """spawnl(mode, file, *args) -> integer

Execute file with arguments from args in a subprocess.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return spawnv(mode, file, args)

    
    def spawnle(mode, file, *args):
        """spawnle(mode, file, *args, env) -> integer

Execute file with arguments from args in a subprocess with the
supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        env = args[-1]
        return spawnve(mode, file, args[:-1], env)

    __all__.extend([
        'spawnl',
        'spawnle'])
if _exists('spawnvp'):
    
    def spawnlp(mode, file, *args):
        """spawnlp(mode, file, *args) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        return spawnvp(mode, file, args)

    
    def spawnlpe(mode, file, *args):
        """spawnlpe(mode, file, *args, env) -> integer

Execute file (which is looked for along $PATH) with arguments from
args in a subprocess with the supplied environment.
If mode == P_NOWAIT return the pid of the process.
If mode == P_WAIT return the process's exit code if it exits normally;
otherwise return -SIG, where SIG is the signal that killed it. """
        env = args[-1]
        return spawnvpe(mode, file, args[:-1], env)

    __all__.extend([
        'spawnlp',
        'spawnlpe'])
if sys.platform != 'vxworks':
    
    def popen(cmd, mode, buffering = ('r', -1)):
        if not isinstance(cmd, str):
            raise TypeError('invalid cmd type (%s, expected string)' % type(cmd))
        if mode not in ('r', 'w'):
            raise ValueError('invalid mode %r' % mode)
    # WARNING: Decompyle incomplete

    
    class _wrap_close:
        
        def __init__(self, stream, proc):
            self._stream = stream
            self._proc = proc

        
        def close(self):
            self._stream.close()
            returncode = self._proc.wait()
            if returncode == 0:
                return None
            if None == 'nt':
                return returncode
            return None << 8

        
        def __enter__(self):
            return self

        
        def __exit__(self, *args):
            self.close()

        
        def __getattr__(self, name):
            return getattr(self._stream, name)

        
        def __iter__(self):
            return iter(self._stream)


    __all__.append('popen')

def fdopen(fd, mode, buffering, encoding = ('r', -1, None), *args, **kwargs):
    if not isinstance(fd, int):
        raise TypeError('invalid fd type (%s, expected integer)' % type(fd))
    import io
    if 'b' not in mode:
        encoding = io.text_encoding(encoding)
# WARNING: Decompyle incomplete


def _fspath(path):
    '''Return the path representation of a path-like object.

    If str or bytes is passed in, it is returned unchanged. Otherwise the
    os.PathLike interface is used to get the path representation. If the
    path representation is not str or bytes, TypeError is raised. If the
    provided path is not str, bytes, or os.PathLike, TypeError is raised.
    '''
    if isinstance(path, (str, bytes)):
        return path
    path_type = None(path)
    
    try:
        path_repr = path_type.__fspath__(path)
    except AttributeError:
        if hasattr(path_type, '__fspath__'):
            raise 
        raise TypeError('expected str, bytes or os.PathLike object, not ' + path_type.__name__)

    if isinstance(path_repr, (str, bytes)):
        return path_repr
    raise None('expected {}.__fspath__() to return str or bytes, not {}'.format(path_type.__name__, type(path_repr).__name__))

if not _exists('fspath'):
    fspath = _fspath
    fspath.__name__ = 'fspath'

class PathLike(abc.ABC):
    '''Abstract base class for implementing the file system path protocol.'''
    __fspath__ = (lambda self: raise NotImplementedError)()
    __subclasshook__ = (lambda cls, subclass: if cls is PathLike:
_check_methods(subclass, '__fspath__'))()
    __class_getitem__ = classmethod(GenericAlias)

if name == 'nt':
    
    class _AddedDllDirectory:
        
        def __init__(self, path, cookie, remove_dll_directory):
            self.path = path
            self._cookie = cookie
            self._remove_dll_directory = remove_dll_directory

        
        def close(self):
            self._remove_dll_directory(self._cookie)
            self.path = None

        
        def __enter__(self):
            return self

        
        def __exit__(self, *args):
            self.close()

        
        def __repr__(self):
            if self.path:
                return '<AddedDllDirectory({!r})>'.format(self.path)


    
    def add_dll_directory(path):
        '''Add a path to the DLL search path.

        This search path is used when resolving dependencies for imported
        extension modules (the module itself is resolved through sys.path),
        and also by ctypes.

        Remove the directory by calling close() on the returned object or
        using it in a with statement.
        '''
        import nt
        cookie = nt._add_dll_directory(path)
        return _AddedDllDirectory(path, cookie, nt._remove_dll_directory)

    return None
