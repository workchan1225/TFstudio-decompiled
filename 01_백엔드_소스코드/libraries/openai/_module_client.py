# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: _module_client.pyc (Python 3.11)

from __future__ import annotations
from typing import TYPE_CHECKING
from typing_extensions import override
if TYPE_CHECKING:
    from resources.files import Files
    from resources.images import Images
    from resources.models import Models
    from resources.videos import Videos
    from resources.batches import Batches
    from resources.webhooks import Webhooks
    from resources.beta.beta import Beta
    from resources.chat.chat import Chat
    from resources.embeddings import Embeddings
    from resources.audio.audio import Audio
    from resources.completions import Completions
    from resources.evals.evals import Evals
    from resources.moderations import Moderations
    from resources.uploads.uploads import Uploads
    from resources.realtime.realtime import Realtime
    from resources.responses.responses import Responses
    from resources.containers.containers import Containers
    from resources.fine_tuning.fine_tuning import FineTuning
    from resources.conversations.conversations import Conversations
    from resources.vector_stores.vector_stores import VectorStores
from  import _load_client
from _utils import LazyProxy

def ChatProxy():
    '''ChatProxy'''
    __load__ = (lambda self = None: _load_client().chat)()

ChatProxy = <NODE:27>(ChatProxy, 'ChatProxy', LazyProxy['Chat'])

def BetaProxy():
    '''BetaProxy'''
    __load__ = (lambda self = None: _load_client().beta)()

BetaProxy = <NODE:27>(BetaProxy, 'BetaProxy', LazyProxy['Beta'])

def FilesProxy():
    '''FilesProxy'''
    __load__ = (lambda self = None: _load_client().files)()

FilesProxy = <NODE:27>(FilesProxy, 'FilesProxy', LazyProxy['Files'])

def AudioProxy():
    '''AudioProxy'''
    __load__ = (lambda self = None: _load_client().audio)()

AudioProxy = <NODE:27>(AudioProxy, 'AudioProxy', LazyProxy['Audio'])

def EvalsProxy():
    '''EvalsProxy'''
    __load__ = (lambda self = None: _load_client().evals)()

EvalsProxy = <NODE:27>(EvalsProxy, 'EvalsProxy', LazyProxy['Evals'])

def ImagesProxy():
    '''ImagesProxy'''
    __load__ = (lambda self = None: _load_client().images)()

ImagesProxy = <NODE:27>(ImagesProxy, 'ImagesProxy', LazyProxy['Images'])

def ModelsProxy():
    '''ModelsProxy'''
    __load__ = (lambda self = None: _load_client().models)()

ModelsProxy = <NODE:27>(ModelsProxy, 'ModelsProxy', LazyProxy['Models'])

def VideosProxy():
    '''VideosProxy'''
    __load__ = (lambda self = None: _load_client().videos)()

VideosProxy = <NODE:27>(VideosProxy, 'VideosProxy', LazyProxy['Videos'])

def BatchesProxy():
    '''BatchesProxy'''
    __load__ = (lambda self = None: _load_client().batches)()

BatchesProxy = <NODE:27>(BatchesProxy, 'BatchesProxy', LazyProxy['Batches'])

def UploadsProxy():
    '''UploadsProxy'''
    __load__ = (lambda self = None: _load_client().uploads)()

UploadsProxy = <NODE:27>(UploadsProxy, 'UploadsProxy', LazyProxy['Uploads'])

def WebhooksProxy():
    '''WebhooksProxy'''
    __load__ = (lambda self = None: _load_client().webhooks)()

WebhooksProxy = <NODE:27>(WebhooksProxy, 'WebhooksProxy', LazyProxy['Webhooks'])

def RealtimeProxy():
    '''RealtimeProxy'''
    __load__ = (lambda self = None: _load_client().realtime)()

RealtimeProxy = <NODE:27>(RealtimeProxy, 'RealtimeProxy', LazyProxy['Realtime'])

def ResponsesProxy():
    '''ResponsesProxy'''
    __load__ = (lambda self = None: _load_client().responses)()

ResponsesProxy = <NODE:27>(ResponsesProxy, 'ResponsesProxy', LazyProxy['Responses'])

def EmbeddingsProxy():
    '''EmbeddingsProxy'''
    __load__ = (lambda self = None: _load_client().embeddings)()

EmbeddingsProxy = <NODE:27>(EmbeddingsProxy, 'EmbeddingsProxy', LazyProxy['Embeddings'])

def ContainersProxy():
    '''ContainersProxy'''
    __load__ = (lambda self = None: _load_client().containers)()

ContainersProxy = <NODE:27>(ContainersProxy, 'ContainersProxy', LazyProxy['Containers'])

def CompletionsProxy():
    '''CompletionsProxy'''
    __load__ = (lambda self = None: _load_client().completions)()

CompletionsProxy = <NODE:27>(CompletionsProxy, 'CompletionsProxy', LazyProxy['Completions'])

def ModerationsProxy():
    '''ModerationsProxy'''
    __load__ = (lambda self = None: _load_client().moderations)()

ModerationsProxy = <NODE:27>(ModerationsProxy, 'ModerationsProxy', LazyProxy['Moderations'])

def FineTuningProxy():
    '''FineTuningProxy'''
    __load__ = (lambda self = None: _load_client().fine_tuning)()

FineTuningProxy = <NODE:27>(FineTuningProxy, 'FineTuningProxy', LazyProxy['FineTuning'])

def VectorStoresProxy():
    '''VectorStoresProxy'''
    __load__ = (lambda self = None: _load_client().vector_stores)()

VectorStoresProxy = <NODE:27>(VectorStoresProxy, 'VectorStoresProxy', LazyProxy['VectorStores'])

def ConversationsProxy():
    '''ConversationsProxy'''
    __load__ = (lambda self = None: _load_client().conversations)()

ConversationsProxy = <NODE:27>(ConversationsProxy, 'ConversationsProxy', LazyProxy['Conversations'])
chat: 'Chat' = ChatProxy().__as_proxied__()
beta: 'Beta' = BetaProxy().__as_proxied__()
files: 'Files' = FilesProxy().__as_proxied__()
audio: 'Audio' = AudioProxy().__as_proxied__()
evals: 'Evals' = EvalsProxy().__as_proxied__()
images: 'Images' = ImagesProxy().__as_proxied__()
models: 'Models' = ModelsProxy().__as_proxied__()
videos: 'Videos' = VideosProxy().__as_proxied__()
batches: 'Batches' = BatchesProxy().__as_proxied__()
uploads: 'Uploads' = UploadsProxy().__as_proxied__()
webhooks: 'Webhooks' = WebhooksProxy().__as_proxied__()
realtime: 'Realtime' = RealtimeProxy().__as_proxied__()
responses: 'Responses' = ResponsesProxy().__as_proxied__()
embeddings: 'Embeddings' = EmbeddingsProxy().__as_proxied__()
containers: 'Containers' = ContainersProxy().__as_proxied__()
completions: 'Completions' = CompletionsProxy().__as_proxied__()
moderations: 'Moderations' = ModerationsProxy().__as_proxied__()
fine_tuning: 'FineTuning' = FineTuningProxy().__as_proxied__()
vector_stores: 'VectorStores' = VectorStoresProxy().__as_proxied__()
conversations: 'Conversations' = ConversationsProxy().__as_proxied__()
