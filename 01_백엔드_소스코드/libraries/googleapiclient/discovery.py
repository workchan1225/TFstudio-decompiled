# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: discovery.pyc (Python 3.11)

"""Client for discovery based APIs.

A client library for Google's discovery based APIs.
"""
from __future__ import absolute_import
__author__ = 'jcgregorio@google.com (Joe Gregorio)'
__all__ = [
    'build',
    'build_from_document',
    'fix_method_name',
    'key2param']
from collections import OrderedDict
import collections.abc as collections
import copy
from email.generator import BytesGenerator
from email.mime.multipart import MIMEMultipart
from email.mime.nonmultipart import MIMENonMultipart
from http.client import client as http_client
import io
import json
import keyword
import logging
import mimetypes
import os
import re
import urllib
import google.api_core.client_options as google
from google.auth.exceptions import MutualTLSChannelError
from google.auth.transport import mtls
from google.oauth2 import service_account
import httplib2
import uritemplate

try:
    import google_auth_httplib2
except ImportError:
    google_auth_httplib2 = None


try:
    from google.api_core import universe
    HAS_UNIVERSE = True
except ImportError:
    HAS_UNIVERSE = False

from googleapiclient import _auth, mimeparse
from googleapiclient._helpers import _add_query_parameter, positional
from googleapiclient.errors import HttpError, InvalidJsonError, MediaUploadSizeError, UnacceptableMimeTypeError, UnknownApiNameOrVersion, UnknownFileType
from googleapiclient.http import BatchHttpRequest, HttpMock, HttpMockSequence, HttpRequest, MediaFileUpload, MediaUpload, build_http
from googleapiclient.model import JsonModel, MediaModel, RawModel
from googleapiclient.schema import Schemas
httplib2.RETRIES = 1
logger = logging.getLogger(__name__)
URITEMPLATE = re.compile('{[^}]*}')
VARNAME = re.compile('[a-zA-Z0-9_-]+')
DISCOVERY_URI = 'https://www.googleapis.com/discovery/v1/apis/{api}/{apiVersion}/rest'
V1_DISCOVERY_URI = DISCOVERY_URI
V2_DISCOVERY_URI = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'
DEFAULT_METHOD_DOC = 'A description of how to use this function'
HTTP_PAYLOAD_METHODS = frozenset([
    'PUT',
    'POST',
    'PATCH'])
_MEDIA_SIZE_BIT_SHIFTS = {
    'KB': 10,
    'MB': 20,
    'GB': 30,
    'TB': 40 }
BODY_PARAMETER_DEFAULT_VALUE = {
    'description': 'The request body.',
    'type': 'object' }
MEDIA_BODY_PARAMETER_DEFAULT_VALUE = {
    'description': 'The filename of the media request body, or an instance of a MediaUpload object.',
    'type': 'string',
    'required': False }
MEDIA_MIME_TYPE_PARAMETER_DEFAULT_VALUE = {
    'description': 'The MIME type of the media request body, or an instance of a MediaUpload object.',
    'type': 'string',
    'required': False }
_PAGE_TOKEN_NAMES = ('pageToken', 'nextPageToken')
GOOGLE_API_USE_CLIENT_CERTIFICATE = 'GOOGLE_API_USE_CLIENT_CERTIFICATE'
GOOGLE_API_USE_MTLS_ENDPOINT = 'GOOGLE_API_USE_MTLS_ENDPOINT'
GOOGLE_CLOUD_UNIVERSE_DOMAIN = 'GOOGLE_CLOUD_UNIVERSE_DOMAIN'
DEFAULT_UNIVERSE = 'googleapis.com'
STACK_QUERY_PARAMETERS = frozenset([
    'trace',
    'pp',
    'userip',
    'strict'])
STACK_QUERY_PARAMETER_DEFAULT_VALUE = {
    'type': 'string',
    'location': 'query' }

class APICoreVersionError(ValueError):
    pass
# WARNING: Decompyle incomplete

RESERVED_WORDS = frozenset([
    'body'])

class _BytesGenerator(BytesGenerator):
    _write_lines = BytesGenerator.write


def fix_method_name(name):
    """Fix method names to avoid '$' characters and reserved word conflicts.

    Args:
      name: string, method name.

    Returns:
      The name with '_' appended if the name is a reserved word and '$' and '-'
      replaced with '_'.
    """
    name = name.replace('$', '_').replace('-', '_')
    if keyword.iskeyword(name) or name in RESERVED_WORDS:
        return name + '_'


def key2param(key):
    '''Converts key names into parameter names.

    For example, converting "max-results" -> "max_results"

    Args:
      key: string, the method key name.

    Returns:
      A safe method name based on the key name.
    '''
    result = []
    key = list(key)
    if not key[0].isalpha():
        result.append('x')
    for c in key:
        if c.isalnum():
            result.append(c)
            continue
        result.append('_')
        return ''.join(result)

build = (lambda serviceName, version, http, discoveryServiceUrl, developerKey, model, requestBuilder, credentials, cache_discovery, cache, client_options, adc_cert_path, adc_key_path, num_retries, static_discovery, always_use_jwt_access = (None, None, None, None, HttpRequest, None, True, None, None, None, None, 1, None, False): params = {
'api': serviceName,
'apiVersion': version }# WARNING: Decompyle incomplete
)()

def _discovery_service_uri_options(discoveryServiceUrl, version):
    '''
      Returns Discovery URIs to be used for attempting to build the API Resource.

    Args:
      discoveryServiceUrl:
          string, the Original Discovery Service URL preferred by the customer.
      version:
          string, API Version requested

    Returns:
        A list of URIs to be tried for the Service Discovery, in order.
    '''
    pass
# WARNING: Decompyle incomplete


def _retrieve_discovery_doc(url, http, cache_discovery, serviceName, version, cache, developerKey, num_retries, static_discovery = (None, None, 1, True)):
    '''Retrieves the discovery_doc from cache or the internet.

    Args:
      url: string, the URL of the discovery document.
      http: httplib2.Http, An instance of httplib2.Http or something that acts
        like it through which HTTP requests will be made.
      cache_discovery: Boolean, whether or not to cache the discovery doc.
      serviceName: string, name of the service.
      version: string, the version of the service.
      cache: googleapiclient.discovery_cache.base.Cache, an optional cache
        object for the discovery documents.
      developerKey: string, Key for controlling API usage, generated
        from the API Console.
      num_retries: Integer, number of times to retry discovery with
        randomized exponential backoff in case of intermittent/connection issues.
      static_discovery: Boolean, whether or not to use the static discovery docs
        included in the library.

    Returns:
      A unicode string representation of the discovery document.
    '''
    discovery_cache = discovery_cache
    import 
# WARNING: Decompyle incomplete


def _check_api_core_compatible_with_credentials_universe(credentials):
    if not HAS_UNIVERSE:
        credentials_universe = getattr(credentials, 'universe_domain', None)
        if credentials_universe or credentials_universe != DEFAULT_UNIVERSE:
            raise APICoreVersionError
    return None
    return None

build_from_document = (lambda service, base, future, http, developerKey, model, requestBuilder, credentials, client_options, adc_cert_path, adc_key_path, always_use_jwt_access = (None, None, None, None, None, HttpRequest, None, None, None, None, False): pass# WARNING: Decompyle incomplete
)()

def _cast(value, schema_type):
    """Convert value to a string based on JSON Schema type.

    See http://tools.ietf.org/html/draft-zyp-json-schema-03 for more details on
    JSON Schema.

    Args:
      value: any, the value to convert
      schema_type: string, the type that value should be interpreted as

    Returns:
      A string representation of 'value' based on the schema_type.
    """
    if schema_type == 'string':
        if type(value) == type('') or type(value) == type(''):
            return value
        return None(value)
    if None == 'integer':
        return str(int(value))
    if None == 'number':
        return str(float(value))
    if None == 'boolean':
        return str(bool(value)).lower()
    if None(value) == type('') or type(value) == type(''):
        return value
    return None(value)


def _media_size_to_long(maxSize):
    '''Convert a string media size, such as 10GB or 3TB into an integer.

    Args:
      maxSize: string, size as a string, such as 2MB or 7GB.

    Returns:
      The size as an integer value.
    '''
    if len(maxSize) < 2:
        return 0
    units = None[-2:].upper()
    bit_shift = _MEDIA_SIZE_BIT_SHIFTS.get(units)
# WARNING: Decompyle incomplete


def _media_path_url_from_info(root_desc, path_url):
    '''Creates an absolute media path URL.

    Constructed using the API root URI and service path from the discovery
    document and the relative path for the API method.

    Args:
      root_desc: Dictionary; the entire original deserialized discovery document.
      path_url: String; the relative URL for the API method. Relative to the API
          root, which is specified in the discovery document.

    Returns:
      String; the absolute URI for media upload for the API method.
    '''
    return '%(root)supload/%(service_path)s%(path)s' % {
        'root': root_desc['rootUrl'],
        'service_path': root_desc['servicePath'],
        'path': path_url }


def _fix_up_parameters(method_desc, root_desc, http_method, schema):
    """Updates parameters of an API method with values specific to this library.

    Specifically, adds whatever global parameters are specified by the API to the
    parameters for the individual method. Also adds parameters which don't
    appear in the discovery document, but are available to all discovery based
    APIs (these are listed in STACK_QUERY_PARAMETERS).

    SIDE EFFECTS: This updates the parameters dictionary object in the method
    description.

    Args:
      method_desc: Dictionary with metadata describing an API method. Value comes
          from the dictionary of methods stored in the 'methods' key in the
          deserialized discovery document.
      root_desc: Dictionary; the entire original deserialized discovery document.
      http_method: String; the HTTP method used to call the API method described
          in method_desc.
      schema: Object, mapping of schema names to schema descriptions.

    Returns:
      The updated Dictionary stored in the 'parameters' key of the method
          description dictionary.
    """
    parameters = method_desc.setdefault('parameters', { })
    for name, description in root_desc.get('parameters', { }).items():
        parameters[name] = description
        for name in STACK_QUERY_PARAMETERS:
            parameters[name] = STACK_QUERY_PARAMETER_DEFAULT_VALUE.copy()
            if http_method in HTTP_PAYLOAD_METHODS and 'request' in method_desc:
                body = BODY_PARAMETER_DEFAULT_VALUE.copy()
                body.update(method_desc['request'])
                parameters['body'] = body
    return parameters


def _fix_up_media_upload(method_desc, root_desc, path_url, parameters):
    """Adds 'media_body' and 'media_mime_type' parameters if supported by method.

    SIDE EFFECTS: If there is a 'mediaUpload' in the method description, adds
    'media_upload' key to parameters.

    Args:
      method_desc: Dictionary with metadata describing an API method. Value comes
          from the dictionary of methods stored in the 'methods' key in the
          deserialized discovery document.
      root_desc: Dictionary; the entire original deserialized discovery document.
      path_url: String; the relative URL for the API method. Relative to the API
          root, which is specified in the discovery document.
      parameters: A dictionary describing method parameters for method described
          in method_desc.

    Returns:
      Triple (accept, max_size, media_path_url) where:
        - accept is a list of strings representing what content types are
          accepted for media upload. Defaults to empty list if not in the
          discovery document.
        - max_size is a long representing the max size in bytes allowed for a
          media upload. Defaults to 0L if not in the discovery document.
        - media_path_url is a String; the absolute URI for media upload for the
          API method. Constructed using the API root URI and service path from
          the discovery document and the relative path for the API method. If
          media upload is not supported, this is None.
    """
    media_upload = method_desc.get('mediaUpload', { })
    accept = media_upload.get('accept', [])
    max_size = _media_size_to_long(media_upload.get('maxSize', ''))
    media_path_url = None
    if media_upload:
        media_path_url = _media_path_url_from_info(root_desc, path_url)
        parameters['media_body'] = MEDIA_BODY_PARAMETER_DEFAULT_VALUE.copy()
        parameters['media_mime_type'] = MEDIA_MIME_TYPE_PARAMETER_DEFAULT_VALUE.copy()
    return (accept, max_size, media_path_url)


def _fix_up_method_description(method_desc, root_desc, schema):
    """Updates a method description in a discovery document.

    SIDE EFFECTS: Changes the parameters dictionary in the method description with
    extra parameters which are used locally.

    Args:
      method_desc: Dictionary with metadata describing an API method. Value comes
          from the dictionary of methods stored in the 'methods' key in the
          deserialized discovery document.
      root_desc: Dictionary; the entire original deserialized discovery document.
      schema: Object, mapping of schema names to schema descriptions.

    Returns:
      Tuple (path_url, http_method, method_id, accept, max_size, media_path_url)
      where:
        - path_url is a String; the relative URL for the API method. Relative to
          the API root, which is specified in the discovery document.
        - http_method is a String; the HTTP method used to call the API method
          described in the method description.
        - method_id is a String; the name of the RPC method associated with the
          API method, and is in the method description in the 'id' key.
        - accept is a list of strings representing what content types are
          accepted for media upload. Defaults to empty list if not in the
          discovery document.
        - max_size is a long representing the max size in bytes allowed for a
          media upload. Defaults to 0L if not in the discovery document.
        - media_path_url is a String; the absolute URI for media upload for the
          API method. Constructed using the API root URI and service path from
          the discovery document and the relative path for the API method. If
          media upload is not supported, this is None.
    """
    path_url = method_desc['path']
    http_method = method_desc['httpMethod']
    method_id = method_desc['id']
    parameters = _fix_up_parameters(method_desc, root_desc, http_method, schema)
    (accept, max_size, media_path_url) = _fix_up_media_upload(method_desc, root_desc, path_url, parameters)
    return (path_url, http_method, method_id, accept, max_size, media_path_url)


def _fix_up_media_path_base_url(media_path_url, base_url):
    """
    Update the media upload base url if its netloc doesn't match base url netloc.

    This can happen in case the base url was overridden by
    client_options.api_endpoint.

    Args:
      media_path_url: String; the absolute URI for media upload.
      base_url: string, base URL for the API. All requests are relative to this URI.

    Returns:
      String; the absolute URI for media upload.
    """
    parsed_media_url = urllib.parse.urlparse(media_path_url)
    parsed_base_url = urllib.parse.urlparse(base_url)
    if parsed_media_url.netloc == parsed_base_url.netloc:
        return media_path_url
    return None.parse.urlunparse(parsed_media_url._replace(netloc = parsed_base_url.netloc))


def _urljoin(base, url):
    '''Custom urljoin replacement supporting : before / in url.'''
    if url.startswith('http://') or url.startswith('https://'):
        return urllib.parse.urljoin(base, url)
    new_base = base if None.endswith('/') else base + '/'
    new_url = url[1:] if url.startswith('/') else url
    return new_base + new_url


class ResourceMethodParameters(object):
    """Represents the parameters associated with a method.

    Attributes:
      argmap: Map from method parameter name (string) to query parameter name
          (string).
      required_params: List of required parameters (represented by parameter
          name as string).
      repeated_params: List of repeated parameters (represented by parameter
          name as string).
      pattern_params: Map from method parameter name (string) to regular
          expression (as a string). If the pattern is set for a parameter, the
          value for that parameter must match the regular expression.
      query_params: List of parameters (represented by parameter name as string)
          that will be used in the query string.
      path_params: Set of parameters (represented by parameter name as string)
          that will be used in the base URL path.
      param_types: Map from method parameter name (string) to parameter type. Type
          can be any valid JSON schema type; valid values are 'any', 'array',
          'boolean', 'integer', 'number', 'object', or 'string'. Reference:
          http://tools.ietf.org/html/draft-zyp-json-schema-03#section-5.1
      enum_params: Map from method parameter name (string) to list of strings,
         where each list of strings is the list of acceptable enum values.
    """
    
    def __init__(self, method_desc):
        """Constructor for ResourceMethodParameters.

        Sets default values and defers to set_parameters to populate.

        Args:
          method_desc: Dictionary with metadata describing an API method. Value
              comes from the dictionary of methods stored in the 'methods' key in
              the deserialized discovery document.
        """
        self.argmap = { }
        self.required_params = []
        self.repeated_params = []
        self.pattern_params = { }
        self.query_params = []
        self.path_params = set()
        self.param_types = { }
        self.enum_params = { }
        self.set_parameters(method_desc)

    
    def set_parameters(self, method_desc):
        """Populates maps and lists based on method description.

        Iterates through each parameter for the method and parses the values from
        the parameter dictionary.

        Args:
          method_desc: Dictionary with metadata describing an API method. Value
              comes from the dictionary of methods stored in the 'methods' key in
              the deserialized discovery document.
        """
        parameters = method_desc.get('parameters', { })
        sorted_parameters = OrderedDict(sorted(parameters.items()))
        for arg, desc in sorted_parameters.items():
            param = key2param(arg)
            self.argmap[param] = arg
            if desc.get('pattern'):
                self.pattern_params[param] = desc['pattern']
            if desc.get('enum'):
                self.enum_params[param] = desc['enum']
            if desc.get('required'):
                self.required_params.append(param)
            if desc.get('repeated'):
                self.repeated_params.append(param)
            if desc.get('location') == 'query':
                self.query_params.append(param)
            if desc.get('location') == 'path':
                self.path_params.add(param)
            self.param_types[param] = desc.get('type', 'string')
            for match in URITEMPLATE.finditer(method_desc['path']):
                for namematch in VARNAME.finditer(match.group(0)):
                    name = key2param(namematch.group(0))
                    self.path_params.add(name)
                    if name in self.query_params:
                        self.query_params.remove(name)
                    return None



def createMethod(methodName, methodDesc, rootDesc, schema):
    '''Creates a method for attaching to a Resource.

    Args:
      methodName: string, name of the method to use.
      methodDesc: object, fragment of deserialized discovery document that
        describes the method.
      rootDesc: object, the entire deserialized discovery document.
      schema: object, mapping of schema names to schema descriptions.
    '''
    pass
# WARNING: Decompyle incomplete


def createNextMethod(methodName, pageTokenName, nextPageTokenName, isPageTokenParameter = ('pageToken', 'nextPageToken', True)):
    '''Creates any _next methods for attaching to a Resource.

    The _next methods allow for easy iteration through list() responses.

    Args:
      methodName: string, name of the method to use.
      pageTokenName: string, name of request page token field.
      nextPageTokenName: string, name of response page token field.
      isPageTokenParameter: Boolean, True if request page token is a query
          parameter, False if request page token is a field of the request body.
    '''
    pass
# WARNING: Decompyle incomplete


class Resource(object):
    '''A class for interacting with a resource.'''
    
    def __init__(self, http, baseUrl, model, requestBuilder, developerKey, resourceDesc, rootDesc, schema, universe_domain = (universe.DEFAULT_UNIVERSE if HAS_UNIVERSE else '',)):
        '''Build a Resource from the API description.

        Args:
          http: httplib2.Http, Object to make http requests with.
          baseUrl: string, base URL for the API. All requests are relative to this
              URI.
          model: googleapiclient.Model, converts to and from the wire format.
          requestBuilder: class or callable that instantiates an
              googleapiclient.HttpRequest object.
          developerKey: string, key obtained from
              https://code.google.com/apis/console
          resourceDesc: object, section of deserialized discovery document that
              describes a resource. Note that the top level discovery document
              is considered a resource.
          rootDesc: object, the entire deserialized discovery document.
          schema: object, mapping of schema names to schema descriptions.
          universe_domain: string, the universe for the API. The default universe
          is "googleapis.com".
        '''
        self._dynamic_attrs = []
        self._http = http
        self._baseUrl = baseUrl
        self._model = model
        self._developerKey = developerKey
        self._requestBuilder = requestBuilder
        self._resourceDesc = resourceDesc
        self._rootDesc = rootDesc
        self._schema = schema
        self._universe_domain = universe_domain
        self._credentials_validated = False
        self._set_service_methods()

    
    def _set_dynamic_attr(self, attr_name, value):
        '''Sets an instance attribute and tracks it in a list of dynamic attributes.

        Args:
          attr_name: string; The name of the attribute to be set
          value: The value being set on the object and tracked in the dynamic cache.
        '''
        self._dynamic_attrs.append(attr_name)
        self.__dict__[attr_name] = value

    
    def __getstate__(self):
        '''Trim the state down to something that can be pickled.

        Uses the fact that the instance variable _dynamic_attrs holds attrs that
        will be wiped and restored on pickle serialization.
        '''
        state_dict = copy.copy(self.__dict__)
        for dynamic_attr in self._dynamic_attrs:
            del state_dict[dynamic_attr]
            del state_dict['_dynamic_attrs']
            return state_dict

    
    def __setstate__(self, state):
        '''Reconstitute the state of the object from being pickled.

        Uses the fact that the instance variable _dynamic_attrs holds attrs that
        will be wiped and restored on pickle serialization.
        '''
        self.__dict__.update(state)
        self._dynamic_attrs = []
        self._set_service_methods()

    
    def __enter__(self):
        return self

    
    def __exit__(self, exc_type, exc, exc_tb):
        self.close()

    
    def close(self):
        '''Close httplib2 connections.'''
        self._http.close()

    
    def _set_service_methods(self):
        self._add_basic_methods(self._resourceDesc, self._rootDesc, self._schema)
        self._add_nested_resources(self._resourceDesc, self._rootDesc, self._schema)
        self._add_next_methods(self._resourceDesc, self._schema)

    
    def _add_basic_methods(self, resourceDesc, rootDesc, schema):
        pass
    # WARNING: Decompyle incomplete

    
    def _add_nested_resources(self, resourceDesc, rootDesc, schema):
        pass
    # WARNING: Decompyle incomplete

    
    def _add_next_methods(self, resourceDesc, schema):
        if 'methods' not in resourceDesc:
            return None
        for methodName, methodDesc in None['methods'].items():
            nextPageTokenName = _findPageTokenName(_methodProperties(methodDesc, schema, 'response'))
            if not nextPageTokenName:
                continue
            isPageTokenParameter = True
            pageTokenName = _findPageTokenName(methodDesc.get('parameters', { }))
            if not pageTokenName:
                isPageTokenParameter = False
                pageTokenName = _findPageTokenName(_methodProperties(methodDesc, schema, 'request'))
            if not pageTokenName:
                continue
            (fixedMethodName, method) = createNextMethod(methodName + '_next', pageTokenName, nextPageTokenName, isPageTokenParameter)
            self._set_dynamic_attr(fixedMethodName, method.__get__(self, self.__class__))
            return None

    
    def _validate_credentials(self):
        """Validates client's and credentials' universe domains are consistent.

        Returns:
            bool: True iff the configured universe domain is valid.

        Raises:
            UniverseMismatchError: If the configured universe domain is not valid.
        """
        credentials = getattr(self._http, 'credentials', None)
        if HAS_UNIVERSE:
            pass
        self._credentials_validated = universe.compare_domains(self._universe_domain, credentials) if not self._credentials_validated else True
        return self._credentials_validated



def _findPageTokenName(fields):
    """Search field names for one like a page token.

    Args:
      fields: container of string, names of fields.

    Returns:
      First name that is either 'pageToken' or 'nextPageToken' if one exists,
      otherwise None.
    """
    pass
# WARNING: Decompyle incomplete


def _methodProperties(methodDesc, schema, name):
    """Get properties of a field in a method description.

    Args:
      methodDesc: object, fragment of deserialized discovery document that
        describes the method.
      schema: object, mapping of schema names to schema descriptions.
      name: string, name of top-level field in method description.

    Returns:
      Object representing fragment of deserialized discovery document
      corresponding to 'properties' field of object corresponding to named field
      in method description, if it exists, otherwise empty dict.
    """
    desc = methodDesc.get(name, { })
    if '$ref' in desc:
        desc = schema.get(desc['$ref'], { })
    return desc.get('properties', { })
