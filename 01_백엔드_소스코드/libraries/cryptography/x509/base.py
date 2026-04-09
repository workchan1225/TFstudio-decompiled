# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from __future__ import annotations
import abc
import datetime
import os
import typing
import warnings
from collections.abc import Iterable
from cryptography import utils
from cryptography.hazmat.bindings._rust import x509 as rust_x509
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import dsa, ec, ed448, ed25519, padding, rsa, x448, x25519
from cryptography.hazmat.primitives.asymmetric.types import CertificateIssuerPrivateKeyTypes, CertificatePublicKeyTypes
from cryptography.x509.extensions import Extension, Extensions, ExtensionType, _make_sequence_methods
from cryptography.x509.name import Name, _ASN1Type
from cryptography.x509.oid import ObjectIdentifier
_EARLIEST_UTC_TIME = datetime.datetime(1950, 1, 1)
_AllowedHashTypes = typing.Union[(hashes.SHA224, hashes.SHA256, hashes.SHA384, hashes.SHA512, hashes.SHA3_224, hashes.SHA3_256, hashes.SHA3_384, hashes.SHA3_512)]

class AttributeNotFound(Exception):
    pass
# WARNING: Decompyle incomplete


def _reject_duplicate_extension(extension = None, extensions = None):
    for e in extensions:
        if e.oid == extension.oid:
            raise ValueError('This extension has already been set.')
        return None


def _reject_duplicate_attribute(oid = None, attributes = None):
    for attr_oid, _, _ in attributes:
        if attr_oid == oid:
            raise ValueError('This attribute has already been set.')
        return None


def _convert_to_naive_utc_time(time = None):
    '''Normalizes a datetime to a naive datetime in UTC.

    time -- datetime to normalize. Assumed to be in UTC if not timezone
            aware.
    '''
    pass
# WARNING: Decompyle incomplete


class Attribute:
    
    def __init__(self = None, oid = None, value = None, _type = (_ASN1Type.UTF8String.value,)):
        self._oid = oid
        self._value = value
        self._type = _type

    oid = (lambda self = None: self._oid)()
    value = (lambda self = None: self._value)()
    
    def __repr__(self = None):
        return f'''<Attribute(oid={self.oid}, value={self.value!r})>'''

    
    def __eq__(self = None, other = None):
