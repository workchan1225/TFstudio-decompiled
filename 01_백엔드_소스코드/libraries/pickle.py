# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pickle.pyc (Python 3.11)

'''Create portable serialized representations of Python objects.

See module copyreg for a mechanism for registering custom picklers.
See module pickletools source for extensive comments.

Classes:

    Pickler
    Unpickler

Functions:

    dump(object, file)
    dumps(object) -> string
    load(file) -> object
    loads(bytes) -> object

Misc variables:

    __version__
    format_version
    compatible_formats

'''
from types import FunctionType
from copyreg import dispatch_table
from copyreg import _extension_registry, _inverted_registry, _extension_cache
from itertools import islice
from functools import partial
import sys
from sys import maxsize
from struct import pack, unpack
import re
import io
import codecs
import _compat_pickle
__all__ = [
    'PickleError',
    'PicklingError',
    'UnpicklingError',
    'Pickler',
    'Unpickler',
    'dump',
    'dumps',
    'load',
    'loads']

try:
    from _pickle import PickleBuffer
    __all__.append('PickleBuffer')
    _HAVE_PICKLE_BUFFER = True
except ImportError:
    _HAVE_PICKLE_BUFFER = False

bytes_types = (bytes, bytearray)
format_version = '4.0'
compatible_formats = [
    '1.0',
    '1.1',
    '1.2',
    '1.3',
    '2.0',
    '3.0',
    '4.0',
    '5.0']
HIGHEST_PROTOCOL = 5
DEFAULT_PROTOCOL = 4

class PickleError(Exception):
    '''A common base class for the other pickling exceptions.'''
    pass


class PicklingError(PickleError):
    '''This exception is raised when an unpicklable object is passed to the
    dump() method.

    '''
    pass


class UnpicklingError(PickleError):
    '''This exception is raised when there is a problem unpickling an object,
    such as a security violation.

    Note that other exceptions may also be raised during unpickling, including
    (but not necessarily limited to) AttributeError, EOFError, ImportError,
    and IndexError.

    '''
    pass


class _Stop(Exception):
    
    def __init__(self, value):
        self.value = value



try:
    from org.python.core import PyStringMap
except ImportError:
    PyStringMap = None

MARK = b'('
STOP = b'.'
POP = b'0'
POP_MARK = b'1'
DUP = b'2'
FLOAT = b'F'
INT = b'I'
BININT = b'J'
BININT1 = b'K'
LONG = b'L'
BININT2 = b'M'
NONE = b'N'
PERSID = b'P'
BINPERSID = b'Q'
REDUCE = b'R'
STRING = b'S'
BINSTRING = b'T'
SHORT_BINSTRING = b'U'
UNICODE = b'V'
BINUNICODE = b'X'
APPEND = b'a'
BUILD = b'b'
GLOBAL = b'c'
DICT = b'd'
EMPTY_DICT = b'}'
APPENDS = b'e'
GET = b'g'
BINGET = b'h'
INST = b'i'
LONG_BINGET = b'j'
LIST = b'l'
EMPTY_LIST = b']'
OBJ = b'o'
PUT = b'p'
BINPUT = b'q'
LONG_BINPUT = b'r'
SETITEM = b's'
TUPLE = b't'
EMPTY_TUPLE = b')'
SETITEMS = b'u'
BINFLOAT = b'G'
TRUE = b'I01\n'
FALSE = b'I00\n'
PROTO = b'\x80'
NEWOBJ = b'\x81'
EXT1 = b'\x82'
EXT2 = b'\x83'
EXT4 = b'\x84'
TUPLE1 = b'\x85'
TUPLE2 = b'\x86'
TUPLE3 = b'\x87'
NEWTRUE = b'\x88'
NEWFALSE = b'\x89'
LONG1 = b'\x8a'
LONG4 = b'\x8b'
_tuplesize2code = [
    EMPTY_TUPLE,
    TUPLE1,
    TUPLE2,
    TUPLE3]
BINBYTES = b'B'
SHORT_BINBYTES = b'C'
SHORT_BINUNICODE = b'\x8c'
BINUNICODE8 = b'\x8d'
BINBYTES8 = b'\x8e'
EMPTY_SET = b'\x8f'
ADDITEMS = b'\x90'
FROZENSET = b'\x91'
NEWOBJ_EX = b'\x92'
STACK_GLOBAL = b'\x93'
MEMOIZE = b'\x94'
FRAME = b'\x95'
BYTEARRAY8 = b'\x96'
NEXT_BUFFER = b'\x97'
READONLY_BUFFER = b'\x98'
(lambda .0: pass# WARNING: Decompyle incomplete
)(dir()())

class _Framer:
    _FRAME_SIZE_MIN = 4
    _FRAME_SIZE_TARGET = 65536
    
    def __init__(self, file_write):
        self.file_write = file_write
        self.current_frame = None

    
    def start_framing(self):
        self.current_frame = io.BytesIO()

    
    def end_framing(self):
        if self.current_frame or self.current_frame.tell() > 0:
            self.commit_frame(force = True)
            self.current_frame = None
            return None
        return None

    
    def commit_frame(self, force = (False,)):
        if self.current_frame:
            f = self.current_frame
            if f.tell() >= self._FRAME_SIZE_TARGET or force:
                data = f.getbuffer()
                write = self.file_write
                if len(data) >= self._FRAME_SIZE_MIN:
                    write(FRAME + pack('<Q', len(data)))
                write(data)
                self.current_frame = io.BytesIO()
                return None
            return None

    
    def write(self, data):
        if self.current_frame:
            return self.current_frame.write(data)
        return None.file_write(data)

    
    def write_large_bytes(self, header, payload):
        write = self.file_write
        if self.current_frame:
            self.commit_frame(force = True)
        write(header)
        write(payload)



class _Unframer:
    
    def __init__(self, file_read, file_readline, file_tell = (None,)):
        self.file_read = file_read
        self.file_readline = file_readline
        self.current_frame = None

    
    def readinto(self, buf):
        if self.current_frame:
            n = self.current_frame.readinto(buf)
            if n == 0 and len(buf) != 0:
                self.current_frame = None
                n = len(buf)
                buf[:] = self.file_read(n)
                return n
            if None < len(buf):
                raise UnpicklingError('pickle exhausted before end of frame')
            return n
        n = None(buf)
        buf[:] = self.file_read(n)
        return n

    
    def read(self, n):
        if self.current_frame:
            data = self.current_frame.read(n)
            if data and n != 0:
                self.current_frame = None
                return self.file_read(n)
            if None(data) < n:
                raise UnpicklingError('pickle exhausted before end of frame')
            return data
        return None.file_read(n)

    
    def readline(self):
        if self.current_frame:
            data = self.current_frame.readline()
            if not data:
                self.current_frame = None
                return self.file_readline()
            if None[-1] != 10:
                raise UnpicklingError('pickle exhausted before end of frame')
            return data
        return None.file_readline()

    
    def load_frame(self, frame_size):
        if self.current_frame and self.current_frame.read() != b'':
            raise UnpicklingError('beginning of a new frame before end of current frame')
        self.current_frame = io.BytesIO(self.file_read(frame_size))



def _getattribute(obj, name):
    for subpath in name.split('.'):
        if subpath == '<locals>':
            raise AttributeError("Can't get local attribute {!r} on {!r}".format(name, obj))
        parent = obj
        obj = getattr(obj, subpath)
        except AttributeError:
            raise AttributeError("Can't get attribute {!r} on {!r}".format(name, obj)), None
        return (obj, parent)


def whichmodule(obj, name):
    '''Find the module an object belong to.'''
    module_name = getattr(obj, '__module__', None)
# WARNING: Decompyle incomplete


def encode_long(x):
    """Encode a long to a two's complement little-endian binary string.
    Note that 0 is a special case, returning an empty string, to save a
    byte in the LONG1 pickling context.

    >>> encode_long(0)
    b''
    >>> encode_long(255)
    b'\\xff\\x00'
    >>> encode_long(32767)
    b'\\xff\\x7f'
    >>> encode_long(-256)
    b'\\x00\\xff'
    >>> encode_long(-32768)
    b'\\x00\\x80'
    >>> encode_long(-128)
    b'\\x80'
    >>> encode_long(127)
    b'\\x7f'
    >>>
    """
    if x == 0:
        return b''
    nbytes = (None.bit_length() >> 3) + 1
    result = x.to_bytes(nbytes, byteorder = 'little', signed = True)
    if x < 0 and nbytes > 1 and result[-1] == 255 and result[-2] & 128 != 0:
        result = result[:-1]
    return result


def decode_long(data):
    '''Decode a long from a two\'s complement little-endian binary string.

    >>> decode_long(b\'\')
    0
    >>> decode_long(b"\\xff\\x00")
    255
    >>> decode_long(b"\\xff\\x7f")
    32767
    >>> decode_long(b"\\x00\\xff")
    -256
    >>> decode_long(b"\\x00\\x80")
    -32768
    >>> decode_long(b"\\x80")
    -128
    >>> decode_long(b"\\x7f")
    127
    '''
    return int.from_bytes(data, byteorder = 'little', signed = True)


class _Pickler:
    __module__ = __name__
    __qualname__ = '_Pickler'
    
    def __init__(self = None, file = (None,), protocol = {
        'fix_imports': True,
        'buffer_callback': None }, *, fix_imports, buffer_callback):
        '''This takes a binary file for writing a pickle data stream.

        The optional *protocol* argument tells the pickler to use the
        given protocol; supported protocols are 0, 1, 2, 3, 4 and 5.
        The default protocol is 4. It was introduced in Python 3.4, and
        is incompatible with previous versions.

        Specifying a negative protocol version selects the highest
        protocol version supported.  The higher the protocol used, the
        more recent the version of Python needed to read the pickle
        produced.

        The *file* argument must have a write() method that accepts a
        single bytes argument. It can thus be a file object opened for
        binary writing, an io.BytesIO instance, or any other custom
        object that meets this interface.

        If *fix_imports* is True and *protocol* is less than 3, pickle
        will try to map the new Python 3 names to the old module names
        used in Python 2, so that the pickle data stream is readable
        with Python 2.

        If *buffer_callback* is None (the default), buffer views are
        serialized into *file* as part of the pickle stream.

        If *buffer_callback* is not None, then it can be called any number
        of times with a buffer view.  If the callback returns a false value
        (such as None), the given buffer is out-of-band; otherwise the
        buffer is serialized in-band, i.e. inside the pickle stream.

        It is an error if *buffer_callback* is not None and *protocol*
        is None or smaller than 5.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def clear_memo(self):
        '''Clears the pickler\'s "memo".

        The memo is the data structure that remembers which objects the
        pickler has already seen, so that shared or recursive objects
        are pickled by reference and not by value.  This method is
        useful when re-using picklers.
        '''
        self.memo.clear()

    
    def dump(self, obj):
        '''Write a pickled representation of obj to the open file.'''
        if not hasattr(self, '_file_write'):
            raise PicklingError(f'''Pickler.__init__() was not called by {self.__class__.__name__!s}.__init__()''')
        if self.proto >= 2:
            self.write(PROTO + pack('<B', self.proto))
        if self.proto >= 4:
            self.framer.start_framing()
        self.save(obj)
        self.write(STOP)
        self.framer.end_framing()

    
    def memoize(self, obj):
        '''Store an object in the memo.'''
        if self.fast:
            return None
    # WARNING: Decompyle incomplete

    
    def put(self, idx):
        if self.proto >= 4:
            return MEMOIZE
        if None.bin:
            if idx < 256:
                return BINPUT + pack('<B', idx)
            return None + pack('<I', idx)
        return None + repr(idx).encode('ascii') + b'\n'

    
    def get(self, i):
        if self.bin:
            if i < 256:
                return BINGET + pack('<B', i)
            return None + pack('<I', i)
        return None + repr(i).encode('ascii') + b'\n'

    
    def save(self, obj, save_persistent_id = (True,)):
        self.framer.commit_frame()
        pid = self.persistent_id(obj)
    # WARNING: Decompyle incomplete

    
    def persistent_id(self, obj):
        pass

    
    def save_pers(self, pid):
        if self.bin:
            self.save(pid, save_persistent_id = False)
            self.write(BINPERSID)
            return None
        
        try:
            self.write(PERSID + str(pid).encode('ascii') + b'\n')
            return None
        except UnicodeEncodeError:
            raise PicklingError('persistent IDs in protocol 0 must be ASCII strings')


    
    def save_reduce(self, func, args, state, listitems = None, dictitems = (None, None, None, None), state_setter = {
        'obj': None }, *, obj):
        if not isinstance(args, tuple):
            raise PicklingError('args from save_reduce() must be a tuple')
        if not callable(func):
            raise PicklingError('func from save_reduce() must be callable')
        save = self.save
        write = self.write
        func_name = getattr(func, '__name__', '')
    # WARNING: Decompyle incomplete

    dispatch = { }
    
    def save_none(self, obj):
        self.write(NONE)

    dispatch[type(None)] = save_none
    
    def save_bool(self, obj):
        if self.proto >= 2:
            self.write(NEWTRUE if obj else NEWFALSE)
            return None
        None.write(TRUE if obj else FALSE)

    dispatch[bool] = save_bool
    
    def save_long(self, obj):
        if self.bin:
            if obj >= 0:
                if obj <= 255:
                    self.write(BININT1 + pack('<B', obj))
                    return None
                if None <= 65535:
                    self.write(BININT2 + pack('<H', obj))
                    return None
                if  <= None, obj or None, obj <= 2147483647:
                    pass
                
            else:
                self.write(BININT + pack('<i', obj))
                return None
            if None.proto >= 2:
                len(encoded) = encode_long(obj)
                if n < 256:
                    self.write(LONG1 + pack('<B', n) + encoded)
                else:
                    self.write(LONG4 + pack('<i', n) + encoded)
                return None
            if  <= None, obj or None, obj <= 2147483647:
                pass
            
        else:
            self.write(INT + repr(obj).encode('ascii') + b'\n')
            return None
        None.write(LONG + repr(obj).encode('ascii') + b'L\n')

    dispatch[int] = save_long
    
    def save_float(self, obj):
        if self.bin:
            self.write(BINFLOAT + pack('>d', obj))
            return None
        None.write(FLOAT + repr(obj).encode('ascii') + b'\n')

    dispatch[float] = save_float
    
    def save_bytes(self, obj):
        if self.proto < 3:
            if not obj:
                self.save_reduce(bytes, (), obj = obj)
            else:
                self.save_reduce(codecs.encode, (str(obj, 'latin1'), 'latin1'), obj = obj)
            return None
        n = None(obj)
        if n <= 255:
            self.write(SHORT_BINBYTES + pack('<B', n) + obj)
        elif n > 0xFFFFFFFF and self.proto >= 4:
            self._write_large_bytes(BINBYTES8 + pack('<Q', n), obj)
        elif n >= self.framer._FRAME_SIZE_TARGET:
            self._write_large_bytes(BINBYTES + pack('<I', n), obj)
        else:
            self.write(BINBYTES + pack('<I', n) + obj)
        self.memoize(obj)

    dispatch[bytes] = save_bytes
    
    def save_bytearray(self, obj):
        if self.proto < 5:
            if not obj:
                self.save_reduce(bytearray, (), obj = obj)
            else:
                self.save_reduce(bytearray, (bytes(obj),), obj = obj)
            return None
        n = None(obj)
        if n >= self.framer._FRAME_SIZE_TARGET:
            self._write_large_bytes(BYTEARRAY8 + pack('<Q', n), obj)
        else:
            self.write(BYTEARRAY8 + pack('<Q', n) + obj)
        self.memoize(obj)

    dispatch[bytearray] = save_bytearray
    if _HAVE_PICKLE_BUFFER:
        
        def save_picklebuffer(self, obj):
            if self.proto < 5:
                raise PicklingError('PickleBuffer can only pickled with protocol >= 5')
            m = obj.raw()
            if not m.contiguous:
                raise PicklingError('PickleBuffer can not be pickled when pointing to a non-contiguous buffer')
            in_band = True
        # WARNING: Decompyle incomplete

        dispatch[PickleBuffer] = save_picklebuffer
    
    def save_str(self, obj):
        if self.bin:
            encoded = obj.encode('utf-8', 'surrogatepass')
            n = len(encoded)
            if n <= 255 and self.proto >= 4:
                self.write(SHORT_BINUNICODE + pack('<B', n) + encoded)
            elif n > 0xFFFFFFFF and self.proto >= 4:
                self._write_large_bytes(BINUNICODE8 + pack('<Q', n), encoded)
            elif n >= self.framer._FRAME_SIZE_TARGET:
                self._write_large_bytes(BINUNICODE + pack('<I', n), encoded)
            else:
                self.write(BINUNICODE + pack('<I', n) + encoded)
        else:
            tmp = obj.replace('\\', '\\u005c')
            tmp = tmp.replace('\x00', '\\u0000')
            tmp = tmp.replace('\n', '\\u000a')
            tmp = tmp.replace('\r', '\\u000d')
            tmp = tmp.replace('\x1a', '\\u001a')
            self.write(UNICODE + tmp.encode('raw-unicode-escape') + b'\n')
        self.memoize(obj)

    dispatch[str] = save_str
    
    def save_tuple(self, obj):
        if not obj:
            if self.bin:
                self.write(EMPTY_TUPLE)
            else:
                self.write(MARK + TUPLE)
            return None
        n = None(obj)
        save = self.save
        memo = self.memo
        if n <= 3 and self.proto >= 2:
            for element in obj:
                save(element)
                if id(obj) in memo:
                    get = self.get(memo[id(obj)][0])
                    self.write(POP * n + get)
                else:
                    self.write(_tuplesize2code[n])
                    self.memoize(obj)
            return None
        write = self.write
        write(MARK)
        for element in obj:
            save(element)
            if id(obj) in memo:
                get = self.get(memo[id(obj)][0])
                if self.bin:
                    write(POP_MARK + get)
                else:
                    write(POP * (n + 1) + get)
                return None
            write(TUPLE)
            self.memoize(obj)
            return None

    dispatch[tuple] = save_tuple
    
    def save_list(self, obj):
        if self.bin:
            self.write(EMPTY_LIST)
        else:
            self.write(MARK + LIST)
        self.memoize(obj)
        self._batch_appends(obj)

    dispatch[list] = save_list
    _BATCHSIZE = 1000
    
    def _batch_appends(self, items):
        save = self.save
        write = self.write
        if not self.bin:
            for x in items:
                save(x)
                write(APPEND)
                return None
                it = iter(items)
                tmp = list(islice(it, self._BATCHSIZE))
                n = len(tmp)
                if n > 1:
                    write(MARK)
                    for x in tmp:
                        save(x)
                        write(APPENDS)
        if n:
            save(tmp[0])
            write(APPEND)
        if n < self._BATCHSIZE:
            return None

    
    def save_dict(self, obj):
        if self.bin:
            self.write(EMPTY_DICT)
        else:
            self.write(MARK + DICT)
        self.memoize(obj)
        self._batch_setitems(obj.items())

    dispatch[dict] = save_dict
# WARNING: Decompyle incomplete


class _Unpickler:
    
    def __init__(self = None, file = {
        'fix_imports': True,
        'encoding': 'ASCII',
        'errors': 'strict',
        'buffers': None }, *, fix_imports, encoding, errors, buffers):
        """This takes a binary file for reading a pickle data stream.

        The protocol version of the pickle is detected automatically, so
        no proto argument is needed.

        The argument *file* must have two methods, a read() method that
        takes an integer argument, and a readline() method that requires
        no arguments.  Both methods should return bytes.  Thus *file*
        can be a binary file object opened for reading, an io.BytesIO
        object, or any other custom object that meets this interface.

        The file-like object must have two methods, a read() method
        that takes an integer argument, and a readline() method that
        requires no arguments.  Both methods should return bytes.
        Thus file-like object can be a binary file object opened for
        reading, a BytesIO object, or any other custom object that
        meets this interface.

        If *buffers* is not None, it should be an iterable of buffer-enabled
        objects that is consumed each time the pickle stream references
        an out-of-band buffer view.  Such buffers have been given in order
        to the *buffer_callback* of a Pickler object.

        If *buffers* is None (the default), then the buffers are taken
        from the pickle stream, assuming they are serialized there.
        It is an error for *buffers* to be None if the pickle stream
        was produced with a non-None *buffer_callback*.

        Other optional arguments are *fix_imports*, *encoding* and
        *errors*, which are used to control compatibility support for
        pickle stream generated by Python 2.  If *fix_imports* is True,
        pickle will try to map the old Python 2 names to the new names
        used in Python 3.  The *encoding* and *errors* tell pickle how
        to decode 8-bit string instances pickled by Python 2; these
        default to 'ASCII' and 'strict', respectively. *encoding* can be
        'bytes' to read these 8-bit string instances as bytes objects.
        """
        pass
    # WARNING: Decompyle incomplete

    
    def load(self):
        '''Read a pickled object representation from the open file.

        Return the reconstituted object hierarchy specified in the file.
        '''
        if not hasattr(self, '_file_read'):
            raise UnpicklingError(f'''Unpickler.__init__() was not called by {self.__class__.__name__!s}.__init__()''')
        self._unframer = _Unframer(self._file_read, self._file_readline)
        self.read = self._unframer.read
        self.readinto = self._unframer.readinto
        self.readline = self._unframer.readline
        self.metastack = []
        self.stack = []
        self.append = self.stack.append
        self.proto = 0
        read = self.read
        dispatch = self.dispatch
    # WARNING: Decompyle incomplete

    
    def pop_mark(self):
        items = self.stack
        self.stack = self.metastack.pop()
        self.append = self.stack.append
        return items

    
    def persistent_load(self, pid):
        raise UnpicklingError('unsupported persistent id encountered')

    dispatch = { }
    
    def load_proto(self):
        proto = self.read(1)[0]
        if not  <= 0, proto or 0, proto <= HIGHEST_PROTOCOL:
            pass
        
        raise ValueError('unsupported pickle protocol: %d' % proto)

    dispatch[PROTO[0]] = load_proto
    
    def load_frame(self):
        (frame_size,) = unpack('<Q', self.read(8))
        if frame_size > sys.maxsize:
            raise ValueError('frame size > sys.maxsize: %d' % frame_size)
        self._unframer.load_frame(frame_size)

    dispatch[FRAME[0]] = load_frame
    
    def load_persid(self):
        
        try:
            pid = self.readline()[:-1].decode('ascii')
        except UnicodeDecodeError:
            raise UnpicklingError('persistent IDs in protocol 0 must be ASCII strings')

        self.append(self.persistent_load(pid))

    dispatch[PERSID[0]] = load_persid
    
    def load_binpersid(self):
        pid = self.stack.pop()
        self.append(self.persistent_load(pid))

    dispatch[BINPERSID[0]] = load_binpersid
    
    def load_none(self):
        self.append(None)

    dispatch[NONE[0]] = load_none
    
    def load_false(self):
        self.append(False)

    dispatch[NEWFALSE[0]] = load_false
    
    def load_true(self):
        self.append(True)

    dispatch[NEWTRUE[0]] = load_true
    
    def load_int(self):
        data = self.readline()
        if data == FALSE[1:]:
            val = False
        elif data == TRUE[1:]:
            val = True
        else:
            val = int(data, 0)
        self.append(val)

    dispatch[INT[0]] = load_int
    
    def load_binint(self):
        self.append(unpack('<i', self.read(4))[0])

    dispatch[BININT[0]] = load_binint
    
    def load_binint1(self):
        self.append(self.read(1)[0])

    dispatch[BININT1[0]] = load_binint1
    
    def load_binint2(self):
        self.append(unpack('<H', self.read(2))[0])

    dispatch[BININT2[0]] = load_binint2
    
    def load_long(self):
        val = self.readline()[:-1]
        if val and val[-1] == 76:
            val = val[:-1]
        self.append(int(val, 0))

    dispatch[LONG[0]] = load_long
    
    def load_long1(self):
        n = self.read(1)[0]
        data = self.read(n)
        self.append(decode_long(data))

    dispatch[LONG1[0]] = load_long1
    
    def load_long4(self):
        (n,) = unpack('<i', self.read(4))
        if n < 0:
            raise UnpicklingError('LONG pickle has negative byte count')
        data = self.read(n)
        self.append(decode_long(data))

    dispatch[LONG4[0]] = load_long4
    
    def load_float(self):
        self.append(float(self.readline()[:-1]))

    dispatch[FLOAT[0]] = load_float
    
    def load_binfloat(self):
        self.append(unpack('>d', self.read(8))[0])

    dispatch[BINFLOAT[0]] = load_binfloat
    
    def _decode_string(self, value):
        if self.encoding == 'bytes':
            return value
        return None.decode(self.encoding, self.errors)

    
    def load_string(self):
        data = self.readline()[:-1]
        if len(data) >= 2 and data[0] == data[-1] and data[0] in b'"\'':
            data = data[1:-1]
        else:
            raise UnpicklingError('the STRING opcode argument must be quoted')
        self.append(self._decode_string(codecs.escape_decode(data)[0]))

    dispatch[STRING[0]] = load_string
    
    def load_binstring(self):
        (len,) = unpack('<i', self.read(4))
        if len < 0:
            raise UnpicklingError('BINSTRING pickle has negative byte count')
        data = self.read(len)
        self.append(self._decode_string(data))

    dispatch[BINSTRING[0]] = load_binstring
    
    def load_binbytes(self):
        (len,) = unpack('<I', self.read(4))
        if len > maxsize:
            raise UnpicklingError("BINBYTES exceeds system's maximum size of %d bytes" % maxsize)
        self.append(self.read(len))

    dispatch[BINBYTES[0]] = load_binbytes
    
    def load_unicode(self):
        self.append(str(self.readline()[:-1], 'raw-unicode-escape'))

    dispatch[UNICODE[0]] = load_unicode
    
    def load_binunicode(self):
        (len,) = unpack('<I', self.read(4))
        if len > maxsize:
            raise UnpicklingError("BINUNICODE exceeds system's maximum size of %d bytes" % maxsize)
        self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

    dispatch[BINUNICODE[0]] = load_binunicode
    
    def load_binunicode8(self):
        (len,) = unpack('<Q', self.read(8))
        if len > maxsize:
            raise UnpicklingError("BINUNICODE8 exceeds system's maximum size of %d bytes" % maxsize)
        self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

    dispatch[BINUNICODE8[0]] = load_binunicode8
    
    def load_binbytes8(self):
        (len,) = unpack('<Q', self.read(8))
        if len > maxsize:
            raise UnpicklingError("BINBYTES8 exceeds system's maximum size of %d bytes" % maxsize)
        self.append(self.read(len))

    dispatch[BINBYTES8[0]] = load_binbytes8
    
    def load_bytearray8(self):
        (len,) = unpack('<Q', self.read(8))
        if len > maxsize:
            raise UnpicklingError("BYTEARRAY8 exceeds system's maximum size of %d bytes" % maxsize)
        b = bytearray(len)
        self.readinto(b)
        self.append(b)

    dispatch[BYTEARRAY8[0]] = load_bytearray8
    
    def load_next_buffer(self):
        pass
    # WARNING: Decompyle incomplete

    dispatch[NEXT_BUFFER[0]] = load_next_buffer
    
    def load_readonly_buffer(self):
        buf = self.stack[-1]
        m = memoryview(buf)
        if not m.readonly:
            self.stack[-1] = m.toreadonly()
        None(None, None)
        return None
        with None:
            if not None:
                pass

    dispatch[READONLY_BUFFER[0]] = load_readonly_buffer
    
    def load_short_binstring(self):
        len = self.read(1)[0]
        data = self.read(len)
        self.append(self._decode_string(data))

    dispatch[SHORT_BINSTRING[0]] = load_short_binstring
    
    def load_short_binbytes(self):
        len = self.read(1)[0]
        self.append(self.read(len))

    dispatch[SHORT_BINBYTES[0]] = load_short_binbytes
    
    def load_short_binunicode(self):
        len = self.read(1)[0]
        self.append(str(self.read(len), 'utf-8', 'surrogatepass'))

    dispatch[SHORT_BINUNICODE[0]] = load_short_binunicode
    
    def load_tuple(self):
        items = self.pop_mark()
        self.append(tuple(items))

    dispatch[TUPLE[0]] = load_tuple
    
    def load_empty_tuple(self):
        self.append(())

    dispatch[EMPTY_TUPLE[0]] = load_empty_tuple
    
    def load_tuple1(self):
        self.stack[-1] = (self.stack[-1],)

    dispatch[TUPLE1[0]] = load_tuple1
    
    def load_tuple2(self):
        self.stack[-2:] = [
            (self.stack[-2], self.stack[-1])]

    dispatch[TUPLE2[0]] = load_tuple2
    
    def load_tuple3(self):
        self.stack[-3:] = [
            (self.stack[-3], self.stack[-2], self.stack[-1])]

    dispatch[TUPLE3[0]] = load_tuple3
    
    def load_empty_list(self):
        self.append([])

    dispatch[EMPTY_LIST[0]] = load_empty_list
    
    def load_empty_dictionary(self):
        self.append({ })

    dispatch[EMPTY_DICT[0]] = load_empty_dictionary
    
    def load_empty_set(self):
        self.append(set())

    dispatch[EMPTY_SET[0]] = load_empty_set
    
    def load_frozenset(self):
        items = self.pop_mark()
        self.append(frozenset(items))

    dispatch[FROZENSET[0]] = load_frozenset
    
    def load_list(self):
        items = self.pop_mark()
        self.append(items)

    dispatch[LIST[0]] = load_list
    
    def load_dict(self):
        pass
    # WARNING: Decompyle incomplete

    dispatch[DICT[0]] = load_dict
    
    def _instantiate(self, klass, args):
        pass
    # WARNING: Decompyle incomplete

    
    def load_inst(self):
        module = self.readline()[:-1].decode('ascii')
        name = self.readline()[:-1].decode('ascii')
        klass = self.find_class(module, name)
        self._instantiate(klass, self.pop_mark())

    dispatch[INST[0]] = load_inst
    
    def load_obj(self):
        args = self.pop_mark()
        cls = args.pop(0)
        self._instantiate(cls, args)

    dispatch[OBJ[0]] = load_obj
    
    def load_newobj(self):
        args = self.stack.pop()
        cls = self.stack.pop()
    # WARNING: Decompyle incomplete

    dispatch[NEWOBJ[0]] = load_newobj
    
    def load_newobj_ex(self):
        kwargs = self.stack.pop()
        args = self.stack.pop()
        cls = self.stack.pop()
    # WARNING: Decompyle incomplete

    dispatch[NEWOBJ_EX[0]] = load_newobj_ex
    
    def load_global(self):
        module = self.readline()[:-1].decode('utf-8')
        name = self.readline()[:-1].decode('utf-8')
        klass = self.find_class(module, name)
        self.append(klass)

    dispatch[GLOBAL[0]] = load_global
    
    def load_stack_global(self):
        name = self.stack.pop()
        module = self.stack.pop()
        if type(name) is not str or type(module) is not str:
            raise UnpicklingError('STACK_GLOBAL requires str')
        self.append(self.find_class(module, name))

    dispatch[STACK_GLOBAL[0]] = load_stack_global
    
    def load_ext1(self):
        code = self.read(1)[0]
        self.get_extension(code)

    dispatch[EXT1[0]] = load_ext1
    
    def load_ext2(self):
        (code,) = unpack('<H', self.read(2))
        self.get_extension(code)

    dispatch[EXT2[0]] = load_ext2
    
    def load_ext4(self):
        (code,) = unpack('<i', self.read(4))
        self.get_extension(code)

    dispatch[EXT4[0]] = load_ext4
    
    def get_extension(self, code):
        nil = []
        obj = _extension_cache.get(code, nil)
        if obj is not nil:
            self.append(obj)
            return None
        key = None.get(code)
        if not key:
            if code <= 0:
                raise UnpicklingError('EXT specifies code <= 0')
            raise ValueError('unregistered extension code %d' % code)
    # WARNING: Decompyle incomplete

    
    def find_class(self, module, name):
        sys.audit('pickle.find_class', module, name)
        if self.proto < 3 and self.fix_imports:
            if (module, name) in _compat_pickle.NAME_MAPPING:
                (module, name) = _compat_pickle.NAME_MAPPING[(module, name)]
            elif module in _compat_pickle.IMPORT_MAPPING:
                module = _compat_pickle.IMPORT_MAPPING[module]
        __import__(module, level = 0)
        if self.proto >= 4:
            return _getattribute(sys.modules[module], name)[0]
        return None(sys.modules[module], name)

    
    def load_reduce(self):
        stack = self.stack
        args = stack.pop()
        func = stack[-1]
    # WARNING: Decompyle incomplete

    dispatch[REDUCE[0]] = load_reduce
    
    def load_pop(self):
        if self.stack:
            del self.stack[-1]
            return None
        None.pop_mark()

    dispatch[POP[0]] = load_pop
    
    def load_pop_mark(self):
        self.pop_mark()

    dispatch[POP_MARK[0]] = load_pop_mark
    
    def load_dup(self):
        self.append(self.stack[-1])

    dispatch[DUP[0]] = load_dup
    
    def load_get(self):
        i = int(self.readline()[:-1])
        
        try:
            self.append(self.memo[i])
            return None
        except KeyError:
            msg = f'''Memo value not found at index {i}'''
            raise UnpicklingError(msg), None


    dispatch[GET[0]] = load_get
    
    def load_binget(self):
        i = self.read(1)[0]
        
        try:
            self.append(self.memo[i])
            return None
        except KeyError:
            exc = None
            msg = f'''Memo value not found at index {i}'''
            raise UnpicklingError(msg), None
            exc = None
            del exc


    dispatch[BINGET[0]] = load_binget
    
    def load_long_binget(self):
        (i,) = unpack('<I', self.read(4))
        
        try:
            self.append(self.memo[i])
            return None
        except KeyError:
            exc = None
            msg = f'''Memo value not found at index {i}'''
            raise UnpicklingError(msg), None
            exc = None
            del exc


    dispatch[LONG_BINGET[0]] = load_long_binget
    
    def load_put(self):
        i = int(self.readline()[:-1])
        if i < 0:
            raise ValueError('negative PUT argument')
        self.memo[i] = self.stack[-1]

    dispatch[PUT[0]] = load_put
    
    def load_binput(self):
        i = self.read(1)[0]
        if i < 0:
            raise ValueError('negative BINPUT argument')
        self.memo[i] = self.stack[-1]

    dispatch[BINPUT[0]] = load_binput
    
    def load_long_binput(self):
        (i,) = unpack('<I', self.read(4))
        if i > maxsize:
            raise ValueError('negative LONG_BINPUT argument')
        self.memo[i] = self.stack[-1]

    dispatch[LONG_BINPUT[0]] = load_long_binput
    
    def load_memoize(self):
        memo = self.memo
        memo[len(memo)] = self.stack[-1]

    dispatch[MEMOIZE[0]] = load_memoize
    
    def load_append(self):
        stack = self.stack
        value = stack.pop()
        list = stack[-1]
        list.append(value)

    dispatch[APPEND[0]] = load_append
    
    def load_appends(self):
        items = self.pop_mark()
        list_obj = self.stack[-1]
        
        try:
            extend = list_obj.extend
            extend(items)
            return None
        except AttributeError:
            pass

        append = list_obj.append
        for item in items:
            append(item)
            return None

    dispatch[APPENDS[0]] = load_appends
    
    def load_setitem(self):
        stack = self.stack
        value = stack.pop()
        key = stack.pop()
        dict = stack[-1]
        dict[key] = value

    dispatch[SETITEM[0]] = load_setitem
    
    def load_setitems(self):
        items = self.pop_mark()
        dict = self.stack[-1]
        for i in range(0, len(items), 2):
            dict[items[i]] = items[i + 1]
            return None

    dispatch[SETITEMS[0]] = load_setitems
    
    def load_additems(self):
        items = self.pop_mark()
        set_obj = self.stack[-1]
        if isinstance(set_obj, set):
            set_obj.update(items)
            return None
        add = None.add
        for item in items:
            add(item)
            return None

    dispatch[ADDITEMS[0]] = load_additems
    
    def load_build(self):
        stack = self.stack
        state = stack.pop()
        inst = stack[-1]
        setstate = getattr(inst, '__setstate__', None)
    # WARNING: Decompyle incomplete

    dispatch[BUILD[0]] = load_build
    
    def load_mark(self):
        self.metastack.append(self.stack)
        self.stack = []
        self.append = self.stack.append

    dispatch[MARK[0]] = load_mark
    
    def load_stop(self):
        value = self.stack.pop()
        raise _Stop(value)

    dispatch[STOP[0]] = load_stop


def _dump(obj = None, file = (None,), protocol = {
    'fix_imports': True,
    'buffer_callback': None }, *, fix_imports, buffer_callback):
    _Pickler(file, protocol, fix_imports = fix_imports, buffer_callback = buffer_callback).dump(obj)


def _dumps(obj = None, protocol = (None,), *, fix_imports, buffer_callback):
    f = io.BytesIO()
    _Pickler(f, protocol, fix_imports = fix_imports, buffer_callback = buffer_callback).dump(obj)
    res = f.getvalue()
# WARNING: Decompyle incomplete


def _load(file = None, *, fix_imports, encoding, errors, buffers):
    return _Unpickler(file, fix_imports = fix_imports, buffers = buffers, encoding = encoding, errors = errors).load()


def _loads(s = None, *, fix_imports, encoding, errors, buffers):
    if isinstance(s, str):
        raise TypeError("Can't load pickle from unicode string")
    file = io.BytesIO(s)
    return _Unpickler(file, fix_imports = fix_imports, buffers = buffers, encoding = encoding, errors = errors).load()


try:
    from _pickle import PickleError, PicklingError, UnpicklingError, Pickler, Unpickler, dump, dumps, load, loads
except ImportError:
    Pickler, Unpickler = _Pickler, _Unpickler
    (dump, dumps, load, loads) = (_dump, _dumps, _load, _loads)


def _test():
    import doctest
    return doctest.testmod()

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description = 'display contents of the pickle files')
    parser.add_argument('pickle_file', nargs = '*', help = 'the pickle file')
    parser.add_argument('-t', '--test', action = 'store_true', help = 'run self-test suite')
    parser.add_argument('-v', action = 'store_true', help = 'run verbosely; only affects self-test run')
    args = parser.parse_args()
    if args.test:
        _test()
        return None
    if not None.pickle_file:
        parser.print_help()
        return None
    import pprint
    for fn in args.pickle_file:
        if fn == '-':
            obj = load(sys.stdin.buffer)
        else:
            f = open(fn, 'rb')
            obj = load(f)
            None(None, None)
    with None:
        if not None:
            pass
    pprint.pprint(obj)
    continue
return None
