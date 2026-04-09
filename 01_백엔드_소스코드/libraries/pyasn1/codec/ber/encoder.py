# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: encoder.pyc (Python 3.11)

import sys
import warnings
from pyasn1 import debug
from pyasn1 import error
from pyasn1.codec.ber import eoo
from pyasn1.compat import _MISSING
from pyasn1.compat.integer import to_bytes
from pyasn1.type import char
from pyasn1.type import tag
from pyasn1.type import univ
from pyasn1.type import useful
__all__ = [
    'Encoder',
    'encode']
LOG = debug.registerLoggee(__name__, flags = debug.DEBUG_ENCODER)

class AbstractItemEncoder(object):
    supportIndefLenMode = True
    eooIntegerSubstrate = (0, 0)
    eooOctetsSubstrate = bytes(eooIntegerSubstrate)
    
    def encodeTag(self, singleTag, isConstructed):
        (tagClass, tagFormat, tagId) = singleTag
        encodedTag = tagClass | tagFormat
        if isConstructed:
            encodedTag |= tag.tagFormatConstructed
        if tagId < 31:
            return (encodedTag | tagId,)
        substrate = (None & 127,)
        tagId >>= 7
    # WARNING: Decompyle incomplete

    
    def encodeLength(self, length, defMode):
        if defMode and self.supportIndefLenMode:
            return (128,)
        if None < 128:
            return (length,)
        substrate = None
    # WARNING: Decompyle incomplete

    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
        raise error.PyAsn1Error('Not implemented')

    
    def encode(self, value, asn1Spec, encodeFun = (None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class EndOfOctetsEncoder(AbstractItemEncoder):
    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
        return (b'', False, True)



class BooleanEncoder(AbstractItemEncoder):
    supportIndefLenMode = False
    
    def encodeValue(self, value, asn1Spec, encodeFun, **options):
