# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

__doc__ = "Cryptography helpers for verifying and signing messages.\n\nThe simplest way to verify signatures is using :func:`verify_signature`::\n\n    cert = open('certs.pem').read()\n    valid = crypt.verify_signature(message, signature, cert)\n\nIf you're going to verify many messages with the same certificate, you can use\n:class:`RSAVerifier`::\n\n    cert = open('certs.pem').read()\n    verifier = crypt.RSAVerifier.from_string(cert)\n    valid = verifier.verify(message, signature)\n\nTo sign messages use :class:`RSASigner` with a private key::\n\n    private_key = open('private_key.pem').read()\n    signer = crypt.RSASigner.from_string(private_key)\n    signature = signer.sign(message)\n\nThe code above also works for :class:`ES256Signer` and :class:`ES256Verifier`.\nNote that these two classes are only available if your `cryptography` dependency\nversion is at least 1.4.0.\n"
from google.auth.crypt import base
from google.auth.crypt import rsa

try:
    from google.auth.crypt import es256
except ImportError:
    es256 = None

# WARNING: Decompyle incomplete
