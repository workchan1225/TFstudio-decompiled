# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: base.pyc (Python 3.11)

from __future__ import annotations
from collections.abc import Sequence
from frames import Frame
from typing import ExtensionName, ExtensionParameter
__all__ = [
    'Extension',
    'ClientExtensionFactory',
    'ServerExtensionFactory']

class Extension:
    name: 'ExtensionName' = '\n    Base class for extensions.\n\n    '
    
    def decode(self = None, frame = None, *, max_size):
        '''
        Decode an incoming frame.

        Args:
            frame: Incoming frame.
            max_size: Maximum payload size in bytes.

        Returns:
            Decoded frame.

        Raises:
            PayloadTooBig: If decoding the payload exceeds ``max_size``.

        '''
        raise NotImplementedError

    
    def encode(self = None, frame = None):
        '''
        Encode an outgoing frame.

        Args:
            frame: Outgoing frame.

        Returns:
            Encoded frame.

        '''
        raise NotImplementedError



class ClientExtensionFactory:
    name: 'ExtensionName' = '\n    Base class for client-side extension factories.\n\n    '
    
    def get_request_params(self = None):
        '''
        Build parameters to send to the server for this extension.

        Returns:
            Parameters to send to the server.

        '''
        raise NotImplementedError

    
    def process_response_params(self = None, params = None, accepted_extensions = None):
        """
        Process parameters received from the server.

        Args:
            params: Parameters received from the server for this extension.
            accepted_extensions: List of previously accepted extensions.

        Returns:
            An extension instance.

        Raises:
            NegotiationError: If parameters aren't acceptable.

        """
        raise NotImplementedError



class ServerExtensionFactory:
    name: 'ExtensionName' = '\n    Base class for server-side extension factories.\n\n    '
    
    def process_request_params(self = None, params = None, accepted_extensions = None):
        """
        Process parameters received from the client.

        Args:
            params: Parameters received from the client for this extension.
            accepted_extensions: List of previously accepted extensions.

        Returns:
            To accept the offer, parameters to send to the client for this
            extension and an extension instance.

        Raises:
            NegotiationError: To reject the offer, if parameters received from
                the client aren't acceptable.

        """
        raise NotImplementedError
