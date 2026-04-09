# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _custom_tls_signer.pyc (Python 3.11)

'''
Code for configuring client side TLS to offload the signing operation to
signing libraries.
'''
import ctypes
import json
import logging
import os
import sys
import cffi
from google.auth import exceptions
_LOGGER = logging.getLogger(__name__)
SIGN_CALLBACK_CTYPE = ctypes.CFUNCTYPE(ctypes.c_int, ctypes.POINTER(ctypes.c_ubyte), ctypes.POINTER(ctypes.c_size_t), ctypes.POINTER(ctypes.c_ubyte), ctypes.c_size_t)

def _cast_ssl_ctx_to_void_p_pyopenssl(ssl_ctx):
    return ctypes.cast(int(cffi.FFI().cast('intptr_t', ssl_ctx)), ctypes.c_void_p)


def _cast_ssl_ctx_to_void_p_stdlib(context):
    return ctypes.c_void_p.from_address(id(context) + ctypes.sizeof(ctypes.c_void_p) * 2)


def load_offload_lib(offload_lib_path):
    _LOGGER.debug('loading offload library from %s', offload_lib_path)
    lib = ctypes.CDLL(offload_lib_path, winmode = 0) if sys.version_info >= (3, 8) and os.name == 'nt' else ctypes.CDLL(offload_lib_path)
    lib.ConfigureSslContext.argtypes = [
        SIGN_CALLBACK_CTYPE,
        ctypes.c_char_p,
        ctypes.c_void_p]
    lib.ConfigureSslContext.restype = ctypes.c_int
    return lib


def load_signer_lib(signer_lib_path):
    _LOGGER.debug('loading signer library from %s', signer_lib_path)
    lib = ctypes.CDLL(signer_lib_path, winmode = 0) if sys.version_info >= (3, 8) and os.name == 'nt' else ctypes.CDLL(signer_lib_path)
    lib.GetCertPemForPython.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int]
    lib.GetCertPemForPython.restype = ctypes.c_int
    lib.SignForPython.argtypes = [
        ctypes.c_char_p,
        ctypes.c_char_p,
        ctypes.c_int,
        ctypes.c_char_p,
        ctypes.c_int]
    lib.SignForPython.restype = ctypes.c_int
    return lib


def load_provider_lib(provider_lib_path):
    _LOGGER.debug('loading provider library from %s', provider_lib_path)
    lib = ctypes.CDLL(provider_lib_path, winmode = 0) if sys.version_info >= (3, 8) and os.name == 'nt' else ctypes.CDLL(provider_lib_path)
    lib.ECP_attach_to_ctx.argtypes = [
        ctypes.c_void_p,
        ctypes.c_char_p]
    lib.ECP_attach_to_ctx.restype = ctypes.c_int
    return lib


def _compute_sha256_digest(to_be_signed, to_be_signed_len):
    hashes = hashes
    import cryptography.hazmat.primitives
    data = ctypes.string_at(to_be_signed, to_be_signed_len)
    hash = hashes.Hash(hashes.SHA256())
    hash.update(data)
    return hash.finalize()


def get_sign_callback(signer_lib, config_file_path):
    pass
# WARNING: Decompyle incomplete


def get_cert(signer_lib, config_file_path):
    cert_len = signer_lib.GetCertPemForPython(config_file_path.encode(), None, 0)
    if cert_len == 0:
        raise exceptions.MutualTLSChannelError('failed to get certificate')
    cert_holder = ctypes.create_string_buffer(cert_len)
    signer_lib.GetCertPemForPython(config_file_path.encode(), cert_holder, cert_len)
    return bytes(cert_holder)


class CustomTlsSigner(object):
    
    def __init__(self, enterprise_cert_file_path):
        '''
        This class loads the offload and signer library, and calls APIs from
        these libraries to obtain the cert and a signing callback, and attach
        them to SSL context. The cert and the signing callback will be used
        for client authentication in TLS handshake.

        Args:
            enterprise_cert_file_path (str): the path to a enterprise cert JSON
                file. The file should contain the following field:

                    {
                        "libs": {
                            "ecp_client": "...",
                            "tls_offload": "..."
                        }
                    }
        '''
        self._enterprise_cert_file_path = enterprise_cert_file_path
        self._cert = None
        self._sign_callback = None
        self._provider_lib = None

    
    def load_libraries(self):
