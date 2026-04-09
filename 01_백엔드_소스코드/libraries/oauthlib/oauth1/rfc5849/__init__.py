# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
oauthlib.oauth1.rfc5849
~~~~~~~~~~~~~~

This module is an implementation of various logic needed
for signing and checking OAuth 1.0 RFC 5849 requests.

It supports all three standard signature methods defined in RFC 5849:

- HMAC-SHA1
- RSA-SHA1
- PLAINTEXT

It also supports signature methods that are not defined in RFC 5849. These are
based on the standard ones but replace SHA-1 with the more secure SHA-256:

- HMAC-SHA256
- RSA-SHA256

'''
import base64
import hashlib
import logging
from urllib.parse import parse as urlparse
from oauthlib.common import Request, generate_nonce, generate_timestamp, to_unicode, urlencode
from  import parameters, signature
log = logging.getLogger(__name__)
SIGNATURE_HMAC_SHA1 = 'HMAC-SHA1'
SIGNATURE_HMAC_SHA256 = 'HMAC-SHA256'
SIGNATURE_HMAC_SHA512 = 'HMAC-SHA512'
SIGNATURE_HMAC = SIGNATURE_HMAC_SHA1
SIGNATURE_RSA_SHA1 = 'RSA-SHA1'
SIGNATURE_RSA_SHA256 = 'RSA-SHA256'
SIGNATURE_RSA_SHA512 = 'RSA-SHA512'
SIGNATURE_RSA = SIGNATURE_RSA_SHA1
SIGNATURE_PLAINTEXT = 'PLAINTEXT'
SIGNATURE_METHODS = (SIGNATURE_HMAC_SHA1, SIGNATURE_HMAC_SHA256, SIGNATURE_HMAC_SHA512, SIGNATURE_RSA_SHA1, SIGNATURE_RSA_SHA256, SIGNATURE_RSA_SHA512, SIGNATURE_PLAINTEXT)
SIGNATURE_TYPE_AUTH_HEADER = 'AUTH_HEADER'
SIGNATURE_TYPE_QUERY = 'QUERY'
SIGNATURE_TYPE_BODY = 'BODY'
CONTENT_TYPE_FORM_URLENCODED = 'application/x-www-form-urlencoded'

class Client:
    '''A client used to sign OAuth 1.0 RFC 5849 requests.'''
    SIGNATURE_METHODS = {
        SIGNATURE_PLAINTEXT: signature.sign_plaintext_with_client,
        SIGNATURE_RSA_SHA512: signature.sign_rsa_sha512_with_client,
        SIGNATURE_RSA_SHA256: signature.sign_rsa_sha256_with_client,
        SIGNATURE_RSA_SHA1: signature.sign_rsa_sha1_with_client,
        SIGNATURE_HMAC_SHA512: signature.sign_hmac_sha512_with_client,
        SIGNATURE_HMAC_SHA256: signature.sign_hmac_sha256_with_client,
        SIGNATURE_HMAC_SHA1: signature.sign_hmac_sha1_with_client }
    register_signature_method = (lambda cls, method_name, method_callback: cls.SIGNATURE_METHODS[method_name] = method_callback)()
    
    def __init__(self, client_key, client_secret, resource_owner_key, resource_owner_secret, callback_uri, signature_method, signature_type, rsa_key, verifier, realm, encoding, decoding, nonce, timestamp = (None, None, None, None, SIGNATURE_HMAC_SHA1, SIGNATURE_TYPE_AUTH_HEADER, None, None, None, 'utf-8', None, None, None)):
        '''Create an OAuth 1 client.

        :param client_key: Client key (consumer key), mandatory.
        :param resource_owner_key: Resource owner key (oauth token).
        :param resource_owner_secret: Resource owner secret (oauth token secret).
        :param callback_uri: Callback used when obtaining request token.
        :param signature_method: SIGNATURE_HMAC, SIGNATURE_RSA or SIGNATURE_PLAINTEXT.
        :param signature_type: SIGNATURE_TYPE_AUTH_HEADER (default),
                               SIGNATURE_TYPE_QUERY or SIGNATURE_TYPE_BODY
                               depending on where you want to embed the oauth
                               credentials.
        :param rsa_key: RSA key used with SIGNATURE_RSA.
        :param verifier: Verifier used when obtaining an access token.
        :param realm: Realm (scope) to which access is being requested.
        :param encoding: If you provide non-unicode input you may use this
                         to have oauthlib automatically convert.
        :param decoding: If you wish that the returned uri, headers and body
                         from sign be encoded back from unicode, then set
                         decoding to your preferred encoding, i.e. utf-8.
        :param nonce: Use this nonce instead of generating one. (Mainly for testing)
        :param timestamp: Use this timestamp instead of using current. (Mainly for testing)
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        attrs = vars(self).copy()
        attrs['client_secret'] = '****' if attrs['client_secret'] else None
        attrs['rsa_key'] = '****' if attrs['rsa_key'] else None
        attrs['resource_owner_secret'] = '****' if attrs['resource_owner_secret'] else None
        attribute_str = (lambda .0: pass# WARNING: Decompyle incomplete
)(attrs.items()())
        return '<{} {}>'.format(self.__class__.__name__, attribute_str)

    
    def get_oauth_signature(self, request):
        """Get an OAuth signature to be used in signing a request

        To satisfy `section 3.4.1.2`_ item 2, if the request argument's
        headers dict attribute contains a Host item, its value will
        replace any netloc part of the request argument's uri attribute
        value.

        .. _`section 3.4.1.2`: https://tools.ietf.org/html/rfc5849#section-3.4.1.2
        """
        if self.signature_method == SIGNATURE_PLAINTEXT:
            return signature.sign_plaintext(self.client_secret, self.resource_owner_secret)
        (uri, headers, body) = None._render(request)
        collected_params = signature.collect_parameters(uri_query = urlparse.urlparse(uri).query, body = body, headers = headers)
        log.debug('Collected params: {}'.format(collected_params))
        normalized_params = signature.normalize_parameters(collected_params)
        normalized_uri = signature.base_string_uri(uri, headers.get('Host', None))
        log.debug('Normalized params: {}'.format(normalized_params))
        log.debug('Normalized URI: {}'.format(normalized_uri))
        base_string = signature.signature_base_string(request.http_method, normalized_uri, normalized_params)
        log.debug('Signing: signature base string: {}'.format(base_string))
        if self.signature_method not in self.SIGNATURE_METHODS:
            raise ValueError('Invalid signature method.')
        sig = self.SIGNATURE_METHODS[self.signature_method](base_string, self)
        log.debug('Signature: {}'.format(sig))
        return sig

    
    def get_oauth_params(self, request):
        '''Get the basic OAuth parameters to be used in generating a signature.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _render(self, request, formencode, realm = (False, None)):
        '''Render a signed request according to signature type

        Returns a 3-tuple containing the request URI, headers, and body.

        If the formencode argument is True and the body contains parameters, it
        is escaped and returned as a valid formencoded string.
        '''
        body = request.body
        headers = request.headers
        uri = request.uri
        if self.signature_type == SIGNATURE_TYPE_AUTH_HEADER:
            headers = parameters.prepare_headers(request.oauth_params, request.headers, realm = realm)
    # WARNING: Decompyle incomplete

    
    def sign(self, uri, http_method, body, headers, realm = ('GET', None, None, None)):
        """Sign a request

        Signs an HTTP request with the specified parts.

        Returns a 3-tuple of the signed request's URI, headers, and body.
        Note that http_method is not returned as it is unaffected by the OAuth
        signing process. Also worth noting is that duplicate parameters
        will be included in the signature, regardless of where they are
        specified (query, body).

        The body argument may be a dict, a list of 2-tuples, or a formencoded
        string. The Content-Type header must be 'application/x-www-form-urlencoded'
        if it is present.

        If the body argument is not one of the above, it will be returned
        verbatim as it is unaffected by the OAuth signing process. Attempting to
        sign a request with non-formencoded data using the OAuth body signature
        type is invalid and will raise an exception.

        If the body does contain parameters, it will be returned as a properly-
        formatted formencoded string.

        Body may not be included if the http_method is either GET or HEAD as
        this changes the semantic meaning of the request.

        All string data MUST be unicode or be encoded with the same encoding
        scheme supplied to the Client constructor, default utf-8. This includes
        strings inside body dicts, for example.
        """
        request = Request(uri, http_method, body, headers, encoding = self.encoding)
        content_type = request.headers.get('Content-Type', None)
        if content_type:
            multipart = content_type.startswith('multipart/')
            should_have_params = content_type == CONTENT_TYPE_FORM_URLENCODED
            has_params = request.decoded_body is not None
            if multipart and has_params:
                raise ValueError('Headers indicate a multipart body but body contains parameters.')
            if not should_have_params and has_params:
                raise ValueError('Headers indicate a formencoded body but body was not decodable.')
            if should_have_params and has_params:
                if not content_type:
                    raise ValueError('Body contains parameters but Content-Type header was {} instead of {}'.format('not set', CONTENT_TYPE_FORM_URLENCODED))
        if self.signature_type == SIGNATURE_TYPE_BODY:
            if should_have_params and has_params or multipart:
                raise ValueError('Body signatures may only be used with form-urlencoded content')
        if http_method.upper() in ('GET', 'HEAD') and has_params:
            raise ValueError('GET/HEAD requests should not include body.')
        request.oauth_params = self.get_oauth_params(request)
        request.oauth_params.append(('oauth_signature', self.get_oauth_signature(request)))
        if not realm:
            (uri, headers, body) = self._render(request, formencode = True, realm = self.realm)
            if self.decoding:
                log.debug('Encoding URI, headers and body to %s.', self.decoding)
                uri = uri.encode(self.decoding)
                body = body.encode(self.decoding) if body else body
                new_headers = { }
                for k, v in headers.items():
                    new_headers[k.encode(self.decoding)] = v.encode(self.decoding)
                    headers = new_headers
                    return (uri, headers, body)
