# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: raw_unicode_escape.pyc (Python 3.11)

""" Python 'raw-unicode-escape' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs

class Codec(codecs.Codec):
    encode = codecs.raw_unicode_escape_encode
    decode = codecs.raw_unicode_escape_decode


class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        return codecs.raw_unicode_escape_encode(input, self.errors)[0]



class IncrementalDecoder(codecs.BufferedIncrementalDecoder):
    
    def _buffer_decode(self, input, errors, final):
        return codecs.raw_unicode_escape_decode(input, errors, final)



class StreamWriter(codecs.StreamWriter, Codec):
    pass


class StreamReader(codecs.StreamReader, Codec):
    
    def decode(self, input, errors = ('strict',)):
        return codecs.raw_unicode_escape_decode(input, errors, False)



def getregentry():
    return codecs.CodecInfo(name = 'raw-unicode-escape', encode = Codec.encode, decode = Codec.decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamwriter = StreamWriter, streamreader = StreamReader)
