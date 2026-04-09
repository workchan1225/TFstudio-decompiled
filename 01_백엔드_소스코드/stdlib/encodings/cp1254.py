# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: cp1254.pyc (Python 3.11)

""" Python Character Mapping Codec cp1254 generated from 'MAPPINGS/VENDORS/MICSFT/WINDOWS/CP1254.TXT' with gencodec.py.

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
    return codecs.CodecInfo(name = 'cp1254', encode = Codec().encode, decode = Codec().decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter)

decoding_table = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~\x7f€￾‚ƒ„…†‡ˆ‰Š‹Œ￾￾￾￾‘’“”•–—˜™š›œ￾￾Ÿ ¡¢£¤¥¦§¨©ª«¬­®¯°±²³´µ¶·¸¹º»¼½¾¿ÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏĞÑÒÓÔÕÖ×ØÙÚÛÜİŞßàáâãäåæçèéêëìíîïğñòóôõö÷øùúûüışÿ'
encoding_table = codecs.charmap_build(decoding_table)
