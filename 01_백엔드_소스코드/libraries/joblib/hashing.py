# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hashing.pyc (Python 3.11)

'''
Fast cryptographic hash of Python objects, with a special case for fast
hashing of numpy arrays.
'''
import decimal
import hashlib
import io
import pickle
import struct
import sys
import types
Pickler = pickle._Pickler

class _ConsistentSet(object):
    '''Class used to ensure the hash of Sets is preserved
    whatever the order of its items.
    '''
    
    def __init__(self, set_sequence):
        
        try:
            self._sequence = sorted(set_sequence)
            return None
        except (TypeError, decimal.InvalidOperation):
            self._sequence = (lambda .0: pass# WARNING: Decompyle incomplete
)(set_sequence())
            return None




class _MyHash(object):
    """Class used to hash objects that won't normally pickle"""
    
    def __init__(self, *args):
        self.args = args



class Hasher(Pickler):
    '''A subclass of pickler, to do cryptographic hashing, rather than
    pickling. This is used to produce a unique hash of the given
    Python object that is not necessarily cryptographically secure.
    '''
    
    def __init__(self, hash_name = ('md5',)):
        self.stream = io.BytesIO()
        protocol = 3
        Pickler.__init__(self, self.stream, protocol = protocol)
        self._hash = hashlib.new(hash_name, usedforsecurity = False)

    
    def hash(self, obj, return_digest = (True,)):
        
        try:
            self.dump(obj)
        except pickle.PicklingError:
            e = None
            raise 
            None = e, e.args += (f'''PicklingError while hashing {obj!r}: {e!r}''',), .args
            del e

        dumps = self.stream.getvalue()
        self._hash.update(dumps)
        if return_digest:
            return self._hash.hexdigest()

    
    def save(self, obj):
        pass
    # WARNING: Decompyle incomplete

    
    def memoize(self, obj):
        if isinstance(obj, (bytes, str)):
            return None
        None.memoize(self, obj)

    
    def save_global(self, obj, name, pack = (None, struct.pack)):
        kwargs = dict(name = name, pack = pack)
        del kwargs['pack']
    # WARNING: Decompyle incomplete

    dispatch = Pickler.dispatch.copy()
    dispatch[type(len)] = save_global
    dispatch[type(object)] = save_global
    dispatch[type(Pickler)] = save_global
    dispatch[type(pickle.dump)] = save_global
    
    def _batch_setitems(self, items, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def save_set(self, set_items):
        Pickler.save(self, _ConsistentSet(set_items))

    dispatch[type(set())] = save_set


class NumpyHasher(Hasher):
    '''Special case the hasher for when numpy is loaded.'''
    
    def __init__(self, hash_name, coerce_mmap = ('md5', False)):
        '''
        Parameters
        ----------
        hash_name: string
            The hash algorithm to be used
        coerce_mmap: boolean
            Make no difference between np.memmap and np.ndarray
            objects.
        '''
        self.coerce_mmap = coerce_mmap
        Hasher.__init__(self, hash_name = hash_name)
        import numpy as np
        self.np = np
        if hasattr(np, 'getbuffer'):
            self._getbuffer = np.getbuffer
            return None
        self._getbuffer = None

    
    def save(self, obj):
        '''Subclass the save method, to hash ndarray subclass, rather
        than pickling them. Off course, this is a total abuse of
        the Pickler class.
        '''
        if not isinstance(obj, self.np.ndarray) and obj.dtype.hasobject:
            if obj.shape == ():
                obj_c_contiguous = obj.flatten()
            elif obj.flags.c_contiguous:
                obj_c_contiguous = obj
            elif obj.flags.f_contiguous:
                obj_c_contiguous = obj.T
            else:
                obj_c_contiguous = obj.flatten()
            self._hash.update(self._getbuffer(obj_c_contiguous.view(self.np.uint8)))
            if self.coerce_mmap and isinstance(obj, self.np.memmap):
                klass = self.np.ndarray
            else:
                klass = obj.__class__
            obj = (klass, ('HASHED', obj.dtype, obj.shape, obj.strides))
        elif isinstance(obj, self.np.dtype):
            self._hash.update('_HASHED_DTYPE'.encode('utf-8'))
            self._hash.update(pickle.dumps(obj))
            return None
        Hasher.save(self, obj)



def hash(obj, hash_name, coerce_mmap = ('md5', False)):
    """Quick calculation of a hash to identify uniquely Python objects
    containing numpy arrays.

    Parameters
    ----------
    hash_name: 'md5' or 'sha1'
        Hashing algorithm used. sha1 is supposedly safer, but md5 is
        faster.
    coerce_mmap: boolean
        Make no difference between np.memmap and np.ndarray
    """
    valid_hash_names = ('md5', 'sha1')
    if hash_name not in valid_hash_names:
        raise ValueError("Valid options for 'hash_name' are {}. Got hash_name={!r} instead.".format(valid_hash_names, hash_name))
    if 'numpy' in sys.modules:
        hasher = NumpyHasher(hash_name = hash_name, coerce_mmap = coerce_mmap)
    else:
        hasher = Hasher(hash_name = hash_name)
    return hasher.hash(obj)
