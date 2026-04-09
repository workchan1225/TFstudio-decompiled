# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cp500.pyc (Python 3.11)

""" Python Character Mapping Codec cp500 generated from 'MAPPINGS/VENDORS/MICSFT/EBCDIC/CP500.TXT' with gencodec.py.

"""
import codecs

class Codec(codecs.Codec):
    
    def encode(self, input, errors = ('strict',)):
        return codecs.charmap_encode(input, errors, encoding_table)

    
    def decode(self, input, errors = ('strict',)):
        return codecs.charmap_decode(input, errors, decoding_table)



class IncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input, final = (False,)):
        return codecs.charmap_encode(input, self.errors, encoding_table)[0]



class IncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input, final = (False,)):
        return codecs.charmap_decode(input, self.errors, decoding_table)[0]



class StreamWriter(codecs.StreamWriter, Codec):
    pass


class StreamReader(codecs.StreamReader, Codec):
    pass


def getregentry():
    return codecs.CodecInfo(name = 'cp500', encode = Codec().encode, decode = Codec().decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter)

decoding_table = '\x00\x01\x02\x03\t\x7f\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x08\x18\x19\x1c\x1d\x1e\x1f\n\x17\x1b\x05\x06\x07\x16\x04\x14\x15\x1a  âäàáãåçñ[.<(+!&éêëèíîïìß]$*);^-/ÂÄÀÁÃÅÇÑ¦,%_>?øÉÊËÈÍÎÏÌ`:#@\'="Øabcdefghi«»ðýþ±°jklmnopqrªºæ¸Æ¤µ~stuvwxyz¡¿ÐÝÞ®¢£¥·©§¶¼½¾¬|¯¨´×{ABCDEFGHI­ôöòóõ}JKLMNOPQR¹ûüùúÿ\\÷STUVWXYZ²ÔÖÒÓÕ0123456789³ÛÜÙÚ'
encoding_table = codecs.charmap_build(decoding_table)
