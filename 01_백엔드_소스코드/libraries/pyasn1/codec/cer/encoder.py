# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: encoder.pyc (Python 3.11)

import warnings
from pyasn1 import error
from pyasn1.codec.ber import encoder
from pyasn1.type import univ
from pyasn1.type import useful
__all__ = [
    'Encoder',
    'encode']

class BooleanEncoder(encoder.IntegerEncoder):
    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
        if value == 0:
            substrate = (0,)
        else:
            substrate = (255,)
        return (substrate, False, False)



class RealEncoder(encoder.RealEncoder):
    
    def _chooseEncBase(self, value):
        (m, b, e) = value
        return self._dropFloatingPoint(m, b, e)



class TimeEncoderMixIn(object):
    Z_CHAR = ord('Z')
    PLUS_CHAR = ord('+')
    MINUS_CHAR = ord('-')
    COMMA_CHAR = ord(',')
    DOT_CHAR = ord('.')
    ZERO_CHAR = ord('0')
    MIN_LENGTH = 12
    MAX_LENGTH = 19
    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
        pass
    # WARNING: Decompyle incomplete



class GeneralizedTimeEncoder(encoder.OctetStringEncoder, TimeEncoderMixIn):
    MIN_LENGTH = 12
    MAX_LENGTH = 20


class UTCTimeEncoder(encoder.OctetStringEncoder, TimeEncoderMixIn):
    MIN_LENGTH = 10
    MAX_LENGTH = 14


class SetOfEncoder(encoder.SequenceOfEncoder):
    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
        pass
    # WARNING: Decompyle incomplete



class SequenceOfEncoder(encoder.SequenceOfEncoder):
    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
        if not options.get('ifNotEmpty', False) and len(value):
            return (b'', True, True)
    # WARNING: Decompyle incomplete



class SetEncoder(encoder.SequenceEncoder):
    _componentSortKey = (lambda componentAndType: (component, asn1Spec) = componentAndType# WARNING: Decompyle incomplete
)()
    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
        substrate = b''
        comps = []
        compsMap = { }
    # WARNING: Decompyle incomplete



class SequenceEncoder(encoder.SequenceEncoder):
    omitEmptyOptionals = True

TAG_MAP = encoder.TAG_MAP.copy()
TAG_MAP.update({
    univ.Sequence.typeId: SequenceEncoder(),
    univ.SetOf.tagSet: SetOfEncoder(),
    useful.UTCTime.tagSet: UTCTimeEncoder(),
    useful.GeneralizedTime.tagSet: GeneralizedTimeEncoder(),
    univ.Real.tagSet: RealEncoder(),
    univ.Boolean.tagSet: BooleanEncoder() })
TYPE_MAP = encoder.TYPE_MAP.copy()
TYPE_MAP.update({
    univ.SequenceOf.typeId: SequenceOfEncoder(),
    univ.Sequence.typeId: SequenceEncoder(),
    univ.SetOf.typeId: SetOfEncoder(),
    univ.Set.typeId: SetEncoder(),
    useful.UTCTime.typeId: UTCTimeEncoder(),
    useful.GeneralizedTime.typeId: GeneralizedTimeEncoder(),
    univ.Real.typeId: RealEncoder(),
    univ.Boolean.typeId: BooleanEncoder() })

class SingleItemEncoder(encoder.SingleItemEncoder):
    fixedDefLengthMode = False
    fixedChunkSize = 1000
    TAG_MAP = TAG_MAP
    TYPE_MAP = TYPE_MAP


class Encoder(encoder.Encoder):
    SINGLE_ITEM_ENCODER = SingleItemEncoder

encode = Encoder()

def __getattr__(attr = None):
    newAttr = {
        'tagMap': 'TAG_MAP',
        'typeMap': 'TYPE_MAP' }.get(attr)
    if {
        'tagMap': 'TAG_MAP',
        'typeMap': 'TYPE_MAP' }.get(attr):
        warnings.warn(f'''{attr} is deprecated. Please use {newAttr} instead.''', DeprecationWarning)
        return globals()[newAttr]
    raise None(attr)
