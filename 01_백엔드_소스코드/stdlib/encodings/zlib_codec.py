# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: zlib_codec.pyc (Python 3.11)

"""Python 'zlib_codec' Codec - zlib compression encoding.

This codec de/encodes from bytes to bytes.

Written by Marc-Andre Lemburg (mal@lemburg.com).
"""
import codecs
import zlib

def zlib_encode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


def zlib_decode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return zlib_encode(input, errors)

    
    def decode(self, input, errors = ('strict',)):
        return zlib_decode(input, errors)



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def __init__(self, errors = ('strict',)):
        pass
    # WARNING: Decompyle incomplete

    
    def encode(self, input, final = (False,)):
        if final:
            c = self.compressobj.compress(input)
            return c + self.compressobj.flush()
        return None.compressobj.compress(input)

    
    def reset(self):
        self.compressobj = zlib.compressobj()



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def __init__(self, errors = ('strict',)):
        pass
    # WARNING: Decompyle incomplete

    
    def decode(self, input, final = (False,)):
        if final:
            c = self.decompressobj.decompress(input)
            return c + self.decompressobj.flush()
        return None.decompressobj.decompress(input)

    
    def reset(self):
        self.decompressobj = zlib.decompressobj()



class StreamWriter(codecs.StreamWriter, Codec):
    charbuffertype = bytes


class StreamReader(codecs.StreamReader, Codec):
    charbuffertype = bytes


def getregentry():
    return codecs.CodecInfo(name = 'zlib', encode = zlib_encode, decode = zlib_decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter, _is_text_encoding = False)
