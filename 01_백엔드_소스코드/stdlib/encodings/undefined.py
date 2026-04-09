# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: undefined.pyc (Python 3.11)

""" Python 'undefined' Codec

    This codec will always raise a ValueError exception when being
    used. It is intended for use by the site.py file to switch off
    automatic string to Unicode coercion.

Written by Marc-Andre Lemburg (mal@lemburg.com).

(c) Copyright CNRI, All Rights Reserved. NO WARRANTY.

"""
import codecs

class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        raise UnicodeError('undefined encoding')

    
    def decode(self, input, errors = ('strict',)):
        raise UnicodeError('undefined encoding')



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        raise UnicodeError('undefined encoding')



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        raise UnicodeError('undefined encoding')



class StreamWriter(codecs.StreamWriter, Codec):
    pass


class StreamReader(codecs.StreamReader, Codec):
    pass


def getregentry():
    return codecs.CodecInfo(name = 'undefined', encode = Codec().encode, decode = Codec().decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamwriter = StreamWriter, streamreader = StreamReader)
