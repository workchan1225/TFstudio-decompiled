# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: utf_32.pyc (Python 3.11)

"""
Python 'utf-32' Codec
"""
import codecs
import sys
encode = codecs.utf_32_encode

def decode(input, errors = ('strict',)):
    return codecs.utf_32_decode(input, errors, True)


class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def __init__(self, errors = ('strict',)):
        codecs.IncrementalEncoder.__init__(self, errors)
        self.encoder = None

    
    def encode(self, input, final = (False,)):
        pass
    # WARNING: Decompyle incomplete

    
    def reset(self):
        codecs.IncrementalEncoder.reset(self)
        self.encoder = None

    
    def getstate(self):
        pass
    # WARNING: Decompyle incomplete

    
    def setstate(self, state):
        if state:
            self.encoder = None
            return None
        if None.byteorder == 'little':
            self.encoder = codecs.utf_32_le_encode
            return None
        self.encoder = None.utf_32_be_encode



class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    
    def __init__(self, errors = ('strict',)):
        codecs.BufferedIncrementalDecoder.__init__(self, errors)
        self.decoder = None

    
    def _buffer_decode(self, input, errors, final):
        pass
    # WARNING: Decompyle incomplete

    
    def reset(self):
        codecs.BufferedIncrementalDecoder.reset(self)
        self.decoder = None

    
    def getstate(self):
        state = codecs.BufferedIncrementalDecoder.getstate(self)[0]
    # WARNING: Decompyle incomplete

    
    def setstate(self, state):
        codecs.BufferedIncrementalDecoder.setstate(self, state)
        state = state[1]
        if state == 0:
            self.decoder = codecs.utf_32_be_decode if sys.byteorder == 'big' else codecs.utf_32_le_decode
            return None
        if None == 1:
            self.decoder = codecs.utf_32_le_decode if sys.byteorder == 'big' else codecs.utf_32_be_decode
            return None
        self.decoder = None



class StreamWriter(codecs.StreamWriter):
    
    def __init__(self, stream, errors = ('strict',)):
        self.encoder = None
        codecs.StreamWriter.__init__(self, stream, errors)

    
    def reset(self):
        codecs.StreamWriter.reset(self)
        self.encoder = None

    
    def encode(self, input, errors = ('strict',)):
        pass
    # WARNING: Decompyle incomplete



class StreamReader(codecs.StreamReader):
    
    def reset(self):
        codecs.StreamReader.reset(self)
        
        try:
            del self.decode
            return None
        except AttributeError:
            return None


    
    def decode(self, input, errors = ('strict',)):
        (object, consumed, byteorder) = codecs.utf_32_ex_decode(input, errors, 0, False)
        if byteorder == -1:
            self.decode = codecs.utf_32_le_decode
        elif byteorder == 1:
            self.decode = codecs.utf_32_be_decode
        elif consumed >= 4:
            raise UnicodeError('UTF-32 stream does not start with BOM')
        return (object, consumed)



def getregentry():
    return codecs.CodecInfo(name = 'utf-32', encode = encode, decode = decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter)
