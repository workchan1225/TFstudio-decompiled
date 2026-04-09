# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: tokens.pyc (Python 3.11)

'''[Experimental] Auth Tokens API client.'''
import json
import logging
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode
from  import _api_module
from  import _common
from  import _tokens_converters as tokens_converters
from  import types
logger = logging.getLogger('google_genai.tokens')

def _get_field_masks(setup = None):
    '''Return field_masks'''
    pass
# WARNING: Decompyle incomplete


def _convert_bidi_setup_to_token_setup(request_dict = None, config = None):
    '''Converts bidiGenerateContentSetup.'''
    bidi_setup = request_dict.get('bidiGenerateContentSetup')
# WARNING: Decompyle incomplete


class Tokens(_api_module.BaseModule):
    '''[Experimental] Auth Tokens API client.

  This class provides methods for creating auth tokens.
  '''
    create = (lambda self = None, *, config: parameter_model = types.CreateAuthTokenParameters(config = config)if self._api_client.vertexai:
raise ValueError('This method is only supported in the Gemini Developer client.')request_dict = tokens_converters._CreateAuthTokenParameters_to_mldev(self._api_client, parameter_model)request_url_dict = request_dict.get('_url')if request_url_dict:
path = 'auth_tokens'.format_map(request_url_dict)else:
path = 'auth_tokens'query_params = request_dict.get('_query')if query_params:
path = f'''{path}?{urlencode(query_params)}'''request_dict.pop('config', None)if request_dict:
request_dict = _convert_bidi_setup_to_token_setup(request_dict, config)http_options = None# WARNING: Decompyle incomplete
)()


class AsyncTokens(_api_module.BaseModule):
    '''[Experimental] Async Auth Tokens API client.

  This class provides asynchronous methods for creating auth tokens.
  '''
    create = (lambda self = None, *, config: pass# WARNING: Decompyle incomplete
)()
