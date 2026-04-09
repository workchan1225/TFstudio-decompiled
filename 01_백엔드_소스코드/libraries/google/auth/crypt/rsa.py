# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: rsa.pyc (Python 3.11)

'''RSA cryptography signer and verifier.'''

try:
    from google.auth.crypt import _cryptography_rsa
    RSASigner = _cryptography_rsa.RSASigner
    RSAVerifier = _cryptography_rsa.RSAVerifier
    return None
except ImportError:
    from google.auth.crypt import _python_rsa
    RSASigner = _python_rsa.RSASigner
    RSAVerifier = _python_rsa.RSAVerifier
    return None
