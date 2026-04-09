# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pyopenssl.pyc (Python 3.11)

"""
Module for using pyOpenSSL as a TLS backend. This module was relevant before
the standard library ``ssl`` module supported SNI, but now that we've dropped
support for Python 2.7 all relevant Python versions support SNI so
**this module is no longer recommended**.

This needs the following packages installed:

* `pyOpenSSL`_ (tested with 16.0.0)
* `cryptography`_ (minimum 1.3.4, from pyopenssl)
* `idna`_ (minimum 2.0)

However, pyOpenSSL depends on cryptography, so while we use all three directly here we
end up having relatively few packages required.

You can install them with the following command:

.. code-block:: bash

    $ python -m pip install pyopenssl cryptography idna

To activate certificate checking, call
:func:`~urllib3.contrib.pyopenssl.inject_into_urllib3` from your Python code
before you begin making HTTP requests. This can be done in a ``sitecustomize``
module, or at any other time before your application begins using ``urllib3``,
like this:

.. code-block:: python

    try:
        import urllib3.contrib.pyopenssl
        urllib3.contrib.pyopenssl.inject_into_urllib3()
    except ImportError:
        pass

.. _pyopenssl: https://www.pyopenssl.org
.. _cryptography: https://cryptography.io
.. _idna: https://github.com/kjd/idna
"""
from __future__ import annotations
import OpenSSL.SSL as OpenSSL
from cryptography import x509

try:
    from cryptography.x509 import UnsupportedExtension
except ImportError:
    
    class UnsupportedExtension(Exception):
        pass


import logging
import ssl
import typing
from io import BytesIO
from socket import socket as socket_cls
from socket import timeout
from  import util
if typing.TYPE_CHECKING:
    from OpenSSL.crypto import X509
__all__ = [
    'inject_into_urllib3',
    'extract_from_urllib3']
_openssl_versions: 'dict[int, int]' = {
    ssl.PROTOCOL_TLSv1: OpenSSL.SSL.TLSv1_METHOD,
    util.ssl_.PROTOCOL_TLS_CLIENT: OpenSSL.SSL.SSLv23_METHOD,
    util.ssl_.PROTOCOL_TLS: OpenSSL.SSL.SSLv23_METHOD }
if hasattr(ssl, 'PROTOCOL_TLSv1_1') and hasattr(OpenSSL.SSL, 'TLSv1_1_METHOD'):
    _openssl_versions[ssl.PROTOCOL_TLSv1_1] = OpenSSL.SSL.TLSv1_1_METHOD
if hasattr(ssl, 'PROTOCOL_TLSv1_2') and hasattr(OpenSSL.SSL, 'TLSv1_2_METHOD'):
    _openssl_versions[ssl.PROTOCOL_TLSv1_2] = OpenSSL.SSL.TLSv1_2_METHOD
_stdlib_to_openssl_verify = {
    ssl.CERT_REQUIRED: OpenSSL.SSL.VERIFY_PEER + OpenSSL.SSL.VERIFY_FAIL_IF_NO_PEER_CERT,
    ssl.CERT_OPTIONAL: OpenSSL.SSL.VERIFY_PEER,
    ssl.CERT_NONE: OpenSSL.SSL.VERIFY_NONE }
_openssl_to_stdlib_verify = _stdlib_to_openssl_verify.items()()
_OP_NO_SSLv2_OR_SSLv3: 'int' = getattr(OpenSSL.SSL, 'OP_NO_SSLv2', 0) | getattr(OpenSSL.SSL, 'OP_NO_SSLv3', 0)
_OP_NO_TLSv1: 'int' = getattr(OpenSSL.SSL, 'OP_NO_TLSv1', 0)
_OP_NO_TLSv1_1: 'int' = getattr(OpenSSL.SSL, 'OP_NO_TLSv1_1', 0)
_OP_NO_TLSv1_2: 'int' = getattr(OpenSSL.SSL, 'OP_NO_TLSv1_2', 0)
_OP_NO_TLSv1_3: 'int' = getattr(OpenSSL.SSL, 'OP_NO_TLSv1_3', 0)
_openssl_to_ssl_minimum_version: 'dict[int, int]' = {
    ssl.TLSVersion.MAXIMUM_SUPPORTED: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1 | _OP_NO_TLSv1_1 | _OP_NO_TLSv1_2,
    ssl.TLSVersion.TLSv1_3: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1 | _OP_NO_TLSv1_1 | _OP_NO_TLSv1_2,
    ssl.TLSVersion.TLSv1_2: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1 | _OP_NO_TLSv1_1,
    ssl.TLSVersion.TLSv1_1: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1,
    ssl.TLSVersion.TLSv1: _OP_NO_SSLv2_OR_SSLv3,
    ssl.TLSVersion.MINIMUM_SUPPORTED: _OP_NO_SSLv2_OR_SSLv3 }
_openssl_to_ssl_maximum_version: 'dict[int, int]' = {
    ssl.TLSVersion.MAXIMUM_SUPPORTED: _OP_NO_SSLv2_OR_SSLv3,
    ssl.TLSVersion.TLSv1_3: _OP_NO_SSLv2_OR_SSLv3,
    ssl.TLSVersion.TLSv1_2: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1_3,
    ssl.TLSVersion.TLSv1_1: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1_2 | _OP_NO_TLSv1_3,
    ssl.TLSVersion.TLSv1: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1_1 | _OP_NO_TLSv1_2 | _OP_NO_TLSv1_3,
    ssl.TLSVersion.MINIMUM_SUPPORTED: _OP_NO_SSLv2_OR_SSLv3 | _OP_NO_TLSv1 | _OP_NO_TLSv1_1 | _OP_NO_TLSv1_2 | _OP_NO_TLSv1_3 }
SSL_WRITE_BLOCKSIZE = 16384
orig_util_SSLContext = util.ssl_.SSLContext
log = logging.getLogger(__name__)

def inject_into_urllib3():
    '''Monkey-patch urllib3 with PyOpenSSL-backed SSL-support.'''
    _validate_dependencies_met()
    util.SSLContext = PyOpenSSLContext
    util.ssl_.SSLContext = PyOpenSSLContext
    util.IS_PYOPENSSL = True
    util.ssl_.IS_PYOPENSSL = True


def extract_from_urllib3():
    '''Undo monkey-patching by :func:`inject_into_urllib3`.'''
    util.SSLContext = orig_util_SSLContext
    util.ssl_.SSLContext = orig_util_SSLContext
    util.IS_PYOPENSSL = False
    util.ssl_.IS_PYOPENSSL = False


def _validate_dependencies_met():
    """
    Verifies that PyOpenSSL's package-level dependencies have been met.
    Throws `ImportError` if they are not met.
    """
    Extensions = Extensions
    import cryptography.x509.extensions
# WARNING: Decompyle incomplete


def _dnsname_to_stdlib(name = None):
    '''
    Converts a dNSName SubjectAlternativeName field to the form used by the
    standard library on the given Python version.

    Cryptography produces a dNSName as a unicode string that was idna-decoded
    from ASCII bytes. We need to idna-encode that string to get it back, and
    then on Python 3 we also need to convert to unicode via UTF-8 (the stdlib
    uses PyUnicode_FromStringAndSize on it, which decodes via UTF-8).

    If the name cannot be idna-encoded then we return None signalling that
    the name given should be skipped.
    '''
    
    def idna_encode(name = None):
        """
        Borrowed wholesale from the Python Cryptography Project. It turns out
        that we can't just safely call `idna.encode`: it can explode for
        wildcard names. This avoids that problem.
        """
        import idna
        
        try:
            for prefix in ('*.', '.'):
                if name.startswith(prefix):
                    name = name[len(prefix):]
                    
                    return None, prefix.encode('ascii') + idna.encode(name)
                return idna.encode(name)
                except idna.core.IDNAError:
                    return None


    if ':' in name:
        return name
    encoded_name = idna_encode(name)
# WARNING: Decompyle incomplete


def get_subj_alt_name(peer_cert = None):
    '''
    Given an PyOpenSSL certificate, provides all the subject alternative names.
    '''
    cert = peer_cert.to_cryptography()
    
    try:
        ext = cert.extensions.get_extension_for_class(x509.SubjectAlternativeName).value
    except x509.ExtensionNotFound:
        return 
        except (x509.DuplicateExtension, UnsupportedExtension, x509.UnsupportedGeneralNameType, UnicodeError):
            log.warning('A problem was encountered with the certificate that prevented urllib3 from finding the SubjectAlternativeName field. This can affect certificate validation. The error was %s', e)
            del e
            return None
            None = 
            del e

    names = map(_dnsname_to_stdlib, ext.get_values_for_type(x509.DNSName))()
    (lambda .0: pass# WARNING: Decompyle incomplete
)(ext.get_values_for_type(x509.IPAddress)())
    return names


class WrappedSocket:
    """API-compatibility wrapper for Python OpenSSL's Connection-class."""
    
    def __init__(self = None, connection = None, socket = None, suppress_ragged_eofs = (True,)):
        self.connection = connection
        self.socket = socket
        self.suppress_ragged_eofs = suppress_ragged_eofs
        self._io_refs = 0
        self._closed = False

    
    def fileno(self = None):
        return self.socket.fileno()

    
    def _decref_socketios(self = None):
        if self._io_refs > 0:
            pass
        if self._closed:
            self.close()
            return None
        return self, self._io_refs -= 1, ._io_refs

    
    def recv(self = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def recv_into(self = None, *args, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def settimeout(self = None, timeout = None):
        return self.socket.settimeout(timeout)

    
    def _send_until_done(self = None, data = None):
        
        try:
            return self.connection.send(data)
        except OpenSSL.SSL.WantWriteError:
            e = None
            if not util.wait_for_write(self.socket, self.socket.gettimeout()):
                raise timeout(), e
            e = None
            del e
            continue
            e = None
            del e
            except OpenSSL.SSL.SysCallError:
                e = None
                raise OSError(e.args[0], str(e)), e
                e = None
                del e


    
    def sendall(self = None, data = None):
        total_sent = 0
    # WARNING: Decompyle incomplete

    
    def shutdown(self = None, how = None):
        
        try:
            self.connection.shutdown()
            return None
        except OpenSSL.SSL.Error:
            e = None
            raise ssl.SSLError(f'''shutdown error: {e!r}'''), e
            e = None
            del e


    
    def close(self = None):
        self._closed = True
        if self._io_refs <= 0:
            self._real_close()
            return None

    
    def _real_close(self = None):
        
        try:
            return self.connection.close()
        except OpenSSL.SSL.Error:
            return None


    
    def getpeercert(self = None, binary_form = None):
        x509 = self.connection.get_peer_certificate()
        if not x509:
            return x509
        if None:
            return OpenSSL.crypto.dump_certificate(OpenSSL.crypto.FILETYPE_ASN1, x509)
        return {
            'subject': (((None, x509.get_subject().CN),),),
            'subjectAltName': get_subj_alt_name(x509) }

    
    def version(self = None):
        return self.connection.get_protocol_version_name()

    
    def selected_alpn_protocol(self = None):
        alpn_proto = self.connection.get_alpn_proto_negotiated()
        return alpn_proto.decode() if alpn_proto else None


WrappedSocket.makefile = socket_cls.makefile

class PyOpenSSLContext:
    '''
    I am a wrapper class for the PyOpenSSL ``Context`` object. I am responsible
    for translating the interface of the standard library ``SSLContext`` object
    to calls into PyOpenSSL.
    '''
    
    def __init__(self = None, protocol = None):
        self.protocol = _openssl_versions[protocol]
        self._ctx = OpenSSL.SSL.Context(self.protocol)
        self._options = 0
        self.check_hostname = False
        self._minimum_version = ssl.TLSVersion.MINIMUM_SUPPORTED
        self._maximum_version = ssl.TLSVersion.MAXIMUM_SUPPORTED
        self._verify_flags = ssl.VERIFY_X509_TRUSTED_FIRST

    options = (lambda self = None: self._options)()
    options = (lambda self = None, value = None: self._options = valueself._set_ctx_options())()
    verify_flags = (lambda self = None: self._verify_flags)()
    verify_flags = (lambda self = None, value = None: self._verify_flags = valueself._ctx.get_cert_store().set_flags(self._verify_flags))()
    verify_mode = (lambda self = None: _openssl_to_stdlib_verify[self._ctx.get_verify_mode()])()
    verify_mode = (lambda self = None, value = None: self._ctx.set_verify(_stdlib_to_openssl_verify[value], _verify_callback))()
    
    def set_default_verify_paths(self = None):
        self._ctx.set_default_verify_paths()

    
    def set_ciphers(self = None, ciphers = None):
        if isinstance(ciphers, str):
            ciphers = ciphers.encode('utf-8')
        self._ctx.set_cipher_list(ciphers)

    
    def load_verify_locations(self = None, cafile = None, capath = None, cadata = (None, None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def load_cert_chain(self = None, certfile = None, keyfile = None, password = (None, None)):
        pass
    # WARNING: Decompyle incomplete

    
    def set_alpn_protocols(self = None, protocols = None):
        protocols = protocols()
        return self._ctx.set_alpn_protos(protocols)

    
    def wrap_socket(self, sock = None, server_side = None, do_handshake_on_connect = None, suppress_ragged_eofs = (False, True, True, None), server_hostname = ('sock', 'socket_cls', 'server_side', 'bool', 'do_handshake_on_connect', 'bool', 'suppress_ragged_eofs', 'bool', 'server_hostname', 'bytes | str | None', 'return', 'WrappedSocket')):
        cnx = OpenSSL.SSL.Connection(self._ctx, sock)
        if not server_hostname and util.ssl_.is_ipaddress(server_hostname):
            if isinstance(server_hostname, str):
                server_hostname = server_hostname.encode('utf-8')
            cnx.set_tlsext_host_name(server_hostname)
        cnx.set_connect_state()
        
        try:
            cnx.do_handshake()
        except OpenSSL.SSL.WantReadError:
            e = None
            if not util.wait_for_read(sock, sock.gettimeout()):
                raise timeout('select timed out'), e
            e = None
            del e
            continue
            e = None
            del e
            except OpenSSL.SSL.Error:
                e = None
                raise ssl.SSLError(f'''bad handshake: {e!r}'''), e
                e = None
                del e

        return WrappedSocket(cnx, sock)

    
    def _set_ctx_options(self = None):
        self._ctx.set_options(self._options | _openssl_to_ssl_minimum_version[self._minimum_version] | _openssl_to_ssl_maximum_version[self._maximum_version])

    minimum_version = (lambda self = None: self._minimum_version)()
    minimum_version = (lambda self = None, minimum_version = None: self._minimum_version = minimum_versionself._set_ctx_options())()
    maximum_version = (lambda self = None: self._maximum_version)()
    maximum_version = (lambda self = None, maximum_version = None: self._maximum_version = maximum_versionself._set_ctx_options())()


def _verify_callback(cnx, x509 = None, err_no = None, err_depth = None, return_code = ('cnx', 'OpenSSL.SSL.Connection', 'x509', 'X509', 'err_no', 'int', 'err_depth', 'int', 'return_code', 'int', 'return', 'bool')):
    return err_no == 0
