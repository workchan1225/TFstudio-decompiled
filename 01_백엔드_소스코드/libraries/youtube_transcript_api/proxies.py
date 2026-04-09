# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: proxies.pyc (Python 3.11)

from abc import ABC, abstractmethod
from typing import TypedDict, Optional, List

class InvalidProxyConfig(Exception):
    pass


class RequestsProxyConfigDict(TypedDict):
    https: str = '\n    This type represents the Dict that is used by the requests library to configure\n    the proxies used. More information on this can be found in the official requests\n    documentation: https://requests.readthedocs.io/en/latest/user/advanced/#proxies\n    '


class ProxyConfig(ABC):
    '''
    The base class for all proxy configs. Anything can be a proxy config, as longs as
    it can be turned into a `RequestsProxyConfigDict` by calling `to_requests_dict`.
    '''
    to_requests_dict = (lambda self = None: pass)()
    prevent_keeping_connections_alive = (lambda self = None: False)()
    retries_when_blocked = (lambda self = None: 0)()


class GenericProxyConfig(ProxyConfig):
    '''
    This proxy config can be used to set up any generic HTTP/HTTPS/SOCKS proxy. As it
    the requests library is used under the hood, you can follow the requests
    documentation to get more detailed information on how to set up proxies:
    https://requests.readthedocs.io/en/latest/user/advanced/#proxies

    If only an HTTP or an HTTPS proxy is provided, it will be used for both types of
    connections. However, you will have to provide at least one of the two.
    '''
    
    def __init__(self = None, http_url = None, https_url = None):
        '''
        If only an HTTP or an HTTPS proxy is provided, it will be used for both types of
        connections. However, you will have to provide at least one of the two.

        :param http_url: the proxy URL used for HTTP requests. Defaults to `https_url`
            if None.
        :param https_url: the proxy URL used for HTTPS requests. Defaults to `http_url`
            if None.
        '''
        if not http_url and https_url:
            raise InvalidProxyConfig('GenericProxyConfig requires you to define at least one of the two: http or https')
        self.http_url = http_url
        self.https_url = https_url

    
    def to_requests_dict(self = None):
