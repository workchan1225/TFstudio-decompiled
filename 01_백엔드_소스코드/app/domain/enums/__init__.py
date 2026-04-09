# Source: pycdc (Decompyle++)
# Quality: HIGH - actual Python source

# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.11)

'''
Domain Enums

Type-safe enumerations replacing magic strings throughout the domain.
These enums are framework-agnostic and provide type safety.
'''
from enum import Enum
from typing import Optional

class ProjectType(Enum):
    '''Type of project workflow'''
    DIRECT = 'direct'
    SIMPLE = 'simple'
    from_string = (lambda cls = None, value = None: pass# WARNING: Decompyle incomplete
)()


class ProjectStatus(Enum):
    '''Status of a project in the workflow'''
    DRAFT = 'draft'
    IN_PROGRESS = 'in-progress'
    COMPLETED = 'completed'
    from_string = (lambda cls = None, value = None: pass# WARNING: Decompyle incomplete
)()


class TTSMethod(Enum):
    '''Available TTS (Text-to-Speech) methods'''
    TYPECAST = 'typecast'
    WEB_TTS = 'web-tts'
    LOCAL_UPLOAD = 'local-upload'
    GOOGLE_VOICE = 'google-voice'
    NO_VOICE = 'no-voice'
    GEMINI_VOICE = 'gemini-voice'
    SPEAKER_MERGED = 'speaker-merged'
    EDGE_TTS = 'edge-tts'
    QWEN3 = 'qwen3'
    GEMINI_NATIVE = 'gemini-native'
    ELEVENLABS = 'elevenlabs'
    SUPERTONIC = 'supertonic'
    from_string = (lambda cls = None, value = None: pass# WARNING: Decompyle incomplete
)()


class AIProvider(Enum):
    '''Available AI providers for content generation'''
    CLAUDE = 'claude'
    OPENAI = 'openai'
    GOOGLE = 'google'
    from_string = (lambda cls = None, value = None: pass# WARNING: Decompyle incomplete
)()


class YouTubeUploadStatus(Enum):
    '''Status of YouTube video upload'''
    NOT_UPLOADED = 'not_uploaded'
    UPLOADING = 'uploading'
    UPLOADED = 'uploaded'
    FAILED = 'failed'
    SCHEDULED = 'scheduled'
    CANCELLED = 'cancelled'
    from_string = (lambda cls = None, value = None: pass# WARNING: Decompyle incomplete
)()


class MediaType(Enum):
    '''Type of media file'''
    IMAGE = 'image'
    VIDEO = 'video'
    AUDIO = 'audio'
    SUBTITLE = 'subtitle'
    from_string = (lambda cls = None, value = None: pass# WARNING: Decompyle incomplete
)()
