# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: serializer.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import abc as cabc
import json
import typing as t
from encoding import want_bytes
from exc import BadPayload
from exc import BadSignature
from signer import _make_keys_list
from signer import Signer
if t.TYPE_CHECKING:
    import typing_extensions as te
    _TSerialized = te.TypeVar('_TSerialized', bound = t.Union[(str, bytes)], default = t.Union[(str, bytes)])
else:
    _TSerialized = t.TypeVar('_TSerialized', bound = t.Union[(str, bytes)])

def _PDataSerializer():
    '''_PDataSerializer'''
    
    def loads(self = None, payload = None):
        pass

    
    def dumps(self = None, obj = None):
        pass


_PDataSerializer = <NODE:27>(_PDataSerializer, '_PDataSerializer', t.Protocol[_TSerialized])

def is_text_serializer(serializer = None):
    '''Checks whether a serializer generates text or binary.'''
    return isinstance(serializer.dumps({ }), str)


def Serializer():
    '''Serializer'''
    __doc__ = "A serializer wraps a :class:`~itsdangerous.signer.Signer` to\n    enable serializing and securely signing data other than bytes. It\n    can unsign to verify that the data hasn't been changed.\n\n    The serializer provides :meth:`dumps` and :meth:`loads`, similar to\n    :mod:`json`, and by default uses :mod:`json` internally to serialize\n    the data to bytes.\n\n    The secret key should be a random string of ``bytes`` and should not\n    be saved to code or version control. Different salts should be used\n    to distinguish signing in different contexts. See :doc:`/concepts`\n    for information about the security of the secret key and salt.\n\n    :param secret_key: The secret key to sign and verify with. Can be a\n        list of keys, oldest to newest, to support key rotation.\n    :param salt: Extra key to combine with ``secret_key`` to distinguish\n        signatures in different contexts.\n    :param serializer: An object that provides ``dumps`` and ``loads``\n        methods for serializing data to a string. Defaults to\n        :attr:`default_serializer`, which defaults to :mod:`json`.\n    :param serializer_kwargs: Keyword arguments to pass when calling\n        ``serializer.dumps``.\n    :param signer: A ``Signer`` class to instantiate when signing data.\n        Defaults to :attr:`default_signer`, which defaults to\n        :class:`~itsdangerous.signer.Signer`.\n    :param signer_kwargs: Keyword arguments to pass when instantiating\n        the ``Signer`` class.\n    :param fallback_signers: List of signer parameters to try when\n        unsigning with the default signer fails. Each item can be a dict\n        of ``signer_kwargs``, a ``Signer`` class, or a tuple of\n        ``(signer, signer_kwargs)``. Defaults to\n        :attr:`default_fallback_signers`.\n\n    .. versionchanged:: 2.0\n        Added support for key rotation by passing a list to\n        ``secret_key``.\n\n    .. versionchanged:: 2.0\n        Removed the default SHA-512 fallback signer from\n        ``default_fallback_signers``.\n\n    .. versionchanged:: 1.1\n        Added support for ``fallback_signers`` and configured a default\n        SHA-512 fallback. This fallback is for users who used the yanked\n        1.0.0 release which defaulted to SHA-512.\n\n    .. versionchanged:: 0.14\n        The ``signer`` and ``signer_kwargs`` parameters were added to\n        the constructor.\n    "
    default_serializer: '_PDataSerializer[t.Any]' = json
    default_signer: 'type[Signer]' = Signer
    default_fallback_signers: 'list[dict[str, t.Any] | tuple[type[Signer], dict[str, t.Any]] | type[Signer]]' = []
    __init__ = (lambda self, secret_key, salt, serializer = None, serializer_kwargs = None, signer = t.overload, signer_kwargs = (b'itsdangerous', None, None, None, None, None), fallback_signers = ('self', 'Serializer[str]', 'secret_key', 'str | bytes | cabc.Iterable[str] | cabc.Iterable[bytes]', 'salt', 'str | bytes | None', 'serializer', 'None | _PDataSerializer[str]', 'serializer_kwargs', 'dict[str, t.Any] | None', 'signer', 'type[Signer] | None', 'signer_kwargs', 'dict[str, t.Any] | None', 'fallback_signers', 'list[dict[str, t.Any] | tuple[type[Signer], dict[str, t.Any]] | type[Signer]] | None'): pass)()
    __init__ = (lambda self, secret_key, salt, serializer = None, serializer_kwargs = None, signer = t.overload, signer_kwargs = (None, None, None, None), fallback_signers = ('self', 'Serializer[bytes]', 'secret_key', 'str | bytes | cabc.Iterable[str] | cabc.Iterable[bytes]', 'salt', 'str | bytes | None', 'serializer', '_PDataSerializer[bytes]', 'serializer_kwargs', 'dict[str, t.Any] | None', 'signer', 'type[Signer] | None', 'signer_kwargs', 'dict[str, t.Any] | None', 'fallback_signers', 'list[dict[str, t.Any] | tuple[type[Signer], dict[str, t.Any]] | type[Signer]] | None'): pass)()
    __init__ = (lambda self = None, secret_key = None, salt = None, *, serializer, serializer_kwargs, signer: pass)()
    __init__ = (lambda self, secret_key, salt, serializer = None, serializer_kwargs = None, signer = t.overload, signer_kwargs = (None, None, None, None), fallback_signers = ('secret_key', 'str | bytes | cabc.Iterable[str] | cabc.Iterable[bytes]', 'salt', 'str | bytes | None', 'serializer', 't.Any', 'serializer_kwargs', 'dict[str, t.Any] | None', 'signer', 'type[Signer] | None', 'signer_kwargs', 'dict[str, t.Any] | None', 'fallback_signers', 'list[dict[str, t.Any] | tuple[type[Signer], dict[str, t.Any]] | type[Signer]] | None'): pass)()
    __init__ = (lambda self = None, secret_key = None, salt = None, *, serializer, serializer_kwargs, signer: pass)()
    
    def __init__(self, secret_key, salt, serializer = None, serializer_kwargs = None, signer = None, signer_kwargs = (b'itsdangerous', None, None, None, None, None), fallback_signers = ('secret_key', 'str | bytes | cabc.Iterable[str] | cabc.Iterable[bytes]', 'salt', 'str | bytes | None', 'serializer', 't.Any | None', 'serializer_kwargs', 'dict[str, t.Any] | None', 'signer', 'type[Signer] | None', 'signer_kwargs', 'dict[str, t.Any] | None', 'fallback_signers', 'list[dict[str, t.Any] | tuple[type[Signer], dict[str, t.Any]] | type[Signer]] | None')):
        self.secret_keys = _make_keys_list(secret_key)
    # WARNING: Decompyle incomplete

    secret_key = (lambda self = None: self.secret_keys[-1])()
    
    def load_payload(self = None, payload = None, serializer = None):
        '''Loads the encoded object. This function raises
        :class:`.BadPayload` if the payload is not valid. The
        ``serializer`` parameter can be used to override the serializer
        stored on the class. The encoded ``payload`` should always be
        bytes.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def dump_payload(self = None, obj = None):
        '''Dumps the encoded object. The return value is always bytes.
        If the internal serializer returns text, the value will be
        encoded as UTF-8.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def make_signer(self = None, salt = None):
        '''Creates a new instance of the signer to be used. The default
        implementation uses the :class:`.Signer` base class.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def iter_unsigners(self = None, salt = None):
        '''Iterates over all signers to be tried for unsigning. Starts
        with the configured signer, then constructs each signer
        specified in ``fallback_signers``.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def dumps(self = None, obj = None, salt = None):
        '''Returns a signed string serialized with the internal
        serializer. The return value can be either a byte or unicode
        string depending on the format of the internal serializer.
        '''
        payload = want_bytes(self.dump_payload(obj))
        rv = self.make_signer(salt).sign(payload)
        if self.is_text_serializer:
            return rv.decode('utf-8')

    
    def dump(self = None, obj = None, f = None, salt = (None,)):
        '''Like :meth:`dumps` but dumps into a file. The file handle has
        to be compatible with what the internal serializer expects.
        '''
        f.write(self.dumps(obj, salt))

    
    def loads(self = None, s = None, salt = None, **kwargs):
        '''Reverse of :meth:`dumps`. Raises :exc:`.BadSignature` if the
        signature validation fails.
        '''
        s = want_bytes(s)
        last_exception = None
        for signer in self.iter_unsigners(salt):
            
            return None, self.load_payload(signer.unsign(s))
            except BadSignature:
                err = None
                err = None
                del err
                continue
                err = None
                del err
            raise t.cast(BadSignature, last_exception)

    
    def load(self = None, f = None, salt = None):
        '''Like :meth:`loads` but loads from a file.'''
        return self.loads(f.read(), salt)

    
    def loads_unsafe(self = None, s = None, salt = None):
        '''Like :meth:`loads` but without verifying the signature. This
        is potentially very dangerous to use depending on how your
        serializer works. The return value is ``(signature_valid,
        payload)`` instead of just the payload. The first item will be a
        boolean that indicates if the signature is valid. This function
        never fails.

        Use it for debugging only and if you know that your serializer
        module is not exploitable (for example, do not use it with a
        pickle serializer).

        .. versionadded:: 0.15
        '''
        return self._loads_unsafe_impl(s, salt)

    
    def _loads_unsafe_impl(self = None, s = None, salt = None, load_kwargs = (None, None), load_payload_kwargs = ('s', 'str | bytes', 'salt', 'str | bytes | None', 'load_kwargs', 'dict[str, t.Any] | None', 'load_payload_kwargs', 'dict[str, t.Any] | None', 'return', 'tuple[bool, t.Any]')):
        '''Low level helper function to implement :meth:`loads_unsafe`
        in serializer subclasses.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def load_unsafe(self = None, f = None, salt = None):
        '''Like :meth:`loads_unsafe` but loads from a file.

        .. versionadded:: 0.15
        '''
        return self.loads_unsafe(f.read(), salt = salt)


Serializer = <NODE:27>(Serializer, 'Serializer', t.Generic[_TSerialized])
