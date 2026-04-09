# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: decoder.pyc (Python 3.11)

import io
import os
import sys
import warnings
from pyasn1 import debug
from pyasn1 import error
from pyasn1.codec.ber import eoo
from pyasn1.codec.streaming import asSeekableStream
from pyasn1.codec.streaming import isEndOfStream
from pyasn1.codec.streaming import peekIntoStream
from pyasn1.codec.streaming import readFromStream
from pyasn1.compat import _MISSING
from pyasn1.error import PyAsn1Error
from pyasn1.type import base
from pyasn1.type import char
from pyasn1.type import tag
from pyasn1.type import tagmap
from pyasn1.type import univ
from pyasn1.type import useful
__all__ = [
    'StreamingDecoder',
    'Decoder',
    'decode']
LOG = debug.registerLoggee(__name__, flags = debug.DEBUG_DECODER)
noValue = base.noValue
SubstrateUnderrunError = error.SubstrateUnderrunError

class AbstractPayloadDecoder(object):
    protoComponent = None
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        '''Decode value with fixed byte length.

        The decoder is allowed to consume as many bytes as necessary.
        '''
        raise error.PyAsn1Error(f'''SingleItemDecoder not implemented for {tagSet!s}''')

    
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        '''Decode value with undefined length.

        The decoder is allowed to consume as many bytes as necessary.
        '''
        raise error.PyAsn1Error(f'''Indefinite length mode decoder not implemented for {tagSet!s}''')

    _passAsn1Object = (lambda asn1Object, options: if 'asn1Object' not in options:
options['asn1Object'] = asn1Objectoptions)()


class AbstractSimplePayloadDecoder(AbstractPayloadDecoder):
    substrateCollector = (lambda asn1Object, substrate, length, options: pass# WARNING: Decompyle incomplete
)()
    
    def _createComponent(self, asn1Spec, tagSet, value, **options):
        if options.get('native'):
            return value
    # WARNING: Decompyle incomplete



class RawPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.Any('')
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete


rawPayloadDecoder = RawPayloadDecoder()

class IntegerPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.Integer(0)
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class BooleanPayloadDecoder(IntegerPayloadDecoder):
    protoComponent = univ.Boolean(0)
    
    def _createComponent(self, asn1Spec, tagSet, value, **options):
        pass
    # WARNING: Decompyle incomplete



class BitStringPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.BitString(())
    supportConstructedForm = True
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class OctetStringPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.OctetString('')
    supportConstructedForm = True
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class NullPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.Null('')
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class ObjectIdentifierPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.ObjectIdentifier(())
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class RelativeOIDPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.RelativeOID(())
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class RealPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.Real()
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class AbstractConstructedPayloadDecoder(AbstractPayloadDecoder):
    protoComponent = None


class ConstructedPayloadDecoderBase(AbstractConstructedPayloadDecoder):
    protoRecordComponent = None
    protoSequenceComponent = None
    
    def _getComponentTagMap(self, asn1Object, idx):
        raise NotImplementedError

    
    def _getComponentPositionByType(self, asn1Object, tagSet, idx):
        raise NotImplementedError

    
    def _decodeComponentsSchemaless(self, substrate, tagSet, decodeFun, length = (None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class SequenceOrSequenceOfPayloadDecoder(ConstructedPayloadDecoderBase):
    protoRecordComponent = univ.Sequence()
    protoSequenceComponent = univ.SequenceOf()


class SequencePayloadDecoder(SequenceOrSequenceOfPayloadDecoder):
    protoComponent = univ.Sequence()


class SequenceOfPayloadDecoder(SequenceOrSequenceOfPayloadDecoder):
    protoComponent = univ.SequenceOf()


class SetOrSetOfPayloadDecoder(ConstructedPayloadDecoderBase):
    protoRecordComponent = univ.Set()
    protoSequenceComponent = univ.SetOf()


class SetPayloadDecoder(SetOrSetOfPayloadDecoder):
    protoComponent = univ.Set()


class SetOfPayloadDecoder(SetOrSetOfPayloadDecoder):
    protoComponent = univ.SetOf()


class ChoicePayloadDecoder(ConstructedPayloadDecoderBase):
    protoComponent = univ.Choice()
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class AnyPayloadDecoder(AbstractSimplePayloadDecoder):
    protoComponent = univ.Any()
    
    def valueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete

    
    def indefLenValueDecoder(self, substrate, asn1Spec, tagSet, length, state, decodeFun, substrateFun = (None, None, None, None, None), **options):
        pass
    # WARNING: Decompyle incomplete



class UTF8StringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.UTF8String()


class NumericStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.NumericString()


class PrintableStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.PrintableString()


class TeletexStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.TeletexString()


class VideotexStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.VideotexString()


class IA5StringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.IA5String()


class GraphicStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.GraphicString()


class VisibleStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.VisibleString()


class GeneralStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.GeneralString()


class UniversalStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.UniversalString()


class BMPStringPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = char.BMPString()


class ObjectDescriptorPayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = useful.ObjectDescriptor()


class GeneralizedTimePayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = useful.GeneralizedTime()


class UTCTimePayloadDecoder(OctetStringPayloadDecoder):
    protoComponent = useful.UTCTime()

# WARNING: Decompyle incomplete
