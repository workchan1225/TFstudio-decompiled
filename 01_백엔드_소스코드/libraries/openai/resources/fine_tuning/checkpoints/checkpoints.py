# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: checkpoints.pyc (Python 3.11)

from __future__ import annotations
from _compat import cached_property
from permissions import Permissions, AsyncPermissions, PermissionsWithRawResponse, AsyncPermissionsWithRawResponse, PermissionsWithStreamingResponse, AsyncPermissionsWithStreamingResponse
from _resource import SyncAPIResource, AsyncAPIResource
__all__ = [
    'Checkpoints',
    'AsyncCheckpoints']

class Checkpoints(SyncAPIResource):
    permissions = (lambda self = None: Permissions(self._client))()
    with_raw_response = (lambda self = None: CheckpointsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: CheckpointsWithStreamingResponse(self))()


class AsyncCheckpoints(AsyncAPIResource):
    permissions = (lambda self = None: AsyncPermissions(self._client))()
    with_raw_response = (lambda self = None: AsyncCheckpointsWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncCheckpointsWithStreamingResponse(self))()


class CheckpointsWithRawResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints

    permissions = (lambda self = None: PermissionsWithRawResponse(self._checkpoints.permissions))()


class AsyncCheckpointsWithRawResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints

    permissions = (lambda self = None: AsyncPermissionsWithRawResponse(self._checkpoints.permissions))()


class CheckpointsWithStreamingResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints

    permissions = (lambda self = None: PermissionsWithStreamingResponse(self._checkpoints.permissions))()


class AsyncCheckpointsWithStreamingResponse:
    
    def __init__(self = None, checkpoints = None):
        self._checkpoints = checkpoints

    permissions = (lambda self = None: AsyncPermissionsWithStreamingResponse(self._checkpoints.permissions))()
