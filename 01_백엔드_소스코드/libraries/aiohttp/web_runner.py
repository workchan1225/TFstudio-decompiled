# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: web_runner.pyc (Python 3.11)

import asyncio
import signal
import socket
import warnings
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Any, List, Optional, Set
from yarl import URL
from typedefs import PathLike
from web_app import Application
from web_server import Server
if TYPE_CHECKING:
    from ssl import SSLContext
else:
    
    try:
        from ssl import SSLContext
    except ImportError:
        SSLContext = object

    __all__ = ('BaseSite', 'TCPSite', 'UnixSite', 'NamedPipeSite', 'SockSite', 'BaseRunner', 'AppRunner', 'ServerRunner', 'GracefulExit')
    
    class GracefulExit(SystemExit):
        code = 1

    
    def _raise_graceful_exit():
        raise GracefulExit()

    
    class BaseSite(ABC):
        __slots__ = ('_runner', '_ssl_context', '_backlog', '_server')
        
        def __init__(self = None, runner = None, *, shutdown_timeout, ssl_context, backlog):
            pass
        # WARNING: Decompyle incomplete

        name = (lambda self = None: pass)()()
        start = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        
        async def stop(self = None):
            pass
        # WARNING: Decompyle incomplete


    
    class TCPSite(BaseSite):
        pass
    # WARNING: Decompyle incomplete

    
    class UnixSite(BaseSite):
        pass
    # WARNING: Decompyle incomplete

    
    class NamedPipeSite(BaseSite):
        pass
    # WARNING: Decompyle incomplete

    
    class SockSite(BaseSite):
        pass
    # WARNING: Decompyle incomplete

    
    class BaseRunner(ABC):
        __slots__ = ('_handle_signals', '_kwargs', '_server', '_sites', '_shutdown_timeout')
        
        def __init__(self = None, *, handle_signals, shutdown_timeout, **kwargs):
            self._handle_signals = handle_signals
            self._kwargs = kwargs
            self._server = None
            self._sites = []
            self._shutdown_timeout = shutdown_timeout

        server = (lambda self = None: self._server)()
        addresses = (lambda self = None: ret = []# WARNING: Decompyle incomplete
)()
        sites = (lambda self = None: set(self._sites))()
        
        async def setup(self = None):
            pass
        # WARNING: Decompyle incomplete

        shutdown = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        
        async def cleanup(self = None):
            pass
        # WARNING: Decompyle incomplete

        _make_server = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        _cleanup_server = (lambda self = None: pass# WARNING: Decompyle incomplete
)()
        
        def _reg_site(self = None, site = None):
            if site in self._sites:
                raise RuntimeError(f'''Site {site} is already registered in runner {self}''')
            self._sites.append(site)

        
        def _check_site(self = None, site = None):
            if site not in self._sites:
                raise RuntimeError(f'''Site {site} is not registered in runner {self}''')

        
        def _unreg_site(self = None, site = None):
            if site not in self._sites:
                raise RuntimeError(f'''Site {site} is not registered in runner {self}''')
            self._sites.remove(site)


    
    class ServerRunner(BaseRunner):
        pass
    # WARNING: Decompyle incomplete

    
    class AppRunner(BaseRunner):
        pass
    # WARNING: Decompyle incomplete

    return None
