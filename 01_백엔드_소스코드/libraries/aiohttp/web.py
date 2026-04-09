# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web.pyc (Python 3.11)

import asyncio
import logging
import os
import socket
import sys
import warnings
from argparse import ArgumentParser
from collections.abc import Iterable
from contextlib import suppress
from importlib import import_module
from typing import TYPE_CHECKING, Any, Awaitable, Callable, Iterable as TypingIterable, List, Optional, Set, Type, Union, cast
from abc import AbstractAccessLogger
from helpers import AppKey
from log import access_logger
from typedefs import PathLike
from web_app import Application, CleanupError
from web_exceptions import HTTPAccepted, HTTPBadGateway, HTTPBadRequest, HTTPClientError, HTTPConflict, HTTPCreated, HTTPError, HTTPException, HTTPExpectationFailed, HTTPFailedDependency, HTTPForbidden, HTTPFound, HTTPGatewayTimeout, HTTPGone, HTTPInsufficientStorage, HTTPInternalServerError, HTTPLengthRequired, HTTPMethodNotAllowed, HTTPMisdirectedRequest, HTTPMove, HTTPMovedPermanently, HTTPMultipleChoices, HTTPNetworkAuthenticationRequired, HTTPNoContent, HTTPNonAuthoritativeInformation, HTTPNotAcceptable, HTTPNotExtended, HTTPNotFound, HTTPNotImplemented, HTTPNotModified, HTTPOk, HTTPPartialContent, HTTPPaymentRequired, HTTPPermanentRedirect, HTTPPreconditionFailed, HTTPPreconditionRequired, HTTPProxyAuthenticationRequired, HTTPRedirection, HTTPRequestEntityTooLarge, HTTPRequestHeaderFieldsTooLarge, HTTPRequestRangeNotSatisfiable, HTTPRequestTimeout, HTTPRequestURITooLong, HTTPResetContent, HTTPSeeOther, HTTPServerError, HTTPServiceUnavailable, HTTPSuccessful, HTTPTemporaryRedirect, HTTPTooManyRequests, HTTPUnauthorized, HTTPUnavailableForLegalReasons, HTTPUnprocessableEntity, HTTPUnsupportedMediaType, HTTPUpgradeRequired, HTTPUseProxy, HTTPVariantAlsoNegotiates, HTTPVersionNotSupported, NotAppKeyWarning
from web_fileresponse import FileResponse
from web_log import AccessLogger
from web_middlewares import middleware, normalize_path_middleware
from web_protocol import PayloadAccessError, RequestHandler, RequestPayloadError
from web_request import BaseRequest, FileField, Request
from web_response import ContentCoding, Response, StreamResponse, json_response
from web_routedef import AbstractRouteDef, RouteDef, RouteTableDef, StaticDef, delete, get, head, options, patch, post, put, route, static, view
from web_runner import AppRunner, BaseRunner, BaseSite, GracefulExit, NamedPipeSite, ServerRunner, SockSite, TCPSite, UnixSite
from web_server import Server
from web_urldispatcher import AbstractResource, AbstractRoute, DynamicResource, PlainResource, PrefixedSubAppResource, Resource, ResourceRoute, StaticResource, UrlDispatcher, UrlMappingMatchInfo, View
from web_ws import WebSocketReady, WebSocketResponse, WSMsgType
__all__ = ('AppKey', 'Application', 'CleanupError', 'NotAppKeyWarning', 'HTTPAccepted', 'HTTPBadGateway', 'HTTPBadRequest', 'HTTPClientError', 'HTTPConflict', 'HTTPCreated', 'HTTPError', 'HTTPException', 'HTTPExpectationFailed', 'HTTPFailedDependency', 'HTTPForbidden', 'HTTPFound', 'HTTPGatewayTimeout', 'HTTPGone', 'HTTPInsufficientStorage', 'HTTPInternalServerError', 'HTTPLengthRequired', 'HTTPMethodNotAllowed', 'HTTPMisdirectedRequest', 'HTTPMove', 'HTTPMovedPermanently', 'HTTPMultipleChoices', 'HTTPNetworkAuthenticationRequired', 'HTTPNoContent', 'HTTPNonAuthoritativeInformation', 'HTTPNotAcceptable', 'HTTPNotExtended', 'HTTPNotFound', 'HTTPNotImplemented', 'HTTPNotModified', 'HTTPOk', 'HTTPPartialContent', 'HTTPPaymentRequired', 'HTTPPermanentRedirect', 'HTTPPreconditionFailed', 'HTTPPreconditionRequired', 'HTTPProxyAuthenticationRequired', 'HTTPRedirection', 'HTTPRequestEntityTooLarge', 'HTTPRequestHeaderFieldsTooLarge', 'HTTPRequestRangeNotSatisfiable', 'HTTPRequestTimeout', 'HTTPRequestURITooLong', 'HTTPResetContent', 'HTTPSeeOther', 'HTTPServerError', 'HTTPServiceUnavailable', 'HTTPSuccessful', 'HTTPTemporaryRedirect', 'HTTPTooManyRequests', 'HTTPUnauthorized', 'HTTPUnavailableForLegalReasons', 'HTTPUnprocessableEntity', 'HTTPUnsupportedMediaType', 'HTTPUpgradeRequired', 'HTTPUseProxy', 'HTTPVariantAlsoNegotiates', 'HTTPVersionNotSupported', 'FileResponse', 'middleware', 'normalize_path_middleware', 'PayloadAccessError', 'RequestHandler', 'RequestPayloadError', 'BaseRequest', 'FileField', 'Request', 'ContentCoding', 'Response', 'StreamResponse', 'json_response', 'AbstractRouteDef', 'RouteDef', 'RouteTableDef', 'StaticDef', 'delete', 'get', 'head', 'options', 'patch', 'post', 'put', 'route', 'static', 'view', 'AppRunner', 'BaseRunner', 'BaseSite', 'GracefulExit', 'ServerRunner', 'SockSite', 'TCPSite', 'UnixSite', 'NamedPipeSite', 'Server', 'AbstractResource', 'AbstractRoute', 'DynamicResource', 'PlainResource', 'PrefixedSubAppResource', 'Resource', 'ResourceRoute', 'StaticResource', 'UrlDispatcher', 'UrlMappingMatchInfo', 'View', 'WebSocketReady', 'WebSocketResponse', 'WSMsgType', 'run_app')
if TYPE_CHECKING:
    from ssl import SSLContext
else:
    
    try:
        from ssl import SSLContext
    except ImportError:
        SSLContext = object

    warnings.filterwarnings('ignore', category = NotAppKeyWarning, append = True)
    HostSequence = TypingIterable[str]
    
    async def _run_app(app = None, *, host, port, path, sock, ssl_context, print, backlog, reuse_address, reuse_port, **kwargs):
        pass
    # WARNING: Decompyle incomplete

    
    def _cancel_tasks(to_cancel = None, loop = None):
        if not to_cancel:
            return None
    # WARNING: Decompyle incomplete

    
    def run_app(app = None, *, host, port, path, sock, shutdown_timeout, keepalive_timeout, ssl_context, print, backlog, access_log_class, access_log_format, access_log, handle_signals, reuse_address, reuse_port, handler_cancellation, loop, **kwargs):
        '''Run an app locally'''
        pass
    # WARNING: Decompyle incomplete

    
    def main(argv = None):
        arg_parser = ArgumentParser(description = 'aiohttp.web Application server', prog = 'aiohttp.web')
        arg_parser.add_argument('entry_func', help = "Callable returning the `aiohttp.web.Application` instance to run. Should be specified in the 'module:function' syntax.", metavar = 'entry-func')
        arg_parser.add_argument('-H', '--hostname', help = 'TCP/IP hostname to serve on (default: localhost)', default = None)
        arg_parser.add_argument('-P', '--port', help = 'TCP/IP port to serve on (default: %(default)r)', type = int, default = 8080)
        arg_parser.add_argument('-U', '--path', help = 'Unix file system path to serve on. Can be combined with hostname to serve on both Unix and TCP.')
        (args, extra_argv) = arg_parser.parse_known_args(argv)
        (mod_str, _, func_str) = args.entry_func.partition(':')
        if not func_str or mod_str:
            arg_parser.error("'entry-func' not in 'module:function' syntax")
        if mod_str.startswith('.'):
            arg_parser.error('relative module names not supported')
        
        try:
            module = import_module(mod_str)
        except ImportError:
            ex = None
            arg_parser.error(f'''unable to import {mod_str}: {ex}''')
            ex = None
            del ex
        except:
            ex = None
            del ex

        
        try:
            func = getattr(module, func_str)
        except AttributeError:
            arg_parser.error(f'''module {mod_str!r} has no attribute {func_str!r}''')

    # WARNING: Decompyle incomplete

    if __name__ == '__main__':
        main(sys.argv[1:])
        return None
    return None
