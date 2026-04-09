# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: webauthn_handler_factory.pyc (Python 3.11)

from typing import List, Optional
from google.oauth2.webauthn_handler import PluginHandler, WebAuthnHandler

class WebauthnHandlerFactory:
    handlers: List[WebAuthnHandler] = 'WebauthnHandlerFactory'
    
    def __init__(self):
        self.handlers = [
            PluginHandler()]

    
    def get_handler(self = None):
        for handler in self.handlers:
            if handler.is_available():
                
                return None, handler
            return None
