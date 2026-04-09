# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: extensions.pyc (Python 3.11)

from __future__ import annotations
import abc
import datetime
import hashlib
import ipaddress
import typing
from collections.abc import Iterable, Iterator
from cryptography import utils
from cryptography.hazmat.bindings._rust import asn1
from cryptography.hazmat.bindings._rust import x509 as rust_x509
from cryptography.hazmat.primitives import constant_time, serialization
from cryptography.hazmat.primitives.asymmetric.ec import EllipticCurvePublicKey
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPublicKey
from cryptography.hazmat.primitives.asymmetric.types import CertificateIssuerPublicKeyTypes, CertificatePublicKeyTypes
from cryptography.x509.certificate_transparency import SignedCertificateTimestamp
from cryptography.x509.general_name import DirectoryName, DNSName, GeneralName, IPAddress, OtherName, RegisteredID, RFC822Name, UniformResourceIdentifier, _IPAddressTypes
from cryptography.x509.name import Name, RelativeDistinguishedName
from cryptography.x509.oid import CRLEntryExtensionOID, ExtensionOID, ObjectIdentifier, OCSPExtensionOID
ExtensionTypeVar = typing.TypeVar('ExtensionTypeVar', bound = 'ExtensionType', covariant = True)

def _key_identifier_from_public_key(public_key = None):
    if isinstance(public_key, RSAPublicKey):
        data = public_key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.PKCS1)
    elif isinstance(public_key, EllipticCurvePublicKey):
        data = public_key.public_bytes(serialization.Encoding.X962, serialization.PublicFormat.UncompressedPoint)
    else:
        serialized = public_key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        data = asn1.parse_spki_for_data(serialized)
    return hashlib.sha1(data).digest()


def _make_sequence_methods(field_name = None):
    pass
# WARNING: Decompyle incomplete


class DuplicateExtension(Exception):
    pass
# WARNING: Decompyle incomplete


class ExtensionNotFound(Exception):
    pass
# WARNING: Decompyle incomplete


def ExtensionType():
    '''ExtensionType'''
    oid: 'typing.ClassVar[ObjectIdentifier]' = 'ExtensionType'
    
    def public_bytes(self = None):
        '''
        Serializes the extension type to DER.
        '''
        raise NotImplementedError(f'''public_bytes is not implemented for extension type {self!r}''')


ExtensionType = <NODE:27>(ExtensionType, 'ExtensionType', metaclass = abc.ABCMeta)

class Extensions:
    
    def __init__(self = None, extensions = None):
        self._extensions = list(extensions)

    
    def get_extension_for_oid(self = None, oid = None):
        for ext in self:
            if ext.oid == oid:
                
                return None, ext
            raise ExtensionNotFound(f'''No {oid} extension was found''', oid)

    
    def get_extension_for_class(self = None, extclass = None):
        if extclass is UnrecognizedExtension:
            raise TypeError("UnrecognizedExtension can't be used with get_extension_for_class because more than one instance of the class may be present.")
        for ext in self:
            if isinstance(ext.value, extclass):
                
                return None, ext
            raise ExtensionNotFound(f'''No {extclass} extension was found''', extclass.oid)

    (__len__, __iter__, __getitem__) = _make_sequence_methods('_extensions')
    
    def __repr__(self = None):
        return f'''<Extensions({self._extensions})>'''



class CRLNumber(ExtensionType):
    oid = ExtensionOID.CRL_NUMBER
    
    def __init__(self = None, crl_number = None):
        if not isinstance(crl_number, int):
            raise TypeError('crl_number must be an integer')
        self._crl_number = crl_number

    
    def __eq__(self = None, other = None):
        if not isinstance(other, CRLNumber):
            return NotImplemented
        return None.crl_number == other.crl_number

    
    def __hash__(self = None):
        return hash(self.crl_number)

    
    def __repr__(self = None):
        return f'''<CRLNumber({self.crl_number})>'''

    crl_number = (lambda self = None: self._crl_number)()
    
    def public_bytes(self = None):
        return rust_x509.encode_extension_value(self)



class AuthorityKeyIdentifier(ExtensionType):
    oid = ExtensionOID.AUTHORITY_KEY_IDENTIFIER
    
    def __init__(self = None, key_identifier = None, authority_cert_issuer = None, authority_cert_serial_number = ('key_identifier', 'bytes | None', 'authority_cert_issuer', 'Iterable[GeneralName] | None', 'authority_cert_serial_number', 'int | None', 'return', 'None')):
        if (authority_cert_issuer is None) != (authority_cert_serial_number is None):
            raise ValueError('authority_cert_issuer and authority_cert_serial_number must both be present or both None')
    # WARNING: Decompyle incomplete

    from_issuer_public_key = (lambda cls = None, public_key = None: digest = _key_identifier_from_public_key(public_key)cls(key_identifier = digest, authority_cert_issuer = None, authority_cert_serial_number = None))()
    from_issuer_subject_key_identifier = (lambda cls = None, ski = None: cls(key_identifier = ski.digest, authority_cert_issuer = None, authority_cert_serial_number = None))()
    
    def __repr__(self = None):
        return f'''<AuthorityKeyIdentifier(key_identifier={self.key_identifier!r}, authority_cert_issuer={self.authority_cert_issuer}, authority_cert_serial_number={self.authority_cert_serial_number})>'''

    
    def __eq__(self = None, other = None):
