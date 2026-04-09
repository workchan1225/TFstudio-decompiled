# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: codecs.pyc (Python 3.11)

''' codecs -- Python Codec Registry, API and helpers.


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

'''
import builtins
import sys

try:
    from _codecs import *
except ImportError:
    why = None
    raise SystemError('Failed to load the builtin codecs: %s' % why)
    why = None
    del why

__all__ = [
    'register',
    'lookup',
    'open',
    'EncodedFile',
    'BOM',
    'BOM_BE',
    'BOM_LE',
    'BOM32_BE',
    'BOM32_LE',
    'BOM64_BE',
    'BOM64_LE',
    'BOM_UTF8',
    'BOM_UTF16',
    'BOM_UTF16_LE',
    'BOM_UTF16_BE',
    'BOM_UTF32',
    'BOM_UTF32_LE',
    'BOM_UTF32_BE',
    'CodecInfo',
    'Codec',
    'IncrementalEncoder',
    'IncrementalDecoder',
    'StreamReader',
    'StreamWriter',
    'StreamReaderWriter',
    'StreamRecoder',
    'getencoder',
    'getdecoder',
    'getincrementalencoder',
    'getincrementaldecoder',
    'getreader',
    'getwriter',
    'encode',
    'decode',
    'iterencode',
    'iterdecode',
    'strict_errors',
    'ignore_errors',
    'replace_errors',
    'xmlcharrefreplace_errors',
    'backslashreplace_errors',
    'namereplace_errors',
    'register_error',
    'lookup_error']
BOM_UTF8 = b'\xef\xbb\xbf'
BOM_LE = b'\xff\xfe'
BOM_UTF16_LE = b'\xff\xfe'
BOM_BE = b'\xfe\xff'
BOM_UTF16_BE = b'\xfe\xff'
BOM_UTF32_LE = b'\xff\xfe\x00\x00'
BOM_UTF32_BE = b'\x00\x00\xfe\xff'
if sys.byteorder == 'little':
    BOM = BOM_UTF16_LE
    BOM_UTF16 = BOM_UTF16_LE
    BOM_UTF32 = BOM_UTF32_LE
else:
    BOM = BOM_UTF16_BE
    BOM_UTF16 = BOM_UTF16_BE
    BOM_UTF32 = BOM_UTF32_BE
BOM32_LE = BOM_UTF16_LE
BOM32_BE = BOM_UTF16_BE
BOM64_LE = BOM_UTF32_LE
BOM64_BE = BOM_UTF32_BE

class CodecInfo(tuple):
    '''Codec details when looking up the codec registry'''
    _is_text_encoding = True
    
    def __new__(cls, encode, decode, streamreader, streamwriter, incrementalencoder = None, incrementaldecoder = (None, None, None, None, None), name = {
        '_is_text_encoding': None }, *, _is_text_encoding):
        self = tuple.__new__(cls, (encode, decode, streamreader, streamwriter))
        self.name = name
        self.encode = encode
        self.decode = decode
        self.incrementalencoder = incrementalencoder
        self.incrementaldecoder = incrementaldecoder
        self.streamwriter = streamwriter
        self.streamreader = streamreader
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<%s.%s object for encoding %s at %#x>' % (self.__class__.__module__, self.__class__.__qualname__, self.name, id(self))



class Codec:
    """ Defines the interface for stateless encoders/decoders.

        The .encode()/.decode() methods may use different error
        handling schemes by providing the errors argument. These
        string values are predefined:

         'strict' - raise a ValueError error (or a subclass)
         'ignore' - ignore the character and continue with the next
         'replace' - replace with a suitable replacement character;
                    Python will use the official U+FFFD REPLACEMENT
                    CHARACTER for the builtin Unicode codecs on
                    decoding and '?' on encoding.
         'surrogateescape' - replace with private code points U+DCnn.
         'xmlcharrefreplace' - Replace with the appropriate XML
                               character reference (only for encoding).
         'backslashreplace'  - Replace with backslashed escape sequences.
         'namereplace'       - Replace with \\N{...} escape sequences
                               (only for encoding).

        The set of allowed values can be extended via register_error.

    """
    
    def encode(self, input, errors = ('strict',)):
        """ Encodes the object input and returns a tuple (output
            object, length consumed).

            errors defines the error handling to apply. It defaults to
            'strict' handling.

            The method may not store state in the Codec instance. Use
            StreamWriter for codecs which have to keep state in order to
            make encoding efficient.

            The encoder must be able to handle zero length input and
            return an empty object of the output object type in this
            situation.

        """
        raise NotImplementedError

    
    def decode(self, input, errors = ('strict',)):
        """ Decodes the object input and returns a tuple (output
            object, length consumed).

            input must be an object which provides the bf_getreadbuf
            buffer slot. Python strings, buffer objects and memory
            mapped files are examples of objects providing this slot.

            errors defines the error handling to apply. It defaults to
            'strict' handling.

            The method may not store state in the Codec instance. Use
            StreamReader for codecs which have to keep state in order to
            make decoding efficient.

            The decoder must be able to handle zero length input and
            return an empty object of the output object type in this
            situation.

        """
        raise NotImplementedError



class IncrementalEncoder(object):
    '''
    An IncrementalEncoder encodes an input in multiple steps. The input can
    be passed piece by piece to the encode() method. The IncrementalEncoder
    remembers the state of the encoding process between calls to encode().
    '''
    
    def __init__(self, errors = ('strict',)):
        '''
        Creates an IncrementalEncoder instance.

        The IncrementalEncoder may use different error handling schemes by
        providing the errors keyword argument. See the module docstring
        for a list of possible values.
        '''
        self.errors = errors
        self.buffer = ''

    
    def encode(self, input, final = (False,)):
        '''
        Encodes input and returns the resulting object.
        '''
        raise NotImplementedError

    
    def reset(self):
        '''
        Resets the encoder to the initial state.
        '''
        pass

    
    def getstate(self):
        '''
        Return the current state of the encoder.
        '''
        return 0

    
    def setstate(self, state):
        '''
        Set the current state of the encoder. state must have been
        returned by getstate().
        '''
        pass



class BufferedIncrementalEncoder(IncrementalEncoder):
    '''
    This subclass of IncrementalEncoder can be used as the baseclass for an
    incremental encoder if the encoder must keep some of the output in a
    buffer between calls to encode().
    '''
    
    def __init__(self, errors = ('strict',)):
        IncrementalEncoder.__init__(self, errors)
        self.buffer = ''

    
    def _buffer_encode(self, input, errors, final):
        raise NotImplementedError

    
    def encode(self, input, final = (False,)):
        data = self.buffer + input
        (result, consumed) = self._buffer_encode(data, self.errors, final)
        self.buffer = data[consumed:]
        return result

    
    def reset(self):
        IncrementalEncoder.reset(self)
        self.buffer = ''

    
    def getstate(self):
