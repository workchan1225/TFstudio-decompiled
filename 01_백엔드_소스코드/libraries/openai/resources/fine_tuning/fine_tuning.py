# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: fine_tuning.pyc (Python 3.11)

from __future__ import annotations
from _compat import cached_property
from jobs.jobs import Jobs, AsyncJobs, JobsWithRawResponse, AsyncJobsWithRawResponse, JobsWithStreamingResponse, AsyncJobsWithStreamingResponse
from _resource import SyncAPIResource, AsyncAPIResource
from alpha.alpha import Alpha, AsyncAlpha, AlphaWithRawResponse, AsyncAlphaWithRawResponse, AlphaWithStreamingResponse, AsyncAlphaWithStreamingResponse
from checkpoints.checkpoints import Checkpoints, AsyncCheckpoints, CheckpointsWithRawResponse, AsyncCheckpointsWithRawResponse, CheckpointsWithStreamingResponse, AsyncCheckpointsWithStreamingResponse
__all__ = [
    'FineTuning',
    'AsyncFineTuning']

class FineTuning(SyncAPIResource):
    jobs = (lambda self = None: Jobs(self._client))()
    checkpoints = (lambda self = None: Checkpoints(self._client))()
    alpha = (lambda self = None: Alpha(self._client))()
    with_raw_response = (lambda self = None: FineTuningWithRawResponse(self))()
    with_streaming_response = (lambda self = None: FineTuningWithStreamingResponse(self))()


class AsyncFineTuning(AsyncAPIResource):
    jobs = (lambda self = None: AsyncJobs(self._client))()
    checkpoints = (lambda self = None: AsyncCheckpoints(self._client))()
    alpha = (lambda self = None: AsyncAlpha(self._client))()
    with_raw_response = (lambda self = None: AsyncFineTuningWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncFineTuningWithStreamingResponse(self))()


class FineTuningWithRawResponse:
    
    def __init__(self = None, fine_tuning = None):
        self._fine_tuning = fine_tuning

    jobs = (lambda self = None: JobsWithRawResponse(self._fine_tuning.jobs))()
    checkpoints = (lambda self = None: CheckpointsWithRawResponse(self._fine_tuning.checkpoints))()
    alpha = (lambda self = None: AlphaWithRawResponse(self._fine_tuning.alpha))()


class AsyncFineTuningWithRawResponse:
    
    def __init__(self = None, fine_tuning = None):
        self._fine_tuning = fine_tuning

    jobs = (lambda self = None: AsyncJobsWithRawResponse(self._fine_tuning.jobs))()
    checkpoints = (lambda self = None: AsyncCheckpointsWithRawResponse(self._fine_tuning.checkpoints))()
    alpha = (lambda self = None: AsyncAlphaWithRawResponse(self._fine_tuning.alpha))()


class FineTuningWithStreamingResponse:
    
    def __init__(self = None, fine_tuning = None):
        self._fine_tuning = fine_tuning

    jobs = (lambda self = None: JobsWithStreamingResponse(self._fine_tuning.jobs))()
    checkpoints = (lambda self = None: CheckpointsWithStreamingResponse(self._fine_tuning.checkpoints))()
    alpha = (lambda self = None: AlphaWithStreamingResponse(self._fine_tuning.alpha))()


class AsyncFineTuningWithStreamingResponse:
    
    def __init__(self = None, fine_tuning = None):
        self._fine_tuning = fine_tuning

    jobs = (lambda self = None: AsyncJobsWithStreamingResponse(self._fine_tuning.jobs))()
    checkpoints = (lambda self = None: AsyncCheckpointsWithStreamingResponse(self._fine_tuning.checkpoints))()
    alpha = (lambda self = None: AsyncAlphaWithStreamingResponse(self._fine_tuning.alpha))()
