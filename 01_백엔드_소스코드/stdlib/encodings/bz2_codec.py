# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: bz2_codec.pyc (Python 3.11)

"""Python 'bz2_codec' Codec - bz2 compression encoding.

This codec de/encodes from bytes to bytes and is therefore usable with
bytes.transform() and bytes.untransform().

Adapted by Raymond Hettinger from zlib_codec.py which was written
by Marc-Andre Lemburg (mal@lemburg.com).
"""
import codecs
import bz2

def bz2_encode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


def bz2_decode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return bz2_encode(input, errors)

    
    def decode(self, input, errors = ('strict',)):
        return bz2_decode(input, errors)



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
        self.compressobj = bz2.BZ2Compressor()



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def __init__(self, errors = ('strict',)):
        pass
    # WARNING: Decompyle incomplete

    
    def decode(self, input, final = (False,)):
        
        try:
            return self.decompressobj.decompress(input)
        except EOFError:
            return ''


    
    def reset(self):
        self.decompressobj = bz2.BZ2Decompressor()



class StreamWriter(codecs.StreamWriter, Codec):
    charbuffertype = bytes


class StreamReader(codecs.StreamReader, Codec):
    charbuffertype = bytes


def getregentry():
    return codecs.CodecInfo(name = 'bz2', encode = bz2_encode, decode = bz2_decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamwriter = StreamWriter, streamreader = StreamReader, _is_text_encoding = False)
