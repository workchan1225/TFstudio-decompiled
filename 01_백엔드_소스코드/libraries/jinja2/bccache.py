# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bccache.pyc (Python 3.11)

'''The optional bytecode cache system. This is useful if you have very
complex template situations and the compilation of all those templates
slows down your application too much.

Situations where this is useful are often forking web applications that
are initialized on the first request.
'''
import errno
import fnmatch
import marshal
import os
import pickle
import stat
import sys
import tempfile
import typing as t
from hashlib import sha1
from io import BytesIO
from types import CodeType
if t.TYPE_CHECKING:
    import typing_extensions as te
    from environment import Environment
    
    class _MemcachedClient(te.Protocol):
        
        def get(self = None, key = None):
            pass

        
        def set(self = None, key = None, value = None, timeout = (None,)):
            pass


bc_version = 5
bc_magic = b'j2' + pickle.dumps(bc_version, 2) + pickle.dumps(sys.version_info[0] << 24 | sys.version_info[1], 2)

class Bucket:
    """Buckets are used to store the bytecode for one template.  It's created
    and initialized by the bytecode cache and passed to the loading functions.

    The buckets get an internal checksum from the cache assigned and use this
    to automatically reject outdated cache material.  Individual bytecode
    cache subclasses don't have to care about cache invalidation.
    """
    
    def __init__(self = None, environment = None, key = None, checksum = ('environment', 'Environment', 'key', str, 'checksum', str, 'return', None)):
        self.environment = environment
        self.key = key
        self.checksum = checksum
        self.reset()

    
    def reset(self = None):
        '''Resets the bucket (unloads the bytecode).'''
        self.code = None

    
    def load_bytecode(self = None, f = None):
        '''Loads bytecode from a file or file like object.'''
        magic = f.read(len(bc_magic))
        if magic != bc_magic:
            self.reset()
            return None
        checksum = None.load(f)
        if self.checksum != checksum:
            self.reset()
            return None
        
        try:
            self.code = marshal.load(f)
            return None
        except (EOFError, ValueError, TypeError):
            self.reset()
            return None


    
    def write_bytecode(self = None, f = None):
        '''Dump the bytecode into the file or file like object passed.'''
        pass
    # WARNING: Decompyle incomplete

    
    def bytecode_from_string(self = None, string = None):
        '''Load bytecode from bytes.'''
        self.load_bytecode(BytesIO(string))

    
    def bytecode_to_string(self = None):
        '''Return the bytecode as bytes.'''
        out = BytesIO()
        self.write_bytecode(out)
        return out.getvalue()



class BytecodeCache:
    """To implement your own bytecode cache you have to subclass this class
    and override :meth:`load_bytecode` and :meth:`dump_bytecode`.  Both of
    these methods are passed a :class:`~jinja2.bccache.Bucket`.

    A very basic bytecode cache that saves the bytecode on the file system::

        from os import path

        class MyCache(BytecodeCache):

            def __init__(self, directory):
                self.directory = directory

            def load_bytecode(self, bucket):
                filename = path.join(self.directory, bucket.key)
                if path.exists(filename):
                    with open(filename, 'rb') as f:
                        bucket.load_bytecode(f)

            def dump_bytecode(self, bucket):
                filename = path.join(self.directory, bucket.key)
                with open(filename, 'wb') as f:
                    bucket.write_bytecode(f)

    A more advanced version of a filesystem based bytecode cache is part of
    Jinja.
    """
    
    def load_bytecode(self = None, bucket = None):
        '''Subclasses have to override this method to load bytecode into a
        bucket.  If they are not able to find code in the cache for the
        bucket, it must not do anything.
        '''
        raise NotImplementedError()

    
    def dump_bytecode(self = None, bucket = None):
        '''Subclasses have to override this method to write the bytecode
        from a bucket back to the cache.  If it unable to do so it must not
        fail silently but raise an exception.
        '''
        raise NotImplementedError()

    
    def clear(self = None):
        '''Clears the cache.  This method is not used by Jinja but should be
        implemented to allow applications to clear the bytecode cache used
        by a particular environment.
        '''
        pass

    
    def get_cache_key(self = None, name = None, filename = None):
        '''Returns the unique hash key for this template name.'''
        hash = sha1(name.encode('utf-8'))
    # WARNING: Decompyle incomplete

    
    def get_source_checksum(self = None, source = None):
        '''Returns a checksum for the source.'''
        return sha1(source.encode('utf-8')).hexdigest()

    
    def get_bucket(self, environment = None, name = None, filename = None, source = ('environment', 'Environment', 'name', str, 'filename', t.Optional[str], 'source', str, 'return', Bucket)):
        '''Return a cache bucket for the given template.  All arguments are
        mandatory but filename may be `None`.
        '''
        key = self.get_cache_key(name, filename)
        checksum = self.get_source_checksum(source)
        bucket = Bucket(environment, key, checksum)
        self.load_bytecode(bucket)
        return bucket

    
    def set_bucket(self = None, bucket = None):
        '''Put the bucket into the cache.'''
        self.dump_bytecode(bucket)



class FileSystemBytecodeCache(BytecodeCache):
    """A bytecode cache that stores bytecode on the filesystem.  It accepts
    two arguments: The directory where the cache items are stored and a
    pattern string that is used to build the filename.

    If no directory is specified a default cache directory is selected.  On
    Windows the user's temp directory is used, on UNIX systems a directory
    is created for the user in the system temp directory.

    The pattern can be used to have multiple separate caches operate on the
    same directory.  The default pattern is ``'__jinja2_%s.cache'``.  ``%s``
    is replaced with the cache key.

    >>> bcc = FileSystemBytecodeCache('/tmp/jinja_cache', '%s.cache')

    This bytecode cache supports clearing of the cache using the clear method.
    """
    
    def __init__(self = None, directory = None, pattern = None):
        pass
    # WARNING: Decompyle incomplete

    
    def _get_default_cache_dir(self = None):
        
        def _unsafe_dir():
            raise RuntimeError('Cannot determine safe temp directory.  You need to explicitly provide one.')

        tmpdir = tempfile.gettempdir()
        if os.name == 'nt':
            return tmpdir
        if not None(os, 'getuid'):
            _unsafe_dir()
        dirname = f'''_jinja2-cache-{os.getuid()}'''
        actual_dir = os.path.join(tmpdir, dirname)
        
        try:
            os.mkdir(actual_dir, stat.S_IRWXU)
        except OSError:
            e = None
            if e.errno != errno.EEXIST:
                raise 
            e = None
            del e
        except:
            e = None
            del e

        
        try:
            os.chmod(actual_dir, stat.S_IRWXU)
            actual_dir_stat = os.lstat(actual_dir)
            if actual_dir_stat.st_uid != os.getuid() and stat.S_ISDIR(actual_dir_stat.st_mode) or stat.S_IMODE(actual_dir_stat.st_mode) != stat.S_IRWXU:
                _unsafe_dir()
            else:
                except OSError:
                    e = None
                    if e.errno != errno.EEXIST:
                        raise 
                    e = None
                    del e
                except:
                    e = None
                    del e
                actual_dir_stat = os.lstat(actual_dir)
                if actual_dir_stat.st_uid != os.getuid() and stat.S_ISDIR(actual_dir_stat.st_mode) or stat.S_IMODE(actual_dir_stat.st_mode) != stat.S_IRWXU:
                    _unsafe_dir()

        return actual_dir

    
    def _get_cache_filename(self = None, bucket = None):
        return os.path.join(self.directory, self.pattern % (bucket.key,))

    
    def load_bytecode(self = None, bucket = None):
        filename = self._get_cache_filename(bucket)
        
        try:
            f = open(filename, 'rb')
        except (FileNotFoundError, IsADirectoryError, PermissionError):
            return None

        f
        bucket.load_bytecode(f)
        None(None, None)
        return None
        with None:
            if not None:
                pass

    
    def dump_bytecode(self = None, bucket = None):
        pass
    # WARNING: Decompyle incomplete

    
    def clear(self = None):
        remove = remove
        import os
        files = fnmatch.filter(os.listdir(self.directory), self.pattern % ('*',))
        for filename in files:
            remove(os.path.join(self.directory, filename))
            except OSError:
                continue
            return None



class MemcachedBytecodeCache(BytecodeCache):
    """This class implements a bytecode cache that uses a memcache cache for
    storing the information.  It does not enforce a specific memcache library
    (tummy's memcache or cmemcache) but will accept any class that provides
    the minimal interface required.

    Libraries compatible with this class:

    -   `cachelib <https://github.com/pallets/cachelib>`_
    -   `python-memcached <https://pypi.org/project/python-memcached/>`_

    (Unfortunately the django cache interface is not compatible because it
    does not support storing binary data, only text. You can however pass
    the underlying cache client to the bytecode cache which is available
    as `django.core.cache.cache._client`.)

    The minimal interface for the client passed to the constructor is this:

    .. class:: MinimalClientInterface

        .. method:: set(key, value[, timeout])

            Stores the bytecode in the cache.  `value` is a string and
            `timeout` the timeout of the key.  If timeout is not provided
            a default timeout or no timeout should be assumed, if it's
            provided it's an integer with the number of seconds the cache
            item should exist.

        .. method:: get(key)

            Returns the value for the cache key.  If the item does not
            exist in the cache the return value must be `None`.

    The other arguments to the constructor are the prefix for all keys that
    is added before the actual cache key and the timeout for the bytecode in
    the cache system.  We recommend a high (or no) timeout.

    This bytecode cache does not support clearing of used items in the cache.
    The clear method is a no-operation function.

    .. versionadded:: 2.7
       Added support for ignoring memcache errors through the
       `ignore_memcache_errors` parameter.
    """
    
    def __init__(self = None, client = None, prefix = None, timeout = ('jinja2/bytecode/', None, True), ignore_memcache_errors = ('client', '_MemcachedClient', 'prefix', str, 'timeout', t.Optional[int], 'ignore_memcache_errors', bool)):
        self.client = client
        self.prefix = prefix
        self.timeout = timeout
        self.ignore_memcache_errors = ignore_memcache_errors

    
    def load_bytecode(self = None, bucket = None):
        
        try:
            code = self.client.get(self.prefix + bucket.key)
            bucket.bytecode_from_string(code)
            return None
        except Exception:
            if not self.ignore_memcache_errors:
                raise 
            return None


    
    def dump_bytecode(self = None, bucket = None):
        key = self.prefix + bucket.key
        value = bucket.bytecode_to_string()
    # WARNING: Decompyle incomplete
