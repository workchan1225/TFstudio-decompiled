# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: quopri_codec.pyc (Python 3.11)

'''Codec for quoted-printable encoding.

This codec de/encodes from bytes to bytes.
'''
import codecs
import quopri
from io import BytesIO

def quopri_encode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


def quopri_decode(input, errors = ('strict',)):
    pass
# WARNING: Decompyle incomplete


class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return quopri_encode(input, errors)

    
    def decode(self, input, errors = ('strict',)):
        return quopri_decode(input, errors)



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        return quopri_encode(input, self.errors)[0]



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        return quopri_decode(input, self.errors)[0]



class StreamWriter(codecs.StreamWriter, Codec):
    charbuffertype = bytes


class StreamReader(codecs.StreamReader, Codec):
    charbuffertype = bytes


def getregentry():
    return codecs.CodecInfo(name = 'quopri', encode = quopri_encode, decode = quopri_decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamwriter = StreamWriter, streamreader = StreamReader, _is_text_encoding = False)
