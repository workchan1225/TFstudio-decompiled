# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: parameters.pyc (Python 3.11)

'''
oauthlib.parameters
~~~~~~~~~~~~~~~~~~~

This module contains methods related to `section 3.5`_ of the OAuth 1.0a spec.

.. _`section 3.5`: https://tools.ietf.org/html/rfc5849#section-3.5
'''
from urllib.parse import urlparse, urlunparse
from oauthlib.common import extract_params, urlencode
from  import utils
prepare_headers = (lambda oauth_params, headers, realm = (None, None): if not headers:
headers = { }authorization_header_parameters_parts = []for oauth_parameter_name, value in oauth_params:
escaped_name = utils.escape(oauth_parameter_name)escaped_value = utils.escape(value)part = '{}="{}"'.format(escaped_name, escaped_value)authorization_header_parameters_parts.append(part)authorization_header_parameters = ', '.join(authorization_header_parameters_parts)if realm:
authorization_header_parameters = 'realm="%s", ' % realm + authorization_header_parametersauthorization_header = 'OAuth %s' % authorization_header_parametersfull_headers = { }full_headers.update(headers)full_headers['Authorization'] = authorization_headerfull_headers)()

def _append_params(oauth_params, params):
    '''Append OAuth params to an existing set of parameters.

    Both params and oauth_params is must be lists of 2-tuples.

    Per `section 3.5.2`_ and `3.5.3`_ of the spec.

    .. _`section 3.5.2`: https://tools.ietf.org/html/rfc5849#section-3.5.2
    .. _`3.5.3`: https://tools.ietf.org/html/rfc5849#section-3.5.3

    '''
    merged = list(params)
    merged.extend(oauth_params)
    merged.sort(key = (lambda i: i[0].startswith('oauth_')))
    return merged


def prepare_form_encoded_body(oauth_params, body):
    '''Prepare the Form-Encoded Body.

    Per `section 3.5.2`_ of the spec.

    .. _`section 3.5.2`: https://tools.ietf.org/html/rfc5849#section-3.5.2

    '''
    return _append_params(oauth_params, body)


def prepare_request_uri_query(oauth_params, uri):
