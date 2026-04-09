# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _client.pyc (Python 3.11)

from __future__ import annotations
import os
from typing import TYPE_CHECKING, Any, Mapping, Callable, Awaitable
from typing_extensions import Self, override
import httpx
from  import _exceptions
from _qs import Querystring
from _types import Omit, Timeout, NotGiven, Transport, ProxiesTypes, RequestOptions, not_given
from _utils import is_given, is_mapping, get_async_library
from _compat import cached_property
from _models import FinalRequestOptions
from _version import __version__
from _streaming import Stream, AsyncStream
from _exceptions import OpenAIError, APIStatusError
from _base_client import DEFAULT_MAX_RETRIES, SyncAPIClient, AsyncAPIClient
if TYPE_CHECKING:
    from resources import beta, chat, audio, evals, files, images, models, videos, batches, uploads, realtime, responses, containers, embeddings, completions, fine_tuning, moderations, conversations, vector_stores
    from resources.files import Files, AsyncFiles
    from resources.images import Images, AsyncImages
    from resources.models import Models, AsyncModels
    from resources.videos import Videos, AsyncVideos
    from resources.batches import Batches, AsyncBatches
    from resources.webhooks import Webhooks, AsyncWebhooks
    from resources.beta.beta import Beta, AsyncBeta
    from resources.chat.chat import Chat, AsyncChat
    from resources.embeddings import Embeddings, AsyncEmbeddings
    from resources.audio.audio import Audio, AsyncAudio
    from resources.completions import Completions, AsyncCompletions
    from resources.evals.evals import Evals, AsyncEvals
    from resources.moderations import Moderations, AsyncModerations
    from resources.uploads.uploads import Uploads, AsyncUploads
    from resources.realtime.realtime import Realtime, AsyncRealtime
    from resources.responses.responses import Responses, AsyncResponses
    from resources.containers.containers import Containers, AsyncContainers
    from resources.fine_tuning.fine_tuning import FineTuning, AsyncFineTuning
    from resources.conversations.conversations import Conversations, AsyncConversations
    from resources.vector_stores.vector_stores import VectorStores, AsyncVectorStores
__all__ = [
    'Timeout',
    'Transport',
    'ProxiesTypes',
    'RequestOptions',
    'OpenAI',
    'AsyncOpenAI',
    'Client',
    'AsyncClient']

class OpenAI(SyncAPIClient):
    pass
# WARNING: Decompyle incomplete


class AsyncOpenAI(AsyncAPIClient):
    pass
# WARNING: Decompyle incomplete


class OpenAIWithRawResponse:
    _client: 'OpenAI' = 'OpenAIWithRawResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: CompletionsWithRawResponse = CompletionsWithRawResponseimport resources.completionsCompletionsWithRawResponse(self._client.completions))()
    chat = (lambda self = None: ChatWithRawResponse = ChatWithRawResponseimport resources.chatChatWithRawResponse(self._client.chat))()
    embeddings = (lambda self = None: EmbeddingsWithRawResponse = EmbeddingsWithRawResponseimport resources.embeddingsEmbeddingsWithRawResponse(self._client.embeddings))()
    files = (lambda self = None: FilesWithRawResponse = FilesWithRawResponseimport resources.filesFilesWithRawResponse(self._client.files))()
    images = (lambda self = None: ImagesWithRawResponse = ImagesWithRawResponseimport resources.imagesImagesWithRawResponse(self._client.images))()
    audio = (lambda self = None: AudioWithRawResponse = AudioWithRawResponseimport resources.audioAudioWithRawResponse(self._client.audio))()
    moderations = (lambda self = None: ModerationsWithRawResponse = ModerationsWithRawResponseimport resources.moderationsModerationsWithRawResponse(self._client.moderations))()
    models = (lambda self = None: ModelsWithRawResponse = ModelsWithRawResponseimport resources.modelsModelsWithRawResponse(self._client.models))()
    fine_tuning = (lambda self = None: FineTuningWithRawResponse = FineTuningWithRawResponseimport resources.fine_tuningFineTuningWithRawResponse(self._client.fine_tuning))()
    vector_stores = (lambda self = None: VectorStoresWithRawResponse = VectorStoresWithRawResponseimport resources.vector_storesVectorStoresWithRawResponse(self._client.vector_stores))()
    beta = (lambda self = None: BetaWithRawResponse = BetaWithRawResponseimport resources.betaBetaWithRawResponse(self._client.beta))()
    batches = (lambda self = None: BatchesWithRawResponse = BatchesWithRawResponseimport resources.batchesBatchesWithRawResponse(self._client.batches))()
    uploads = (lambda self = None: UploadsWithRawResponse = UploadsWithRawResponseimport resources.uploadsUploadsWithRawResponse(self._client.uploads))()
    responses = (lambda self = None: ResponsesWithRawResponse = ResponsesWithRawResponseimport resources.responsesResponsesWithRawResponse(self._client.responses))()
    realtime = (lambda self = None: RealtimeWithRawResponse = RealtimeWithRawResponseimport resources.realtimeRealtimeWithRawResponse(self._client.realtime))()
    conversations = (lambda self = None: ConversationsWithRawResponse = ConversationsWithRawResponseimport resources.conversationsConversationsWithRawResponse(self._client.conversations))()
    evals = (lambda self = None: EvalsWithRawResponse = EvalsWithRawResponseimport resources.evalsEvalsWithRawResponse(self._client.evals))()
    containers = (lambda self = None: ContainersWithRawResponse = ContainersWithRawResponseimport resources.containersContainersWithRawResponse(self._client.containers))()
    videos = (lambda self = None: VideosWithRawResponse = VideosWithRawResponseimport resources.videosVideosWithRawResponse(self._client.videos))()


class AsyncOpenAIWithRawResponse:
    _client: 'AsyncOpenAI' = 'AsyncOpenAIWithRawResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: AsyncCompletionsWithRawResponse = AsyncCompletionsWithRawResponseimport resources.completionsAsyncCompletionsWithRawResponse(self._client.completions))()
    chat = (lambda self = None: AsyncChatWithRawResponse = AsyncChatWithRawResponseimport resources.chatAsyncChatWithRawResponse(self._client.chat))()
    embeddings = (lambda self = None: AsyncEmbeddingsWithRawResponse = AsyncEmbeddingsWithRawResponseimport resources.embeddingsAsyncEmbeddingsWithRawResponse(self._client.embeddings))()
    files = (lambda self = None: AsyncFilesWithRawResponse = AsyncFilesWithRawResponseimport resources.filesAsyncFilesWithRawResponse(self._client.files))()
    images = (lambda self = None: AsyncImagesWithRawResponse = AsyncImagesWithRawResponseimport resources.imagesAsyncImagesWithRawResponse(self._client.images))()
    audio = (lambda self = None: AsyncAudioWithRawResponse = AsyncAudioWithRawResponseimport resources.audioAsyncAudioWithRawResponse(self._client.audio))()
    moderations = (lambda self = None: AsyncModerationsWithRawResponse = AsyncModerationsWithRawResponseimport resources.moderationsAsyncModerationsWithRawResponse(self._client.moderations))()
    models = (lambda self = None: AsyncModelsWithRawResponse = AsyncModelsWithRawResponseimport resources.modelsAsyncModelsWithRawResponse(self._client.models))()
    fine_tuning = (lambda self = None: AsyncFineTuningWithRawResponse = AsyncFineTuningWithRawResponseimport resources.fine_tuningAsyncFineTuningWithRawResponse(self._client.fine_tuning))()
    vector_stores = (lambda self = None: AsyncVectorStoresWithRawResponse = AsyncVectorStoresWithRawResponseimport resources.vector_storesAsyncVectorStoresWithRawResponse(self._client.vector_stores))()
    beta = (lambda self = None: AsyncBetaWithRawResponse = AsyncBetaWithRawResponseimport resources.betaAsyncBetaWithRawResponse(self._client.beta))()
    batches = (lambda self = None: AsyncBatchesWithRawResponse = AsyncBatchesWithRawResponseimport resources.batchesAsyncBatchesWithRawResponse(self._client.batches))()
    uploads = (lambda self = None: AsyncUploadsWithRawResponse = AsyncUploadsWithRawResponseimport resources.uploadsAsyncUploadsWithRawResponse(self._client.uploads))()
    responses = (lambda self = None: AsyncResponsesWithRawResponse = AsyncResponsesWithRawResponseimport resources.responsesAsyncResponsesWithRawResponse(self._client.responses))()
    realtime = (lambda self = None: AsyncRealtimeWithRawResponse = AsyncRealtimeWithRawResponseimport resources.realtimeAsyncRealtimeWithRawResponse(self._client.realtime))()
    conversations = (lambda self = None: AsyncConversationsWithRawResponse = AsyncConversationsWithRawResponseimport resources.conversationsAsyncConversationsWithRawResponse(self._client.conversations))()
    evals = (lambda self = None: AsyncEvalsWithRawResponse = AsyncEvalsWithRawResponseimport resources.evalsAsyncEvalsWithRawResponse(self._client.evals))()
    containers = (lambda self = None: AsyncContainersWithRawResponse = AsyncContainersWithRawResponseimport resources.containersAsyncContainersWithRawResponse(self._client.containers))()
    videos = (lambda self = None: AsyncVideosWithRawResponse = AsyncVideosWithRawResponseimport resources.videosAsyncVideosWithRawResponse(self._client.videos))()


class OpenAIWithStreamedResponse:
    _client: 'OpenAI' = 'OpenAIWithStreamedResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: CompletionsWithStreamingResponse = CompletionsWithStreamingResponseimport resources.completionsCompletionsWithStreamingResponse(self._client.completions))()
    chat = (lambda self = None: ChatWithStreamingResponse = ChatWithStreamingResponseimport resources.chatChatWithStreamingResponse(self._client.chat))()
    embeddings = (lambda self = None: EmbeddingsWithStreamingResponse = EmbeddingsWithStreamingResponseimport resources.embeddingsEmbeddingsWithStreamingResponse(self._client.embeddings))()
    files = (lambda self = None: FilesWithStreamingResponse = FilesWithStreamingResponseimport resources.filesFilesWithStreamingResponse(self._client.files))()
    images = (lambda self = None: ImagesWithStreamingResponse = ImagesWithStreamingResponseimport resources.imagesImagesWithStreamingResponse(self._client.images))()
    audio = (lambda self = None: AudioWithStreamingResponse = AudioWithStreamingResponseimport resources.audioAudioWithStreamingResponse(self._client.audio))()
    moderations = (lambda self = None: ModerationsWithStreamingResponse = ModerationsWithStreamingResponseimport resources.moderationsModerationsWithStreamingResponse(self._client.moderations))()
    models = (lambda self = None: ModelsWithStreamingResponse = ModelsWithStreamingResponseimport resources.modelsModelsWithStreamingResponse(self._client.models))()
    fine_tuning = (lambda self = None: FineTuningWithStreamingResponse = FineTuningWithStreamingResponseimport resources.fine_tuningFineTuningWithStreamingResponse(self._client.fine_tuning))()
    vector_stores = (lambda self = None: VectorStoresWithStreamingResponse = VectorStoresWithStreamingResponseimport resources.vector_storesVectorStoresWithStreamingResponse(self._client.vector_stores))()
    beta = (lambda self = None: BetaWithStreamingResponse = BetaWithStreamingResponseimport resources.betaBetaWithStreamingResponse(self._client.beta))()
    batches = (lambda self = None: BatchesWithStreamingResponse = BatchesWithStreamingResponseimport resources.batchesBatchesWithStreamingResponse(self._client.batches))()
    uploads = (lambda self = None: UploadsWithStreamingResponse = UploadsWithStreamingResponseimport resources.uploadsUploadsWithStreamingResponse(self._client.uploads))()
    responses = (lambda self = None: ResponsesWithStreamingResponse = ResponsesWithStreamingResponseimport resources.responsesResponsesWithStreamingResponse(self._client.responses))()
    realtime = (lambda self = None: RealtimeWithStreamingResponse = RealtimeWithStreamingResponseimport resources.realtimeRealtimeWithStreamingResponse(self._client.realtime))()
    conversations = (lambda self = None: ConversationsWithStreamingResponse = ConversationsWithStreamingResponseimport resources.conversationsConversationsWithStreamingResponse(self._client.conversations))()
    evals = (lambda self = None: EvalsWithStreamingResponse = EvalsWithStreamingResponseimport resources.evalsEvalsWithStreamingResponse(self._client.evals))()
    containers = (lambda self = None: ContainersWithStreamingResponse = ContainersWithStreamingResponseimport resources.containersContainersWithStreamingResponse(self._client.containers))()
    videos = (lambda self = None: VideosWithStreamingResponse = VideosWithStreamingResponseimport resources.videosVideosWithStreamingResponse(self._client.videos))()


class AsyncOpenAIWithStreamedResponse:
    _client: 'AsyncOpenAI' = 'AsyncOpenAIWithStreamedResponse'
    
    def __init__(self = None, client = None):
        self._client = client

    completions = (lambda self = None: AsyncCompletionsWithStreamingResponse = AsyncCompletionsWithStreamingResponseimport resources.completionsAsyncCompletionsWithStreamingResponse(self._client.completions))()
    chat = (lambda self = None: AsyncChatWithStreamingResponse = AsyncChatWithStreamingResponseimport resources.chatAsyncChatWithStreamingResponse(self._client.chat))()
    embeddings = (lambda self = None: AsyncEmbeddingsWithStreamingResponse = AsyncEmbeddingsWithStreamingResponseimport resources.embeddingsAsyncEmbeddingsWithStreamingResponse(self._client.embeddings))()
    files = (lambda self = None: AsyncFilesWithStreamingResponse = AsyncFilesWithStreamingResponseimport resources.filesAsyncFilesWithStreamingResponse(self._client.files))()
    images = (lambda self = None: AsyncImagesWithStreamingResponse = AsyncImagesWithStreamingResponseimport resources.imagesAsyncImagesWithStreamingResponse(self._client.images))()
    audio = (lambda self = None: AsyncAudioWithStreamingResponse = AsyncAudioWithStreamingResponseimport resources.audioAsyncAudioWithStreamingResponse(self._client.audio))()
    moderations = (lambda self = None: AsyncModerationsWithStreamingResponse = AsyncModerationsWithStreamingResponseimport resources.moderationsAsyncModerationsWithStreamingResponse(self._client.moderations))()
    models = (lambda self = None: AsyncModelsWithStreamingResponse = AsyncModelsWithStreamingResponseimport resources.modelsAsyncModelsWithStreamingResponse(self._client.models))()
    fine_tuning = (lambda self = None: AsyncFineTuningWithStreamingResponse = AsyncFineTuningWithStreamingResponseimport resources.fine_tuningAsyncFineTuningWithStreamingResponse(self._client.fine_tuning))()
    vector_stores = (lambda self = None: AsyncVectorStoresWithStreamingResponse = AsyncVectorStoresWithStreamingResponseimport resources.vector_storesAsyncVectorStoresWithStreamingResponse(self._client.vector_stores))()
    beta = (lambda self = None: AsyncBetaWithStreamingResponse = AsyncBetaWithStreamingResponseimport resources.betaAsyncBetaWithStreamingResponse(self._client.beta))()
    batches = (lambda self = None: AsyncBatchesWithStreamingResponse = AsyncBatchesWithStreamingResponseimport resources.batchesAsyncBatchesWithStreamingResponse(self._client.batches))()
    uploads = (lambda self = None: AsyncUploadsWithStreamingResponse = AsyncUploadsWithStreamingResponseimport resources.uploadsAsyncUploadsWithStreamingResponse(self._client.uploads))()
    responses = (lambda self = None: AsyncResponsesWithStreamingResponse = AsyncResponsesWithStreamingResponseimport resources.responsesAsyncResponsesWithStreamingResponse(self._client.responses))()
    realtime = (lambda self = None: AsyncRealtimeWithStreamingResponse = AsyncRealtimeWithStreamingResponseimport resources.realtimeAsyncRealtimeWithStreamingResponse(self._client.realtime))()
    conversations = (lambda self = None: AsyncConversationsWithStreamingResponse = AsyncConversationsWithStreamingResponseimport resources.conversationsAsyncConversationsWithStreamingResponse(self._client.conversations))()
    evals = (lambda self = None: AsyncEvalsWithStreamingResponse = AsyncEvalsWithStreamingResponseimport resources.evalsAsyncEvalsWithStreamingResponse(self._client.evals))()
    containers = (lambda self = None: AsyncContainersWithStreamingResponse = AsyncContainersWithStreamingResponseimport resources.containersAsyncContainersWithStreamingResponse(self._client.containers))()
    videos = (lambda self = None: AsyncVideosWithStreamingResponse = AsyncVideosWithStreamingResponseimport resources.videosAsyncVideosWithStreamingResponse(self._client.videos))()

Client = OpenAI
AsyncClient = AsyncOpenAI
