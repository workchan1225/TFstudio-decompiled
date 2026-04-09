# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

'''Base classes for cryptographic signers and verifiers.'''
import abc
import io
import json
from google.auth import exceptions
_JSON_FILE_PRIVATE_KEY = 'private_key'
_JSON_FILE_PRIVATE_KEY_ID = 'private_key_id'

def Verifier():
    '''Verifier'''
    __doc__ = 'Abstract base class for crytographic signature verifiers.'
    verify = (lambda self, message, signature: raise NotImplementedError('Verify must be implemented'))()

Verifier = <NODE:27>(Verifier, 'Verifier', metaclass = abc.ABCMeta)

def Signer():
    '''Signer'''
    __doc__ = 'Abstract base class for cryptographic signers.'
    key_id = (lambda self: raise NotImplementedError('Key id must be implemented'))()
    sign = (lambda self, message: raise NotImplementedError('Sign must be implemented'))()

Signer = <NODE:27>(Signer, 'Signer', metaclass = abc.ABCMeta)

def FromServiceAccountMixin():
    '''FromServiceAccountMixin'''
    __doc__ = 'Mix-in to enable factory constructors for a Signer.'
    from_string = (lambda cls, key, key_id = (None,): raise NotImplementedError('from_string must be implemented'))()
    from_service_account_info = (lambda cls, info: if _JSON_FILE_PRIVATE_KEY not in info:
raise exceptions.MalformedError('The private_key field was not found in the service account info.')cls.from_string(info[_JSON_FILE_PRIVATE_KEY], info.get(_JSON_FILE_PRIVATE_KEY_ID)))()
    from_service_account_file = (lambda cls, filename: json_file = io.open(filename, 'r', encoding = 'utf-8')data = json.load(json_file)None(None, None))()

FromServiceAccountMixin = <NODE:27>(FromServiceAccountMixin, 'FromServiceAccountMixin', metaclass = abc.ABCMeta)
