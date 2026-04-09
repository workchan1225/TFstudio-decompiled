# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webauthn_handler.pyc (Python 3.11)

import abc
import os
import struct
import subprocess
from google.auth import exceptions
from google.oauth2.webauthn_types import GetRequest, GetResponse

class WebAuthnHandler(abc.ABC):
    is_available = (lambda self = None: raise NotImplementedError('is_available method must be implemented'))()
    get = (lambda self = None, get_request = None: raise NotImplementedError('get method must be implemented'))()


class PluginHandler(WebAuthnHandler):
    '''Offloads WebAuthn get reqeust to a pluggable command-line tool.

    Offloads WebAuthn get to a plugin which takes the form of a
    command-line tool. The command-line tool is configurable via the
    PluginHandler._ENV_VAR environment variable.

    The WebAuthn plugin should implement the following interface:

    Communication occurs over stdin/stdout, and messages are both sent and
    received in the form:

    [4 bytes - payload size (little-endian)][variable bytes - json payload]
    '''
    _ENV_VAR = 'GOOGLE_AUTH_WEBAUTHN_PLUGIN'
    
    def is_available(self = None):
        
        try:
            self._find_plugin()
            return True
        except Exception:
            return False


    
    def get(self = None, get_request = None):
        request_json = get_request.to_json()
        cmd = self._find_plugin()
        response_json = self._call_plugin(cmd, request_json)
        return GetResponse.from_json(response_json)

    
    def _call_plugin(self = None, cmd = None, input_json = None):
        input_length = len(input_json)
        length_bytes_le = struct.pack('<I', input_length)
        request = length_bytes_le + input_json.encode()
        process_result = subprocess.run([
            cmd], input = request, capture_output = True, check = True)
        response_len_le = process_result.stdout[:4]
        response_len = struct.unpack('<I', response_len_le)[0]
        response = process_result.stdout[4:]
        if response_len != len(response):
            raise exceptions.MalformedError('Plugin response length {} does not match data {}'.format(response_len, len(response)))
        return response.decode()

    
    def _find_plugin(self = None):
        plugin_cmd = os.environ.get(PluginHandler._ENV_VAR)
    # WARNING: Decompyle incomplete
