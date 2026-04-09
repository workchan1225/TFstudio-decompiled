# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: model.pyc (Python 3.11)

'''Model objects for requests and responses.

Each API may support one or more serializations, such
as JSON, Atom, etc. The model classes are responsible
for converting between the wire format and the Python
object representation.
'''
from __future__ import absolute_import
__author__ = 'jcgregorio@google.com (Joe Gregorio)'
import json
import logging
import platform
import urllib
import warnings
from googleapiclient import version as googleapiclient_version
from googleapiclient.errors import HttpError

try:
    from google.api_core.version_header import API_VERSION_METADATA_KEY
    HAS_API_VERSION = True
except ImportError:
    HAS_API_VERSION = False

_LIBRARY_VERSION = googleapiclient_version.__version__
_PY_VERSION = platform.python_version()
LOGGER = logging.getLogger(__name__)
dump_request_response = False

def _abstract():
    raise NotImplementedError('You need to override this function')


class Model(object):
    '''Model base class.

    All Model classes should implement this interface.
    The Model serializes and de-serializes between a wire
    format such as JSON and a Python object representation.
    '''
    
    def request(self, headers, path_params, query_params, body_value):
        '''Updates outgoing requests with a serialized body.

        Args:
          headers: dict, request headers
          path_params: dict, parameters that appear in the request path
          query_params: dict, parameters that appear in the query
          body_value: object, the request body as a Python object, which must be
                      serializable.
        Returns:
          A tuple of (headers, path_params, query, body)

          headers: dict, request headers
          path_params: dict, parameters that appear in the request path
          query: string, query part of the request URI
          body: string, the body serialized in the desired wire format.
        '''
        _abstract()

    
    def response(self, resp, content):
        '''Convert the response wire format into a Python object.

        Args:
          resp: httplib2.Response, the HTTP response headers and status
          content: string, the body of the HTTP response

        Returns:
          The body de-serialized as a Python object.

        Raises:
          googleapiclient.errors.HttpError if a non 2xx response is received.
        '''
        _abstract()



class BaseModel(Model):
    '''Base model class.

    Subclasses should provide implementations for the "serialize" and
    "deserialize" methods, as well as values for the following class attributes.

    Attributes:
      accept: The value to use for the HTTP Accept header.
      content_type: The value to use for the HTTP Content-type header.
      no_content_response: The value to return when deserializing a 204 "No
          Content" response.
      alt_param: The value to supply as the "alt" query parameter for requests.
    '''
    accept = None
    content_type = None
    no_content_response = None
    alt_param = None
    
    def _log_request(self, headers, path_params, query, body):
        '''Logs debugging information about the request if requested.'''
        if dump_request_response:
            LOGGER.info('--request-start--')
            LOGGER.info('-headers-start-')
            for h, v in headers.items():
                LOGGER.info('%s: %s', h, v)
                LOGGER.info('-headers-end-')
                LOGGER.info('-path-parameters-start-')
                for h, v in path_params.items():
                    LOGGER.info('%s: %s', h, v)
                    LOGGER.info('-path-parameters-end-')
                    LOGGER.info('body: %s', body)
                    LOGGER.info('query: %s', query)
                    LOGGER.info('--request-end--')
                    return None
                    return None

    
    def request(self, headers, path_params, query_params, body_value, api_version = (None,)):
        '''Updates outgoing requests with a serialized body.

        Args:
          headers: dict, request headers
          path_params: dict, parameters that appear in the request path
          query_params: dict, parameters that appear in the query
          body_value: object, the request body as a Python object, which must be
              serializable by json.
          api_version: str, The precise API version represented by this request,
              which will result in an API Version header being sent along with the
              HTTP request.
        Returns:
          A tuple of (headers, path_params, query, body)

          headers: dict, request headers
          path_params: dict, parameters that appear in the request path
          query: string, query part of the request URI
          body: string, the body serialized as JSON
        '''
        query = self._build_query(query_params)
        headers['accept'] = self.accept
        headers['accept-encoding'] = 'gzip, deflate'
        if 'user-agent' in headers:
            pass
        else:
            '' = None
        if 'x-goog-api-client' in headers:
            pass
        else:
            '' = None
        if api_version and HAS_API_VERSION:
            api_version = None
        elif api_version:
            warnings.warn('The `api_version` argument is ignored as a newer version of `google-api-core` is required to use this feature.Please upgrade `google-api-core` to 2.19.0 or newer.')
    # WARNING: Decompyle incomplete

    
    def _build_query(self, params):
        '''Builds a query string.

        Args:
          params: dict, the query parameters

        Returns:
          The query parameters properly encoded into an HTTP URI query string.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def _log_response(self, resp, content):
        '''Logs debugging information about the response if requested.'''
        if dump_request_response:
            LOGGER.info('--response-start--')
            for h, v in resp.items():
                LOGGER.info('%s: %s', h, v)
                if content:
                    LOGGER.info(content)
            LOGGER.info('--response-end--')
            return None

    
    def response(self, resp, content):
        '''Convert the response wire format into a Python object.

        Args:
          resp: httplib2.Response, the HTTP response headers and status
          content: string, the body of the HTTP response

        Returns:
          The body de-serialized as a Python object.

        Raises:
          googleapiclient.errors.HttpError if a non 2xx response is received.
        '''
        self._log_response(resp, content)
        if resp.status < 300:
            if resp.status == 204:
                return self.no_content_response
            return None.deserialize(content)
        None.debug('Content from bad request was: %r' % content)
        raise HttpError(resp, content)

    
    def serialize(self, body_value):
        '''Perform the actual Python object serialization.

        Args:
          body_value: object, the request body as a Python object.

        Returns:
          string, the body in serialized form.
        '''
        _abstract()

    
    def deserialize(self, content):
        '''Perform the actual deserialization from response string to Python
        object.

        Args:
          content: string, the body of the HTTP response

        Returns:
          The body de-serialized as a Python object.
        '''
        _abstract()



class JsonModel(BaseModel):
    '''Model class for JSON.

    Serializes and de-serializes between JSON and the Python
    object representation of HTTP request and response bodies.
    '''
    accept = 'application/json'
    content_type = 'application/json'
    alt_param = 'json'
    
    def __init__(self, data_wrapper = (False,)):
        '''Construct a JsonModel.

        Args:
          data_wrapper: boolean, wrap requests and responses in a data wrapper
        '''
        self._data_wrapper = data_wrapper

    
    def serialize(self, body_value):
        if isinstance(body_value, dict) and 'data' not in body_value and self._data_wrapper:
            body_value = {
                'data': body_value }
        return json.dumps(body_value)

    
    def deserialize(self, content):
