# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rot_13.pyc (Python 3.11)

__doc__ = ' Python Character Mapping Codec for ROT13.\n\nThis codec de/encodes from str to str.\n\nWritten by Marc-Andre Lemburg (mal@lemburg.com).\n'
import codecs

class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return (str.translate(input, rot13_map), len(input))

    
    def decode(self, input, errors = ('strict',)):
        return (str.translate(input, rot13_map), len(input))



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        return str.translate(input, rot13_map)



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        return str.translate(input, rot13_map)



class StreamWriter(codecs.StreamWriter, Codec):
    pass


class StreamReader(codecs.StreamReader, Codec):
    pass


def getregentry():
    return codecs.CodecInfo(name = 'rot-13', encode = Codec().encode, decode = Codec().decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamwriter = StreamWriter, streamreader = StreamReader, _is_text_encoding = False)

rot13_map = codecs.make_identity_dict(range(256))
# WARNING: Decompyle incomplete
