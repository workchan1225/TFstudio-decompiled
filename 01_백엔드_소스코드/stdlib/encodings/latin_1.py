# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: latin_1.pyc (Python 3.11)

""" Python 'latin-1' Codec


Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs

class Codec(codecs.Codec):
    encode = codecs.latin_1_encode
    decode = codecs.latin_1_decode


class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        return codecs.latin_1_encode(input, self.errors)[0]



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        return codecs.latin_1_decode(input, self.errors)[0]



class StreamWriter(codecs.StreamWriter, Codec):
    pass


class StreamReader(codecs.StreamReader, Codec):
    pass


class StreamConverter(StreamReader, StreamWriter):
    encode = codecs.latin_1_decode
    decode = codecs.latin_1_encode


def getregentry():
    return codecs.CodecInfo(name = 'iso8859-1', encode = Codec.encode, decode = Codec.decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter)
