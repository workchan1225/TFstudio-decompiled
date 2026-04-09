# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: pre_configured.pyc (Python 3.11)

from  import AccessTokenEndpoint, AuthorizationEndpoint, RequestTokenEndpoint, ResourceEndpoint

class WebApplicationServer(ResourceEndpoint, AccessTokenEndpoint, AuthorizationEndpoint, RequestTokenEndpoint):
    
    def __init__(self, request_validator):
        RequestTokenEndpoint.__init__(self, request_validator)
        AuthorizationEndpoint.__init__(self, request_validator)
        AccessTokenEndpoint.__init__(self, request_validator)
        ResourceEndpoint.__init__(self, request_validator)
