# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: core.pyc (Python 3.11)

'''
    core
    ~~~~
    Core functionality shared between the extension and the decorator.

    :copyright: (c) 2016 by Cory Dolphin.
    :license: MIT, see LICENSE for more details.
'''
import re
import logging
from collections.abc import Iterable
from datetime import timedelta
from flask import request, current_app
from werkzeug.datastructures import Headers, MultiDict
LOG = logging.getLogger(__name__)
ACL_ORIGIN = 'Access-Control-Allow-Origin'
ACL_METHODS = 'Access-Control-Allow-Methods'
ACL_ALLOW_HEADERS = 'Access-Control-Allow-Headers'
ACL_EXPOSE_HEADERS = 'Access-Control-Expose-Headers'
ACL_CREDENTIALS = 'Access-Control-Allow-Credentials'
ACL_MAX_AGE = 'Access-Control-Max-Age'
ACL_RESPONSE_PRIVATE_NETWORK = 'Access-Control-Allow-Private-Network'
ACL_REQUEST_METHOD = 'Access-Control-Request-Method'
ACL_REQUEST_HEADERS = 'Access-Control-Request-Headers'
ACL_REQUEST_HEADER_PRIVATE_NETWORK = 'Access-Control-Request-Private-Network'
ALL_METHODS = [
    'GET',
    'HEAD',
    'POST',
    'OPTIONS',
    'PUT',
    'PATCH',
    'DELETE']
CONFIG_OPTIONS = [
    'CORS_ORIGINS',
    'CORS_METHODS',
    'CORS_ALLOW_HEADERS',
    'CORS_EXPOSE_HEADERS',
    'CORS_SUPPORTS_CREDENTIALS',
    'CORS_MAX_AGE',
    'CORS_SEND_WILDCARD',
    'CORS_AUTOMATIC_OPTIONS',
    'CORS_VARY_HEADER',
    'CORS_RESOURCES',
    'CORS_INTERCEPT_EXCEPTIONS',
    'CORS_ALWAYS_SEND']
FLASK_CORS_EVALUATED = '_FLASK_CORS_EVALUATED'
RegexObject = type(re.compile(''))
DEFAULT_OPTIONS = dict(origins = '*', methods = ALL_METHODS, allow_headers = '*', expose_headers = None, supports_credentials = False, max_age = None, send_wildcard = False, automatic_options = True, vary_header = True, resources = '/*', intercept_exceptions = True, always_send = True)

def parse_resources(resources):
    if isinstance(resources, dict):
        resources = resources.items()()
        
        def pattern_length(pair):
            (maybe_regex, _) = pair
            return len(get_regexp_pattern(maybe_regex))

        return sorted(resources, key = pattern_length, reverse = True)
    if None(resources, str):
        return [
            (re_fix(resources), { })]
    if None(resources, Iterable):
        return resources()
    if None(resources, RegexObject):
        return [
            (re_fix(resources), { })]
    raise None('Unexpected value for resources argument.')


def get_regexp_pattern(regexp):
    '''
    Helper that returns regexp pattern from given value.

    :param regexp: regular expression to stringify
    :type regexp: _sre.SRE_Pattern or str
    :returns: string representation of given regexp pattern
    :rtype: str
    '''
    
    try:
        return regexp.pattern
    except AttributeError:
        return 



def get_cors_origins(options, request_origin):
    origins = options.get('origins')
    wildcard = '.*' in origins
    if request_origin:
        LOG.debug("CORS request received with 'Origin' %s", request_origin)
        if wildcard and options.get('send_wildcard'):
            LOG.debug("Allowed origins are set to '*'. Sending wildcard CORS header.")
            return [
                '*']
        if None(request_origin, origins):
            LOG.debug("The request's Origin header matches. Sending CORS headers.")
            return [
                request_origin]
        None.debug("The request's Origin header does not match any of allowed origins.")
        return None
    if None.get('always_send'):
        if wildcard:
            if options.get('supports_credentials'):
                return None
            return [
                None]
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(origins())
    None.debug("The request did not contain an 'Origin' header. This means the browser or client did not request CORS, ensure the Origin Header is set.")


def get_allow_headers(options, acl_request_headers):
    pass
# WARNING: Decompyle incomplete


def get_cors_headers(options, request_headers, request_method):
    origins_to_set = get_cors_origins(options, request_headers.get('Origin'))
    headers = MultiDict()
    if not origins_to_set:
        return headers
    for origin in None:
        headers.add(ACL_ORIGIN, origin)
        headers[ACL_EXPOSE_HEADERS] = options.get('expose_headers')
        if options.get('supports_credentials'):
            headers[ACL_CREDENTIALS] = 'true'
    if ACL_REQUEST_HEADER_PRIVATE_NETWORK in request_headers and request_headers.get(ACL_REQUEST_HEADER_PRIVATE_NETWORK) == 'true':
        headers[ACL_RESPONSE_PRIVATE_NETWORK] = 'true'
    if request_method == 'OPTIONS':
        acl_request_method = request_headers.get(ACL_REQUEST_METHOD, '').upper()
        if acl_request_method and acl_request_method in options.get('methods'):
            headers[ACL_ALLOW_HEADERS] = get_allow_headers(options, request_headers.get(ACL_REQUEST_HEADERS))
            headers[ACL_MAX_AGE] = options.get('max_age')
            headers[ACL_METHODS] = options.get('methods')
        else:
            LOG.info("The request's Access-Control-Request-Method header does not match allowed methods. CORS headers will not be applied.")
    if options.get('vary_header'):
        if headers[ACL_ORIGIN] == '*':
            pass
        elif len(options.get('origins')) > 1 and len(origins_to_set) > 1 or any(map(probably_regex, options.get('origins'))):
            headers.add('Vary', 'Origin')
    return (lambda .0: pass# WARNING: Decompyle incomplete
)(headers.items()())


def set_cors_headers(resp, options):
    '''
    Performs the actual evaluation of Flask-CORS options and actually
    modifies the response object.

    This function is used both in the decorator and the after_request
    callback
    '''
    if hasattr(resp, FLASK_CORS_EVALUATED):
        LOG.debug('CORS have been already evaluated, skipping')
        return resp
    if not None(resp.headers, Headers) and isinstance(resp.headers, MultiDict):
        resp.headers = MultiDict(resp.headers)
    headers_to_set = get_cors_headers(options, request.headers, request.method)
    LOG.debug('Settings CORS headers: %s', str(headers_to_set))
    for k, v in headers_to_set.items():
        resp.headers.add(k, v)
        return resp


def probably_regex(maybe_regex):
    pass
# WARNING: Decompyle incomplete


def re_fix(reg):
    """
        Replace the invalid regex r'*' with the valid, wildcard regex r'/.*' to
        enable the CORS app extension to have a more user friendly api.
    """
    return '.*' if reg == '*' else reg


def try_match_any(inst, patterns):
    pass
# WARNING: Decompyle incomplete


def try_match(request_origin, maybe_regex):
    '''Safely attempts to match a pattern or string to a request origin.'''
    if isinstance(maybe_regex, RegexObject):
        return re.match(maybe_regex, request_origin)
    if None(maybe_regex):
        return re.match(maybe_regex, request_origin, flags = re.IGNORECASE)
    
    try:
        return request_origin.lower() == maybe_regex.lower()
    except AttributeError:
        return 



def get_cors_options(appInstance, *dicts):
    """
    Compute CORS options for an application by combining the DEFAULT_OPTIONS,
    the app's configuration-specified options and any dictionaries passed. The
    last specified option wins.
    """
    options = DEFAULT_OPTIONS.copy()
    options.update(get_app_kwarg_dict(appInstance))
    if dicts:
        for d in dicts:
            options.update(d)
            return serialize_options(options)


def get_app_kwarg_dict(appInstance = (None,)):
    '''Returns the dictionary of CORS specific app configurations.'''
    pass
# WARNING: Decompyle incomplete


def flexible_str(obj):
    '''
    A more flexible str function which intelligently handles stringifying
    strings, lists and other iterables. The results are lexographically sorted
    to ensure generated responses are consistent when iterables such as Set
    are used.
    '''
    pass
# WARNING: Decompyle incomplete


def serialize_option(options_dict, key, upper = (False,)):
    if key in options_dict:
        value = flexible_str(options_dict[key])
        options_dict[key] = value.upper() if upper else value
        return None


def ensure_iterable(inst):
    '''
    Wraps scalars or string types as a list, or returns the iterable instance.
    '''
    if isinstance(inst, str):
        return [
            inst]
    if not None(inst, Iterable):
        return [
            inst]


def sanitize_regex_param(param):
    return ensure_iterable(param)()


def serialize_options(opts):
    '''
    A helper method to serialize and processes the options dictionary.
    '''
    if not opts:
        options = { }.copy()
        for key in opts.keys():
            if key not in DEFAULT_OPTIONS:
                LOG.warning('Unknown option passed to Flask-CORS: %s', key)
            options['origins'] = sanitize_regex_param(options.get('origins'))
            options['allow_headers'] = sanitize_regex_param(options.get('allow_headers'))
            if '.*' in options['origins'] and options['supports_credentials'] and options['send_wildcard']:
                raise ValueError("Cannot use supports_credentials in conjunction withan origin string of '*'. See: http://www.w3.org/TR/cors/#resource-requests")
            serialize_option(options, 'expose_headers')
            serialize_option(options, 'methods', upper = True)
            if isinstance(options.get('max_age'), timedelta):
                options['max_age'] = str(int(options['max_age'].total_seconds()))
    return options
