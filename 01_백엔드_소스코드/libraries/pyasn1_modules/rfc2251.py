# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rfc2251.pyc (Python 3.11)

from pyasn1.type import constraint
from pyasn1.type import namedtype
from pyasn1.type import namedval
from pyasn1.type import tag
from pyasn1.type import univ
maxInt = univ.Integer(2147483647)

class LDAPString(univ.OctetString):
    pass


class LDAPOID(univ.OctetString):
    pass


class LDAPDN(LDAPString):
    pass


class RelativeLDAPDN(LDAPString):
    pass


class AttributeType(LDAPString):
    pass


class AttributeDescription(LDAPString):
    pass


class AttributeDescriptionList(univ.SequenceOf):
    componentType = AttributeDescription()


class AttributeValue(univ.OctetString):
    pass


class AssertionValue(univ.OctetString):
    pass


class AttributeValueAssertion(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('attributeDesc', AttributeDescription()), namedtype.NamedType('assertionValue', AssertionValue()))


class Attribute(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('type', AttributeDescription()), namedtype.NamedType('vals', univ.SetOf(componentType = AttributeValue())))


class MatchingRuleId(LDAPString):
    pass


class Control(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('controlType', LDAPOID()), namedtype.DefaultedNamedType('criticality', univ.Boolean('False')), namedtype.OptionalNamedType('controlValue', univ.OctetString()))


class Controls(univ.SequenceOf):
    componentType = Control()


class LDAPURL(LDAPString):
    pass


class Referral(univ.SequenceOf):
    componentType = LDAPURL()


class SaslCredentials(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('mechanism', LDAPString()), namedtype.OptionalNamedType('credentials', univ.OctetString()))


class AuthenticationChoice(univ.Choice):
    componentType = namedtype.NamedTypes(namedtype.NamedType('simple', univ.OctetString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))), namedtype.NamedType('reserved-1', univ.OctetString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))), namedtype.NamedType('reserved-2', univ.OctetString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))), namedtype.NamedType('sasl', SaslCredentials().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))))


class BindRequest(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 0))
    componentType = namedtype.NamedTypes(namedtype.NamedType('version', univ.Integer().subtype(subtypeSpec = constraint.ValueRangeConstraint(1, 127))), namedtype.NamedType('name', LDAPDN()), namedtype.NamedType('authentication', AuthenticationChoice()))


class PartialAttributeList(univ.SequenceOf):
    componentType = univ.Sequence(componentType = namedtype.NamedTypes(namedtype.NamedType('type', AttributeDescription()), namedtype.NamedType('vals', univ.SetOf(componentType = AttributeValue()))))


class SearchResultEntry(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 4))
    componentType = namedtype.NamedTypes(namedtype.NamedType('objectName', LDAPDN()), namedtype.NamedType('attributes', PartialAttributeList()))


class MatchingRuleAssertion(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.OptionalNamedType('matchingRule', MatchingRuleId().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))), namedtype.OptionalNamedType('type', AttributeDescription().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))), namedtype.NamedType('matchValue', AssertionValue().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))), namedtype.DefaultedNamedType('dnAttributes', univ.Boolean('False').subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4))))


class SubstringFilter(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('type', AttributeDescription()), namedtype.NamedType('substrings', univ.SequenceOf(componentType = univ.Choice(componentType = namedtype.NamedTypes(namedtype.NamedType('initial', LDAPString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))), namedtype.NamedType('any', LDAPString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))), namedtype.NamedType('final', LDAPString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))))))))


class Filter3(univ.Choice):
    componentType = namedtype.NamedTypes(namedtype.NamedType('equalityMatch', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))), namedtype.NamedType('substrings', SubstringFilter().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))), namedtype.NamedType('greaterOrEqual', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))), namedtype.NamedType('lessOrEqual', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))), namedtype.NamedType('present', AttributeDescription().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))), namedtype.NamedType('approxMatch', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))), namedtype.NamedType('extensibleMatch', MatchingRuleAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))))


class Filter2(univ.Choice):
    componentType = namedtype.NamedTypes(namedtype.NamedType('and', univ.SetOf(componentType = Filter3()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))), namedtype.NamedType('or', univ.SetOf(componentType = Filter3()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))), namedtype.NamedType('not', Filter3().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))), namedtype.NamedType('equalityMatch', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))), namedtype.NamedType('substrings', SubstringFilter().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))), namedtype.NamedType('greaterOrEqual', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))), namedtype.NamedType('lessOrEqual', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))), namedtype.NamedType('present', AttributeDescription().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))), namedtype.NamedType('approxMatch', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))), namedtype.NamedType('extensibleMatch', MatchingRuleAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))))


class Filter(univ.Choice):
    componentType = namedtype.NamedTypes(namedtype.NamedType('and', univ.SetOf(componentType = Filter2()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))), namedtype.NamedType('or', univ.SetOf(componentType = Filter2()).subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 1))), namedtype.NamedType('not', Filter2().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))), namedtype.NamedType('equalityMatch', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))), namedtype.NamedType('substrings', SubstringFilter().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))), namedtype.NamedType('greaterOrEqual', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))), namedtype.NamedType('lessOrEqual', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))), namedtype.NamedType('present', AttributeDescription().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))), namedtype.NamedType('approxMatch', AttributeValueAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))), namedtype.NamedType('extensibleMatch', MatchingRuleAssertion().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9))))


class SearchRequest(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 3))
    componentType = namedtype.NamedTypes(namedtype.NamedType('baseObject', LDAPDN()), namedtype.NamedType('scope', univ.Enumerated(namedValues = namedval.NamedValues(('baseObject', 0), ('singleLevel', 1), ('wholeSubtree', 2)))), namedtype.NamedType('derefAliases', univ.Enumerated(namedValues = namedval.NamedValues(('neverDerefAliases', 0), ('derefInSearching', 1), ('derefFindingBaseObj', 2), ('derefAlways', 3)))), namedtype.NamedType('sizeLimit', univ.Integer().subtype(subtypeSpec = constraint.ValueRangeConstraint(0, maxInt))), namedtype.NamedType('timeLimit', univ.Integer().subtype(subtypeSpec = constraint.ValueRangeConstraint(0, maxInt))), namedtype.NamedType('typesOnly', univ.Boolean()), namedtype.NamedType('filter', Filter()), namedtype.NamedType('attributes', AttributeDescriptionList()))


class UnbindRequest(univ.Null):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 2))


class BindResponse(univ.Sequence):
    __module__ = __name__
    __qualname__ = 'BindResponse'
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 1))
# WARNING: Decompyle incomplete


class LDAPResult(univ.Sequence):
    __module__ = __name__
    __qualname__ = 'LDAPResult'
# WARNING: Decompyle incomplete


class SearchResultReference(univ.SequenceOf):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 19))
    componentType = LDAPURL()


class SearchResultDone(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 5))


class AttributeTypeAndValues(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('type', AttributeDescription()), namedtype.NamedType('vals', univ.SetOf(componentType = AttributeValue())))


class ModifyRequest(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 6))
    componentType = namedtype.NamedTypes(namedtype.NamedType('object', LDAPDN()), namedtype.NamedType('modification', univ.SequenceOf(componentType = univ.Sequence(componentType = namedtype.NamedTypes(namedtype.NamedType('operation', univ.Enumerated(namedValues = namedval.NamedValues(('add', 0), ('delete', 1), ('replace', 2)))), namedtype.NamedType('modification', AttributeTypeAndValues()))))))


class ModifyResponse(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 7))


class AttributeList(univ.SequenceOf):
    componentType = univ.Sequence(componentType = namedtype.NamedTypes(namedtype.NamedType('type', AttributeDescription()), namedtype.NamedType('vals', univ.SetOf(componentType = AttributeValue()))))


class AddRequest(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 8))
    componentType = namedtype.NamedTypes(namedtype.NamedType('entry', LDAPDN()), namedtype.NamedType('attributes', AttributeList()))


class AddResponse(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 9))


class DelRequest(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 10))


class DelResponse(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 11))


class ModifyDNRequest(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 12))
    componentType = namedtype.NamedTypes(namedtype.NamedType('entry', LDAPDN()), namedtype.NamedType('newrdn', RelativeLDAPDN()), namedtype.NamedType('deleteoldrdn', univ.Boolean()), namedtype.OptionalNamedType('newSuperior', LDAPDN().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))))


class ModifyDNResponse(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 13))


class CompareRequest(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 14))
    componentType = namedtype.NamedTypes(namedtype.NamedType('entry', LDAPDN()), namedtype.NamedType('ava', AttributeValueAssertion()))


class CompareResponse(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 15))


class AbandonRequest(LDAPResult):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 16))


class ExtendedRequest(univ.Sequence):
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 23))
    componentType = namedtype.NamedTypes(namedtype.NamedType('requestName', LDAPOID().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))), namedtype.OptionalNamedType('requestValue', univ.OctetString().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))))


class ExtendedResponse(univ.Sequence):
    __module__ = __name__
    __qualname__ = 'ExtendedResponse'
    tagSet = univ.Sequence.tagSet.tagImplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 24))
# WARNING: Decompyle incomplete


class MessageID(univ.Integer):
    subtypeSpec = univ.Integer.subtypeSpec + constraint.ValueRangeConstraint(0, maxInt)


class LDAPMessage(univ.Sequence):
    componentType = namedtype.NamedTypes(namedtype.NamedType('messageID', MessageID()), namedtype.NamedType('protocolOp', univ.Choice(componentType = namedtype.NamedTypes(namedtype.NamedType('bindRequest', BindRequest()), namedtype.NamedType('bindResponse', BindResponse()), namedtype.NamedType('unbindRequest', UnbindRequest()), namedtype.NamedType('searchRequest', SearchRequest()), namedtype.NamedType('searchResEntry', SearchResultEntry()), namedtype.NamedType('searchResDone', SearchResultDone()), namedtype.NamedType('searchResRef', SearchResultReference()), namedtype.NamedType('modifyRequest', ModifyRequest()), namedtype.NamedType('modifyResponse', ModifyResponse()), namedtype.NamedType('addRequest', AddRequest()), namedtype.NamedType('addResponse', AddResponse()), namedtype.NamedType('delRequest', DelRequest()), namedtype.NamedType('delResponse', DelResponse()), namedtype.NamedType('modDNRequest', ModifyDNRequest()), namedtype.NamedType('modDNResponse', ModifyDNResponse()), namedtype.NamedType('compareRequest', CompareRequest()), namedtype.NamedType('compareResponse', CompareResponse()), namedtype.NamedType('abandonRequest', AbandonRequest()), namedtype.NamedType('extendedReq', ExtendedRequest()), namedtype.NamedType('extendedResp', ExtendedResponse())))), namedtype.OptionalNamedType('controls', Controls().subtype(implicitTag = tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 0))))
