# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cp855.pyc (Python 3.11)

__doc__ = " Python Character Mapping Codec generated from 'VENDORS/MICSFT/PC/CP855.TXT' with gencodec.py.\n\n"
import codecs

class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return codecs.charmap_encode(input, errors, encoding_map)

    
    def decode(self, input, errors = ('strict',)):
        return codecs.charmap_decode(input, errors, decoding_table)



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        return codecs.charmap_encode(input, self.errors, encoding_map)[0]



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]



class StreamWriter(codecs.StreamWriter, Codec):
    pass


class StreamReader(codecs.StreamReader, Codec):
    pass


def getregentry():
    return codecs.CodecInfo(name = 'cp855', encode = Codec().encode, decode = Codec().decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter)

decoding_map = codecs.make_identity_dict(range(256))
# WARNING: Decompyle incomplete
