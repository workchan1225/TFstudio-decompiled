# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: alpha.pyc (Python 3.11)

from __future__ import annotations
from graders import Graders, AsyncGraders, GradersWithRawResponse, AsyncGradersWithRawResponse, GradersWithStreamingResponse, AsyncGradersWithStreamingResponse
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
__all__ = [
    'Alpha',
    'AsyncAlpha']

class Alpha(SyncAPIResource):
    graders = (lambda self = None: Graders(self._client))()
    with_raw_response = (lambda self = None: AlphaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AlphaWithStreamingResponse(self))()


class AsyncAlpha(AsyncAPIResource):
    graders = (lambda self = None: AsyncGraders(self._client))()
    with_raw_response = (lambda self = None: AsyncAlphaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncAlphaWithStreamingResponse(self))()


class AlphaWithRawResponse:
    
    def __init__(self = None, alpha = None):
        self._alpha = alpha

    graders = (lambda self = None: GradersWithRawResponse(self._alpha.graders))()


class AsyncAlphaWithRawResponse:
    
    def __init__(self = None, alpha = None):
        self._alpha = alpha

    graders = (lambda self = None: AsyncGradersWithRawResponse(self._alpha.graders))()


class AlphaWithStreamingResponse:
    
    def __init__(self = None, alpha = None):
        self._alpha = alpha

    graders = (lambda self = None: GradersWithStreamingResponse(self._alpha.graders))()


class AsyncAlphaWithStreamingResponse:
    
    def __init__(self = None, alpha = None):
        self._alpha = alpha

    graders = (lambda self = None: AsyncGradersWithStreamingResponse(self._alpha.graders))()
