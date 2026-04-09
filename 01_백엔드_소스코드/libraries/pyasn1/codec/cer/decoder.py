# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decoder.pyc (Python 3.11)

import warnings
from pyasn1 import error
from pyasn1.codec.streaming import readFromStream
from pyasn1.codec.ber import decoder
from pyasn1.type import univ
__all__ = [
    'decode',
    'StreamingDecoder']
SubstrateUnderrunError = error.SubstrateUnderrunError

class BooleanPayloadDecoder(decoder.AbstractSimplePayloadDecoder):
    protoComponent = univ.Boolean(0)
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete


BitStringPayloadDecoder = decoder.BitStringPayloadDecoder
OctetStringPayloadDecoder = decoder.OctetStringPayloadDecoder
RealPayloadDecoder = decoder.RealPayloadDecoder
TAG_MAP = decoder.TAG_MAP.copy()
TAG_MAP.update({
    univ.Real.tagSet: RealPayloadDecoder(),
    univ.OctetString.tagSet: OctetStringPayloadDecoder(),
    univ.BitString.tagSet: BitStringPayloadDecoder(),
    univ.Boolean.tagSet: BooleanPayloadDecoder() })
TYPE_MAP = decoder.TYPE_MAP.copy()
# WARNING: Decompyle incomplete
