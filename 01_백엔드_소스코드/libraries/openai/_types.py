# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _types.pyc (Python 3.11)

from __future__ import annotations
from os import PathLike
from typing import IO, TYPE_CHECKING, Any, Dict, List, Type, Tuple, Union, Mapping, TypeVar, Callable, Iterator, Optional, Sequence
from typing_extensions import Set, Literal, Protocol, TypeAlias, TypedDict, SupportsIndex, overload, override, runtime_checkable
import httpx
import pydantic
from httpx import URL, Proxy, Timeout, Response, BaseTransport, AsyncBaseTransport
if TYPE_CHECKING:
    from _models import BaseModel
    from _response import APIResponse, AsyncAPIResponse
    from _legacy_response import HttpxBinaryResponseContent
Transport = BaseTransport
AsyncTransport = AsyncBaseTransport
Query = Mapping[(str, object)]
Body = object
AnyMapping = Mapping[(str, object)]
ModelT = TypeVar('ModelT', bound = pydantic.BaseModel)
_T = TypeVar('_T')
ProxiesDict = Dict[('str | URL', Union[(None, str, URL, Proxy)])]
ProxiesTypes = Union[(str, Proxy, ProxiesDict)]
if TYPE_CHECKING:
    Base64FileInput = Union[(IO[bytes], PathLike[str])]
    FileContent = Union[(IO[bytes], bytes, PathLike[str])]
else:
    Base64FileInput = Union[(IO[bytes], PathLike)]
    FileContent = Union[(IO[bytes], bytes, PathLike)]
FileTypes = Union[(FileContent, Tuple[(Optional[str], FileContent)], Tuple[(Optional[str], FileContent, Optional[str])], Tuple[(Optional[str], FileContent, Optional[str], Mapping[(str, str)])])]
RequestFiles = Union[(Mapping[(str, FileTypes)], Sequence[Tuple[(str, FileTypes)]])]
HttpxFileContent = Union[(IO[bytes], bytes)]
HttpxFileTypes = Union[(HttpxFileContent, Tuple[(Optional[str], HttpxFileContent)], Tuple[(Optional[str], HttpxFileContent, Optional[str])], Tuple[(Optional[str], HttpxFileContent, Optional[str], Mapping[(str, str)])])]
HttpxRequestFiles = Union[(Mapping[(str, HttpxFileTypes)], Sequence[Tuple[(str, HttpxFileTypes)]])]
if TYPE_CHECKING:
    NoneType: 'Type[None]'
else:
    NoneType = type(None)

def RequestOptions():
    '''RequestOptions'''
    follow_redirects: 'bool' = 'RequestOptions'

RequestOptions = <NODE:27>(RequestOptions, 'RequestOptions', TypedDict, total = False)

class NotGiven:
    """
    For parameters with a meaningful None value, we need to distinguish between
    the user explicitly passing None, and the user not passing the parameter at
    all.

    User code shouldn't need to use not_given directly.

    For example:

    ```py
    def create(timeout: Timeout | None | NotGiven = not_given): ...


    create(timeout=1)  # 1s timeout
    create(timeout=None)  # No timeout
    create()  # Default timeout behavior
    ```
    """
    
    def __bool__(self = None):
        return False

    __repr__ = (lambda self = None: 'NOT_GIVEN')()

not_given = NotGiven()
NOT_GIVEN = NotGiven()

class Omit:
    '''
    To explicitly omit something from being sent in a request, use `omit`.

    ```py
    # as the default `Content-Type` header is `application/json` that will be sent
    client.post("/upload/files", files={"file": b"my raw file content"})

    # you can\'t explicitly override the header as it has to be dynamically generated
    # to look something like: \'multipart/form-data; boundary=0d8382fcf5f8c3be01ca2e11002d2983\'
    client.post(..., headers={"Content-Type": "multipart/form-data"})

    # instead you can remove the default `application/json` header by passing omit
    client.post(..., headers={"Content-Type": omit})
    ```
    '''
    
    def __bool__(self = None):
        return False


omit = Omit()
Omittable = Union[(_T, Omit)]
ModelBuilderProtocol = <NODE:12>()
Headers = Mapping[(str, Union[(str, Omit)])]

class HeadersLikeProtocol(Protocol):
    
    def get(self = None, _HeadersLikeProtocol__key = None):
        pass


HeadersLike = Union[(Headers, HeadersLikeProtocol)]
ResponseT = TypeVar('ResponseT', bound = Union[(object, str, None, 'BaseModel', List[Any], Dict[(str, Any)], Response, ModelBuilderProtocol, 'APIResponse[Any]', 'AsyncAPIResponse[Any]', 'HttpxBinaryResponseContent')])
StrBytesIntFloat = Union[(str, bytes, int, float)]
IncEx: 'TypeAlias' = Union[(Set[int], Set[str], Mapping[(int, Union[('IncEx', bool)])], Mapping[(str, Union[('IncEx', bool)])])]
PostParser = Callable[([
    Any], Any)]
InheritsGeneric = <NODE:12>()

class _GenericAlias(Protocol):
    __origin__: 'type[object]' = '_GenericAlias'


def HttpxSendArgs():
    '''HttpxSendArgs'''
    follow_redirects: 'bool' = 'HttpxSendArgs'

HttpxSendArgs = <NODE:27>(HttpxSendArgs, 'HttpxSendArgs', TypedDict, total = False)
_T_co = TypeVar('_T_co', covariant = True)
if TYPE_CHECKING:
    
    def SequenceNotStr():
        '''SequenceNotStr'''
        __getitem__ = (lambda self = None, index = None: pass)()
        __getitem__ = (lambda self = None, index = None: pass)()
        
        def __contains__(self = None, value = None):
            pass

        
        def __len__(self = None):
            pass

        
        def __iter__(self = None):
            pass

        
        def __reversed__(self = None):
            pass


    SequenceNotStr = <NODE:27>(SequenceNotStr, 'SequenceNotStr', Protocol[_T_co])
    return None
SequenceNotStr = None
