# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: error.pyc (Python 3.11)


class HttpLib2Error(Exception):
    pass


class HttpLib2ErrorWithResponse(HttpLib2Error):
    
    def __init__(self, desc, response, content):
        self.response = response
        self.content = content
        HttpLib2Error.__init__(self, desc)



class RedirectMissingLocation(HttpLib2ErrorWithResponse):
    pass


class RedirectLimit(HttpLib2ErrorWithResponse):
    pass


class FailedToDecompressContent(HttpLib2ErrorWithResponse):
    pass


class UnimplementedDigestAuthOptionError(HttpLib2ErrorWithResponse):
    pass


class UnimplementedHmacDigestAuthOptionError(HttpLib2ErrorWithResponse):
    pass


class MalformedHeader(HttpLib2Error):
    pass


class RelativeURIError(HttpLib2Error):
    pass


class ServerNotFoundError(HttpLib2Error):
    pass


class ProxiesUnavailableError(HttpLib2Error):
    pass
