# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shutil.pyc (Python 3.11)

"""Utility functions for copying and archiving files and directory trees.

XXX The functions here don't copy the resource fork or other metadata on Mac.

"""
import os
import sys
import stat
import fnmatch
import collections
import errno

try:
    import zlib
    del zlib
    _ZLIB_SUPPORTED = True
except ImportError:
    _ZLIB_SUPPORTED = False


try:
    import bz2
    del bz2
    _BZ2_SUPPORTED = True
except ImportError:
    _BZ2_SUPPORTED = False


try:
    import lzma
    del lzma
    _LZMA_SUPPORTED = True
except ImportError:
    _LZMA_SUPPORTED = False

_WINDOWS = os.name == 'nt'
posix = None
nt = None
if os.name == 'posix':
    import posix
elif _WINDOWS:
    import nt
COPY_BUFSIZE = 1048576 if _WINDOWS else 65536
if hasattr(os, 'sendfile'):
    _USE_CP_SENDFILE = sys.platform.startswith('linux')
    if posix:
        _HAS_FCOPYFILE = hasattr(posix, '_fcopyfile')
        _WIN_DEFAULT_PATHEXT = '.COM;.EXE;.BAT;.CMD;.VBS;.JS;.WS;.MSC'
        __all__ = [
            'copyfileobj',
            'copyfile',
            'copymode',
            'copystat',
            'copy',
            'copy2',
            'copytree',
            'move',
            'rmtree',
            'Error',
            'SpecialFileError',
            'ExecError',
            'make_archive',
            'get_archive_formats',
            'register_archive_format',
            'unregister_archive_format',
            'get_unpack_formats',
            'register_unpack_format',
            'unregister_unpack_format',
            'unpack_archive',
            'ignore_patterns',
            'chown',
            'which',
            'get_terminal_size',
            'SameFileError']
        
        class Error(OSError):
            pass

        
        class SameFileError(Error):
            '''Raised when source and destination are the same file.'''
            pass

        
        class SpecialFileError(OSError):
            '''Raised when trying to do a kind of operation (e.g. copying) which is
    not supported on a special file (e.g. a named pipe)'''
            pass

        
        class ExecError(OSError):
            '''Raised when a command could not be executed'''
            pass

        
        class ReadError(OSError):
            '''Raised when an archive cannot be read'''
            pass

        
        class RegistryError(Exception):
            '''Raised when a registry operation with the archiving
    and unpacking registries fails'''
            pass

        
        class _GiveupOnFastCopy(Exception):
            '''Raised as a signal to fallback on using raw read()/write()
    file copy when fast-copy functions fail to do so.
    '''
            pass

        
        def _fastcopy_fcopyfile(fsrc, fdst, flags):
            '''Copy a regular file content or metadata by using high-performance
    fcopyfile(3) syscall (macOS).
    '''
            
            try:
                infd = fsrc.fileno()
                outfd = fdst.fileno()
            except Exception:
                err = None
                raise _GiveupOnFastCopy(err)
                err = None
                del err

            
            try:
                posix._fcopyfile(infd, outfd, flags)
                return None
            except OSError:
                err = None
                err.filename = fsrc.name
                err.filename2 = fdst.name
                if err.errno in {
                    errno.EINVAL,
                    errno.ENOTSUP}:
                    raise _GiveupOnFastCopy(err)
                raise err, None
                err = None
                del err


        
        def _fastcopy_sendfile(fsrc, fdst):
            '''Copy data from one regular mmap-like fd to another by using
    high-performance sendfile(2) syscall.
    This should work on Linux >= 2.6.33 only.
    '''
            global _USE_CP_SENDFILE
            
            try:
                infd = fsrc.fileno()
                outfd = fdst.fileno()
            except Exception:
                err = None
                raise _GiveupOnFastCopy(err)
                err = None
                del err

            
            try:
                blocksize = max(os.fstat(infd).st_size, 8388608)
            except OSError:
                blocksize = 134217728

            if sys.maxsize < 0x100000000:
                blocksize = min(blocksize, 1073741824)
            offset = 0
            
            try:
                sent = os.sendfile(outfd, infd, offset, blocksize)
                if sent == 0:
                    return None
                None += sent
            except OSError:
                err = None
                err.filename = fsrc.name
                err.filename2 = fdst.name
                if err.errno == errno.ENOTSOCK:
                    _USE_CP_SENDFILE = False
                    raise _GiveupOnFastCopy(err)
                if err.errno == errno.ENOSPC:
                    raise err, None
                if offset == 0 and os.lseek(outfd, 0, os.SEEK_CUR) == 0:
                    raise _GiveupOnFastCopy(err)
                raise err
                err = None
                del err

            continue

        
        def _copyfileobj_readinto(fsrc, fdst, length = (COPY_BUFSIZE,)):
            '''readinto()/memoryview() based variant of copyfileobj().
    *fsrc* must support readinto() method and both files must be
    open in binary mode.
    '''
            fsrc_readinto = fsrc.readinto
            fdst_write = fdst.write
            mv = memoryview(bytearray(length))
            n = fsrc_readinto(mv)
            if not n:
                pass
            elif n < length:
                smv = mv[:n]
                fdst.write(smv)
                None(None, None)
            else:
                with None:
                    if not None:
                        pass
            fdst_write(mv)
            continue
            None(None, None)
            return None
            with None:
                if not None:
                    pass

        
        def copyfileobj(fsrc, fdst, length = (0,)):
            '''copy data from file-like object fsrc to file-like object fdst'''
            if not length:
                length = COPY_BUFSIZE
            fsrc_read = fsrc.read
            fdst_write = fdst.write
            buf = fsrc_read(length)
            if not buf:
                return None
            fdst_write(buf)
            continue

        
        def _samefile(src, dst):
            if isinstance(src, os.DirEntry) and hasattr(os.path, 'samestat'):
                
                try:
                    return os.path.samestat(src.stat(), os.stat(dst))
                except OSError:
                    return False
                    if hasattr(os.path, 'samefile'):
                        
                        try:
                            return os.path.samefile(src, dst)
                        except OSError:
                            return False
                            return os.path.normcase(os.path.abspath(src)) == os.path.normcase(os.path.abspath(dst))



        
        def _stat(fn):
            return fn.stat() if isinstance(fn, os.DirEntry) else os.stat(fn)

        
        def _islink(fn):
            return fn.is_symlink() if isinstance(fn, os.DirEntry) else os.path.islink(fn)

        
        def copyfile(src = None, dst = {
            'follow_symlinks': True }, *, follow_symlinks):
            '''Copy data from src to dst in the most efficient way possible.

    If follow_symlinks is not set and src is a symbolic link, a new
    symlink will be created instead of copying the file it points to.

    '''
            sys.audit('shutil.copyfile', src, dst)
            if _samefile(src, dst):
                raise SameFileError('{!r} and {!r} are the same file'.format(src, dst))
            file_size = 0
            for i, fn in enumerate([
                src,
                dst]):
                st = _stat(fn)
                if stat.S_ISFIFO(st.st_mode):
                    fn = fn.path if isinstance(fn, os.DirEntry) else fn
                    raise SpecialFileError('`%s` is a named pipe' % fn)
                if _WINDOWS and i == 0:
                    file_size = st.st_size
                except OSError:
                    continue
                if follow_symlinks and _islink(src):
                    os.symlink(os.readlink(src), dst)
                else:
                    fsrc = open(src, 'rb')
                    fdst = open(dst, 'wb')
                    if _HAS_FCOPYFILE:
                        _fastcopy_fcopyfile(fsrc, fdst, posix._COPYFILE_DATA)
                        None(None, None)
                        None(None, None)
                        return 
                    except _GiveupOnFastCopy:
                        pass
                    except _GiveupOnFastCopy:
                        pass
                    except:
                        if _WINDOWS and file_size > 0:
                            _copyfileobj_readinto(fsrc, fdst, min(file_size, COPY_BUFSIZE))
                            None(None, None)
                            None(None, None)
                            return 
                        None(fsrc, fdst)
                        None(None, None)
                    except:
                        with None:
                            if not None:
                                pass
            except IsADirectoryError:
                if not os.path.exists(dst):
                    raise FileNotFoundError(f'''Directory does not exist: {dst}'''), e
                raise 
                None = None
                del e
            None(None, None)

        
        def copymode(src = None, dst = {
            'follow_symlinks': True }, *, follow_symlinks):
            """Copy mode bits from src to dst.

    If follow_symlinks is not set, symlinks aren't followed if and only
    if both `src` and `dst` are symlinks.  If `lchmod` isn't available
    (e.g. Linux) this method does nothing.

    """
            sys.audit('shutil.copymode', src, dst)
            if follow_symlinks and _islink(src) and os.path.islink(dst):
                if os.name == 'nt':
                    chmod_func = os.chmod
                    stat_func = os.lstat
                elif hasattr(os, 'lchmod'):
                    chmod_func = os.lchmod
                    stat_func = os.lstat
                else:
                    return None
                if None.name == 'nt' and os.path.islink(dst):
                    dst = os.path.realpath(dst, strict = True)
            chmod_func = os.chmod
            stat_func = _stat
            st = stat_func(src)
            chmod_func(dst, stat.S_IMODE(st.st_mode))


def copystat(src = None if hasattr(os, 'listxattr') else None, dst = {
    'follow_symlinks': True }, *, follow_symlinks):
    '''Copy file metadata

    Copy the permission bits, last access time, last modification time, and
    flags from `src` to `dst`. On Linux, copystat() also copies the "extended
    attributes" where possible. The file contents, owner, and group are
    unaffected. `src` and `dst` are path-like objects or path names given as
    strings.

    If the optional flag `follow_symlinks` is not set, symlinks aren\'t
    followed if and only if both `src` and `dst` are symlinks.
    '''
    pass
# WARNING: Decompyle incomplete


def copy(src = None, dst = {
    'follow_symlinks': True }, *, follow_symlinks):
    '''Copy data and mode bits ("cp src dst"). Return the file\'s destination.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won\'t be followed. This
    resembles GNU\'s "cp -P src dst".

    If source and destination are the same file, a SameFileError will be
    raised.

    '''
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst, follow_symlinks = follow_symlinks)
    copymode(src, dst, follow_symlinks = follow_symlinks)
    return dst


def copy2(src = None, dst = {
    'follow_symlinks': True }, *, follow_symlinks):
    '''Copy data and metadata. Return the file\'s destination.

    Metadata is copied with copystat(). Please see the copystat function
    for more information.

    The destination may be a directory.

    If follow_symlinks is false, symlinks won\'t be followed. This
    resembles GNU\'s "cp -P src dst".
    '''
    if os.path.isdir(dst):
        dst = os.path.join(dst, os.path.basename(src))
    copyfile(src, dst, follow_symlinks = follow_symlinks)
    copystat(src, dst, follow_symlinks = follow_symlinks)
    return dst


def ignore_patterns(*patterns):
    '''Function that can be used as copytree() ignore parameter.

    Patterns is a sequence of glob-style patterns
    that are used to exclude files'''
    pass
# WARNING: Decompyle incomplete


def _copytree(entries, src, dst, symlinks, ignore, copy_function, ignore_dangling_symlinks, dirs_exist_ok = (False,)):
    pass
# WARNING: Decompyle incomplete


def copytree(src, dst, symlinks, ignore, copy_function, ignore_dangling_symlinks, dirs_exist_ok = (False, None, copy2, False, False)):
    """Recursively copy a directory tree and return the destination directory.

    If exception(s) occur, an Error is raised with a list of reasons.

    If the optional symlinks flag is true, symbolic links in the
    source tree result in symbolic links in the destination tree; if
    it is false, the contents of the files pointed to by symbolic
    links are copied. If the file pointed by the symlink doesn't
    exist, an exception will be added in the list of errors raised in
    an Error exception at the end of the copy process.

    You can set the optional ignore_dangling_symlinks flag to true if you
    want to silence this exception. Notice that this has no effect on
    platforms that don't support os.symlink.

    The optional ignore argument is a callable. If given, it
    is called with the `src` parameter, which is the directory
    being visited by copytree(), and `names` which is the list of
    `src` contents, as returned by os.listdir():

        callable(src, names) -> ignored_names

    Since copytree() is called recursively, the callable will be
    called once for each directory that is copied. It returns a
    list of names relative to the `src` directory that should
    not be copied.

    The optional copy_function argument is a callable that will be used
    to copy each file. It will be called with the source path and the
    destination path as arguments. By default, copy2() is used, but any
    function that supports the same signature (like copy()) can be used.

    If dirs_exist_ok is false (the default) and `dst` already exists, a
    `FileExistsError` is raised. If `dirs_exist_ok` is true, the copying
    operation will continue if it encounters existing directories, and files
    within the `dst` tree will be overwritten by corresponding files from the
    `src` tree.
    """
    sys.audit('shutil.copytree', src, dst)
    itr = os.scandir(src)
    entries = list(itr)
    None(None, None)

if hasattr(os.stat_result, 'st_file_attributes'):
    
    def _rmtree_isdir(entry):
        
        try:
            st = entry.stat(follow_symlinks = False)
            if stat.S_ISDIR(st.st_mode):
                if st.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                    return not (st.st_reparse_tag == stat.IO_REPARSE_TAG_MOUNT_POINT)
                except OSError:
                    return False


    
    def _rmtree_islink(path):
        
        try:
            st = os.lstat(path)
            if not stat.S_ISLNK(st.st_mode):
                if st.st_file_attributes & stat.FILE_ATTRIBUTE_REPARSE_POINT:
                    return st.st_reparse_tag == stat.IO_REPARSE_TAG_MOUNT_POINT
                except OSError:
                    return False


else:
    
    def _rmtree_isdir(entry):
        
        try:
            return entry.is_dir(follow_symlinks = False)
        except OSError:
            return False


    
    def _rmtree_islink(path):
        return os.path.islink(path)


def _rmtree_unsafe(path, onerror):
    
    try:
        scandir_it = os.scandir(path)
        entries = list(scandir_it)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except OSError:
                        onerror(os.scandir, path, sys.exc_info())
                        entries = []

                    for entry in entries:
                        fullname = entry.path
                        _rmtree_unsafe(fullname, onerror)
                        os.unlink(fullname)
                        except OSError:
                            onerror(os.unlink, fullname, sys.exc_info())
                            continue
                        
                        try:
                            os.rmdir(path)
                            return None
                        except OSError:
                            onerror(os.rmdir, path, sys.exc_info())
                            return None






def _rmtree_safe_fd(topfd, path, onerror):
    
    try:
        scandir_it = os.scandir(topfd)
        entries = list(scandir_it)
        
        try:
            None(None, None)
        with None:
            if not None:
                
                try:
                    
                    try:
                        pass
                    except OSError:
                        err = None
                        err.filename = path
                        onerror(os.scandir, path, sys.exc_info())
                        err = None
                        del err
                        return None
                        err = None
                        del err

                    for entry in entries:
                        fullname = os.path.join(path, entry.name)
                        is_dir = entry.is_dir(follow_symlinks = False)
                        if is_dir:
                            orig_st = entry.stat(follow_symlinks = False)
                            is_dir = stat.S_ISDIR(orig_st.st_mode)
                        else:
                            except OSError:
                                onerror(os.lstat, fullname, sys.exc_info())
                                continue
                    except OSError:
                        is_dir = False



    continue
    if not dirfd_closed:
        os.close(dirfd)
        except OSError:
            onerror(os.close, fullname, sys.exc_info())
    except OSError:
        onerror(os.open, fullname, sys.exc_info())
        continue
    os.unlink(entry.name, dir_fd = topfd)
    continue
    except OSError:
        onerror(os.unlink, fullname, sys.exc_info())
        continue

if {
    os.open,
    os.stat,
    os.unlink,
    os.rmdir} <= os.supports_dir_fd:
    if os.scandir in os.supports_fd:
        _use_fd_functions = os.stat in os.supports_follow_symlinks
        
        def rmtree(path = None, ignore_errors = (False, None), onerror = {
            'dir_fd': None }, *, dir_fd):
            '''Recursively delete a directory tree.

    If dir_fd is not None, it should be a file descriptor open to a directory;
    path will then be relative to that directory.
    dir_fd may not be implemented on your platform.
    If it is unavailable, using it will raise a NotImplementedError.

    If ignore_errors is set, errors are ignored; otherwise, if onerror
    is set, it is called to handle the error with arguments (func,
    path, exc_info) where func is platform and implementation dependent;
    path is the argument to that function that caused it to fail; and
    exc_info is a tuple returned by sys.exc_info().  If ignore_errors
    is false and onerror is None, an exception is raised.

    '''
            sys.audit('shutil.rmtree', path, dir_fd)
            if ignore_errors:
                
                def onerror(*args):
                    pass

        # WARNING: Decompyle incomplete

        rmtree.avoids_symlink_attacks = _use_fd_functions
        
        def _basename(path):
