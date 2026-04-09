# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _types.pyc (Python 3.11)

'''
Type definitions for type checking purposes.
'''
from http.cookiejar import CookieJar
from typing import IO, TYPE_CHECKING, Any, AsyncIterable, AsyncIterator, Callable, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple, Union
if TYPE_CHECKING:
    from _auth import Auth
    from _config import Proxy, Timeout
    from _models import Cookies, Headers, Request
    from _urls import URL, QueryParams
PrimitiveData = Optional[Union[(str, int, float, bool)]]
URLTypes = Union[('URL', str)]
QueryParamTypes = Union[('QueryParams', Mapping[(str, Union[(PrimitiveData, Sequence[PrimitiveData])])], List[Tuple[(str, PrimitiveData)]], Tuple[(Tuple[(str, PrimitiveData)], ...)], str, bytes)]
HeaderTypes = Union[('Headers', Mapping[(str, str)], Mapping[(bytes, bytes)], Sequence[Tuple[(str, str)]], Sequence[Tuple[(bytes, bytes)]])]
CookieTypes = Union[('Cookies', CookieJar, Dict[(str, str)], List[Tuple[(str, str)]])]
TimeoutTypes = Union[(Optional[float], Tuple[(Optional[float], Optional[float], Optional[float], Optional[float])], 'Timeout')]
ProxyTypes = Union[('URL', str, 'Proxy')]
CertTypes = Union[(str, Tuple[(str, str)], Tuple[(str, str, str)])]
AuthTypes = Union[(Tuple[(Union[(str, bytes)], Union[(str, bytes)])], Callable[([
    'Request'], 'Request')], 'Auth')]
RequestContent = Union[(str, bytes, Iterable[bytes], AsyncIterable[bytes])]
ResponseContent = Union[(str, bytes, Iterable[bytes], AsyncIterable[bytes])]
ResponseExtensions = Mapping[(str, Any)]
RequestData = Mapping[(str, Any)]
FileContent = Union[(IO[bytes], bytes, str)]
FileTypes = Union[(FileContent, Tuple[(Optional[str], FileContent)], Tuple[(Optional[str], FileContent, Optional[str])], Tuple[(Optional[str], FileContent, Optional[str], Mapping[(str, str)])])]
RequestFiles = Union[(Mapping[(str, FileTypes)], Sequence[Tuple[(str, FileTypes)]])]
RequestExtensions = Mapping[(str, Any)]
__all__ = [
    'AsyncByteStream',
    'SyncByteStream']

class SyncByteStream:
    
    def __iter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        '''
        Subclasses can override this method to release any network resources
        after a request/response cycle is complete.
        '''
        pass



class AsyncByteStream:
    
    def __aiter__(self = None):
        pass
    # WARNING: Decompyle incomplete

    
    async def aclose(self = None):
        pass
    # WARNING: Decompyle incomplete
