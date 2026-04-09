# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: uu_codec.pyc (Python 3.11)

"""Python 'uu_codec' Codec - UU content transfer encoding.

This codec de/encodes from bytes to bytes.

Written by Marc-Andre Lemburg (mal@lemburg.com). Some details were
adapted from uu.py which was written by Lance Ellinghouse and
modified by Jack Jansen and Fredrik Lundh.
"""
import codecs
import binascii
from io import BytesIO

def uu_encode(input, errors, filename, mode = ('strict', '<data>', 438)):
    pass
# WARNING: Decompyle incomplete


def uu_decode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return uu_encode(input, errors)

    
    def decode(self, input, errors = ('strict',)):
        return uu_decode(input, errors)



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        return uu_encode(input, self.errors)[0]



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        return uu_decode(input, self.errors)[0]



class StreamWriter(codecs.StreamWriter, Codec):
    charbuffertype = bytes


class StreamReader(codecs.StreamReader, Codec):
    charbuffertype = bytes


def getregentry():
    return codecs.CodecInfo(name = 'uu', encode = uu_encode, decode = uu_decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter, _is_text_encoding = False)
