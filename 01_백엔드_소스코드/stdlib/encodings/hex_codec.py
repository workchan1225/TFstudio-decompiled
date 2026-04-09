# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: hex_codec.pyc (Python 3.11)

"""Python 'hex_codec' Codec - 2-digit hex content transfer encoding.

This codec de/encodes from bytes to bytes.

Written by Marc-Andre Lemburg (mal@lemburg.com).
"""
import codecs
import binascii

def hex_encode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


def hex_decode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return hex_encode(input, errors)

    
    def decode(self, input, errors = ('strict',)):
        return hex_decode(input, errors)



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        pass
    # WARNING: Decompyle incomplete



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        pass
    # WARNING: Decompyle incomplete



class StreamWriter(codecs.StreamWriter, Codec):
    charbuffertype = bytes


class StreamReader(codecs.StreamReader, Codec):
    charbuffertype = bytes


def getregentry():
    return codecs.CodecInfo(name = 'hex', encode = hex_encode, decode = hex_decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamwriter = StreamWriter, streamreader = StreamReader, _is_text_encoding = False)
