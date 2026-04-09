# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decoder.pyc (Python 3.11)

import warnings
from pyasn1.codec.cer import decoder
from pyasn1.type import univ
__all__ = [
    'decode',
    'StreamingDecoder']

class BitStringPayloadDecoder(decoder.BitStringPayloadDecoder):
    supportConstructedForm = False


class OctetStringPayloadDecoder(decoder.OctetStringPayloadDecoder):
    supportConstructedForm = False

RealPayloadDecoder = decoder.RealPayloadDecoder
TAG_MAP = decoder.TAG_MAP.copy()
TAG_MAP.update({
    univ.Real.tagSet: RealPayloadDecoder(),
    univ.OctetString.tagSet: OctetStringPayloadDecoder(),
    univ.BitString.tagSet: BitStringPayloadDecoder() })
TYPE_MAP = decoder.TYPE_MAP.copy()
# WARNING: Decompyle incomplete
