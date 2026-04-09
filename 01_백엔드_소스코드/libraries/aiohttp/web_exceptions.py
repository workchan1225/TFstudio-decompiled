# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_exceptions.pyc (Python 3.11)

import warnings
from typing import Any, Dict, Iterable, List, Optional, Set
from yarl import URL
from typedefs import LooseHeaders, StrOrURL
from web_response import Response
__all__ = ('HTTPException', 'HTTPError', 'HTTPRedirection', 'HTTPSuccessful', 'HTTPOk', 'HTTPCreated', 'HTTPAccepted', 'HTTPNonAuthoritativeInformation', 'HTTPNoContent', 'HTTPResetContent', 'HTTPPartialContent', 'HTTPMove', 'HTTPMultipleChoices', 'HTTPMovedPermanently', 'HTTPFound', 'HTTPSeeOther', 'HTTPNotModified', 'HTTPUseProxy', 'HTTPTemporaryRedirect', 'HTTPPermanentRedirect', 'HTTPClientError', 'HTTPBadRequest', 'HTTPUnauthorized', 'HTTPPaymentRequired', 'HTTPForbidden', 'HTTPNotFound', 'HTTPMethodNotAllowed', 'HTTPNotAcceptable', 'HTTPProxyAuthenticationRequired', 'HTTPRequestTimeout', 'HTTPConflict', 'HTTPGone', 'HTTPLengthRequired', 'HTTPPreconditionFailed', 'HTTPRequestEntityTooLarge', 'HTTPRequestURITooLong', 'HTTPUnsupportedMediaType', 'HTTPRequestRangeNotSatisfiable', 'HTTPExpectationFailed', 'HTTPMisdirectedRequest', 'HTTPUnprocessableEntity', 'HTTPFailedDependency', 'HTTPUpgradeRequired', 'HTTPPreconditionRequired', 'HTTPTooManyRequests', 'HTTPRequestHeaderFieldsTooLarge', 'HTTPUnavailableForLegalReasons', 'HTTPServerError', 'HTTPInternalServerError', 'HTTPNotImplemented', 'HTTPBadGateway', 'HTTPServiceUnavailable', 'HTTPGatewayTimeout', 'HTTPVersionNotSupported', 'HTTPVariantAlsoNegotiates', 'HTTPInsufficientStorage', 'HTTPNotExtended', 'HTTPNetworkAuthenticationRequired')

class NotAppKeyWarning(UserWarning):
    '''Warning when not using AppKey in Application.'''
    pass


class HTTPException(Exception, Response):
    status_code = -1
    empty_body = False
    __http_exception__ = True
    
    def __init__(self = None, *, headers, reason, body, text, content_type):
        pass
    # WARNING: Decompyle incomplete

    
    def __bool__(self = None):
        return True



class HTTPError(HTTPException):
    '''Base class for exceptions with status codes in the 400s and 500s.'''
    pass


class HTTPRedirection(HTTPException):
    '''Base class for exceptions with status codes in the 300s.'''
    pass


class HTTPSuccessful(HTTPException):
    '''Base class for exceptions with status codes in the 200s.'''
    pass


class HTTPOk(HTTPSuccessful):
    status_code = 200


class HTTPCreated(HTTPSuccessful):
    status_code = 201


class HTTPAccepted(HTTPSuccessful):
    status_code = 202


class HTTPNonAuthoritativeInformation(HTTPSuccessful):
    status_code = 203


class HTTPNoContent(HTTPSuccessful):
    status_code = 204
    empty_body = True


class HTTPResetContent(HTTPSuccessful):
    status_code = 205
    empty_body = True


class HTTPPartialContent(HTTPSuccessful):
    status_code = 206


class HTTPMove(HTTPRedirection):
    pass
# WARNING: Decompyle incomplete


class HTTPMultipleChoices(HTTPMove):
    status_code = 300


class HTTPMovedPermanently(HTTPMove):
    status_code = 301


class HTTPFound(HTTPMove):
    status_code = 302


class HTTPSeeOther(HTTPMove):
    status_code = 303


class HTTPNotModified(HTTPRedirection):
    status_code = 304
    empty_body = True


class HTTPUseProxy(HTTPMove):
    status_code = 305


class HTTPTemporaryRedirect(HTTPMove):
    status_code = 307


class HTTPPermanentRedirect(HTTPMove):
    status_code = 308


class HTTPClientError(HTTPError):
    pass


class HTTPBadRequest(HTTPClientError):
    status_code = 400


class HTTPUnauthorized(HTTPClientError):
    status_code = 401


class HTTPPaymentRequired(HTTPClientError):
    status_code = 402


class HTTPForbidden(HTTPClientError):
    status_code = 403


class HTTPNotFound(HTTPClientError):
    status_code = 404


class HTTPMethodNotAllowed(HTTPClientError):
    pass
# WARNING: Decompyle incomplete


class HTTPNotAcceptable(HTTPClientError):
    status_code = 406


class HTTPProxyAuthenticationRequired(HTTPClientError):
    status_code = 407


class HTTPRequestTimeout(HTTPClientError):
    status_code = 408


class HTTPConflict(HTTPClientError):
    status_code = 409


class HTTPGone(HTTPClientError):
    status_code = 410


class HTTPLengthRequired(HTTPClientError):
    status_code = 411


class HTTPPreconditionFailed(HTTPClientError):
    status_code = 412


class HTTPRequestEntityTooLarge(HTTPClientError):
    pass
# WARNING: Decompyle incomplete


class HTTPRequestURITooLong(HTTPClientError):
    status_code = 414


class HTTPUnsupportedMediaType(HTTPClientError):
    status_code = 415


class HTTPRequestRangeNotSatisfiable(HTTPClientError):
    status_code = 416


class HTTPExpectationFailed(HTTPClientError):
    status_code = 417


class HTTPMisdirectedRequest(HTTPClientError):
    status_code = 421


class HTTPUnprocessableEntity(HTTPClientError):
    status_code = 422


class HTTPFailedDependency(HTTPClientError):
    status_code = 424


class HTTPUpgradeRequired(HTTPClientError):
    status_code = 426


class HTTPPreconditionRequired(HTTPClientError):
    status_code = 428


class HTTPTooManyRequests(HTTPClientError):
    status_code = 429


class HTTPRequestHeaderFieldsTooLarge(HTTPClientError):
    status_code = 431


class HTTPUnavailableForLegalReasons(HTTPClientError):
    pass
# WARNING: Decompyle incomplete


class HTTPServerError(HTTPError):
    pass


class HTTPInternalServerError(HTTPServerError):
    status_code = 500


class HTTPNotImplemented(HTTPServerError):
    status_code = 501


class HTTPBadGateway(HTTPServerError):
    status_code = 502


class HTTPServiceUnavailable(HTTPServerError):
    status_code = 503


class HTTPGatewayTimeout(HTTPServerError):
    status_code = 504


class HTTPVersionNotSupported(HTTPServerError):
    status_code = 505


class HTTPVariantAlsoNegotiates(HTTPServerError):
    status_code = 506


class HTTPInsufficientStorage(HTTPServerError):
    status_code = 507


class HTTPNotExtended(HTTPServerError):
    status_code = 510


class HTTPNetworkAuthenticationRequired(HTTPServerError):
    status_code = 511
