# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: beta.pyc (Python 3.11)

from __future__ import annotations
from files import Files, AsyncFiles, FilesWithRawResponse, AsyncFilesWithRawResponse, FilesWithStreamingResponse, AsyncFilesWithStreamingResponse
from models import Models, AsyncModels, ModelsWithRawResponse, AsyncModelsWithRawResponse, ModelsWithStreamingResponse, AsyncModelsWithStreamingResponse
from _compat import cached_property
from _resource import SyncAPIResource, AsyncAPIResource
from skills.skills import Skills, AsyncSkills, SkillsWithRawResponse, AsyncSkillsWithRawResponse, SkillsWithStreamingResponse, AsyncSkillsWithStreamingResponse
from messages.messages import Messages, AsyncMessages, MessagesWithRawResponse, AsyncMessagesWithRawResponse, MessagesWithStreamingResponse, AsyncMessagesWithStreamingResponse
__all__ = [
    'Beta',
    'AsyncBeta']

class Beta(SyncAPIResource):
    models = (lambda self = None: Models(self._client))()
    messages = (lambda self = None: Messages(self._client))()
    files = (lambda self = None: Files(self._client))()
    skills = (lambda self = None: Skills(self._client))()
    with_raw_response = (lambda self = None: BetaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: BetaWithStreamingResponse(self))()


class AsyncBeta(AsyncAPIResource):
    models = (lambda self = None: AsyncModels(self._client))()
    messages = (lambda self = None: AsyncMessages(self._client))()
    files = (lambda self = None: AsyncFiles(self._client))()
    skills = (lambda self = None: AsyncSkills(self._client))()
    with_raw_response = (lambda self = None: AsyncBetaWithRawResponse(self))()
    with_streaming_response = (lambda self = None: AsyncBetaWithStreamingResponse(self))()


class BetaWithRawResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    models = (lambda self = None: ModelsWithRawResponse(self._beta.models))()
    messages = (lambda self = None: MessagesWithRawResponse(self._beta.messages))()
    files = (lambda self = None: FilesWithRawResponse(self._beta.files))()
    skills = (lambda self = None: SkillsWithRawResponse(self._beta.skills))()


class AsyncBetaWithRawResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    models = (lambda self = None: AsyncModelsWithRawResponse(self._beta.models))()
    messages = (lambda self = None: AsyncMessagesWithRawResponse(self._beta.messages))()
    files = (lambda self = None: AsyncFilesWithRawResponse(self._beta.files))()
    skills = (lambda self = None: AsyncSkillsWithRawResponse(self._beta.skills))()


class BetaWithStreamingResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    models = (lambda self = None: ModelsWithStreamingResponse(self._beta.models))()
    messages = (lambda self = None: MessagesWithStreamingResponse(self._beta.messages))()
    files = (lambda self = None: FilesWithStreamingResponse(self._beta.files))()
    skills = (lambda self = None: SkillsWithStreamingResponse(self._beta.skills))()


class AsyncBetaWithStreamingResponse:
    
    def __init__(self = None, beta = None):
        self._beta = beta

    models = (lambda self = None: AsyncModelsWithStreamingResponse(self._beta.models))()
    messages = (lambda self = None: AsyncMessagesWithStreamingResponse(self._beta.messages))()
    files = (lambda self = None: AsyncFilesWithStreamingResponse(self._beta.files))()
    skills = (lambda self = None: AsyncSkillsWithStreamingResponse(self._beta.skills))()
