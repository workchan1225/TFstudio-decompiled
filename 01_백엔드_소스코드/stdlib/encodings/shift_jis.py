# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: shift_jis.pyc (Python 3.11)

import _codecs_jp
import codecs
import _multibytecodec as mbc
codec = _codecs_jp.getcodec('shift_jis')

class Codec(codecs.Codec):
    encode = codec.encode
    decode = codec.decode


class IncrementalEncoder(codecs.IncrementalEncoder, mbc.MultibyteIncrementalEncoder):
    codec = codec


class IncrementalDecoder(codecs.IncrementalDecoder, mbc.MultibyteIncrementalDecoder):
    codec = codec


class StreamReader(codecs.StreamReader, mbc.MultibyteStreamReader, Codec):
    codec = codec


class StreamWriter(codecs.StreamWriter, mbc.MultibyteStreamWriter, Codec):
    codec = codec


def getregentry():
    return codecs.CodecInfo(name = 'shift_jis', encode = Codec().encode, decode = Codec().decode, incrementalencoder = IncrementalEncoder, incrementaldecoder = IncrementalDecoder, streamreader = StreamReader, streamwriter = StreamWriter)
